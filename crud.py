from sqlalchemy.orm import Session
import models
import schemas


def create_blog(db: Session, blog: schemas.BlogCreate):
    new_blog = models.Blog(title=blog.title, content=blog.content)
    db.add(new_blog)
    db.commit()
    db.refresh(new_blog)
    return new_blog


def get_blogs(db: Session, skip: int = 0, limit: int = 10):
    return db.query(models.Blog).offset(skip).limit(limit).all()


def get_blog_by_id(db: Session, blog_id: int):
    return db.query(models.Blog).filter(models.Blog.id == blog_id).first()


def update_blog(db: Session, blog_id: int, blog_update: schemas.BlogUpdate):
    blog = db.query(models.Blog).filter(models.Blog.id == blog_id).first()
    if not blog:
        return None

    if blog_update.title is not None:
        blog.title = blog_update.title
    if blog_update.content is not None:
        blog.content = blog_update.content

    db.commit()
    db.refresh(blog)
    return blog


def delete_blog(db: Session, blog_id: int):
    blog = db.query(models.Blog).filter(models.Blog.id == blog_id).first()
    if blog:
        db.delete(blog)
        db.commit()
        return True
    return False

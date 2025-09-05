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

def delete_blog(db: Session, blog_id: int):
    blog = db.query(models.Blog).filter(models.Blog.id == blog_id).first()
    if blog:
        db.delete(blog)
        db.commit()
        return True
    return False

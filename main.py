from fastapi import FastAPI, Depends, HTTPException
from sqlalchemy.orm import Session
import models
import schemas
import crud
import database

# Create database tables
models.Base.metadata.create_all(bind=database.engine)

# App instance
app = FastAPI(title="Blog API")


# Dependency
def get_db():
    db = database.SessionLocal()
    try:
        yield db
    finally:
        db.close()


# create a blog post
@app.post("/blogs/", response_model=schemas.BlogResponse)
def create_blog(blog: schemas.BlogCreate, db: Session = Depends(get_db)):
    return crud.create_blog(db=db, blog=blog)


# List all blogs with query params (pagination)
@app.get("/blogs/", response_model=list[schemas.BlogResponse])
def read_blogs(skip: int = 0, limit: int = 10, db: Session = Depends(get_db)):
    return crud.get_blogs(db=db, skip=skip, limit=limit)


# Get blog by id
@app.get("/blogs/{blog_id}", response_model=schemas.BlogResponse)
def read_blog(blog_id: int, db: Session = Depends(get_db)):
    blog = crud.get_blog_by_id(db=db, blog_id=blog_id)
    if not blog:
        raise HTTPException(status_code=404, detail="Blog not found")
    return blog


# Update Blog by id
@app.put("/blogs/{blog_id", response_model=schemas.BlogResponse)
def update_blog(blog_id: int, blog_update: schemas.BlogUpdate, db: Session = Depends(get_db)):
    updated_blog = crud.update_blog(db=db, blog_id=blog_id, blog_update=blog_update)
    if not update_blog:
        raise HTTPException(status_code=404, detail="Blog not found")
    return updated_blog


# Delete a blog by ID (path param)
@app.delete("/blogs/{blog_id}")
def delete_blog(blog_id: int, db: Session = Depends(get_db)):
    deleted = crud.delete_blog(db=db, blog_id=blog_id)
    if not deleted:
        raise HTTPException(status_code=404, detail="Blog not found")
    return {"message": f"Blog {blog_id} deleted successfully"}

from fastapi import FastAPI, Depends
from sqlalchemy.sql.functions import mode
import schemas
import models
import database
from sqlalchemy.orm import Session


models.Base.metadata.create_all(database.engine)
app = FastAPI()

def get_db():
    db = database.SessionLocal()
    try:
        yield db
    finally:
        db.close()


# @app.post('/blog')
# def create(title, body):
#     return {'title':title, 'body':body}

@app.post('/blog')
def create(request: schemas.Blog, db: Session = Depends(get_db)):
    new_blog = models.Blog(title=request.title, body=request.body)
    print(db)
    db.add(new_blog)
    db.commit()
    db.refresh(new_blog)
    return new_blog

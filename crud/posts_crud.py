from tables import Post
from pydantic import BaseModel
from sqlalchemy import select
from datetime import date
from fastapi import HTTPException

class Item(BaseModel):
    author: str
    title: str
    content: str

def create_post(item: Item, session):
    post = Post(
        author = item.author,
        title = item.title,
        content = item.content,
        date_posted = date.today()
    )

    session.add(post)
    session.commit()
    

def delete_post(id:int, session):
    if not session.query(Post).filter(Post.post_id==id).first():
        raise HTTPException(status_code=404, detail="Post not found")
    
    session.query(Post).filter(Post.post_id==id).delete()
    session.commit()
            

def show_posts(session, limit: int = 10):
    stmt = select(Post).order_by(Post.post_id.desc()).limit(limit)
    posts = session.execute(stmt)

    data: list[Post] = []
    for post in posts.scalars():
            data.append(post)

    return data
    

def edit_post(data: dict, session):
    post = session.get(Post, data["id"])
    setattr(post, data["attribute"], data["edit"])
    session.commit()
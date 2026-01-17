from fastapi import FastAPI,HTTPException
from app.schemas import post_create,post_response
app=FastAPI()

text_posts={1:{"title":"New post","content":"cool test post"}}

@app.get("/posts")
def get_all_posts(limit:int):
    if limit :
        return list(text_posts.values())[:limit]
    return text_posts

@app.get("/posts/{id}")
def get_post_id(id :int)->post_response:
    if id not in text_posts:
        raise HTTPException(status_code=404,detail="Post not FOUND")
    return text_posts.get(id)

@app.post("/posts")
def create_post(post: post_create)->post_response:
     new_post={"title":post.title,"content":post.content}
     text_posts[max(text_posts.keys()) +1]=new_post
     return new_post
from fastapi import FastAPI

app  = FastAPI()

@app.get('/')
def index():
    return {'data': 'Blog List'}

@app.get('/blog/unpublished')
def unpublished():
    return {'data': 'all unpublished blogs'}

@app.get('/blog/{id}')
def show(id: int):
    # Fetch blog with id = id
    return {'data': id}


@app.get('/blog/{id}/comments')
def comment(id):
    # Fetch comments of blog with id = id
    return {'data': {'1','2'}}
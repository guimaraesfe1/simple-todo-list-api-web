from fastapi import FastAPI

from src.dependencies.lifespan import lifespan_db
from src.routes import task, user

app = FastAPI(title='ToDo List API', version='1.0.0', lifespan=lifespan_db)


@app.get('/', tags=['Index redirect'])
def index_page_redirect():
    return {
        'message': 'Please access one of link below',
        'Link 1 - Swagger': 'http://127.0.0.1:8000/docs',
        'Link 2 - Redoc': 'http://127.0.0.1:8000/redoc',
    }


app.include_router(user.router, prefix='/api/v1')
app.include_router(task.router, prefix='/api/v1')

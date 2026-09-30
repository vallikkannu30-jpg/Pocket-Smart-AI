from pathlib import Path

from fastapi import FastAPI

from fastapi.middleware.cors import CORSMiddleware

from fastapi.staticfiles import StaticFiles

from fastapi.templating import Jinja2Templates

from .config import settings

from .database import init_db

from .routes import pages
from .routes import auth
from .routes import api


BASE_DIR = Path(
    __file__
).resolve().parent


app = FastAPI(

    title=settings.APP_NAME,

    version="1.0.0",

    description=(
        "PocketSmart AI - "
        "Smart budget and recommendation assistant"
    )
)


app.add_middleware(
    CORSMiddleware,

    allow_origins=[
        "http://127.0.0.1:8000",
        "http://localhost:8000"
    ],

    allow_credentials=True,

    allow_methods=["*"],

    allow_headers=["*"]
)


app.mount(
    "/static",

    StaticFiles(
        directory=BASE_DIR / "static"
    ),

    name="static"
)


app.state.templates = Jinja2Templates(
    directory=BASE_DIR / "templates"
)


app.include_router(
    pages.router
)

app.include_router(
    auth.router
)

app.include_router(
    api.router
)


@app.on_event("startup")
def startup():

    init_db()


if __name__ == "__main__":

    import uvicorn

    uvicorn.run(
        "app.main:app",
        host="127.0.0.1",
        port=8000,
        reload=True
    )
from contextlib import asynccontextmanager

from fastapi import FastAPI

from account.api import account_api
from account.container import Container

# DIコンテナを作成
container = Container()


# アプリケーション起動時にコンテナを初期化
@asynccontextmanager
async def lifespan(app: FastAPI):
    container.init_resources()
    account_api.wire_container(container)
    yield


app = FastAPI(lifespan=lifespan)

# APIルーターをアプリケーションに含める
app.include_router(account_api.router)

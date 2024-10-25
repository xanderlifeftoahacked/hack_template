from contextlib import asynccontextmanager

from fastapi import FastAPI, Request, Response
from api.agents import router as agent_router
from db.crud.agents import fill_defaults as fill_agents
from api.exceptions import db_exception_handler
from schemas.exceptions import BaseDBException


@asynccontextmanager
async def lifespan(app: FastAPI):
    await fill_agents()
    yield

app = FastAPI(lifespan=lifespan)
app.include_router(agent_router)
app.add_exception_handler(BaseDBException, db_exception_handler)


@app.middleware("http")
async def some_middleware(request: Request, call_next):
    print(await request.body())
    response = await call_next(request)
    print(request.headers)
    response_body = b""
    async for chunk in response.body_iterator:
        response_body += chunk
    print(f"response_body={response_body.decode()}")
    return Response(content=response_body, status_code=response.status_code,
                    headers=dict(response.headers), media_type=response.media_type)

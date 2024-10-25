from typing import Annotated
from fastapi import APIRouter

from schemas.agents import AgentSchema, AgentAddSchema
from db.crud.agents import get_agent_by_id, add_agent
from api.dependencies import JWTAuth


router = APIRouter(prefix='/agents', tags=["agents"])


@router.get('/')
async def get_agent_handler(
        user_id: JWTAuth) -> list[AgentSchema | None]:

    agent = await get_agent_by_id(1)
    if not agent:
        print("NOAGENTS")
        return None

    return [agent]


@router.post('/')
async def add_agents_handler(agent: AgentAddSchema) -> AgentSchema | None:
    agent_ret = await add_agent(agent)

    return agent_ret

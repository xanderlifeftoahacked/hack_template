from datetime import datetime
from enum import Enum

from pydantic import BaseModel, Field


class AgentSchema(BaseModel):
    id: int
    name: str
    description: str
    phone_number: str  # regex
    photo: str  # link


class AgentAddSchema(BaseModel):
    name: str
    description: str
    phone_number: str  # regex
    photo: str  # link

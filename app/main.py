from datetime import datetime
from uuid import UUID

from fastapi import FastAPI
from pydantic import AnyUrl, BaseModel, EmailStr, Field
from uuid_extensions import uuid7


class StatusResponse(BaseModel):
    status: str
    message: str


class APIResponse(BaseModel):
    message: str
    email: EmailStr
    phone: str
    github: AnyUrl
    linkedin: AnyUrl
    id: UUID = Field(default_factory=uuid7)
    timestamp: datetime = Field(default_factory=datetime.utcnow)


app = FastAPI(
    title="FastAPI, Docker and Github Actions Demo",
    version="0.0.1",
    docs_url="/docs",
)


@app.get("/", tags=["Health"])
async def health():
    return StatusResponse(
        status="OK",
        message="Visit /docs for more information.",
    )


@app.get("/hire-me", tags=["Lawson"])
async def hire_me():
    return APIResponse(
        message="Hire me!",
        email="lawsontaylor@hotmail.co.uk",
        phone="+44 7540077944",
        github="https://github.com/LTMullineux/fastapi-docker-gh-actions-demo",
        linkedin="https://www.linkedin.com/in/lawsontaylor/",
    )

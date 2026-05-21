from fastapi import APIRouter
from pydantic import BaseModel

from crews.content_crew import ContentPipelineCrew


router = APIRouter()


class ContentRequest(BaseModel):
    topic: str
    audience: str
    platform: str

@router.post("/generate-content")
def generate_content(data: ContentRequest):

    crew = ContentPipelineCrew(
        topic=data.topic,
        audience=data.audience
    )

    result = crew.run(platform=data.platform)

    return {
        "post": result["social"]
    }
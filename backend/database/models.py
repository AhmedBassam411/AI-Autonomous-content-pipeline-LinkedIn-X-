from sqlalchemy import Column, Integer, String, Text, JSON
from database.db import Base


class Content(Base):
    __tablename__ = "contents"

    id = Column(Integer, primary_key=True, index=True)
    topic = Column(String, nullable=False)
    audience = Column(String)
    blog = Column(Text)
    seo_data = Column(JSON)
    social_posts = Column(JSON)
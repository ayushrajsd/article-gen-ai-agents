from pydantic import BaseModel, Field
from typing import List, Optional


class Source(BaseModel):
    title: str
    url: str
    snippet: Optional[str] = None


class ResearchBrief(BaseModel):
    topic: str
    key_findings: List[str] = Field(description="Bullet-point summary of key findings")
    notable_quotes: List[str] = Field(description="Notable quotes or statistics with source attribution")
    sources: List[Source] = Field(description="Reference sources retrieved via search")
    trends: List[str] = Field(description="Emerging trends or controversies identified")


class ArticleSection(BaseModel):
    heading: str
    content: str


class ArticleDraft(BaseModel):
    title: str
    introduction: str
    sections: List[ArticleSection] = Field(description="3-5 body sections with subheadings")
    conclusion: str


class FinalArticle(BaseModel):
    title: str
    introduction: str
    sections: List[ArticleSection]
    conclusion: str

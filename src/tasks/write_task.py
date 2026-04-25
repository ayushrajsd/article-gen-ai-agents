from crewai import Task
from src.agents import writer
from src.models import ArticleDraft
from src.tasks.research_task import research_task

write_task = Task(
    description=(
        "Using the research brief provided, write a comprehensive article on {topic}.\n"
        "1. Open with an engaging introduction that hooks the reader.\n"
        "2. Organise the body into 3-5 clearly titled sections.\n"
        "3. Incorporate key facts, statistics, and quotes from the research.\n"
        "4. Close with a concise conclusion that summarises the main takeaways."
    ),
    expected_output=(
        "A well-structured article with a title, introduction, "
        "3-5 body sections each with a heading and content, and a conclusion."
    ),
    output_pydantic=ArticleDraft,
    context=[research_task],
    agent=writer,
)

from crewai import Task
from src.agents import editor
from src.models import FinalArticle
from src.tasks.write_task import write_task

edit_task = Task(
    description=(
        "Review and refine the draft article on {topic}.\n"
        "1. Correct any grammatical or spelling errors.\n"
        "2. Improve sentence flow and paragraph transitions.\n"
        "3. Ensure a consistent, professional tone throughout.\n"
        "4. Verify that all claims are supported by the cited sources."
    ),
    expected_output=(
        "A polished, publication-ready article with a title, introduction, "
        "refined body sections, and a conclusion — all errors corrected, tone consistent."
    ),
    output_pydantic=FinalArticle,
    context=[write_task],
    agent=editor,
)

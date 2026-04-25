from crewai import Task
from src.agents import editor

edit_task = Task(
    description=(
        "Review and refine the draft article on {topic}.\n"
        "1. Correct any grammatical or spelling errors.\n"
        "2. Improve sentence flow and paragraph transitions.\n"
        "3. Ensure a consistent, professional tone throughout.\n"
        "4. Verify that all claims are supported by the cited sources."
    ),
    expected_output=(
        "A polished, publication-ready article in markdown format "
        "with all errors corrected and tone consistent."
    ),
    agent=editor,
)

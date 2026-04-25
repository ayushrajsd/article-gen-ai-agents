from crewai import Task
from src.agents import writer

write_task = Task(
    description=(
        "Using the research brief provided, write a comprehensive article on {topic}.\n"
        "1. Open with an engaging introduction that hooks the reader.\n"
        "2. Organise the body into clearly titled sections.\n"
        "3. Incorporate key facts, statistics, and quotes from the research.\n"
        "4. Close with a concise conclusion that summarises the main takeaways."
    ),
    expected_output=(
        "A well-structured article in markdown format with:\n"
        "- An engaging title and introduction\n"
        "- 3-5 body sections with subheadings\n"
        "- Inline citations referencing the research sources\n"
        "- A concluding summary paragraph"
    ),
    agent=writer,
)

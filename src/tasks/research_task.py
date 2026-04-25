from crewai import Task
from src.agents import researcher
from src.models import ResearchBrief

research_task = Task(
    description=(
        "Search the web for the latest articles and information on {topic}.\n"
        "1. Retrieve at least 5 recent, credible sources.\n"
        "2. Summarise the key findings, statistics, and expert opinions.\n"
        "3. Note the source URL for each reference.\n"
        "4. Highlight any emerging trends or controversies."
    ),
    expected_output=(
        "A structured research brief with key findings, notable quotes "
        "or statistics, a list of sources (title + URL), and identified trends."
    ),
    output_pydantic=ResearchBrief,
    agent=researcher,
)

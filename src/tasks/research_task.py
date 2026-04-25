from crewai import Task
from src.agents import researcher

research_task = Task(
    description=(
        "Search the web for the latest articles and information on {topic}.\n"
        "1. Retrieve at least 5 recent, credible sources.\n"
        "2. Summarise the key findings, statistics, and expert opinions.\n"
        "3. Note the source URL and publication date for each reference.\n"
        "4. Highlight any emerging trends or controversies."
    ),
    expected_output=(
        "A structured research brief containing:\n"
        "- A bullet-point summary of key findings\n"
        "- Notable quotes or statistics with their sources\n"
        "- A list of reference URLs with titles and dates"
    ),
    agent=researcher,
)

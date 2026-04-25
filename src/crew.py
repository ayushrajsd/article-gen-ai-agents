from crewai import Crew, Process
from src.agents import researcher, writer, editor
from src.tasks import research_task, write_task, edit_task

crew = Crew(
    agents=[researcher, writer, editor],
    tasks=[research_task, write_task, edit_task],
    process=Process.sequential,
    verbose=True,
)

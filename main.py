import warnings
warnings.filterwarnings("ignore")

import os
from dotenv import load_dotenv

load_dotenv()

os.environ.setdefault("OPENAI_MODEL_NAME", os.getenv("OPENAI_MODEL_NAME", "gpt-4o-mini"))

from src.crew import crew
from src.models import FinalArticle


def print_article(article: FinalArticle) -> None:
    print(f"\n{'=' * 60}")
    print(f"  {article.title}")
    print(f"{'=' * 60}\n")
    print(article.introduction)
    for section in article.sections:
        print(f"\n## {section.heading}\n")
        print(section.content)
    print(f"\n{'—' * 60}\n")
    print(article.conclusion)
    print(f"\n{'=' * 60}\n")


if __name__ == "__main__":
    topic = "Artificial Intelligence"
    result = crew.kickoff(inputs={"topic": topic})

    article = result.pydantic
    if isinstance(article, FinalArticle):
        print_article(article)
    else:
        print("\n=== Final Article ===\n")
        print(result)

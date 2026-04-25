import warnings
warnings.filterwarnings("ignore")

import os
import re
from datetime import datetime
from pathlib import Path
from dotenv import load_dotenv

load_dotenv()

os.environ.setdefault("OPENAI_MODEL_NAME", os.getenv("OPENAI_MODEL_NAME", "gpt-4o-mini"))

from src.crew import crew
from src.models import FinalArticle


def article_to_markdown(article: FinalArticle) -> str:
    lines = [f"# {article.title}", "", article.introduction]
    for section in article.sections:
        lines += ["", f"## {section.heading}", "", section.content]
    lines += ["", "---", "", article.conclusion]
    return "\n".join(lines)


def save_article(article: FinalArticle) -> Path:
    slug = re.sub(r"[^a-z0-9]+", "_", article.title.lower()).strip("_")
    timestamp = datetime.now().strftime("%Y%m%d_%H%M%S")
    output_dir = Path("output")
    output_dir.mkdir(exist_ok=True)
    path = output_dir / f"{slug}_{timestamp}.md"
    path.write_text(article_to_markdown(article), encoding="utf-8")
    return path


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
        path = save_article(article)
        print(f"Article saved to {path}\n")
    else:
        print("\n=== Final Article ===\n")
        print(result)

import warnings
warnings.filterwarnings("ignore")

import argparse
import os
from datetime import datetime
from pathlib import Path
from dotenv import load_dotenv

load_dotenv()

os.environ.setdefault("OPENAI_MODEL_NAME", os.getenv("OPENAI_MODEL_NAME", "gpt-4o-mini"))

from src.crew import crew
from src.models import FinalArticle


def parse_args() -> argparse.Namespace:
    parser = argparse.ArgumentParser(description="Multi-Agent Article Generator")
    parser.add_argument(
        "--topic",
        type=str,
        default="Artificial Intelligence",
        help="Topic to research and write about (default: 'Artificial Intelligence')",
    )
    parser.add_argument(
        "--output-dir",
        type=str,
        default="output",
        help="Directory to save the generated article (default: output/)",
    )
    return parser.parse_args()


def article_to_markdown(article: FinalArticle) -> str:
    lines = [f"# {article.title}\n", article.introduction]
    for section in article.sections:
        lines.append(f"\n## {section.heading}\n")
        lines.append(section.content)
    lines.append("\n---\n")
    lines.append(article.conclusion)
    return "\n".join(lines)


def save_article(article: FinalArticle, topic: str, output_dir: str) -> Path:
    Path(output_dir).mkdir(parents=True, exist_ok=True)
    slug = topic.lower().replace(" ", "_")
    timestamp = datetime.now().strftime("%Y%m%d_%H%M%S")
    path = Path(output_dir) / f"{slug}_{timestamp}.md"
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
    args = parse_args()

    result = crew.kickoff(inputs={"topic": args.topic})
    article = result.pydantic

    if isinstance(article, FinalArticle):
        print_article(article)
        saved_path = save_article(article, args.topic, args.output_dir)
        print(f"Article saved → {saved_path}")
    else:
        print("\n=== Final Article ===\n")
        print(result)

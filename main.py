import warnings
warnings.filterwarnings("ignore")

import os
from dotenv import load_dotenv

load_dotenv()

os.environ.setdefault("OPENAI_MODEL_NAME", os.getenv("OPENAI_MODEL_NAME", "gpt-4o-mini"))

from src.crew import crew

if __name__ == "__main__":
    topic = "Artificial Intelligence"
    result = crew.kickoff(inputs={"topic": topic})

    try:
        from IPython.display import Markdown, display
        display(Markdown(str(result)))
    except ImportError:
        print("\n=== Final Article ===\n")
        print(result)

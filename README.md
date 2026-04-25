# article-gen-ai-agents

# Multi-Agent Blog Writer using CrewAI

This repo demonstrates a multi-agent AI system built with [CrewAI](https://docs.crewai.com/), where three specialized agents collaborate to research and write a fully structured blog article.

## Agents

- **Researcher** — searches Google via SerpAPI and produces a structured `ResearchBrief` (key findings, quotes, sources, trends)
- **Writer** — turns the brief into a full `ArticleDraft` with intro, body sections, and conclusion
- **Editor** — polishes tone, grammar, and structure, outputting the final `FinalArticle`

## Output

After each run the finished article is auto-saved as a Markdown file:

```
output/<slug>_<timestamp>.md
# e.g. output/artificial_intelligence_20260425_143012.md
```

The `output/` directory is git-ignored so generated files are never committed.

---

## Getting Started

### 1. Clone the repo

```bash
git clone https://github.com/ayushrajsd/article-gen-ai-agents
cd article-gen-ai-agents
```

### 2. Create a virtual environment

```bash
python3 -m venv venv
source venv/bin/activate        # macOS/Linux
# or
.\venv\Scripts\activate         # Windows (VS Code terminal)
```

### 3. Install dependencies

```bash
pip install --upgrade pip setuptools wheel
pip install -r requirements.txt
```

### 4. Configure environment variables

```bash
cp .env.example .env
```

Edit `.env` and fill in your keys:

```
OPENAI_API_KEY=sk-your-openai-key-here
SERPAPI_API_KEY=your-serpapi-key-here
OPENAI_MODEL_NAME=gpt-4o-mini
```

- **OpenAI key** — [platform.openai.com](https://platform.openai.com)
- **SerpAPI key** — [serpapi.com](https://serpapi.com) (free tier: 100 searches/month)

### 5. Run

```bash
python3 main.py
```

You'll see the three agents work sequentially in the terminal. When finished, the article is printed and saved to `output/`.

To change the topic, edit line 47 of `main.py`:

```python
topic = "Quantum Computing"
```

## Project Structure

```
article-gen-ai-agents/
├── main.py                  # Entry point
├── requirements.txt
├── .env.example
├── output/                  # Auto-saved articles (git-ignored)
└── src/
    ├── crew.py              # Crew assembly
    ├── models.py            # Pydantic models (ResearchBrief, FinalArticle, …)
    ├── agents/
    │   ├── researcher.py
    │   ├── writer.py
    │   └── editor.py
    ├── tasks/
    │   ├── research_task.py
    │   ├── write_task.py
    │   └── edit_task.py
    └── tools/
        └── search_tool.py   # SerpAPI Google Search tool
```

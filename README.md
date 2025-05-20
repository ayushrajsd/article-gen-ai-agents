# article-gen-ai-agents

# 🧠 Multi-Agent Blog Writer using CrewAI

This repo demonstrates a simple multi-agent AI system built with [CrewAI](https://docs.crewai.com/), where agents collaboratively plan and write a blog post.

### Agents:

- 🧠 **Planner** – creates the article outline
- ✍️ **Writer** – writes a full blog post from the outline
- 📚 **Editor** – (coming soon) for tone and grammar

---

## 🛠️ Getting Started

1. **Clone the repo**

```bash
git clone https://github.com/ayushrajsd/article-gen-ai-agents
cd article-gen-ai-agents
```

2. **Create a virtual environment**

```bash
python3 -m venv crew-env
source crew-env/bin/activate
```

3. **Install uv (if you haven’t already)**

```bash
curl -LsSf https://astral.sh/uv/install.sh | sh

```

4. **Install dependencies**

```bash
uv pip install -r requirements.txt
```

5. **Create a .env file (⚠️ not committed)**

```bash
OPENAI_API_KEY=sk-xxxxxxxxxxxxxxxx
```

6. **Run the crew**

```bash
python article_crew.py

```

7. **You'll see Planner and Writer agents coordinate to create a full markdown blog article.**

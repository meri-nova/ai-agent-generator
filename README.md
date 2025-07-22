# AI Agent Idea Generator

A Python CLI tool that generates personalized AI agent product ideas based on your skills, interests, and goals using OpenAI's GPT models.

## Features

- 🤖 Interactive CLI interface
- ✨ Personalized AI agent ideas based on your profile
- 🎨 Beautiful terminal output with rich formatting
- 🔧 Configurable OpenAI model selection
- 📋 Structured output with name, problem, architecture, and tech stack

## Setup

1. **Clone or download the project**
   ```bash
   cd ai-agent-generator
   ```

2. **Install dependencies**
   ```bash
   pip install -r requirements.txt
   ```

3. **Set up your OpenAI API key**
   ```bash
   cp .env.example .env
   ```
   Edit `.env` and add your OpenAI API key:
   ```
   OPENAI_API_KEY=your_openai_api_key_here
   OPENAI_MODEL=gpt-4
   ```

## Usage

Run the CLI tool:
```bash
python main.py
```

The tool will prompt you for:
- **Skills**: Your technical skills (e.g., Python, JavaScript, Machine Learning)
- **Interests**: Domains you're passionate about (e.g., Healthcare, Education, Finance)
- **Goals**: What you want to achieve (e.g., Build a SaaS product, Automate workflows)

## Example Output

```
🚀 Your AI Agent Ideas:

┌─ 1. CodeReview Assistant ─────────────────────────────────┐
│ Problem: Automates code review process for development    │
│ teams, identifying bugs and suggesting improvements.      │
│                                                           │
│ Architecture: Microservices with webhook integrations,   │
│ ML models for code analysis, and REST API for team      │
│ collaboration tools.                                      │
│                                                           │
│ Tech Stack: Python, FastAPI, GitHub API, OpenAI API,    │
│ Docker, PostgreSQL                                       │
└───────────────────────────────────────────────────────────┘
```

## Configuration

- `OPENAI_API_KEY`: Your OpenAI API key (required)
- `OPENAI_MODEL`: Model to use (default: gpt-4, alternatives: gpt-3.5-turbo)

## Requirements

- Python 3.7+
- OpenAI API key
- Internet connection

## License

MIT License
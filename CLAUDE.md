# CLAUDE.md

This file provides guidance to Claude Code (claude.ai/code) when working with code in this repository.

## Project Overview

AI Agent Idea Generator is a Python CLI tool that generates personalized AI agent product ideas using OpenAI's GPT models. The tool collects user skills, interests, and goals through interactive prompts and generates 3 structured AI agent ideas with name, problem description, architecture, and tech stack.

## Commands

**Setup and Installation:**
```bash
pip install -r requirements.txt
cp .env.example .env
# Edit .env to add OPENAI_API_KEY
```

**Run the application:**
```bash
python main.py
```

**Run with version info:**
```bash
python main.py --version
```

## Architecture

The codebase follows a simple modular structure:

- `main.py` - CLI entry point with Rich-formatted user interface and argument parsing
- `openai_client.py` - OpenAI API client wrapper with JSON response parsing and error handling
- `prompts.py` - Prompt engineering for generating structured AI agent ideas
- `config.py` - Environment configuration management with validation

**Key Components:**
- Interactive CLI uses Rich library for formatted terminal output and user prompts
- OpenAI client expects structured JSON responses with exactly 3 agent ideas
- Configuration requires OPENAI_API_KEY environment variable and supports model selection
- Error handling covers API failures, JSON parsing errors, and missing configuration

**Data Flow:**
1. User provides skills, interests, goals via CLI prompts
2. Prompt template combines user input with structured output requirements
3. OpenAI API generates JSON response with 3 agent ideas
4. Rich library displays formatted results in terminal panels
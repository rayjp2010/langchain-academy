# CLAUDE.md

This file provides guidance to Claude Code (claude.ai/code) when working with code in this repository.

## Repository Overview

This is LangChain Academy - an educational repository with progressive modules teaching LangGraph concepts. The repository contains 6 modules (0-6) with Jupyter notebooks and accompanying LangGraph Studio examples.

## Required Python Version

This codebase requires Python 3.11 or later for optimal compatibility with LangGraph.

## Environment Setup

### Dependencies Installation
```bash
pip install -r requirements.txt
```

### Required API Keys
Set these environment variables:
- `OPENAI_API_KEY` - Required for all modules
- `LANGCHAIN_API_KEY` and `LANGCHAIN_TRACING_V2=true` - For LangSmith tracing
- `TAVILY_API_KEY` - Required for Module 4 (web search functionality)

### Studio Environment Setup
Each module's studio folder requires a `.env` file. Quick setup for all modules:
```bash
for i in {1..5}; do
  cp module-$i/studio/.env.example module-$i/studio/.env
  echo "OPENAI_API_KEY=\"$OPENAI_API_KEY\"" > module-$i/studio/.env
done
echo "TAVILY_API_KEY=\"$TAVILY_API_KEY\"" >> module-4/studio/.env
```

## Development Commands

### Running Notebooks
```bash
jupyter notebook
```

### LangGraph Studio
To run the Studio IDE for any module:
```bash
cd module-X/studio/
langgraph dev
```
This starts:
- API server at http://127.0.0.1:2024
- Studio UI at https://smith.langchain.com/studio/?baseUrl=http://127.0.0.1:2024

## Architecture

### Module Structure
- **Module 0**: Basic setup and introduction
- **Modules 1-4**: Progressive LangGraph concepts (basic graphs → advanced patterns)
- **Modules 5-6**: Memory systems and assistant patterns

### Studio Integration
Each module (1-6) contains a `studio/` subdirectory with:
- `langgraph.json`: Configuration file defining graphs, dependencies, and environment
- Python files: Graph implementations that can be loaded into LangGraph Studio
- `requirements.txt`: Module-specific dependencies
- `.env.example`: Template for required environment variables

### Graph Configuration Pattern
LangGraph Studio uses `langgraph.json` files that define:
- `graphs`: Mapping of graph names to Python file paths and graph objects
- `env`: Environment file location (typically `./.env`)
- `python_version`: Required Python version
- `dependencies`: Package dependencies

### State Management
LangGraph applications use TypedDict classes for state definition, following the pattern:
```python
class State(TypedDict):
    graph_state: str  # or other relevant state fields
```

## Key Dependencies
- `langgraph`: Core graph framework
- `langchain-openai`: OpenAI integration
- `tavily-python`: Web search (Module 4)
- `langgraph-cli[inmem]`: Studio development server
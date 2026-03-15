# 🤖 mcp-agent-orchestrator: Local Agentic AI via Model Context Protocol

[![Python 3.10+](https://img.shields.io/badge/Python-Python_-Orange)](https://www.python.org)
[![MCP](https://img.shields.io/badge/MCP-MCP_-Blue)](https://modelcontextprotocol.io)
[![Ollama](https://img.shields.io/badge/Ollama-Ollama_-Green)](https://ollama.com)

**mcp-agent-orchestrator** is a production-ready starter template for building **local-first Agentic AI** systems. It demonstrates how to connect a **FastMCP (Python) Server** to a **LangGraph Orchestrator** using **Ollama** as the local LLM host.

## 🚀 Key Features

*   **Standardized MCP Integration:** Uses the [Model Context Protocol](https://modelcontextprotocol.io) to decouple tool logic from LLM logic.
*   **Stateful Orchestration:** Built with **LangGraph** for robust, multi-turn agent conversations and error handling.
*   **Privacy-First:** 100% local execution using **Ollama (Llama 3.1/Mistral)**—no API keys required.
*   **Modern UI:** A clean **Streamlit** interface for real-time interaction with your MCP tools.
*   **FastMCP Framework:** Simplified Python tool definition with automatic schema generation.

## 🏗️ Architecture Overview

1.  **MCP Host (Ollama):** Provides the reasoning engine (LLM).
2.  **MCP Server (FastMCP):** Defines Python tools (e.g., SQLite, File System, Web Search).
3.  **MCP Client:** Manages the `stdio` transport and subprocess communication.
4.  **Orchestrator (LangGraph):** A stateful ReAct agent that decides when to call MCP tools.
5.  **Interface (Streamlit):** The user-facing web application.

## 🛠️ Quick Start

### Prerequisites
- Install [Ollama](https://ollama.com) and run `ollama run llama3.1`.
- Python 3.10 or higher.

### Installation
1. **Clone the repository:**
   ```bash
   git clone https://github.com/NxtGenCodeBase/mcp-agent-orchestrator.git
   cd mcp-agent-orchestrator
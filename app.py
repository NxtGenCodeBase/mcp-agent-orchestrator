import streamlit as st
import asyncio
from client_setup import get_mcp_tools
from orchestrator import run_agent

st.set_page_config(page_title="Local MCP Assistant")
st.title("🤖 Local MCP Assistant")

if prompt := st.chat_input("How can I help?"):
    st.chat_message("user").write(prompt)
    with st.chat_message("assistant"):
        # Run async logic in the Streamlit app
        tools = asyncio.run(get_mcp_tools())
        response = asyncio.run(run_agent(prompt, tools))
        st.write(response)

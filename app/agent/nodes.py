from langchain_openai import ChatOpenAI
from langchain_core.messages import SystemMessage, HumanMessage
from langchain_core.prompts import ChatPromptTemplate, MessagesPlaceholder
from langchain_core.output_parsers import StrOutputParser
from app.agent.state import AgentState
from app.agent.prompts import SUPERVISOR_SYSTEM_PROMPT, SALES_AGENT_SYSTEM_PROMPT, SUPPORT_AGENT_SYSTEM_PROMPT
import os

# Initialize LLM
# Note: In a real app, we might use different models for different agents
llm = ChatOpenAI(model="gpt-4o", temperature=0)

def supervisor_node(state: AgentState):
    """
    The supervisor node decides which agent should act next.
    """
    messages = state['messages']
    
    # Simple router using LLM
    prompt = ChatPromptTemplate.from_messages([
        ("system", SUPERVISOR_SYSTEM_PROMPT),
        MessagesPlaceholder(variable_name="messages"),
    ])
    
    chain = prompt | llm | StrOutputParser()
    
    # Get the last message to decide routing
    # In a more complex setup, we might pass the whole history or a summary
    next_agent = chain.invoke({"messages": messages})
    
    # Clean up the output to match node names exactly
    if "SalesAgent" in next_agent:
        return {"next": "SalesAgent"}
    elif "SupportAgent" in next_agent:
        return {"next": "SupportAgent"}
    else:
        return {"next": "GeneralChat"}

from app.agent.tools import product_search, order_lookup

def sales_node(state: AgentState):
    """
    The Sales Agent node.
    """
    messages = state['messages']
    
    prompt = ChatPromptTemplate.from_messages([
        ("system", SALES_AGENT_SYSTEM_PROMPT),
        MessagesPlaceholder(variable_name="messages"),
    ])
    
    # Bind tools to the LLM
    tools = [product_search]
    chain = prompt | llm.bind_tools(tools)
    
    response = chain.invoke({"messages": messages})
    
    return {"messages": [response], "next": "END"}

def support_node(state: AgentState):
    """
    The Support Agent node.
    """
    messages = state['messages']
    
    prompt = ChatPromptTemplate.from_messages([
        ("system", SUPPORT_AGENT_SYSTEM_PROMPT),
        MessagesPlaceholder(variable_name="messages"),
    ])
    
    # Bind tools
    tools = [order_lookup]
    chain = prompt | llm.bind_tools(tools)
    
    response = chain.invoke({"messages": messages})
    
    return {"messages": [response], "next": "END"}

def general_chat_node(state: AgentState):
    """
    Node for general chit-chat.
    """
    messages = state['messages']
    
    prompt = ChatPromptTemplate.from_messages([
        ("system", "You are a friendly e-commerce assistant. Respond politely to general greetings."),
        MessagesPlaceholder(variable_name="messages"),
    ])
    
    chain = prompt | llm
    response = chain.invoke({"messages": messages})
    
    return {"messages": [response], "next": "END"}

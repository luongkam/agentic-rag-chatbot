from langgraph.graph import StateGraph, END
from app.agent.state import AgentState
from app.agent.nodes import supervisor_node, sales_node, support_node, general_chat_node

# Define the graph
workflow = StateGraph(AgentState)

# Add nodes
workflow.add_node("Supervisor", supervisor_node)
workflow.add_node("SalesAgent", sales_node)
workflow.add_node("SupportAgent", support_node)
workflow.add_node("GeneralChat", general_chat_node)

# Define edges
workflow.set_entry_point("Supervisor")

# Conditional edges from Supervisor
workflow.add_conditional_edges(
    "Supervisor",
    lambda state: state["next"],
    {
        "SalesAgent": "SalesAgent",
        "SupportAgent": "SupportAgent",
        "GeneralChat": "GeneralChat"
    }
)

# Edges from agents back to END (or Supervisor if we wanted a loop)
workflow.add_edge("SalesAgent", END)
workflow.add_edge("SupportAgent", END)
workflow.add_edge("GeneralChat", END)

# Compile the graph
graph = workflow.compile()

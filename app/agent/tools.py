from langchain_core.tools import tool
from app.rag.supabase_client import supabase_manager

@tool
def product_search(query: str):
    """
    Search for product information, features, and pricing.
    Use this tool when the user asks about products.
    """
    # For demo purposes, if Supabase isn't set up, return mock data
    if not supabase_manager.client:
        return f"[MOCK] Found products related to '{query}':\n1. Smart AI Camera ($199) - Features: 4K, Night Vision.\n2. Robot Vacuum ($299) - Features: Lidar, Auto-empty."
        
    return supabase_manager.search_products(query)

@tool
def order_lookup(order_id: str):
    """
    Look up the status and details of a specific order by Order ID.
    """
    # For demo purposes, mock data
    if not supabase_manager.client:
        if order_id == "123":
            return "Order #123: Shipped. Expected delivery: Tomorrow."
        return "Order not found. Please check the ID."
        
    return supabase_manager.get_order(order_id)

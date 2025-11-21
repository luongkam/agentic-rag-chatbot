import os
from supabase import create_client, Client
from langchain_community.vectorstores import SupabaseVectorStore
from langchain_openai import OpenAIEmbeddings

class SupabaseManager:
    def __init__(self):
        self.url = os.environ.get("SUPABASE_URL")
        self.key = os.environ.get("SUPABASE_KEY")
        self.client: Client = None
        self.vector_store = None
        
        if self.url and self.key:
            self.client = create_client(self.url, self.key)
            
            # Initialize Vector Store
            embeddings = OpenAIEmbeddings()
            self.vector_store = SupabaseVectorStore(
                client=self.client,
                embedding=embeddings,
                table_name="documents",
                query_name="match_documents",
            )
    
    def search_products(self, query: str, k: int = 3):
        """
        Search for products in the vector store.
        """
        if not self.vector_store:
            return "Error: Supabase not configured."
            
        docs = self.vector_store.similarity_search(query, k=k)
        return "\n\n".join([d.page_content for d in docs])

    def get_order(self, order_id: str):
        """
        Get order details from Supabase DB.
        """
        if not self.client:
            return "Error: Supabase not configured."
            
        # Assuming an 'orders' table exists
        response = self.client.table("orders").select("*").eq("id", order_id).execute()
        if response.data:
            return str(response.data[0])
        return "Order not found."

# Singleton instance
supabase_manager = SupabaseManager()

"""
LLM Configuration Module
Supports multiple LLM providers: OpenAI, Google Gemini, GLM (Zhipu AI)
"""
import os
from typing import Optional
from langchain_openai import ChatOpenAI
from langchain_google_genai import ChatGoogleGenerativeAI

class LLMConfig:
    """
    Centralized LLM configuration that supports multiple providers
    """
    
    @staticmethod
    def get_llm(provider: Optional[str] = None, model: Optional[str] = None, temperature: float = 0):
        """
        Get LLM instance based on provider and model
        
        Args:
            provider: LLM provider (openai, google, glm). If None, auto-detect from env
            model: Model name. If None, use default for provider
            temperature: Temperature setting
        
        Returns:
            LLM instance
        """
        # Auto-detect provider from environment
        if provider is None:
            provider = os.getenv("LLM_PROVIDER", "openai").lower()
        
        if provider == "openai":
            return LLMConfig._get_openai(model, temperature)
        elif provider == "google" or provider == "gemini":
            return LLMConfig._get_google(model, temperature)
        elif provider == "glm" or provider == "zhipu":
            return LLMConfig._get_glm(model, temperature)
        else:
            # Default to OpenAI
            return LLMConfig._get_openai(model, temperature)
    
    @staticmethod
    def _get_openai(model: Optional[str] = None, temperature: float = 0):
        """Get OpenAI LLM"""
        api_key = os.getenv("OPENAI_API_KEY")
        if not api_key:
            raise ValueError("OPENAI_API_KEY not found in environment")
        
        model_name = model or os.getenv("OPENAI_MODEL", "gpt-4o")
        
        return ChatOpenAI(
            model=model_name,
            temperature=temperature,
            api_key=api_key
        )
    
    @staticmethod
    def _get_google(model: Optional[str] = None, temperature: float = 0):
        """Get Google Gemini LLM"""
        api_key = os.getenv("GOOGLE_API_KEY")
        if not api_key:
            raise ValueError("GOOGLE_API_KEY not found in environment")
        
        model_name = model or os.getenv("GOOGLE_MODEL", "gemini-1.5-pro")
        
        return ChatGoogleGenerativeAI(
            model=model_name,
            temperature=temperature,
            google_api_key=api_key
        )
    
    @staticmethod
    def _get_glm(model: Optional[str] = None, temperature: float = 0):
        """Get GLM (Zhipu AI) LLM"""
        api_key = os.getenv("GLM_API_KEY")
        if not api_key:
            raise ValueError("GLM_API_KEY not found in environment")
        
        model_name = model or os.getenv("GLM_MODEL", "glm-4")
        base_url = os.getenv("GLM_BASE_URL", "https://open.bigmodel.cn/api/paas/v4/")
        
        # GLM uses OpenAI-compatible API
        return ChatOpenAI(
            model=model_name,
            temperature=temperature,
            api_key=api_key,
            base_url=base_url
        )

# Singleton instance
def get_default_llm():
    """Get the default LLM configured in environment"""
    return LLMConfig.get_llm()

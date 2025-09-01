from langchain_core.prompts import ChatPromptTemplate, MessagesPlaceholder
from langchain_groq import ChatGroq

import os
from langchain_groq.chat_models import ChatGroq

api_key = os.getenv("GROQ_API_KEY") or "your-groq-api-key"
llm = ChatGroq(model="llama-3.1-8b-instant", api_key="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")


# Generation Prompt
generation_prompt = ChatPromptTemplate.from_messages(
    [
        (
            "system",
            "You are a Twitter techie influencer assistant who writes excellent Twitter posts. "
            "Generate the best Twitter post possible for the user's request. "
            "If the user provides critique, respond with a revised version of your previous attempts."
        ),
        MessagesPlaceholder(variable_name="messages"),
    ]
)

# Reflection Prompt
reflection_prompt = ChatPromptTemplate.from_messages(
    [
        (
            "system",
            "You are a viral Twitter influencer grading a tweet. Generate critique and recommendations for the user's tweet. "
            "Always provide detailed recommendations, including requests for length, virality, style, etc.",
        ),
        MessagesPlaceholder(variable_name="messages"),
    ]
)

# Initialize LLM (ensure credentials/env is set up)
llm = ChatGroq(model="llama-3.1-8b-instant")

# Chains
generation_chain = generation_prompt | llm
reflection_chain = reflection_prompt | llm

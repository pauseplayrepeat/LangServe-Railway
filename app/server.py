from fastapi import FastAPI
from langserve import add_routes
from extraction_openai_functions import chain as extraction_openai_functions_chain
from rag_conversation import chain as rag_conversation_chain
from openai_functions_agent import agent_executor as openai_functions_agent_chain
from research_assistant import chain as research_assistant_chain
from rag_pinecone_multi_query import chain as rag_pinecone_multi_query_chain



app = FastAPI()

add_routes(app, extraction_openai_functions_chain, path="/extraction-openai-functions")
add_routes(app, rag_conversation_chain, path="/rag-conversation")
add_routes(app, openai_functions_agent_chain, path="/openai-functions-agent")
add_routes(app, research_assistant_chain, path="/research-assistant")
add_routes(app, research_assistant_chain, path="/course")
add_routes(app, rag_pinecone_multi_query_chain, path="/rag-pinecone-multi-query")


@app.get("/")
def root():
    return {
        "message": "Welcome to the langserve server! More information and routes can be found at /docs. 🦜 🏓",
    }


@app.get("/health")
def health_check():
    return {"status": "healthy"}


if __name__ == "__main__":
    import uvicorn

    uvicorn.run(app, host="0.0.0.0", port=8000)

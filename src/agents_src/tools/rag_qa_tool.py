import logging

from crewai.tools import tool
from llama_index.core import VectorStoreIndex, StorageContext
from llama_index.vector_stores.chroma import ChromaVectorStore
from llama_index.embeddings.huggingface import HuggingFaceEmbedding
from llama_index.llms.groq import Groq
from llama_index.core import Settings
import chromadb

from src.agents_src.config.agent_settings import AgentSettings

# Get a logger for this module
logger = logging.getLogger(__name__)

# download & load embedding model
logger.info("Loading HuggingFace embedding model...")
embed_model = HuggingFaceEmbedding()


@tool
def rag_query_tool(query: str) -> dict:
    """
    Answers a query by retrieving relevant documents and generating a response.
    Returns both the generated answer and the source file names from which the information was retrieved.

    Args:
        query (str): The input query string to be processed.

    Returns:
        dict: A dictionary with the following keys:
            - 'answer': The generated answer string.
            - 'source_files': List of source file names used for retrieval.

    Notes:
        - Requires properly configured AgentSettings and access to the vector store.
        - The function loads the embedding model and LLM each time it is called.
    """

    settings = AgentSettings()
    vector_store_path = settings.VECTOR_STORE_DIR
    collection_name = settings.COLLECTION_NAME
    # Configure LLM
    Settings.llm = Groq(
        model=settings.MODEL_NAME,
        temperature=settings.MODEL_TEMPERATURE,
        api_key=settings.GROQ_API_KEY,
    )
    # Load Chroma collection
    db = chromadb.PersistentClient(path=vector_store_path)
    chroma_collection = db.get_or_create_collection(collection_name)
    # connect to the vector store
    vector_store = ChromaVectorStore(chroma_collection=chroma_collection)
    storage_context = StorageContext.from_defaults(vector_store=vector_store)
    # Load index from Chroma
    index = VectorStoreIndex.from_vector_store(
        vector_store=vector_store,
        storage_context=storage_context,
        embed_model=embed_model
    )
    # Create the query engine
    query_engine = index.as_query_engine(similarity_top_k=3)
    # Pass the query to the query engine
    response = query_engine.query(query)
    source_file_names = {m.get("file_name") for m in getattr(response, "metadata", {}).values()}

    return {"answer": response.response,
            "source_files": list(source_file_names)}


# For direct testing, uncomment the code below and comment out @tool.
# When using CrewAI, uncomment @tool and comment out the test code.
#
# output = rag_query_tool(query="Explain Ecosystem and Evolution.")
# print(output)
# print(output["answer"])
# print(output["source_files"])
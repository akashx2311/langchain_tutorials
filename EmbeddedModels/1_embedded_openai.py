from langchain_openai import OpenAIEmbeddings

from dotenv import load_dotenv

load_dotenv()

embeddings = OpenAIEmbeddings(
    model="text-embedding-3-large",
    dimensions=1024  # Optional: reduces storage/compute in vector DBs
)
query_vector = embeddings.embed_query("What is the capital of France?")
doc_vectors = embeddings.embed_documents([
    "Paris is the capital of France.",
    "Berlin is the capital of Germany."
])
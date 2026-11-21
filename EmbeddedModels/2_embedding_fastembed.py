from langchain_community.embeddings.fastembed import FastEmbedEmbeddings

# Downloads and runs lightweight ONNX model on CPU
embeddings = FastEmbedEmbeddings(model_name="BAAI/bge-small-en-v1.5")
vector = embeddings.embed_query("Local embeddings without PyTorch!")

from langchain_community.vectorstores import FAISS
from langchain_openai import OpenAIEmbeddings
from langchain_text_splitters import RecursiveCharacterTextSplitter
from langchain_core.documents import Document
import os

def build_vectorstore(kb_path):
    docs = []
    for file in os.listdir(kb_path):
        with open(os.path.join(kb_path, file)) as f:
            docs.append(Document(page_content=f.read()))

    splitter = RecursiveCharacterTextSplitter(chunk_size=200)
    chunks = splitter.split_documents(docs)

    embeddings = OpenAIEmbeddings(
        base_url="https://openai.vocareum.com/v1",
        api_key=os.getenv("OPENAI_API_KEY")
    )

    return FAISS.from_documents(chunks, embeddings)

def retrieve(vectorstore, query):
    results = vectorstore.similarity_search(query, k=2)
    return [r.page_content for r in results]

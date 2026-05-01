from sentence_transformers import SentenceTransformer
import faiss
import numpy as np

model = SentenceTransformer("all-MiniLM-L6-v2")

def load_docs():
    with open("data/emails.txt", "r", encoding="utf-8") as f:
        return f.read().split("\n\n---\n\n")

def create_index():
    docs = load_docs()
    embeddings = model.encode(docs)

    dim = embeddings.shape[1]
    index = faiss.IndexFlatL2(dim)
    index.add(np.array(embeddings))

    return index, docs

def search(query, index, docs, k=3):
    q_emb = model.encode([query])
    D, I = index.search(np.array(q_emb), k)

    return [docs[i] for i in I[0]]
import chromadb

chromadb_client = chromadb.Client()

# tạo collection để lưu trữ dữ liệu

collection = chromadb_client.create_collection("my_collection")

# thêm dữ liệu mẫu

collection.add(
    ids=["id1", "id2"],
    documents=["This is the first document.", "This is the second document."],
)

# thực hiện query collection

results = collection.query(query_texts=["number one document"], n_results=2)
print(results)

# python chroma_db/main.py
# {'ids': [['id1', 'id2']], 'embeddings': None, 'documents': [['This is the first document.', 'This is the second document.']], 'uris': None, 'included': ['metadatas', 'documents', 'distances'], 'data': None, 'metadatas': [[None, None]], 'distances': [[0.7423363327980042, 0.7944488525390625]]}
# cosine_distance nhỏ hơn -> gần hơn -> id1 là đáp án.
# lưu ý cosine distance nhỏ hơn và cosine simlarity thì cần lớn hơn

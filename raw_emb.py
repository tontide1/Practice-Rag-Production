import os

import dotenv
from langchain_google_genai import GoogleGenerativeAIEmbeddings

dotenv.load_dotenv()

text = "Trí tuệ nhân tạo (AI) đang tái định hình nền kinh tế số tại Việt Nam. Theo các chuyên gia tại TP.HCM, việc ứng dụng các mô hình ngôn ngữ lớn (LLM) kết hợp với kỹ thuật RAG (Retrieval-Augmented Generation) giúp doanh nghiệp tối ưu hóa quy trình chăm sóc khách hàng tự động. Tuy nhiên, thách thức lớn nhất hiện nay là xử lý dữ liệu đa phương thức (multimodal data) bao gồm cả hình ảnh hóa đơn, video quay màn hình lỗi và file âm thanh ghi âm cuộc gọi của khách hàng. Để giải quyết bài toán này, các kỹ sư hệ thống đang chuyển sang sử dụng công nghệ Vector Database thế hệ mới để tăng tốc độ truy xuất dữ liệu theo thời gian thực."

embeddings_768 = GoogleGenerativeAIEmbeddings(
    model="gemini-embedding-2-preview", output_dimensionality=768
)
vector_768 = embeddings_768.embed_query(text)

embeddings_384 = GoogleGenerativeAIEmbeddings(
    model="gemini-embedding-2-preview", output_dimensionality=384
)
vector_384 = embeddings_384.embed_query(text)

import numpy as np

embeddings_dot = np.dot(vector_768, vector_384)

norms_L2 = np.linalg.norm(vector_768) * np.linalg.norm(vector_384)

cosine_similarity = embeddings_dot / norms_L2

print(cosine_similarity)
from langchain_community.document_loaders import PyPDFLoader
from langchain_text_splitters import RecursiveCharacterTextSplitter
from langchain_huggingface import HuggingFaceEmbeddings
from langchain_community.vectorstores import FAISS


class VectorService:

    @staticmethod
    def create_vector_store(pdf_path: str):

        loader = PyPDFLoader(pdf_path)
        documents = loader.load()

        splitter = RecursiveCharacterTextSplitter(
            chunk_size=1000,
            chunk_overlap=200
        )

        docs = splitter.split_documents(documents)

        #embeddings = HuggingFaceEmbeddings(model_name="sentence")
        embeddings = HuggingFaceEmbeddings(model_name="sentence-transformers/all-MiniLM-L6-v2")

        vectorstore = FAISS.from_documents(docs, embeddings)

        vectorstore.save_local("faiss_index")

        return vectorstore
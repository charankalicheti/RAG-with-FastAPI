# from langchain_openai import ChatOpenAI, OpenAIEmbeddings
# from langchain_groq import ChatGroq
# from langchain_huggingface import HuggingFaceEmbeddings
# from langchain_community.vectorstores import FAISS
# from langchain_classic.chains import RetrievalQA
# class RagService:

#     @staticmethod
#     def ask_question(question: str):

#         #embeddings = OpenAIEmbeddings()
#         embeddings = HuggingFaceEmbeddings(model_name="sentence-transformers/all-MiniLM-L6-v2")

#         vectorstore = FAISS.load_local(
#             "faiss_index",
#             embeddings,
#             allow_dangerous_deserialization=True
#         )

#         retriever = vectorstore.as_retriever(search_kwargs={"k": 3})

#         llm = ChatGroq(model="openai/gpt-oss-120b", temperature=0)

#         qa_chain = RetrievalQA.from_chain_type(
#             llm=llm,
#             retriever=retriever,
#             chain_type="stuff"
#         )

#         result = qa_chain.invoke(question)

#         return result

from langchain_community.document_loaders import PyPDFLoader

from langchain_text_splitters import RecursiveCharacterTextSplitter

from langchain_huggingface import HuggingFaceEmbeddings

from langchain_community.vectorstores import FAISS


from langchain_classic.chains import RetrievalQA

from langchain_groq import ChatGroq

from app.core.config import settings


class RagService:

    @staticmethod
    def create_vector_store(file_path: str):

        # Load PDF
        loader = PyPDFLoader(file_path)

        documents = loader.load()

        # Split documents
        splitter = RecursiveCharacterTextSplitter(
            chunk_size=1000,
            chunk_overlap=200
        )

        docs = splitter.split_documents(documents)

        # Embeddings
        embeddings = HuggingFaceEmbeddings(
            model_name="sentence-transformers/all-MiniLM-L6-v2"
        )

        # Create vector store
        vectorstore = FAISS.from_documents(
            docs,
            embeddings
        )

        # Save vector db
        vectorstore.save_local("faiss_index")

        return True


    @staticmethod
    def ask_question(question: str):

        # Embeddings
        embeddings = HuggingFaceEmbeddings(
            model_name="sentence-transformers/all-MiniLM-L6-v2"
        )

        # Load vector db
        vectorstore = FAISS.load_local(
            "faiss_index",
            embeddings,
            allow_dangerous_deserialization=True
        )

        retriever = vectorstore.as_retriever()

        # Groq LLM
        llm = ChatGroq(
            groq_api_key=settings.GROQ_API_KEY,
            model_name="openai/gpt-oss-120b"
        )

        # QA Chain
        qa_chain = RetrievalQA.from_chain_type(
            llm=llm,
            retriever=retriever,
            chain_type="stuff"
        )

        result = qa_chain.invoke(question)

        return result["result"]
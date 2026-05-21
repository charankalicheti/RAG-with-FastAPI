import streamlit as st
import requests
from datetime import datetime


# ---------------- CONFIG ----------------

BASE_URL = "http://127.0.0.1:8000"

st.set_page_config(
    page_title="Enterprise RAG Assistant",
    page_icon="🤖",
    layout="wide"
)


# ---------------- CUSTOM CSS ----------------

st.markdown(
    """
    <style>

    /* Main App Background */
    .stApp {
        background-color: white;
        color: black;
    }

    /* Sidebar */
    section[data-testid="stSidebar"] {
        background-color: #F8FAFC;
    }

    /* Main Container */
    .main {
        background-color: white;
    }

    /* Text Inputs */
    .stTextInput > div > div > input {
        background-color: white;
        color: black;
        border: 1px solid #D1D5DB;
        border-radius: 10px;
    }

    /* Password Input */
    .stTextInput input {
        color: black !important;
    }

    /* Chat Input */
    .stChatInput input {
        background-color: white !important;
        color: black !important;
        border: 1px solid #D1D5DB !important;
    }

    /* Buttons */
    .stButton>button {
        width: 100%;
        border-radius: 10px;
        height: 3em;
        background-color: #2563EB;
        color: white;
        font-weight: bold;
        border: none;
    }

    .stButton>button:hover {
        background-color: #1D4ED8;
        color: white;
    }

    /* Chat Cards */
    .chat-box {
        padding: 18px;
        border-radius: 14px;
        margin-bottom: 12px;
        border: 1px solid #E5E7EB;
        color: black;
    }

    /* User Message */
    .user-msg {
        background-color: #DBEAFE;
    }

    /* Assistant Message */
    .bot-msg {
        background-color: #F9FAFB;
    }

    /* Labels & Text */
    label, p, h1, h2, h3, h4, h5, h6, span, div {
        color: black !important;
    }

    </style>
    """,
    unsafe_allow_html=True
)


# ---------------- SESSION STATE ----------------

if "token" not in st.session_state:
    st.session_state.token = None

if "chat_history" not in st.session_state:
    st.session_state.chat_history = []


# ---------------- SIDEBAR ----------------

with st.sidebar:

    st.title("🤖 Enterprise RAG")

    auth_option = st.radio(
        "Choose Option",
        ["Login", "Register"]
    )

    st.markdown("---")


    # ---------------- REGISTER ----------------

    if auth_option == "Register":

        st.subheader("📝 Create Account")

        reg_username = st.text_input(
            "Username"
        )

        reg_email = st.text_input(
            "Email"
        )

        reg_password = st.text_input(
            "Password",
            type="password"
        )

        if st.button("Register"):

            try:

                response = requests.post(

                    f"{BASE_URL}/auth/register",

                    json={
                        "username": reg_username,
                        "email": reg_email,
                        "password": reg_password
                    }
                )

                if response.status_code == 200:

                    st.success("Registration Successful")

                else:

                    st.error(response.text)

            except Exception as e:

                st.error(str(e))


    # ---------------- LOGIN ----------------

    if auth_option == "Login":

        st.subheader("🔐 Login")

        email = st.text_input("Email")

        password = st.text_input(
            "Password",
            type="password"
        )

        if st.button("Login"):

            try:

                response = requests.post(

                    f"{BASE_URL}/auth/login",

                    json={
                        "email": email,
                        "password": password
                    }
                )

                if response.status_code == 200:

                    token = response.json()["access_token"]

                    st.session_state.token = token

                    st.success("Login Successful")

                else:

                    st.error("Invalid Credentials")

            except Exception as e:

                st.error(str(e))


    st.markdown("---")


    # ---------------- PDF UPLOAD ----------------

    if st.session_state.token:

        st.subheader("📄 Upload PDF")

        uploaded_file = st.file_uploader(
            "Choose PDF File",
            type=["pdf"]
        )

        if uploaded_file is not None:

            if st.button("Upload Document"):

                try:

                    headers = {
                        "Authorization": f"Bearer {st.session_state.token}"
                    }

                    files = {
                        "file": (
                            uploaded_file.name,
                            uploaded_file,
                            "application/pdf"
                        )
                    }

                    response = requests.post(
                        f"{BASE_URL}/rag/upload",
                        headers=headers,
                        files=files
                    )

                    if response.status_code == 200:

                        st.success("PDF Uploaded Successfully")

                    else:

                        st.error(response.text)

                except Exception as e:

                    st.error(str(e))


# ---------------- MAIN PAGE ----------------

st.title("📚 AI-Powered RAG Assistant")

st.caption(
    "Upload PDFs and chat with your documents using Groq + HuggingFace + LangChain"
)

st.markdown("---")


# ---------------- CHAT SECTION ----------------

if st.session_state.token:

    question = st.chat_input(
        "Ask a question from your uploaded document..."
    )

    if question:

        # Store User Message
        st.session_state.chat_history.append({
            "role": "user",
            "message": question,
            "time": datetime.now().strftime("%H:%M")
        })

        try:

            headers = {
                "Authorization": f"Bearer {st.session_state.token}"
            }

            data = {
                "question": question
            }

            response = requests.post(
                f"{BASE_URL}/rag/ask",
                headers=headers,
                data=data
            )

            if response.status_code == 200:

                answer = response.json()["answer"]

            else:

                answer = response.text

        except Exception as e:

            answer = str(e)

        # Store Bot Response
        st.session_state.chat_history.append({
            "role": "assistant",
            "message": answer,
            "time": datetime.now().strftime("%H:%M")
        })


    # ---------------- DISPLAY CHAT ----------------

    for chat in st.session_state.chat_history:

        if chat["role"] == "user":

            st.markdown(
                f'''
                <div class="chat-box user-msg">
                    <b>🧑 You</b><br><br>
                    {chat["message"]}
                    <br><br>
                    <small>{chat["time"]}</small>
                </div>
                ''',
                unsafe_allow_html=True
            )

        else:

            st.markdown(
                f'''
                <div class="chat-box bot-msg">
                    <b>🤖 Assistant</b><br><br>
                    {chat["message"]}
                    <br><br>
                    <small>{chat["time"]}</small>
                </div>
                ''',
                unsafe_allow_html=True
            )

else:

    st.info("Please login to continue.")
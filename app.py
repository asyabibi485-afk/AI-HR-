import streamlit as st

from document_loader import load_documents


st.set_page_config(
    page_title="Enterprise College HR Policy AI Assistant",
    page_icon="🎓",
    layout="wide",
)

st.title("🎓 Enterprise College HR Policy AI Assistant")
st.write("Stage 1: HR Policy Document Processing")

st.info(
    "This first version loads PDF, DOCX and TXT HR policy "
    "documents and extracts their text. RAG and FAISS will "
    "be added in the next stage."
)

with st.sidebar:
    st.header("📚 HR Documents")
    st.write(
        "Place your HR policy files inside the `data` folder."
    )
    st.write("Supported formats:")
    st.write("• PDF")
    st.write("• DOCX")
    st.write("• TXT")

documents = load_documents("data")

if not documents:
    st.warning("No HR policy documents were found.")
    st.markdown(
        """
        ### How to add documents

        1. Create/use the `data` folder.
        2. Put your HR policy PDF/DOCX/TXT files inside it.
        3. Restart the Streamlit application.

        Example:
        `data/leave_policy.pdf`
        `data/attendance_policy.pdf`
        `data/hr_manual.pdf`
        """
    )
else:
    st.success(f"Successfully loaded {len(documents)} document(s).")

    st.subheader("📄 Loaded HR Policy Documents")

    for document in documents:
        filename = document["filename"]
        text = document["text"]
        word_count = len(text.split())
        character_count = len(text)

        with st.expander(f"📄 {filename}"):
            col1, col2 = st.columns(2)

            with col1:
                st.metric("Words", word_count)

            with col2:
                st.metric("Characters", character_count)

            st.divider()
            st.subheader("Extracted Text")

            preview = text[:10000]

            st.text_area(
                "Document Preview",
                preview,
                height=400,
                key=f"preview_{filename}",
            )

            if len(text) > 10000:
                st.caption(
                    "Only the first 10,000 characters are shown."
                )

st.divider()
st.subheader("✅ Stage 1 Status")

if documents:
    st.success("Document loading is working successfully.")
    st.write("Next stage: document chunking and embeddings.")
else:
    st.warning("Add at least one HR policy document to continue.")

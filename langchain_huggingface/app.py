import streamlit as st
from PyPDF2 import PdfReader
import tempfile
from langchain.text_splitter import CharacterTextSplitter
from langchain.embeddings import HuggingFaceEmbeddings
from langchain.document_loaders import UnstructuredPDFLoader
from langchain.vectorstores import FAISS
from langchain.chains.question_answering import load_qa_chain
from langchain import HuggingFaceHub

import os
os.environ["HUGGINGFACEHUB_API_TOKEN"] = "your_api_key"

embedding = HuggingFaceEmbeddings()

def main():
    # Display the header for the application
    st.header("Chat with the PDF 😎💻")
    # Allow the user to upload a PDF file
    pdf = st.file_uploader("Upload your PDF", type="pdf")

    if pdf is not None:
        # Save the uploaded PDF to a temporary file
        with tempfile.NamedTemporaryFile(delete=False) as temp_pdf:
            temp_pdf.write(pdf.read())
            temp_pdf_path = temp_pdf.name

        # Load the PDF document from the temporary file
        loader = UnstructuredPDFLoader(temp_pdf_path)
        document = loader.load()

        # Convert the document into chunks of the desired size
        text_splitter = CharacterTextSplitter(chunk_size=1000, chunk_overlap=100)
        docs = text_splitter.split_documents(document)

        # Create a vector store from the document chunks
        db = FAISS.from_documents(docs, embedding)

        # Initialize the Hugging Face model for question answering
        llm = HuggingFaceHub(
            repo_id="lmsys/fastchat-t5-3b-v1.0",
            model_kwargs={"temperature": 0, "max_length": 400}
        )
        # Load the question answering chain
        chain = load_qa_chain(llm, chain_type="stuff")

        # Accept user's question/query
        query = st.text_input("Ask questions")

        if query:
            # Perform similarity search in the document database
            docs = db.similarity_search(query)
            # Generate the response using the question answering chain
            response = chain.run(input_documents=docs, question=query)
            # Display the response to the user
            st.write(response.replace("<pad>", ""))

        # Remove the temporary PDF file
        os.remove(temp_pdf_path)
    else:
        st.write("Upload a PDF to continue.")

if __name__ == "__main__":
    main()

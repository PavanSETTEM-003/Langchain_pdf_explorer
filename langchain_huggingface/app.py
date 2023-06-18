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
os.environ["HUGGINGFACEHUB_API_TOKEN"] = "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"

embedding = HuggingFaceEmbeddings()

def main():
    st.header("Chat with the PDF 😎💻")
    pdf = st.file_uploader("Upload your PDF", type="pdf")

    if pdf is not None:

        # Save the uploaded PDF to a temporary file
        with tempfile.NamedTemporaryFile(delete=False) as temp_pdf:
            temp_pdf.write(pdf.read())
            temp_pdf_path = temp_pdf.name

        loader = UnstructuredPDFLoader(temp_pdf_path)
        document = loader.load()

        # Converting document into chunks of the desired size
        text_splitter = CharacterTextSplitter(chunk_size=1000, chunk_overlap=100)
        docs = text_splitter.split_documents(document)

        db = FAISS.from_documents(docs, embedding)

        llm=HuggingFaceHub(
            repo_id="lmsys/fastchat-t5-3b-v1.0",
            model_kwargs={"temperature":0, "max_length":400}
            )
        chain = load_qa_chain(llm, chain_type="stuff")

        # accept user  queston/query
        query = st.text_input("ask questions")
        # st.write(query)

        if query:
            docs = db.similarity_search(query)
            response = chain.run(input_documents=docs, question=query)
            st.write(response.replace("<pad>",""))
        
        os.remove(temp_pdf_path)

    else:
        st.write("Upload a PDF to continue.")


if __name__ == "__main__":
    main()


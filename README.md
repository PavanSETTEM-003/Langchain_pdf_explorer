<h1>LLM-Powered PDF Chatbot: Conversational Question Answering for Local Documents</h1>

<p>
  Welcome to LangChain-HuggingFace PDF Explorer, an innovative tool that empowers you to gain valuable insights from your PDF documents. Harnessing the power of Language Models (LLMs), this code enables you to extract meaningful information by simply uploading your PDF and asking questions.
</p>
<p>It is recommended to run the project in a virtual environment (venv) to avoid library clashes. This isolates Python packages for different projects, ensuring different versions of the same package can be used without conflicts. Running the project in a venv also prevents any project-specific packages from polluting your system Python installation.</p>

<p>Make sure you have Python's <code>venv</code> package installed. If not, install it by running the following command:</p>

<pre><code>pip install venv</code></pre>

<h2>Setup and Run Instructions</h2>

<p>To set up and run the project locally, follow the steps below:</p>

<ol>
  <li>Open a new folder, create a virtual environment, and activate it:</li>

  <pre><code>python -m venv langchainenv</code></pre>

  <p>On Windows:</p>

  <pre><code>.\langchainenv\Scripts\activate</code></pre>

  <p>On Unix/Linux:</p>

  <pre><code>source langchainenv/bin/activate</code></pre>

  <li>Clone this repository and navigate to the cloned repository:</li>

  <pre><code>git clone https://github.com/PavanSETTEM-003/Langchain_pdf_explorer.git</code></pre>

  <pre><code>cd Langchanin-PDF-Explorer</code></pre>

  <li>Install the required dependencies:</li>

  <pre><code>pip install -r requirements.txt</code></pre>

  <li>Open the <code>app.py</code> file and add your Hugging Face access key:</li>

  <pre><code>os.environ["HUGGINGFACEHUB_API_TOKEN"] = "&lt;your-access-key&gt;"</code></pre>

  <li>Start the application:</li>

  <pre><code>streamlit run app.py</code></pre>

  <p>This will start a local server, and a web page will open in your default browser.</p>

  <li>Use the web page interface to upload a PDF file and ask questions about its content.</li>
</ol>

<p><strong>Note:</strong> Ensure you have an active internet connection as the application uses Hugging Face's API for language model inference.</p>

<p>All the dependencies are listed in the <code>requirements.txt</code> file and will be installed during the setup process.</p>

<hr>
<div>
  <h2>Code Explanation</h2>

<p>1. Libraries:</p>
<ul>
  <li><code>streamlit</code>: A Python library used for creating interactive web applications.</li>
  <li><code>PyPDF2</code>: A Python library for working with PDF files.</li>
  <li><code>tempfile</code>: A Python library for creating and managing temporary files.</li>
  <li><code>langchain</code>: A custom library that offers text processing tools and functionalities.</li>
  <li><code>HuggingFaceHub</code>: A library for working with pre-trained models from the Hugging Face model hub.</li>
  <li><code>FAISS</code>: A library for efficient similarity search and retrieval of vectors.</li>
</ul>

<p>2. Document Processing:</p>
<ul>
  <li>The code utilizes <code>PyPDF2</code> to read and extract content from uploaded PDF files.</li>
  <li>The extracted document is divided into smaller text chunks using the <code>CharacterTextSplitter</code> from <code>langchain</code>, enabling efficient processing and retrieval.</li>
</ul>

<p>3. Vector Store Creation:</p>
<ul>
  <li>The <code>HuggingFaceEmbeddings</code> class from <code>langchain</code> converts the text chunks into numerical embeddings that capture the semantic representation of the text.</li>
  <li>The vector store is created using <code>FAISS</code>, allowing for efficient indexing and similarity-based search of document vectors.</li>
</ul>

<p>4. Question Answering:</p>
<ul>
  <li>The code initializes a question answering model from the Hugging Face model hub using <code>HuggingFaceHub</code>.</li>
  <li>The <code>load_qa_chain</code> function from <code>langchain</code> is used to create a question answering chain, incorporating the question answering model and additional processing steps.</li>
</ul>

<p>5. User Interaction:</p>
<ul>
  <li><code>streamlit</code> is used to create an interactive user interface for uploading PDF files and inputting questions.</li>
  <li>Upon receiving a user's question, the code performs a similarity search in the vector store to identify the most relevant document chunks.</li>
  <li>The question answering chain is then executed on the selected document chunks to generate a response.</li>
</ul>

<p>These technical components collectively enable the code to handle PDF uploads, process the documents, create vector representations, perform similarity searches, and provide question answering functionality.</p>

</div>
<hr>
<h2>Results</h2>
<div class="image-container">
    <ol>
        <li> <figure>
            <figcaption>
                Provided a 35-page ML theory tutorial PDF and tested over it.
              </figcaption>
          <br>
            <img src="https://github.com/PavanSETTEM-003/Langchanin-PDF-Explorer/assets/88257205/79843a29-64a3-4e00-8aa3-29bc8bca5a82" ></figure></li>
      <br>
      <li><figure>
            <figcaption>
              Tested the TCS Transcript 4QFY23 PDF, which consisted of 24 pages.
            </figcaption>
          <br>
          <img src="https://github.com/PavanSETTEM-003/Langchanin-PDF-Explorer/assets/88257205/19bd6f69-8cbf-40b8-8317-f227ce429a10">
          </figure></li>
    </ol>
</div>

<hr>
<h2>Conclusion</h2>
The code offers the capability to efficiently extract insights from local documents. It can be applied to various use cases, such as financial report analysis, educational PDF question assistance for students, and rapid knowledge extraction from research papers. Its versatility enables swift and targeted information retrieval from diverse document sources, empowering users to gain valuable insights effectively.It can be adapted and customized to suit different industries, domains, and specific requirements.

<br>
<br>



Explore the code to meet your specific needs. We highly value your feedback as it enables us to continuously improve the functionality and usability of the code.

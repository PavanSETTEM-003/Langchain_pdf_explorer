<h1>LLM-Powered PDF Chatbot: Conversational Question Answering for Local Documents</h1>

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

  <pre><code>git clone https://github.com/PavanSETTEM-003/Langchanin-PDF-Explorer.git</code></pre>

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

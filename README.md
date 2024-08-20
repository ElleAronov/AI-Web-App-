This project is an interactive web application built using Streamlit and various NLP tools from Hugging Face Transformers. The app allows users to input a URL, fetch and process the webpage content, and then perform a series of NLP tasks such as question-answering, summarization, and generating word clouds. Additionally, users can export the results as a PDF file.

**Features:**

Question Answering: Ask questions based on the content of a webpage and receive accurate answers using the Hugging Face Transformers' question-answering pipeline.
Summarization: Generate a concise summary of the webpage content.
Word Cloud Generation: Create and display a word cloud from the webpage text to visualize the most frequent terms.
Export to PDF: Save the summarized content and Q&A results as a PDF file.

**Technologies Used:**

Streamlit: For creating the web interface.
Hugging Face Transformers: For implementing NLP tasks like question-answering and summarization.
BeautifulSoup: For parsing HTML content from web pages.
Requests: For fetching web page content.
Plotly Express: For creating visualizations (future extension).
WordCloud: For generating word clouds from text.
pdfkit: For exporting content to PDF.

**How to Run**

Clone the repository:
git clone https://github.com/your-username/interactive-qa-web-app.git
cd interactive-qa-web-app

Install the required packages:
pip install -r requirements.txt

Run the Streamlit app:
streamlit run app.py

Open your browser and go to http://localhost:8501 to interact with the app.

**Usage**

Enter a URL to fetch and process the webpage content.
Use the Q&A section to ask questions about the content.
Generate a summary of the webpage or a word cloud to visualize key terms.
Export the results to a PDF file.

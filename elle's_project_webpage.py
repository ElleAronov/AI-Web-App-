import streamlit as st
from transformers import pipeline
from bs4 import BeautifulSoup
import requests
import plotly.express as px
from wordcloud import WordCloud
import pdfkit

# Initialize pipelines
qa_pipeline = pipeline("question-answering")
summarizer = pipeline("summarization")

def fetch_webpage(url):
    response = requests.get(url)
    if response.status_code == 200:
        return response.text
    else:
        return None

def parse_webpage(content):
    soup = BeautifulSoup(content, 'html.parser')
    text = soup.get_text(separator=' ')
    return text

def answer_question(question, context):
    result = qa_pipeline(question=question, context=context)
    return result['answer']

def summarize_content(content):
    summary = summarizer(content, max_length=500, min_length=30, do_sample=False)
    return summary[0]['summary_text']

def create_wordcloud(text):
    wordcloud = WordCloud().generate(text)
    return wordcloud.to_image()

def save_to_pdf(content, filename):
    pdfkit.from_string(content, filename)

st.title("Interactive Q&A Web App")

# Input URL
url = st.text_input("Please enter a URL of your choice")
if url:
    webpage_content = fetch_webpage(url)
    if webpage_content:
        parsed_content = parse_webpage(webpage_content)
        st.write("Webpage content loaded...")

        # Q&A Section
        question = st.text_input("Ask a question")
        if question:
            answer = answer_question(question, parsed_content)
            st.write("Answer:", answer)

        # Summarization Section
        if st.button("Want a summary?"):
            summary = summarize_content(parsed_content)
            st.write("Summary:", summary)

        # Word Cloud Section
        if st.button("Generate Word Cloud"):
            wordcloud_image = create_wordcloud(parsed_content)
            st.image(wordcloud_image)

        # Export to PDF
        if st.button("Export here to PDF"):
            pdf_content = f"Summary: {summary}\n\nQ&A: {answer}"
            save_to_pdf(pdf_content, "output.pdf")
            st.write("Exported to output.pdf")
    else:
        st.write("Failed to load webpage content.")

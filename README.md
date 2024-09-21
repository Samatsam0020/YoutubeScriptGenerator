# 📜 Automated Script Generator

Welcome to the Automated Script Generator project! The primary goal of this project is to develop a system that synthesizes transcripts from multiple YouTube videos into a cohesive script. By leveraging the YouTube Transcript API and the Google Gemini API, this tool aims to simplify content creation by consolidating information from various sources into a single, coherent document.

## Features

- 🎥 **YouTube Transcript Integration:** Automatically fetch transcripts from multiple YouTube videos.
- 🧠 **Content Synthesis:** Utilize the Google Gemini API to generate a cohesive script from the gathered transcripts.
- ✨ **User-Friendly Output:** Receive a well-structured and easily readable document for your content needs.

## Requirements

Before running the project, ensure you have Python installed. You can install the required packages with:

```bash
pip install -r requirements.txt

## Setup

Create a .env file: In the root directory of the project, create a file named .env and add your Google Gemini API key in the following format:
GEMINI_API_KEY=your_api_key_here

Run the Application
```bash
streamlit run python app.py

from dotenv import load_dotenv
import os
import getpass
from youtube_transcript_api import YouTubeTranscriptApi
from .utils import link_id_from_link, format_script
from langchain_google_genai import ChatGoogleGenerativeAI
from langchain.prompts import PromptTemplate
from langchain.chains import LLMChain
import streamlit as st

load_dotenv()
GEMINI_KEY = os.getenv('GEMINI_API_KEY')
if "GOOGLE_API_KEY" not in os.environ:
    os.environ["GOOGLE_API_KEY"] = GEMINI_KEY

llm = ChatGoogleGenerativeAI(model="gemini-pro")

prompt_template = PromptTemplate(
    input_variables=['text_script'],
    template="""
    as input I give you one or more scripts youtube videos and you will give me the 
    best script possible for this text to facilitate content creation by synthesizing
    information from various sources into a single, coherent document. 
    That the output be in English even if the text provided is in French.
    Here it is :
    {text_script}
    """
)
chain = LLMChain(llm=llm, prompt=prompt_template)


def generate_script(liste_link):

    all_text = ''

    for i, _ in enumerate(liste_link):
        link_id = link_id_from_link(liste_link[i])
        print(link_id)
        try:
            script = YouTubeTranscriptApi.get_transcript(link_id)

        except:
            script = YouTubeTranscriptApi.get_transcript(link_id, 'fr')

        text = format_script(script)
        all_text += f"{i} script \n {text} "
    text_script = chain.run(all_text)

    return text_script

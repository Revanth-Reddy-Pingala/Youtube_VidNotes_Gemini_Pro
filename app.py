import streamlit as st
from st_functions import st_button, load_css
from dotenv import load_dotenv
load_dotenv() ##load all the nevironment variables
import os
import google.generativeai as genai
from youtube_transcript_api import YouTubeTranscriptApi

load_css()

#Comment these two lines and Uncomment below one if you are running this project locally in your computer.
api_key = st.secrets["GOOGLE_API_KEY"]
genai.configure(api_key=api_key)

#Uncomment this line if you are running this project locally in your computer.
#genai.configure(api_key=os.getenv("GOOGLE_API_KEY"))

prompt="""
        Title: Detailed Notes from YouTube Video Transcript

        As a Youtube video expert, your task is to provide detailed notes based on the transcript of a YouTube video I'll provide. Assume the role of a student and generate comprehensive notes covering the key concepts discussed in the video.
 
        Your notes should:
        - Be detailed and comprehensive.
        - Cover the key concepts discussed in the video.
        - Highlight the main points and key takeaways in the video.
        - Explain about every detail of the video.

        Please provide the YouTube video transcript, and I'll generate the detailed notes on Youtube video accordingly.
        """


## getting the transcript data from yt videos
def extract_transcript_details(youtube_video_url):
    try:
        video_id=youtube_video_url.split("=")[1]
        
        transcript_text=YouTubeTranscriptApi.get_transcript(video_id)

        transcript = ""
        for i in transcript_text:
            transcript += " " + i["text"]

        return transcript

    except Exception as e:
        raise e
    
## getting the summary based on Prompt from Google Gemini Pro
def generate_gemini_content(transcript_text,prompt):
    model=genai.GenerativeModel("gemini-pro")
    response=model.generate_content(prompt+transcript_text)
    return response.text

st.title("𝚈𝚘𝚞𝚝𝚞𝚋𝚎 VidNotes 📝📚")
st.info("Youtube Video 🎥 Transcript to Detailed Notes 📋 Converter using Google Gemini Pro. This web app efficiently works with videos having English Transcript and Generates notes 🚀. Support for other languages not yet provided. Please enter the YouTube video link in the Text Box and Click on the button to get the detailed notes.")
youtube_link = st.text_input("Enter YouTube Video Link:")

if youtube_link:
    video_id = youtube_link.split("=")[1]
    print(video_id)
    st.image(f"http://img.youtube.com/vi/{video_id}/0.jpg", use_column_width=True)

if st.button("Get Video Notes"):
    transcript_text=extract_transcript_details(youtube_link)

    if transcript_text:
        summary=generate_gemini_content(transcript_text,prompt)
        st.markdown("## Detailed Notes:")
        st.write(summary)

icon_size = 24
st_button('youtube', 'https://www.youtube.com/watch?v=WzkyUtuYG9w', '   Youtube Video Demo', icon_size)
st_button('linkedin', 'https://www.linkedin.com/in/revanth-reddy-pingala/', '   Connect with me on LinkedIn', icon_size)
st_button('github', 'https://github.com/Revanth-Reddy-Pingala', '   Check my Github Profile', icon_size)
st_button('youtube', 'https://www.youtube.com/channel/UCpa8TsplHTVeUbcAv-I4osQ', '   My Youtube Channel', icon_size)
st_button('medium', 'https://rrdatadiaries.blogspot.com/', '   Read my Blogs', icon_size)
st_button('instagram', 'https://www.instagram.com/revanth_reddy.1459/', '   Follow me on Instagram', icon_size)

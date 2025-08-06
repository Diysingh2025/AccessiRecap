import os
import streamlit as st
from input_summary import get_user_input_streamlit
from save_pdf import save_to_pdf
from send_mail import send_gmail_email
from question_detection import extract_questions
from text_to_audio import text_to_audio
from sentiment_analysis import analyze_sentiment

# Suppress TensorFlow logs and warnings
os.environ['TF_CPP_MIN_LOG_LEVEL'] = '3'

st.set_page_config(page_title="AccessiRecap", layout="centered")
st.title("AccessiRecap: Your Meeting Summary Assistant")

# User Input
summary, font_choice, font_size, font_color, filename = get_user_input_streamlit()

# Save PDF
if st.button("Save PDF"):
    save_to_pdf(summary, font_choice, font_size, font_color, filename)
    with open(filename, "rb") as f:
        st.download_button("Download PDF", f, file_name=filename, mime="application/pdf")


# Sentiment Analysis
if st.checkbox(" Analyze the summary sentiment"):
    sentiment, _ = analyze_sentiment(summary)
    st.markdown(f"**Sentiment:** `{sentiment}`")

# Detect Questions
if st.checkbox("Detect Questions in Summary"):
    questions = extract_questions(summary)
    if questions:
        st.write("Questions found:")
        for i, q in enumerate(questions, 1):
            st.markdown(f"{i}. {q}")
    else:
        st.info("No questions detected.")

# Generate Audio
audio_path = None
if st.checkbox(" Generate Audio Summary"):
    audio_path = text_to_audio(summary)
    if audio_path:
        with open(audio_path, "rb") as f:
            st.audio(f.read(), format="audio/mp3")

#Send Email
with st.expander("Send Email"):
    app_password = st.text_input("Your Gmail App Password", type="password")
    recipients = st.text_input("Recipient mails (comma-separated)")
    subject = st.text_input("Email Subject", value="Meeting Summary PDF")
    body = st.text_area("Email Body", value="Attached is the summary material for your reference.")

    if st.button("Send Mail"):
        if app_password and recipients:
            send_gmail_email(
                app_password,
                [r.strip() for r in recipients.split(",")],
                subject,
                body,
                filename,
                audio_path
            )
            st.success("Mail sent successfully!!")
        else:
            st.error("Please provide both app password and recipient emails.")
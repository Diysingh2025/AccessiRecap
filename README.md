# AccessiRecap: AI-powered meeting accessibility tool
AccessiRecap is an AI-powered tool that generates simplified, accessible summaries. It supports PDF export, custom fonts for readability, and audio playback designed to enhance inclusivity for users with cognitive or visual disabilities.

**Features**:

 **Accessible PDF Export**
Custom font options (including OpenDyslexic and Tiresias), font size, and color choices for readability and accessibility. PDFs are saved locally for sharing and recordkeeping.

 **Question Detection**
Highlights questions from summaries using NLP + heuristic rules to help teams identify discussion gaps or follow-up items.

**Emailing to Stakeholder**
Send meeting summaries to external Stakeholders, not just attendees. Useful for accessibility coordinators or team members who missed the meeting.

 **Text-to-Audio Conversion**
Converts summaries into audio using gTTS, enabling auditory consumption of meeting content.

**Sentiment Analysis**

 **Multilingual Support**
Translate summaries into multiple languages.

**Keyword & Action Item Detection** 
Automatically extract action points to streamline task assignment and recap emails.


**Tech Stack**
Python 3.10+

Hugging Face Transformers – question detection and Sentiment analysis

gTTS – for converting text to audio

ReportLab – for PDF generation

Streamlit – for UI implementation

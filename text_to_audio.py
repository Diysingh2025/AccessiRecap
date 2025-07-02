from gtts import gTTS
import os

def text_to_audio(summary_text, output_file="summary_audio.mp3"):
    try:
        tts = gTTS(text=summary_text)
        tts.save(output_file)
        print(f"\n Audio summary saved as: {output_file}")
        os.system(f"start {output_file}") 
    except Exception as e:
        print(f" Error generating audio: {e}")
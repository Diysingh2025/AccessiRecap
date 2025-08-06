import streamlit as st
from reportlab.lib.colors import toColor, black, Color

def get_user_input_streamlit():
    st.subheader(" Enter Summary")

    summary = st.text_area("Please paste your meeting summary here:", height=200)

    font_option = st.selectbox(" Choose a font", [
        "Default",
        "OpenDyslexic",
        "Tiresias",
        "Garamond",
        "Tahoma",
        "Verdana"
    ])

    font_mapping = {
        "Default": "Helvetica",
        "OpenDyslexic": "OpenDyslexic",
        "Tiresias": "Tiresias",
        "Garamond": "Garamond",
        "Tahoma": "Tahoma",
        "Verdana": "Verdana"
    }
    font_choice = font_mapping.get(font_option, "Helvetica")

    font_size = st.slider("Font size", 10, 50, 15)

    use_safe_colors = st.checkbox(" Do you want to use colorblind-safe font color?")

    font_color = black

    if use_safe_colors:
        colorblind_safe_colors = {
            "Sky Blue": Color(0.337, 0.706, 0.914),
            "Bluish Green": Color(0, 0.62, 0.451),
            "Yellow": Color(0.941, 0.894, 0.259)
        }
        selected_color_name = st.selectbox("Choose a color", list(colorblind_safe_colors.keys()))
        font_color = colorblind_safe_colors.get(selected_color_name, black)
    else:
        custom_color = st.color_picker("Pick a font color", "#000000")
        try:
            font_color = toColor(custom_color)
        except Exception:
            st.warning("Invalid color selected, falling back on black.")
            font_color = black

    filename = st.text_input("Output filename (without `.pdf`)", "Summary_Pdf")
    if not filename.endswith(".pdf"):
        filename += ".pdf"

    return summary, font_choice, font_size, font_color, filename

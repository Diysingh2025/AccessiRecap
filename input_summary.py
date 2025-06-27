from reportlab.lib.colors import toColor
from reportlab.lib.colors import black
from reportlab.lib.colors import Color

def get_user_input():
    print("Enter the summary (press enter twice to finish):")
    lines = []
    while True:
        line = input()
        if line.strip() == "":
            break
        lines.append(line)
    summary = "\n".join(lines)

    font_option = input("Available fonts \n 1: Default \n 2: OpenDyslexic \n 3: Tiresias \n 4: Garamond \n 5: Tahoma \n 6: Veradana \n Choose font: ").strip()


    if font_option == "2":
        font_choice = "OpenDyslexic"
    elif font_option == "3":
        font_choice = "Tiresias"
    elif font_option == "4":
        font_choice= "Garamond"
    elif font_option == "5":
        font_choice= "Tahoma"
    elif font_option == "6":
        font_choice= "Verdana"
    else:
        font_choice = "Helvetica"

    try:
        font_size = int(input("Enter font size: ").strip())
    except ValueError:
        font_size = 15
        print("Invalid font size. Using 15.")

    use_safe_colors = input("Do you want to use a colorblind-safe font color?: ").strip().lower()

    colorblind_safe_colors = { "Sky Blue": Color(0.337, 0.706, 0.914), "Bluish Green": Color(0, 0.62, 0.451), "Yellow": Color(0.941, 0.894, 0.259) }
   
    if use_safe_colors in ['yes', 'y']:
        print("Available colorblind safe colors:")
        for i, color_name in enumerate(colorblind_safe_colors, 1):
            print(f"  {i}: {color_name}")

        choice = input("Choose a color: ").strip()
        try:
            if choice.isdigit():
                index = int(choice) - 1
                color_name = list(colorblind_safe_colors.keys())[index]
            else:
                color_name = choice.title()

            font_color = colorblind_safe_colors[color_name]
        except Exception:
            print(f"Invalid choice. Using default black.")
            font_color = black
    else:
        color_input = input("Enter font color u want: ").strip()
        try:
            font_color = toColor(color_input)
        except Exception:
            print(f"Invalid color '{color_input}'. Using default.")
            font_color = black

    filename = input("Enter the file name  (without .pdf): ").strip()
    if not filename:
        filename = "Summary_Pdf"
    filename += ".pdf"

    return summary, font_choice, font_size, font_color, filename

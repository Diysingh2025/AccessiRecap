from input_summary import get_user_input
from save_pdf import save_to_pdf
from send_mail import send_gmail_email
import pwinput

if __name__ == "__main__":
    summary, font_choice, font_size, font_color, filename = get_user_input()
    save_to_pdf(summary, font_choice, font_size, font_color, filename)

    send_choice = input("Want to send this PDF to Stakeholders? (y/n): ").strip().lower()
    if send_choice in ("y", "yes"):
        password = pwinput.pwinput(prompt="Your app password: ", mask="*")
        recipients = input("Recipient mails (separated by comma): ").strip().split(",")
        body = "Attached is the summary PDF for your reference."
        send_gmail_email(password, recipients, body, filename)
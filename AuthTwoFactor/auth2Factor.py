import smtplib
import random
import string
from email.mime.text import MIMEText
from email.mime.multipart import MIMEMultipart

def generate_verification_code(length=6):
    """Genera un codice di verifica casuale."""
    return ''.join(random.choices(string.ascii_uppercase + string.digits, k=length))

def send_email(sender_email, sender_password, recipient_email, smtp_server, smtp_port, verification_code):
    """Invia un'email contenente il codice di verifica."""
    try:
        # Creazione del messaggio email
        message = MIMEMultipart()
        message["From"] = sender_email
        message["To"] = recipient_email
        message["Subject"] = "Codice di verifica"

        body = f"Il tuo codice di verifica è: {verification_code}"
        message.attach(MIMEText(body, "plain"))

        # Connessione al server SMTP
        with smtplib.SMTP(smtp_server, smtp_port) as server:
            server.starttls()  # Avvia la connessione sicura
            server.login(sender_email, sender_password)
            server.send_message(message)

        print("Email inviata con successo!")
    except Exception as e:
        print(f"Errore nell'invio dell'email: {e}")

def email_verification_flow():
    """Flusso principale del programma per l'invio e verifica del codice."""
    # Configurazione dell'email del mittente
    sender_email = "mecitypark@gmail.com"  # Sostituisci con il tuo indirizzo email
    sender_password = "kmbn pdki kpsy nmau"  # Sostituisci con la tua password dell'email

    # Configurazione del destinatario e del server SMTP
    recipient_email = input("Inserisci l'email del destinatario: ")
    smtp_server = "smtp.gmail.com"  # Per Gmail (puoi sostituire con smtp-mail.outlook.com per Outlook)
    smtp_port = 587

    # Generazione del codice di verifica
    verification_code = generate_verification_code()
    print(f"Codice generato: {verification_code}")

    # Invio dell'email
    send_email(sender_email, sender_password, recipient_email, smtp_server, smtp_port, verification_code)

    # Verifica del codice da parte dell'utente
    user_input = input("Inserisci il codice di verifica ricevuto: ")
    if user_input == verification_code:
        print("Verifica completata con successo!")
    else:
        print("Codice errato. Riprova.")

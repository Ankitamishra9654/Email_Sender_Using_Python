import smtplib
from email.message import EmailMessage


server = smtplib.SMTP_SSL("smtp.gmail.com", 465)

server_login_mail = "ankita.mishra0168@gmail.com"
server_login_password = "Enter your App specific password"  

try:
    server.login(server_login_mail, server_login_password)

    user_input_mail = input("Enter recipient address")
    subject = input("Enter email subject: ")
    message = input("Enter email message: ")

    
    email = EmailMessage()
    email['From'] = server_login_mail
    email['To'] = user_input_mail
    email['Subject'] = subject
    email.set_content(message)

    
    server.send_message(email)
    print("Email sent successfully!")

except smtplib.SMTPAuthenticationError as e:
    print("SMTP Authentication error:", e)
except smtplib.SMTPException as e:
    print("SMTP error occurred:", e)
except Exception as e:
    print("Error:", e)

finally:
    server.quit()

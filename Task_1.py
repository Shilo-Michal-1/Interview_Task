import smtplib
import re

# A function that receives data from the user and sends an email accordingly


def send_email(subject, body, to_email):

    from_email = 'Python'
    username = 'michal.studyingathome@gmail.com'
    password = '212369995'
    msg = "\r\n".join([
        "From: {}".format(from_email),
        "To: {}".format(to_email),
        "Subject: {}".format(subject),
        "",
        body
    ])

    try:
        server = smtplib.SMTP('smtp.gmail.com:587')
        server.ehlo()
        server.starttls()
        server.login(username, password)
        server.sendmail(from_email, to_email, msg)
        return 1
    except:
        return 0


if __name__ == '__main__':

        subject = input("Enter an email subject")
        content = input("Enter an email content")
        email_address = input("Enter an email address")

        regex = r'\b[A-Za-z0-9._%+-]+@[A-Za-z0-9.-]+\.[A-Z|a-z]{2,}\b'
        if re.fullmatch(regex, email_address) is None:
            print("The email address is invalid")

        elif subject == "":
            print("There is no subject for this email")

        else:
            isvalid = send_email(subject, content, email_address)
            if isvalid == 1:
                print("Your email has been sent successfully")
            else:
                print("The email sending process failed")









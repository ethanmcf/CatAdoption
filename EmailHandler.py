import smtplib

class EmailHandler:
    def __init__(self):
        self.EMAIL_ADDRESS = 'ethanmcf2@gmail.com'
        self.PASSWORD = 'Hellsatins7&'

    def send_email(self, message, reciver):
        with smtplib.SMTP('smtp.gmail.com',587) as smtp:
            smtp.ehlo()
            smtp.starttls()
            smtp.ehlo()

            smtp.login(self.EMAIL_ADDRESS, self.PASSWORD)
            smtp.sendmail(self.EMAIL_ADDRESS, reciver, message)

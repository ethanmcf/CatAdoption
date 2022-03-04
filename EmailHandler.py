import smtplib
from email.message import EmailMessage

class EmailHandler:
    def __init__(self):
        self.EMAIL_ADDRESS = 'ethanmcf2@gmail.com'
        self.PASSWORD = 'Hellsatins7&'
        self.contacts = ['ethan_mcfarland@outlook.com','scottmcf@bell.net','highland_las@hotmail.com']

    def send_email(self, cat_messages, links):
        msg = EmailMessage()
        msg['Subject'] = 'New cats up for adoption!'
        msg['From'] = self.EMAIL_ADDRESS
        msg['To'] = ', '.join(self.contacts)

        html = """\
        <!DOCTYPE html>
        <html>
            <body>
                <p>Hey McFamily, new cats where posted for adoption: </p>
                <p></p>"""
        for i in range(0,len(links)):
            html += (
                """
                <p>"""+cat_messages[i]+"""</p> 
                <a href="""+links[i]+""">Click here to view</a>
                """)
        html += """
            </body>
        </html>
        """
        msg.add_alternative(html,subtype='html')

        with smtplib.SMTP_SSL('smtp.gmail.com', 465) as smtp:
            smtp.login(self.EMAIL_ADDRESS, self.PASSWORD)

            smtp.send_message(msg)


import smtplib

server = smtplib.SMTP_SSL("smtp.gmail.com",465)
server.login("cybertrack73@gmail.com","LnJhz4wsS22Yqka")
server.sendmail(f"cybertrack73@gmail.com","atharavatadas0@gmail.com","hi")
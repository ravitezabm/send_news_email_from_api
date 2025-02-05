import smtplib,ssl


def send_mail(msg):
    host = "smtp.gmail.com"
    port =465

    username = "abhiramanrs200@gmail.com"
    password = "gfgogabfxvzwkxdr"

    context = ssl.create_default_context()

    receiver = "abhiramanrs200@gmail.com"

    with smtplib.SMTP_SSL(host,port,context=context) as server:
        server.login(username,password)
        server.sendmail(username,receiver,msg)
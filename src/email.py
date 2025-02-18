import smtplib
from email.mime.multipart import MIMEMultipart
from email.mime.base import MIMEBase
from email import encoders

def send_email_with_report():
    fromaddr = "mi_email@dominio.com"
    toaddr = "destinatario@dominio.com"
    msg = MIMEMultipart()
    msg['From'] = fromaddr
    msg['To'] = toaddr
    msg['Subject'] = "Reporte Diario"

    body = "Adjunto el reporte generado en Excel."

    msg.attach(MIMEText(body, 'plain'))

    filename = "reporte.xlsx"
    attachment = open("data/reporte.xlsx", "rb")
    
    part = MIMEBase('application', 'octet-stream')
    part.set_payload(attachment.read())
    encoders.encode_base64(part)
    part.add_header('Content-Disposition', "attachment; filename= %s" % filename)
    msg.attach(part)

    server = smtplib.SMTP('smtp.gmail.com', 587)
    server.starttls()
    server.login(fromaddr, "mi_contraseña")
    text = msg.as_string()
    server.sendmail(fromaddr, toaddr, text)
    server.quit()

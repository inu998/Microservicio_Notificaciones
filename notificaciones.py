
import os
from flask import Flask,render_template, request, redirect,url_for,flash
from sendgrid import SendGridAPIClient
from sendgrid.helpers.mail import Mail

app = Flask(__name__)

@app.route("/")
def hello():
    return "<p>Prueba</p>"

@app.route('/enviarCorreo')
def Enviar_correo():
    sendgrid_key = os.environ['SENGRID_API_KEY']
    correo = request.args.get('correo')
    asunto = request.args.get('asunto')
    mensaje = request.args.get('mensaje')
    
    message = Mail(
        from_email='mejiabrayan000@gmail.com',       
        to_emails=correo,
        subject=asunto,
        html_content=mensaje)
    try:
        sg = SendGridAPIClient(os.environ.get('SENGRID_API_KEY'))
        response = sg.send(message)
        print(response.status_code)
        print(response.body)
        print(response.headers)
        return('Correo electronico enviado exitosamente')
    except Exception as e:
        print(e.message)
        return('Fallo el envio del correo electronico')
    

if __name__ == '__main__':
    app.run()
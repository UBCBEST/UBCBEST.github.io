import flask
import smtplib

from email.mime.text import MIMEText

app = flask.Flask(__name__)


@app.route('/')
def index():
    return flask.render_template('index.html')


@app.route('/api/email', methods=['POST'])
def send_email():
    data = flask.request.get_json()

    msg = MIMEText(data['body'] + '\n\n' + data['name'])
    msg['Subject'] = data['subject']
    msg['From'] = data['email']
    msg['To'] = 'best.ubc@gmail.com'

    s = smtplib.SMTP('smtp.mailgun.org', 587)

    s.login('postmaster@sandboxdc686bea42dd461588344b6135d7b757.mailgun.org', '07c05c110d3caeef2b6786ad2f2be051')
    s.sendmail(msg['From'], msg['To'], msg.as_string())
    s.quit()

    return flask.jsonify({
        'status': 'success',
        'message': 'woooo'
    })


if __name__ == '__main__':
    app.debug = True
    app.run()

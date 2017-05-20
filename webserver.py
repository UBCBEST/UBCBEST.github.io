import flask
import smtplib

from email.mime.text import MIMEText

app = flask.Flask(__name__)
with open('static/data/projectsData.json') as data:
    projects = flask.json.load(data)

with open('static/data/teamsData.json') as data:
    teams = flask.json.load(data)


@app.route('/')
def index():
    return flask.render_template('index.html')


@app.route('/api/teams')
def get_team():
    return flask.json.jsonify(teams)


@app.route('/api/projects')
def get_project():
    return flask.json.jsonify(projects)


@app.route('/api/email', methods=['POST'])
def send_email():
    data = flask.request.get_json()

    msg = MIMEText(data['body'] + '\n\n' + data['name'])
    msg['Subject'] = data['subject']
    msg['From'] = data['email']
    msg['To'] = 'best.ubc@gmail.com'

    s = smtplib.SMTP('smtp.mailgun.org', 587)

    s.login('postmaster@mg.ubcbest.com', 'a966d2bd2c4a74c89e636bb9709b9cf2')
    s.sendmail(msg['From'], msg['To'], msg.as_string())
    s.quit()

    return flask.jsonify({
        'status': 'success',
        'message': 'woooo'
    })


if __name__ == '__main__':
    app.debug = True
    app.run()

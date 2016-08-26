from flask import Flask
from flask import render_template
from flask import request
from flask import json
from flask import jsonify
import smtplib

from email.mime.text import MIMEText
from database import database
from database import GalleryItem, Project, ProjectMember, Team, TeamMember
from pony.orm import db_session
from pony.orm import select

app = Flask(__name__)


class Response(object):
    @classmethod
    def _error(cls, type, status_code, msg=None, exc=None):
        assert type in ["client", "server"]
        response = jsonify({
            'message': exc.message if msg is None else msg,
            'status': '{}-error'.format(type)
        })
        response.status_code = status_code
        return response

    @classmethod
    def server_error(cls, status_code, msg=None, exc=None):
        return cls._error("server", status_code=status_code, msg=msg, exc=exc)

    @classmethod
    def client_error(cls, status_code, msg=None, exc=None):
        return cls._error("client", status_code=status_code, msg=msg, exc=exc)

    @classmethod
    def success(cls, data=None, msg=None):
        response = jsonify({
            'data': data,
            'status': 'success',
            'message': msg
        })
        return response


@app.route('/')
def index():
    return render_template('index.html')


@app.route('/api/gallery')
@db_session
def get_gallery():
    data = []
    for item in select(i for i in GalleryItem):
        print item.to_dict(with_lazy=True)
        data.append(item.to_dict(with_lazy=True))
    return Response.success(data=data)


@app.route('/api/teams')
@app.route('/api/teams/<ii>')
@db_session
def get_team(ii=None):
    if ii:
        team = Team.get(id=int(ii) + 1)
        if not team:
            return Response.client_error(msg='Team not found')
        data = team.to_dict(with_lazy=True)
        data['members'] = []
        for member in team.members:
            data['members'].append(member.to_dict(with_lazy=True))
        return Response.success(data=data)
    else:
        data = []
        for team in select(t for t in Team):
            data.append(team.to_dict(with_lazy=True))
        return Response.success(data=data)


@app.route('/api/projects')
@app.route('/api/projects/<ii>')
@db_session
def get_project(ii=None):
    if ii:
        project = Project.get(id=int(ii) + 1)
        if not project:
            return Response.client_error(msg='Project not found')
        data = project.to_dict(with_lazy=True)
        data['members'] = []
        for member in project.members:
            data['members'].append(member.to_dict(with_lazy=True))
        return Response.success(data=data)
    else:
        data = []
        for project in select(p for p in Project):
            data.append(project.to_dict(with_lazy=True))
        return Response.success(
            data=data
        )


@app.route('/api/email', methods=['POST'])
def send_email():
    data = request.get_json()

    msg = MIMEText(data['body'] + '\n\n' + data['name'])
    msg['Subject'] = data['subject']
    msg['From'] = data['email']
    msg['To'] = 'best.ubc@gmail.com'

    s = smtplib.SMTP('smtp.mailgun.org', 587)

    s.login('postmaster@sandboxdc686bea42dd461588344b6135d7b757.mailgun.org', '07c05c110d3caeef2b6786ad2f2be051')
    s.sendmail(msg['From'], msg['To'], msg.as_string())
    s.quit()

    return jsonify({
        'status': 'success',
        'message': 'woooo'
    })


if __name__ == '__main__':
    app.debug = True
    app.run()

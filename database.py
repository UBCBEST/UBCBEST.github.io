from pony.orm import LongStr
from pony.orm import Optional
from pony.orm import PrimaryKey
from pony.orm import Required
from pony.orm import Set
from pony.orm import Database
from pony.orm import commit
from pony.orm import db_session

import flask

database = Database()


class Project(database.Entity):
    id = PrimaryKey(int, auto=True)
    project_id = Required(str)
    name = Required(LongStr)
    icon = Required(str)
    tab = Required(str)
    abbr = Required(str)
    desc = Required(LongStr)
    members = Set('ProjectMember', lazy=True)


class ProjectMember(database.Entity):
    name = Required(LongStr)
    img = Optional(str)
    project = Required(Project)
    position = Required(str)
    year = Required(str)
    biomed = Optional(bool, default=False)
    department = Required(str)
    desc = Optional(LongStr)


class Team(database.Entity):
    id = PrimaryKey(int, auto=True)
    team_id = Required(str)
    name = Required(LongStr)
    icon = Required(str)
    tab = Required(str)
    members = Set('TeamMember', lazy=True)


class TeamMember(database.Entity):
    name = Required(LongStr)
    img = Optional(str)
    team = Required(Team)
    title = Optional(str)
    link = Required(str)
    occupation = Optional(str)
    desc = Optional(LongStr)


class GalleryItem(database.Entity):
    img = Required(str)
    caption = Optional(LongStr)
    orientation = Optional(str)


database.bind('mysql', host='localhost', user='root', db='ubcbest')
database.generate_mapping()

"""with db_session:
    with open('static/data/galleryData.json') as data:
        for item in flask.json.load(data)['data']:
            i = GalleryItem(
                img=item['img']
            )
            if 'caption' in item:
                i.caption = item['caption']
            if 'orientation' in item:
                i.orientation = item['orientation']
    with open('static/data/projectsData.json') as data:
        projects = flask.json.load(data)['data']
        for project in projects:
            p = Project(
                name=project['name'],
                icon=project['icon'],
                tab=project['tab'],
                project_id=project['id'],
                abbr=project['abbr'],
                desc=' '.join(project['desc'])
            )
            for member in project['members']:
                m = ProjectMember(
                    name=member['name'],
                    img=member['img'],
                    project=p,
                    position=member['position'],
                    year=member['year'],
                    biomed=member['biomed'] if 'biomed' in member else False,
                    department=member['department'],
                    desc=member['desc']
                )
                p.members.add(m)
            commit()

    with open('static/data/teamsData.json') as data:
        teams = flask.json.load(data)['data']
        for team in teams:
            t = Team(
                name=team['name'],
                icon=team['icon'],
                tab=team['tab'],
                team_id=team['id']
            )
            for member in team['members']:
                m = TeamMember(
                    name=member['name'],
                    img=member['img'],
                    team=t,
                    link=member['link'],
                    desc=' '.join(member['desc'])
                )
                if 'title' in member:
                    m.title = member['title']
                if 'occupation' in member:
                    m.occupation = member['occupation']
                t.members.add(m)
            commit()"""

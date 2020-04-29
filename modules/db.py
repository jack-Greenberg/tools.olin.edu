from flask_sqlalchemy import SQLAlchemy
from sqlalchemy.orm.attributes import QueryableAttribute
from flask_login import UserMixin

db = SQLAlchemy()

user_tool = db.Table('users_tools',
    db.Column('user_id', db.Integer, db.ForeignKey('users.id'), primary_key=True),
    db.Column('tool_id', db.Integer, db.ForeignKey('tools.id'), primary_key=True),
    db.Column('level', db.Integer)
)

role_user = db.Table('role_user',
    db.Column('role_id', db.Integer, db.ForeignKey('roles.role_id'), primary_key=True),
    db.Column('user_id', db.Integer, db.ForeignKey('users.id'), primary_key=True)
)

class Tool(db.Model):
    __tablename__ = "tools"
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(255))
    shortname = db.Column(db.String(255))
    category_id = db.Column(db.Integer, db.ForeignKey('tool-category.id'))
    category = db.relationship('ToolCategory')

    _default_fields = ["name", "shortname", "category", "category_id"]

    def __repr__(self):
        return '<Tool %r>' % self.name

    def to_dict(self):
        return {
            'id': self.id,
            'name': self.name,
            'category': {
                'id': self.category.id,
                'name': self.category.name,
            },
            'shortname': self.shortname
        }

class User(UserMixin, db.Model):
    __tablename__ = "users"
    id = db.Column(db.Integer, primary_key=True)
    username = db.Column(db.String(255))
    first_name = db.Column(db.String(255))
    last_name = db.Column(db.String(255))
    role_id = db.Column(db.Integer, db.ForeignKey('roles.role_id'))
    role = db.relationship('Role')
    tools_trained = db.relationship('Tool', secondary=user_tool, lazy='select')

    _default_fields = ['username', 'first_name', 'last_name', 'role', 'tools_trained']

    def __repr__(self):
        return '<User %r>' % self.username

    def to_dict(self):
        return {
            "id": self.id,
            "username": self.username,
            "first_name": self.first_name,
            "last_name": self.last_name,
        }

class Role(db.Model):
    __tablename__ = "roles"
    role_id = db.Column(db.Integer, primary_key=True)
    role_name = db.Column(db.String(255))

    def __repr__(self):
        return self.role_name

class ToolCategory(db.Model):
    __tablename__ = "tool-category"
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(255))
    tools = db.relationship('Tool', backref='tool-category', lazy='joined')

    _default_fields = ["name"]

class Training(db.Model):
    __tablename__ = "trainings"
    id = db.Column(db.Integer, primary_key=True)
    tool_id = db.Column(db.Integer, db.ForeignKey('tools.id'))
    tool = db.relationship('Tool')
    trainee_id = db.Column(db.Integer, db.ForeignKey('users.id'))
    trainee = db.relationship('User')
    started = db.Column(db.DateTime)
    reading_complete = db.Column(db.Boolean)
    worksheet_complete = db.Column(db.Boolean)
    training_complete = db.Column(db.Boolean)
    testpiece_complete = db.Column(db.Boolean)

    def to_dict(self):
        return {
            'id': self.id,
            'tool': self.tool.to_dict(),
            'trainee': self.trainee.to_dict(),
            'started': self.started,
            'reading_complete': self.reading_complete,
            'worksheet_complete': self.worksheet_complete,
            'training_complete': self.training_complete,
            'testpiece_complete': self.testpiece_complete,
        }

#  class Log(db.Model):
    #  __tablename__ = "log"
    #  id = db.Column(db.Integer, primary_key=True)
    #  timestamp = db.Column(db.DateTime)
    #  training_id = db.Column(db.Integer, db.ForeignKey('training.id'))
    #  training = db.relationship("Training")
    #  text = db.Column(db.String(1023))

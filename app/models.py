from . import db
from werkzeug.security import generate_password_hash, check_password_hash
from flask_login import UserMixin,current_user
from . import login_manager
from datetime import datetime


class User(UserMixin, db.Model):
    __tablename__ = 'users'
    id = db.Column(db.Integer, primary_key = True)
    username = db.Column(db.String(255),unique = True,nullable = False)
    email  = db.Column(db.String(255),unique = True,nullable = False)
    secure_password = db.Column(db.String(255),nullable = False)
    bio = db.Column(db.String(255))
    profile_pic_path = db.Column(db.String())
    pitches = db.relationship('Pitch', backref='user', lazy='dynamic')
    comment = db.relationship('Comment', backref='user', lazy='dynamic')

    def save_user(self):
        db.session.add(self)
        db.session.commit()
    def delete_user(self):
        db.session.delete(self)
        db.session.commit()

    @property
    def set_password(self):
        raise AttributeError('You cannot read the password attribute')

    @set_password.setter
    def password(self, password):
        self.secure_password = generate_password_hash(password)

    def verify_password(self, password):
        return check_password_hash(self.secure_password,password) 
    
    def save_u(self):
        db.session.add(self)
        db.session.commit()

    def delete(self):
        db.session.delete(self)
        db.session.commit()
    
    def __repr__(self):
        return f'User {self.username}'

class Pitch(db.Model):
    __tablename__ = 'pitches'
    id = db.Column(db.Integer, primary_key = True)
    title = db.Column(db.String(255), nullable=False)
    content = db.Column(db.String)
    category = db.Column(db.String(40))
    upvote = db.relationship('Upvote', backref='pitch', lazy='dynamic')
    downvote = db.relationship('Downvote', backref='pitch', lazy='dynamic')
    comment = db.relationship('Comment',backref='pitch',lazy='dynamic')
    user_id = db.Column(db.Integer, db.ForeignKey('users.id'))
    time = db.Column(db.DateTime, default = datetime.utcnow)
    
    def save_pitch(self):
        db.session.add(self)
        db.session.commit()

        
    def __repr__(self):
        return f'Pitch {self.post}'

class Comment(db.Model):
    __tablename__ = 'comments'
    id = db.Column(db.Integer, primary_key=True)
    comment = db.Column(db.Text(),nullable = False)
    user_id = db.Column(db.Integer,db.ForeignKey('users.id'),nullable = False)
    pitch_id = db.Column(db.Integer,db.ForeignKey('pitches.id'),nullable = False)

    def save_comment(self):
        db.session.add(self)
        db.session.commit()

    @classmethod
    def get_comments(cls,pitch_id):
        comments = Comment.query.filter_by(pitch_id=pitch_id).all()

        return comments

    
    def __repr__(self):
        return f'comment:{self.comment}'

class PhotoProfile(db.Model):
    __tablename__ = 'profile_photos'

    id = db.Column(db.Integer,primary_key = True)
    pic_path = db.Column(db.String())
    user_id = db.Column(db.Integer, db.ForeignKey("users.id"))
    
class Upvote(db.Model):
    __tablename__ = 'upvotes'
    id = db.Column(db.Integer, primary_key=True)
    upvote = db.Column(db.Integer, default=1)
    user_id = db.Column(db.Integer, db.ForeignKey('users.id'))
    pitch_id = db.Column(db.Integer, db.ForeignKey('pitches.id'))
    def save(self):
        db.session.add(self)
        db.session.commit()
    def upvote(cls, id):
        upvote_pitch = Upvote(user=current_user, pitch_id=id)
        upvote_pitch.save()
    @classmethod
    def query_upvotes(cls, id):
        upvote = Upvote.query.filter_by(pitch_id=id).all()
        return upvote
    @classmethod
    def all_upvotes(cls):
        upvotes = Upvote.query.order_by('id').all()
        return upvotes
    def __repr__(self):
        return f'{self.user_id}:{self.pitch_id}'

class Downvote(db.Model):
    __tablename__ = 'downvotes'
    id = db.Column(db.Integer, primary_key=True)
    downvote = db.Column(db.Integer, default=1)
    user_id = db.Column(db.Integer, db.ForeignKey('users.id'))
    pitch_id = db.Column(db.Integer, db.ForeignKey('pitches.id'))
    def save(self):
        db.session.add(self)
        db.session.commit()
    def downvote(cls, id):
        downvote_pitch = Downvote(user=current_user, pitch_id=id)
        downvote_pitch.save()
    @classmethod
    def query_downvotes(cls, id):
        downvote = Downvote.query.filter_by(pitch_id=id).all()
        return downvote
    @classmethod
    def all_downvotes(cls):
        downvote = Downvote.query.order_by('id').all()
        return downvote
    def __repr__(self):
        return f'{self.user_id}:{self.pitch_id}'          
               


@login_manager.user_loader
def load_user(user_id):
    return User.query.get(user_id)

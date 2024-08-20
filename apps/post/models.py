# -*- encoding: utf-8 -*-
"""
Copyright (c) 2019 - present AppSeed.us
"""

from flask_login import UserMixin, current_user

from sqlalchemy.orm import relationship
from sqlalchemy import ForeignKey

from apps import db, login_manager


from datetime import datetime



class Post(db.Model):

    __tablename__ = 'Post'

    id = db.Column(db.Integer, primary_key=True)
    title = db.Column(db.String(100), nullable=False)
    content = db.Column(db.Text, nullable=False)
    date_posted = db.Column(db.DateTime, nullable=False, default=datetime.utcnow)
    author_id = db.Column(db.Integer, db.ForeignKey('Users.id'), nullable=False)
    

    def __repr__(self):
        return f"Post('{self.title}', '{self.date_posted}')"

    @staticmethod
    def create_post(title, content, author):
        post = Post(title=title, content=content, author=author)
        db.session.add(post)
        db.session.commit()
        return post

    def update_post(self, title, content):
        self.title = title
        self.content = content
        db.session.commit()

    def delete_post(self):
        db.session.delete(self)
        db.session.commit()





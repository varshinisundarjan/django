# models.py
from datetime import datetime
from sqlalchemy import Column, Integer, String, DateTime, ForeignKey
from sqlalchemy.orm import relationship
from sqlalchemy.ext.declarative import declarative_base

Base = declarative_base()

# Question model
class Question(Base):
    __tablename__ = 'questions'
    id = Column(Integer, primary_key=True)
    question_text = Column(String(200), nullable=False)
    pub_date = Column(DateTime, default=datetime.utcnow)

    choices = relationship("Choice", back_populates="question")
    submissions = relationship("Submission", back_populates="question")

    def __repr__(self):
        return f"<Question(id={self.id}, text='{self.question_text}')>"

# Choice model
class Choice(Base):
    __tablename__ = 'choices'
    id = Column(Integer, primary_key=True)
    question_id = Column(Integer, ForeignKey('questions.id'))
    choice_text = Column(String(200), nullable=False)
    votes = Column(Integer, default=0)

    question = relationship("Question", back_populates="choices")
    submissions = relationship("Submission", back_populates="choice")

    def __repr__(self):
        return f"<Choice(id={self.id}, text='{self.choice_text}', votes={self.votes})>"

# Submission model
class Submission(Base):
    __tablename__ = 'submissions'
    id = Column(Integer, primary_key=True)
    user_name = Column(String(100), nullable=False)
    question_id = Column(Integer, ForeignKey('questions.id'))
    choice_id = Column(Integer, ForeignKey('choices.id'))
    submitted_at = Column(DateTime, default=datetime.utcnow)

    question = relationship("Question", back_populates="submissions")
    choice = relationship("Choice", back_populates="submissions")

    def __repr__(self):
        return f"<Submission(user='{self.user_name}', question_id={self.question_id}, choice_id={self.choice_id})>"

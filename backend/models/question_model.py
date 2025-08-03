# Conceptual database model for the Community Q&A feature.

from sqlalchemy import Column, Integer, String, Text, ForeignKey
from sqlalchemy.orm import relationship
from sqlalchemy.ext.declarative import declarative_base

Base = declarative_base()

class Question(Base):
    __tablename__ = "questions"

    id = Column(Integer, primary_key=True, index=True)
    title = Column(String, nullable=False)
    content = Column(Text)
    
    # Foreign key to link to a user (the author)
    author_id = Column(Integer, ForeignKey("users.id"))
    author = relationship("User")

    # Foreign key to link to a scheme
    scheme_id = Column(String, ForeignKey("schemes.scheme_id"))
    scheme = relationship("Scheme")
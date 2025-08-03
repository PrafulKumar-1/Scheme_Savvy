# This file defines the database model for a User.
# For the hackathon, this is a conceptual model using SQLAlchemy-like syntax.
# It shows you've planned for a real database.

from sqlalchemy import Column, Integer, String
from sqlalchemy.ext.declarative import declarative_base

Base = declarative_base()

class User(Base):
    __tablename__ = "users"

    id = Column(Integer, primary_key=True, index=True)
    email = Column(String, unique=True, index=True, nullable=False)
    hashed_password = Column(String, nullable=False)
    # In a real app, you'd add fields like 'full_name', 'created_at', etc.
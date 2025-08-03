# Conceptual database model for a Scheme.

from sqlalchemy import Column, Integer, String, Text, JSON
from sqlalchemy.ext.declarative import declarative_base

Base = declarative_base()

class Scheme(Base):
    __tablename__ = "schemes"

    id = Column(Integer, primary_key=True, index=True)
    scheme_id = Column(String, unique=True, index=True, nullable=False)
    scheme_name = Column(String, nullable=False)
    ministry = Column(String)
    description = Column(Text)
    benefits = Column(Text)
    category = Column(String)
    official_link = Column(String)
    required_documents = Column(JSON) # Storing a list as JSON
    eligibility_rules = Column(JSON) # Storing rules as JSON
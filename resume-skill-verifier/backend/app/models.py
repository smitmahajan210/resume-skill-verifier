from sqlalchemy import Column, Integer, String, Text, Float, DateTime
from sqlalchemy.sql import func

from app.database import Base


class Candidate(Base):
    __tablename__ = "candidates"

    id = Column(Integer, primary_key=True, index=True)
    name = Column(String, nullable=True)
    email = Column(String, nullable=True, unique=True)
    github_username = Column(String, nullable=True)
    created_at = Column(DateTime(timezone=True), server_default=func.now())


class Resume(Base):
    __tablename__ = "resumes"

    id = Column(Integer, primary_key=True, index=True)
    candidate_id = Column(Integer, nullable=True)
    filename = Column(String, nullable=False)
    content_type = Column(String, nullable=True)
    extracted_skills = Column(Text, nullable=True)
    uploaded_at = Column(DateTime(timezone=True), server_default=func.now())


class SkillResult(Base):
    __tablename__ = "skill_results"

    id = Column(Integer, primary_key=True, index=True)
    candidate_id = Column(Integer, nullable=True)
    skill = Column(String, nullable=False)
    trust_score = Column(Float, nullable=True)
    verified = Column(String, nullable=True)
    created_at = Column(DateTime(timezone=True), server_default=func.now())

from sqlalchemy import Column, Integer, String

from ..database import Base


class Tutorial(Base):
    __tablename__ = "tutorial"
    id = Column(Integer, primary_key=True)
    topic = Column(String(50), nullable=False, unique=True)
    category = Column(String, nullable=False)
    author = Column(String, nullable=False)

import sys
from sqlalchemy import Column, ForeignKey, Integer, String, BigInteger
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy import create_engine

Base = declarative_base()

class Users(Base):
    __tablename__ = 'Users'
    username = Column(String(80), primary_key=True)
    passHash = Column(String(255), nullable=False)
    firstName = Column(String(80), nullable=False)
    lastName = Column(String(80), nullable=False)
    XP = Column(Integer, default=0)
    email = Column(String(255), nullable=True)
    
class Matches(Base):
    __tablename__ = 'Matches'
    id = Column(Integer, primary_key=True)
    playerOne = Column(String(80), ForeignKey("Users.username"))
    playerTwo = Column(String(80), ForeignKey("Users.username"))
    playerOneScore = Column(Integer, default=0)
    playerTwoScore = Column(Integer, default=0)
    playerOneHealth = Column(Integer, default=100)
    playerTwoHealth = Column(Integer, default=100)
    playerOnePosX = Column(Integer, default=0)
    playerTwoPosX = Column(Integer, default=0)
    playerOnePosY = Column(Integer, default=0)
    playerTwoPosY = Column(Integer, default=0)
    playerOneRotation = Column(Integer, default=0)
    playerTwoRotation = Column(Integer, default=0)




engine = create_engine('sqlite:///GameDatabase')
Base.metadata.create_all(engine)
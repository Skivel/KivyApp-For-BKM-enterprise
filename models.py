from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy import ForeignKey
from sqlalchemy.orm import relationship
from sqlalchemy import Column, Integer, String
from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker

engine = create_engine('sqlite:///avans.sqlite', echo=False)
Session = sessionmaker(bind=engine)
session = Session()
Base = declarative_base()


class User(Base):
    __tablename__ = 'users'
    id = Column(Integer, primary_key=True)
    name = Column(String, nullable=False)
    avans = relationship("Avans", cascade="all,delete", back_populates="user")

    def __str__(self):
        return self.name

    @classmethod
    def add(cls, name):
        user = cls(name=name)
        session.add(user)
        session.commit()
        return user

    @classmethod
    def find_by_name(cls, name):
        return session.query(cls).filter(cls.name.ilike(f'%{name}%'))

    @classmethod
    def delete_by_id(cls, user_id):
        user = session.query(cls).filter_by(id=user_id).first()
        if user:
            session.delete(user)
            session.commit()
            return True
        return False


class Avans(Base):
    __tablename__ = 'avans'
    id = Column(Integer, primary_key=True)
    avans = Column(String, nullable=True)
    user_id = Column(Integer, ForeignKey('users.id'))
    user = relationship("User", back_populates="avans")

    def __str__(self):
        return self.avans

    @classmethod
    def add(cls, avans, user):
        avans = cls(avans=avans, user=user)
        session.add(avans)
        session.commit()
        return avans


Base.metadata.create_all(engine)

#!/usr/bin/python3
""" Module that saves into a MYSQL database """
from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker
from sqlalchemy.orm import scoped_session
from models.base_model import BaseModel, Base
from models.user import User
from models.place import Place
from models.state import State
from models.city import City
from models.amenity import Amenity
from models.review import Review

import os


class DBStorage:
    """ New Engine to connect to the database """
    __engine = None
    __session = None

    def __init__(self):
        """ Constructor """

        self.__engine = create_engine('mysql+mysqldb://{}:{}@{}/{}'.format(
            os.getenv("HBNB_MYSQL_USER"),
            os.getenv("HBNB_MYSQL_PWD"),
            os.getenv("HBNB_MYSQL_HOST"),
            os.getenv("HBNB_MYSQL_DB")),
            pool_pre_ping=True)

        if os.getenv("HBNB_ENV") == "test":
            Base.metadata.drop_all(self.__engine)

    def all(self, cls=None):
        """ Return a dict of the objects key = class.id & value = obj"""
        dict_obj = {}
        if cls is None:
            list_class = [User, City, Amenity, Place, State, Review]
            # list_class = [City, State]
            for classe in list_class:
                query = self.__session.query(classe).all()
                for obj in query:
                    key = obj.__class__.__name__ + "." + obj.id
                    dict_obj[key] = obj
        else:
            query = self.__session.query(cls).all()
            for obj in query:
                key = obj.__class__.__name__ + "." + obj.id
                dict_obj[key] = obj

        return (dict_obj)

    def new(self, obj):
        """  Object to the current database session """
        self.__session.add(obj)

    def save(self):
        """ commit all changes of the current database session"""
        self.__session.commit()

    def delete(self, obj=None):
        """ delete from the current database session an obj """
        if obj is not None:
            self.__session.delete(obj)

    def reload(self):
        """ Create the current database session """
        Base.metadata.create_all(self.__engine)

        session_factory = sessionmaker(
            bind=self.__engine, expire_on_commit=False,)
        Session = scoped_session(session_factory)
        self.__session = Session()

    def close(self):
        """ Close the session """
        self.__session.close()
        # self.__session.remove()

#!/usr/bin/python3
"""This module defines a base class for all models in our hbnb clone"""
import models
import uuid
from datetime import datetime
<<<<<<< HEAD
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy import Column
from sqlalchemy import DateTime
from sqlalchemy import String
=======
from sqlalchemy import Column, Integer, String
>>>>>>> f85e28fec7b0b65ab3d8bae1817d6efd9745d12f

Base = declarative_base()

class BaseModel:
    """A base class for all hbnb models"""
<<<<<<< HEAD


    id = Column(String(60), nullable = False, primary_key=True)
    created_at = Column(DateTime, nullable = False, default=datetime.utcnow())
    updated_at = Column(DateTime, nullable = False, default= datetime.utcnow())
    

    def __init__(self, *args, **kwargs):
        """Instatntiates a new model"""

        self.id = str(uuid.uuid4())
        self.created_at = datetime.utcnow()
        self.updated_at = datetime.utcnow()
        if kwargs:
            for k, v in kwargs.items():
                if k == "created_at" or k == "updated_at":
                    v = datetime.strptie(v, '%Y-%m-%dT%H:%M:%S.%f')
                if k == "__class__":
                    setattr(self, k, v)
            del kwargs['__class__']
            self.__dict__.update(kwargs)
=======
    # Added id, created_at, and updated_at as class attributes
    id = Column(String(60), nullable=False, primary_key=True)
    created_at = Column(DateTime, nullable=False, default=datetime.utcnow())
    updated_at = Column(DateTime, nullable=False, default=datetime.utcnow())

    def __init__(self, *args, **kwargs):
        """Instatntiates a new model"""
        if not kwargs:
            from models import storage
            self.id = str(uuid.uuid4())
            self.created_at = datetime.now()
            self.updated_at = datetime.now()
            storage.new(self)
        else:
            # Set instance attributes from kwargs dictionary
            for k, v in kwargs.items():
                if k != '__class__':
                    setattr(self, k, v)
            # default values for id created_at and updated_at if not provided
            if 'id' not in kwargs:
                self.id = str(uuid.uuid4())
            if 'created_at' not in kwargs:
                self.created_at = datetime.utcnow()
            if 'updated_at' not in kwargs:
                self.updated_at = datetime.utcnow()
>>>>>>> f85e28fec7b0b65ab3d8bae1817d6efd9745d12f

    def __str__(self):
        """Returns a string representation of the instance"""
        cls = (str(type(self)).split('.')[-1]).split('\'')[0]
        return '[{}] ({}) {}'.format(cls, self.id, self.__dict__)

    def save(self):
        """Updates updated_at with current time when instance is changed"""
        from models import storage
<<<<<<< HEAD
        self.updated_at = datetime.now()
        models.storage.new(self)
        models.storage.save()
=======
        # Moved storage.new(self) from __init__ to save
        storage.new(self)
        self.updated_at = datetime.utcnow()
        storage.save()
>>>>>>> f85e28fec7b0b65ab3d8bae1817d6efd9745d12f

    def to_dict(self):
        """Convert instance into dict format"""
        dictionary = {}
        dictionary.update(self.__dict__)
        dictionary.update({'__class__':
                          (str(type(self)).split('.')[-1]).split('\'')[0]})
        dictionary['created_at'] = self.created_at.isoformat()
        dictionary['updated_at'] = self.updated_at.isoformat()
<<<<<<< HEAD
        if dictionary['_sa_instance_state']:
            del dictionary['_sa_instance_state']
        return dictionary

    def delete(self):
        """delete the current instance from the storage"""
        models.storage.delete(self)
=======
        dictionary.pop('_sa_instance_state', None)
        return dictionary

    # Add a new public instance method: def delete(self)
    def delete(self):
        """Delete the current instance from the storage"""
        from models import storage
        storage.delete(self)
>>>>>>> f85e28fec7b0b65ab3d8bae1817d6efd9745d12f

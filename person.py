#!/usr/bin/env python

# Addressbook person.py

class Person():
    '''Represents a Contact.'''
    def __init__(self, name):
        self.name = name
        self.phone = None
        self.email = None
        self.image = None
        print('Created contact {0}'.format(self.name))

    def __del__(self):
        print('Contact {0} is being deleted!'.format(self.name))
        # Do I delete people from here, or from addressbook.py
        # where AB_dict is?

    def getName(self):
        return self.name

    def getNumber(self):
        return self.phone

    def getEmail(self):
        return self.email

    def createNewPerson(self, name, phone, email, image):
       self.name = name
       self.phone = phone
       self.email = email
       self.image = image

    def updatePerson(self, phone, email, image):
        # Check if args equal to None and if so, leave them as they were.
        self.phone = phone
        self.email = email
        self.image = image

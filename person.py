#!/usr/bin/env python

# Addressbook person.py

class Person():
    '''Represents a Contact.'''
    def __init__(self, name):
        self.name = name
        self.phone = None
        print('Created contact {0}'.format(self.name))

    def __del__(self):
        print('Contact {0} is being deleted!'.format(self.name))
        # Do I delete people from here, or from addressbook.py
        # where AB_dict is?

    def getName(self):
        return self.name

    def getNumber(self):
        return self.phone

    def createNewPerson(self, n, ph):
       self.name = n
       self.phone = ph

    def updatePerson(self, ph):
        self.phone = ph

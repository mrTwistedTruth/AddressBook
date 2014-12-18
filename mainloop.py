#!/bin/python
# Addressbook main loop cycle

import person
import pickle

# Later add option to choose addressbook to load instead of this hardcode
addressbook = {} # Addressbook dictionary of contacts
addressbookFile = 'addressbook.pkl'

running = True

while running:
    print('''
        1. Add Contact
        2. Display Contact
        3. Edit Contact
        4. Delete Contact
        5. Save addressbook
        6. Load addressbook
        7. Exit
        ''')
    option = input('Enter option : ')
    if option == '1': # Add contact
        n = input('Enter name: ')
        ph = input('Enter phone: ')

        entry = person.Person(n) # Initialize a person
        entry.createNewPerson(n,ph) # Fill in person details

        addressbook[n] = entry # Add Person instance to dictionary

    elif option == '2': # Display contact
        print('\nDisplaying all {0} contacts\n'.format(len(addressbook)))
        print('Choose contact from list of all contact names: ')
        for contact in addressbook:
            print(addressbook[contact].name, end=', ')
        n = str(input('\nEnter the name of contact you want to display: '))
        addressbook[n].displaySelf()

    elif option == '3': # Edit contact
        n = str(input('Enter the contact name to edit: '))
        newnumber = str(input('Enter the new number for {0}: '.format(n)))
        addressbook[n].updatePerson(newnumber)

    elif option == '4': # Delete contact
        n = str(input('Enter the contact to delete: '))
        addressbook[n].__del__()
        # del addressbook[n] # doesn't seem to call destructor

    elif option == '5': # Save addressbook
            print('Saving data to file {0}'.format(addressbookFile))
            file = open(addressbookFile, 'wb')
            pickle.dump(addressbook, file)
            file.close()

    elif option == '6': # Load addressbook file
        # Add a warning about overwriting data and add exept handle
        if addressbookFile:
            print('Loading data from file {0}'.format(addressbookFile))
            print('This will overwrite contacts in current memory.')
            file = open(addressbookFile, 'rb')
            addressbook = pickle.load(file)
            file.close()

    elif option == '7': # Exit
        print('Exiting')
        running = False


    else: # Option invalid
        print('\nInvalid selection. Please reselect option.')
        pass




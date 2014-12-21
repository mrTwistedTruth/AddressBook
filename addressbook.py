#!/usr/bin/env python

from gi.repository import Gtk
import person

class AddressBook:
    def __init__(self):
        self.AB_dict = {}
        self.AB_file = 'addressbook.pkl'

        # Set up Window
        window = Gtk.Window()
        window.set_title("GTK AddressBook")
        window.set_position(Gtk.WindowPosition.CENTER)
        #window.set_default_size(300, 300)
        window.connect("destroy", self.destroy)

        # Set up text entries
        self.name_entry = Gtk.Entry()
        self.name_entry.set_alignment(1)
        self.name_entry.set_text('name')

        self.phone_entry = Gtk.Entry()
        self.phone_entry.set_alignment(1)
        self.phone_entry.set_text('phone')
        # /* */--------------------


        # Set up display labels
        self.name_label = Gtk.Label("Name: ")
        self.phone_label = Gtk.Label("Phone: ")
        self.status_label = Gtk.Label("")

        # Set up info bar
        # TODO find out how to close the info bar. Close button functionality.
        self.info_bar = Gtk.InfoBar()
        self.info_bar.set_message_type(Gtk.MessageType.INFO)
        self.info_bar.get_content_area().pack_start(self.status_label, False, False, 0)
        self.info_bar.set_show_close_button(True)

        # Set up buttons
        self.btn_addContact = Gtk.Button(label="Add Contact")
        self.btn_addContact.connect("clicked", self.Add_button_clicked)

        self.btn_displayContact = Gtk.Button(label="Display Contact")
        self.btn_displayContact.connect("clicked", self.Display_button_clicked)

        # Set up layout boxes
        box_main = Gtk.Box.new(Gtk.Orientation.VERTICAL, 5)
        box_entry = Gtk.Box.new(Gtk.Orientation.VERTICAL, 5)
        box_display = Gtk.Box.new(Gtk.Orientation.VERTICAL, 5)
        box_buttons = Gtk.Box.new(Gtk.Orientation.HORIZONTAL, 5)

        box_main.pack_start(box_entry, True, True, 0)
        box_main.pack_start(box_display, True, True, 0)
        box_main.pack_start(box_buttons, True, True, 0)


        box_entry.add(self.name_entry)
        box_entry.add(self.phone_entry)

        box_display.add(self.info_bar)
        box_display.add(self.status_label)
        box_display.add(self.name_label)
        box_display.add(self.phone_label)

        box_buttons.add(self.btn_addContact)
        box_buttons.add(self.btn_displayContact)
        #box_buttons.pack_start(self.btn_addContact, True, True, 0)
        #box_buttons.pack_start(self.btn_displayContact, True, True, 0)

        # /* */--------------------

        window.add(box_main)
        window.show_all()

    def Add_button_clicked(self, btn_add):
        contact = person.Person(self.name_entry.get_text())
        contact.createNewPerson(contact.name, self.phone_entry.get_text())
        self.AB_dict[contact.name] = contact

        self.phone_entry.set_text('') # Clear phone entry after contact added
        self.status_label.set_text('Contact {0} Added.'.format(contact.name))

    def Display_button_clicked(self, btn_display):
        name = self.name_entry.get_text()

        number = str(self.AB_dict[name].getNumber())
        self.name_label.set_text(name)
        self.phone_label.set_text(number)
    def on_bar_response(self, info_bar, response_id):
        pass

    def destroy(self, window):
        Gtk.main_quit()

def main():
    app = AddressBook()
    Gtk.main()

if __name__ == '__main__':
    main()

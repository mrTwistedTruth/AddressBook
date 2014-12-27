#!/usr/bin/env python

from gi.repository import Gtk
import person

class AddressBook:
    def __init__(self):
        # {{{1 ================= SET UP WINDOWS ================
        self.AB_dict = {}
        self.AB_file = 'addressbook.pkl'
        #}}}1
        # Set up Window
        window = Gtk.Window()
        window.set_title("GTK AddressBook")
        window.set_position(Gtk.WindowPosition.CENTER)
        #window.set_default_size(300, 300)
        window.connect("destroy", self.destroy)
        window.set_border_width(8)

        # Set up information entry area
        entry_frame = Gtk.Frame(label="Entry")
        box_main = Gtk.Box.new(Gtk.Orientation.VERTICAL, 5)
        window.add(box_main)

        box_main.add(entry_frame)

        box_entry = Gtk.Box.new(Gtk.Orientation.VERTICAL, 5)
        box_entry.set_border_width(8)

        self.name_entry = Gtk.Entry()
        self.name_entry.set_alignment(1)
        self.name_entry.set_text('name')

        self.phone_entry = Gtk.Entry()
        self.phone_entry.set_alignment(1)
        self.phone_entry.set_text('phone')

        box_entry.add(self.name_entry)
        box_entry.add(self.phone_entry)
        entry_frame.add(box_entry)
        # /* */-------------------- End entry area

        # Set up display area
        display_frame = Gtk.Frame(label="Display")
        box_main.add(display_frame)

        box_display = Gtk.Box.new(Gtk.Orientation.VERTICAL, 5)
        box_display.set_border_width(8)

        self.name_label = Gtk.Label("Name: ")
        self.phone_label = Gtk.Label("Phone: ")
        self.status_label = Gtk.Label("")

        self.info_bar = Gtk.InfoBar()
        self.info_bar.set_message_type(Gtk.MessageType.INFO)
        self.info_bar.get_content_area().pack_start(self.status_label, False, False, 0)
        #self.info_bar.set_show_close_button(True)

        box_display.add(self.name_label)
        box_display.add(self.phone_label)
        box_display.add(self.info_bar)

        display_frame.add(box_display)

        # /* */-------------------- End display area

        # Set up button area
        buttons_frame = Gtk.Frame(label="Buttons")
        box_main.add(buttons_frame)

        btn_addContact = Gtk.Button(label="Add Contact")
        btn_addContact.connect("clicked", self.Add_button_clicked)

        btn_editContact = Gtk.Button(label="Edit Contact")
        btn_editContact.connect("clicked", self.Edit_button_clicked)

        btn_deleteContact = Gtk.Button(label="Delete Contact")
        btn_deleteContact.connect("clicked", self.Delete_button_clicked)

        btn_displayContact = Gtk.Button(label="Display Contact")
        btn_displayContact.connect("clicked", self.Display_button_clicked)

        btn_saveAddressbook = Gtk.Button(label="Save Addressbook")
        btn_saveAddressbook.connect("clicked", self.Save_button_clicked)

        btn_loadAddressbook = Gtk.Button(label="Load Addressbook")
        btn_loadAddressbook.connect("clicked", self.Load_button_clicked)

        grid_buttons = Gtk.Grid()

        grid_buttons.add(btn_addContact)
        grid_buttons.attach(btn_editContact, 1, 0, 1, 1)
        grid_buttons.attach(btn_deleteContact, 2, 0, 1, 1)
        grid_buttons.attach(btn_displayContact, 0, 1, 1, 1)
        grid_buttons.attach(btn_saveAddressbook, 1, 1, 1, 1)
        grid_buttons.attach(btn_loadAddressbook, 2, 1, 1, 1)

        buttons_frame.add(grid_buttons)

        # /* */-------------------- End buttons area

        window.add(box_main)
        window.show_all()

    def Add_button_clicked(self, btn_add):
        contact = person.Person(self.name_entry.get_text())
        contact.createNewPerson(contact.name, self.phone_entry.get_text())
        self.AB_dict[contact.name] = contact

        self.phone_entry.set_text('') # Clear phone entry after contact added
        self.status_label.set_text('Contact {0} Added.'.format(contact.name))

    def Edit_button_clicked(self, btn_editContact): # check second param
        pass

    def Delete_button_clicked(self, btn_deleteContact):
        pass

    def Display_button_clicked(self, btn_displayContact): # Check second param
        name = self.name_entry.get_text()

        number = str(self.AB_dict[name].getNumber())
        self.name_label.set_text(name)
        self.phone_label.set_text(number)

    def Save_button_clicked(self, btn_saveAddressbook):
        pass

    def Load_button_clicked(self, bnt_loadAddressbook):
        pass

    def on_bar_response(self, info_bar, response_id):
        pass

    def destroy(self, window):
        Gtk.main_quit()

def main():
    app = AddressBook()
    Gtk.main()

if __name__ == '__main__':
    main()

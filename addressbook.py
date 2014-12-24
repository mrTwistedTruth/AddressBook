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

        box_buttons = Gtk.Box.new(Gtk.Orientation.HORIZONTAL, 5)
        box_buttons.set_border_width(8)

        buttons_frame.add(box_buttons)

        self.btn_addContact = Gtk.Button(label="Add Contact")
        self.btn_addContact.connect("clicked", self.Add_button_clicked)

        self.btn_displayContact = Gtk.Button(label="Display Contact")
        self.btn_displayContact.connect("clicked", self.Display_button_clicked)

        box_buttons.add(self.btn_addContact)
        box_buttons.add(self.btn_displayContact)

        # /* */-------------------- End buttons area

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

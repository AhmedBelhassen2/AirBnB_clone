#!/usr/bin/python3
'that contains the entry point of the command interpreter'
import cmd
import sys
from models.base_model import BaseModel
import models
from models import storage
from models.amenity import Amenity
from models.city import City
from models.place import Place
from models.review import Review
from models.state import State
from models.user import User

class HBNBCommand(cmd.Cmd):
    'cmd class'
    prompt = '(hbnb)'
    def do_quit(self, arg):
        'Quit command to exit the program'
        return True

    def do_EOF(self, arg):
        'EOF command to exit the program'
        return True

    def do_create(self, arg):
        'Creates a new instance'
    args = arg.split()
    if len(args) == 0:
        print("** class name missing **")
    if args[0] in classes:
        new_dict = self._key_value_parser(args[1:])
        instance = classes[args[0]](**new_dict)
    else:
        print("** class doesn't exist **")
    print(instance.id)
    instance.save()

if __name__ == '__main__':
    HBNBCommand().cmdloop()

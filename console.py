#!/usr/bin/python3
'that contains the entry point of the command interpreter'
import cmd
import sys
import shlex
import models
storage = models.storage
from models.amenity import Amenity
from models.city import City
from models.place import Place
from models.review import Review
from models.state import State
from models.user import User
from models.base_model import BaseModel

class HBNBCommand(cmd.Cmd):
    'cmd class'
    prompt = '(hbnb)'
    classes = ["BaseModel","Amenity","City","Place","Review","User"]

    def do_quit(self, arg):
        'Quit command to exit the program'
        return True

    def do_EOF(self, arg):
        'EOF command to exit the program'
        return True

    def emptyline(self):
        """if an empty line is entered it is passed waits command"""
        pass

    def do_create(self, arg):
        """Creates a new instance of BaseModel"""
        args = shlex.split(arg)
        if len(args) == 0:
            print("** class name missing **")
            return False
        if args[0] in self.classes:
            for i in range(len(self.classes)):
                if self.classes[i] == args[0]:
                    index = i
                break
            instance = eval(self.classes[index])()
        else:
            print("** class doesn't exist **")
            return False
        instance.save()
        print(instance.id)

    def do_show(self, arg):
        'Prints the string representation'
        args = shlex.split(arg)
        if len(args) == 0:
            print("** class name missing **")
            return False
        if args[0] in self.classes:
            if len(args) > 1:
                key = args[0] + "." + args[1]
                if key in models.storage.all():
                    print(models.storage.all()[key])
                else:
                    print("** no instance found **")
            else:
                print("** instance id missing **")
        else:
            print("** class doesn't exist **")

    def do_destroy(self, arg):
        'Deletes an instance based on the class name and id'
        args = shlex.split(arg)
        if len(args) == 0:
            print("** class name missing **")
        elif args[0] in self.classes:
            if len(args) > 1:
                key = args[0] + "." + args[1]
                if key in storage.all():
                    storage.all().pop(key)
                    storage.save()
                else:
                    print("** no instance found **")
            else:
                print("** instance id missing **")
        else:
            print("** class doesn't exist **")

    def do_all(self, arg):
        """Prints string representations of instances"""
        args = shlex.split(arg)
        obj_list = []
        if len(args) == 0:
            for value in models.storage.all().values():
                obj_list.append(str(value))
            print("[", end="")
            print(", ".join(obj_list), end="")
            print("]")
        elif args[0] in self.classes:
            print(args[0])
            storage_all =  storage.all()
            print(storage_all)
            for key in models.storage.all():
                print(key)
                if args[0] in key:
                    obj_list.append(str(models.storage.all()[key]))
            print("[", end="")
            print(", ".join(obj_list), end="")
            print("]")
        else:
            print("** class doesn't exist **")

    def do_update(self, args):
        'update the instance'
        list_arg = shlex.split(args)
        if len(list_arg) == 0:
            print("** class name missing **")
        elif len(list_arg) == 1 and list_arg[0] not in self.classes:
            print("** class doesn't exist **")
        elif len(list_arg) == 1:
            print("** instance id missing **")
        elif len(list_arg) == 2:
            print("** attribute name missing **")
        elif len(list_arg) == 3:
            print("** value missing **")
        else:
            key = "{}.{}".format(args[0], args[1])
            arg_type = type(eval(args[3]))
            attr = args[3].strip('\'\"')
            setattr(storage.all()[key], args[2], arg_type(attr))
            storage.all()[key].save()

if __name__ == '__main__':
    HBNBCommand().cmdloop()

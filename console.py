#!/usr/bin/python3
'that contains the entry point of the command interpreter'
import cmd 


class HBNBCommand(cmd.Cmd):
    'cmd class'
    prompt = '(hbnb)'
    def do_quit(self, arg):
        'Quit command to exit the program'
        return True

    def do_EOF(self, arg):
        'EOF command to exit the program'
        return True
    
if __name__ == '__main__':
    HBNBCommand().cmdloop()

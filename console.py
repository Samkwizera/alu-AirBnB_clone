#!/usr/bin/python3
"""
Console module for the AirBnB clone project.
This module provides a command-line interface for managing objects.
"""
import cmd
import sys


class HBNBCommand(cmd.Cmd):
    """Command interpreter class for the AirBnB clone project."""
    
    prompt = '(hbnb) '

    def do_quit(self, arg):
        """Quit command to exit the program"""
        return True

    def do_EOF(self, arg):
        """EOF command to exit the program"""
        print()
        return True

    def emptyline(self):
        """Do nothing when an empty line is entered"""
        pass


if __name__ == '__main__':
    HBNBCommand().cmdloop() 
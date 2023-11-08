#!/usr/bin/python3

"""cmd control module console.py, for test specific functionality"""
import cmd


class HBNBCommand(cmd.Cmd):
    # Initialize the prompt string
    prompt = '(hbnb) '

    def do_quit(self, arg):
        return True

    def help_quit(self, arg):
        print('quit command: Exit the program')

    def do_EOF(self, arg):
        print()  # Print a new line for better formatting
        return True


if __name__ == '__main__':
    HBNBCommand().cmdloop()

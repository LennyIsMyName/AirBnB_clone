#!/usr/bin/env python3
import cmd
import models
from models.base_model import BaseModel

""" class HBNBCommand containing a command interpreter """

class HBNBCommand(cmd.Cmd):
    """  inherits from cmd module """
    prompt = "(hbnb) "
    def do_quit(self, arg):
        """ Quit command to exit the program"""
        return True

    def do_EOF(self, arg):
        """ EOF command to exit """
        print()
        return True

    def do_create(self, arg):
        """
        Create a new instance of BaseModel, saves it to the JSON file, and prints the id

        """
        if not arg:
            print("** class name missing")
            return
        try:
            obj = eval(arg + "()")
            obj.save()
            print(obj.id)
        except NameError:
            print("** class doesn't exist **")

    def do_show(self, arg):
        """Prints the string representation of an instance
        based on the class name and id"""
        args = arg.split()
        if not arg:
            print("** class name missing **")
            return
        try:
            cls = eval(args[0])
        except NameError:
            print("** class doesn't exist **")
            return
        if not issubclass(cls, models.BaseModel):
            print("** class doesn't exist **")
            return
        if len(args) < 2:
            print("** instance id missing **")
            return
        key = args[0] + '.' + args[1]
        objects = models.storage.all()
        if key not in objects:
            print("** no instance found **")
            return
        print(objects[key])

    def do_destroy(self, arg):
        """
        Deletes an instance based on class name and id 
        """
        args = arg.split()
        if not arg:
            print("** class name missing **")
            return
        try:
            del models.storage.all()[args[0] + '.' + args[1]]
            models.storage.save()
        except KeyError:
            print("** no instance found **")
            return
        except IndexError:
            if not args[1]:
                print("** instance id missing **")
            else:
                print("** class doesn't exist **")

    def do_all(self, arg):
        """
        Prints all string representation of all instances based or not on the class name.
        """
        objects = models.storage.all()
        if not arg:
            print([str(v) for k, v in objects.items()])
            return

        args = arg.split()
        try:
            cls = eval(args[0])
        except NameError:
            print("** class doesn't exist **")
            return

        if not issubclass(cls, models.BaseModel):
            print("** class doesn't exist **")
            return

        print([str(v) for k, v in objects.items() if isinstance(v, cls)])


    def do_update(self, arg):
        """Updates an instance based on the class name
        and id by adding or updating attribute"""
        args = arg.split()
        if not arg:
            print("** class name missing **")
            return
        try:
            obj = models.storage.all()[args[0] + '.' + args[1]]
        except KeyError:
            print("** no instance found **")
            return
        except IndexError:
            if not args[1]:
                print("** instance id missing **")
            else:
                print("** class doesn't exist **")
            return

        if len(args) < 3:
            print("** attribute name missing **")
            return
        elif len(args) < 4:
            print("** value missing **")
            return

        try:
            attr_value = type(getattr(obj, args[2]))(args[3])
        except AttributeError:
            attr_value = args[3]

        setattr(obj, args[2], attr_value)
        obj.save()


if __name__ == '__main__':
    HBNBCommand().cmdloop()

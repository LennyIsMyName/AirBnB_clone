#!/usr/bin/env python3
import cmd
import models
from models.base_model import BaseModel
from models.user import User
from models.state import State
from models.city import City
from models.amenity import Amenity
from models.place import Place
from models.review import Review

storage = models.FileStorage()

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
        """
        Show command to Prints the string representation of an instance based
        on
        the class name and id
        Usage: show <Class_Name> <obj_id>
        """
        args = arg.split()
        if len(args) == 0:
            print("** class name missing **")
            return
        try:
            eval(args[0])
        except Exception:
            print("** class doesn't exist **")
            return
        if len(args) == 1:
            print("** instance id missing **")
        else:
            storage.reload()
            container_obj = storage.all()
            key_id = args[0] + "." + args[1]
            if key_id in container_obj:
                value = container_obj[key_id]
                print(value)
            else:
                print("** no instance found **")

    def do_destroy(self, arg):
        """
        Destroy command to Deletes an instance based on the class name and id
        Usage: destroy <Class_Name> <obj_id>
        """

        args = arg.split()
        container_obj = []
        if len(args) == 0:
            print("** class name missing **")
            return
        try:
            eval(args[0])
        except Exception:
            print("** class doesn't exist **")
            return
        if len(args) == 1:
            print("** instance id missing **")
        else:
            storage.reload()
            container_obj = storage.all()
            key_id = args[0] + "." + args[1]
            if key_id in container_obj:
                del container_obj[key_id]
                storage.save()
            else:
                print("** no instance found **")

    def do_all(self, arg):
        """
        All command to Prints all string representation of all instances
        based or not on the class name.
        Usage: all <Class_Name>  OR  all
        """
        storage.reload()
        container_obj = storage.all()
        args = arg.split()
        list_strings = []
        if len(args) == 0:
            for obj_id in container_obj.keys():
                obj = container_obj[obj_id]
                list_strings.append(str(obj))
            print(list_strings)
            return
        if len(args) == 1:
            try:
                eval(args[0])
                for obj_id in container_obj.keys():
                    if type(container_obj[obj_id]) is eval(args[0]):
                        # the solution is using reper() => print the type too
                        # str(container_obj[obj_id]) => is a string
                        obj = container_obj[obj_id]
                        list_strings.append(str(obj))
                print(list_strings)
            except Exception:
                print("** class doesn't exist **")
                return

    def do_update(self, arg):
        """
        Update command Updates an instance based on the class name and id
        by adding or updating attribute
        Usage: update <class name> <id> <attribute name> "<attribute value>"
        $ update BaseModel 1234-1234 email "x@g.com" first_name "yy" is equal
        $ update BaseModel 1234-1234 email "x@g.com"
        """
        storage.reload()
        args = arg.split()
        length_args = len(args)
        if length_args == 0:
            print("** class name missing **")
            return
        if len(args) >= 1:
            try:
                eval(args[0])
                if len(args) == 1:
                    print("** instance id missing **")
                    return
                try:
                    key_id = args[0] + "." + args[1]
                    container_obj = storage.all()
                    container_obj[key_id]
                except Exception:
                    print("** no instance found **")
                    return
            except Exception:
                print("** class doesn't exist **")
                return
        if len(args) >= 2:
            try:
                eval(args[0])
                if len(args) == 2:
                    print("** attribute name missing **")
                    return
            except Exception:
                print("** class doesn't exist **")
                return

        if len(args) >= 3:
            try:
                eval(args[0])
                if len(args) == 3:
                    print("** value missing **")
                    return
            except Exception:
                print("** class doesn't exist **")
                return
        if len(args) >= 4:
            args = " ".join(str(arg).split(maxsplit=3)).split(maxsplit=3)

            class_name = args[0]
            obj_id = args[1]
            obj_attr = args[2].strip("\"\'")
            obj_new_val = args[3]
            try:
                eval(class_name)
                key_id = class_name + "." + obj_id
                container_obj = storage.all()
                if key_id in container_obj:
                    obj = container_obj[key_id]
                    try:
                        type_attr = type(getattr(obj, obj_attr))
                        obj_new_val = self.same_type_as_attr(obj_new_val,
                                                             type_attr)
                        if obj_new_val is False:
                            return
                    except Exception:
                        obj_new_val = self.convert_new_val(obj_new_val)
                    setattr(obj, obj_attr, obj_new_val)
                    storage.save()
                else:
                    print("** no instance found **")
                    return
            except Exception as ex:
                print("** class doesn't exist **")

    def precmd(self, arg):
        classname = arg.split('.')[0]
        if classname in storage.classes() and '(' in arg and ')' == arg[-1]:
            command = arg.split('.')[1].split('(')[0]
            commands = ['all', 'count', 'show', 'destroy', 'update']
            if command in commands:
                if command == 'count':
                    values = [str(obj) for obj in storage.all().values()
                              if obj.__class__.__name__ == classname]
                    print(len(values))
                    return ""
                elif command == 'show' or command == 'destroy':
                    id = arg.split('.')[1].split('(')[1][1:-2]
                    return f"{command} {classname} {id}"
                elif command == 'update':
                    args = arg.split('.')[1].split('(')[1][:-1]
                    id = args.split(',')[0].strip()[1:-1]
                    attr = "".join(args.split('{')[1:]).strip()
                    attr = '{' + attr
                    if '{' in attr and '}' in attr:
                        attr = json.loads(attr.replace('\'', '"'))
                        for k, v in attr.items():
                            self.do_update(f"{classname} {id} {k} {v}")
                        return ""
                    else:
                        a = args.split(',')[1].strip().strip('"')
                        value = args.split(',')[2].strip().strip('"')
                        return f"{command} {classname} {id} {a} {value}"
                return f"{command} {classname}"
        return arg

if __name__ == '__main__':
    HBNBCommand().cmdloop()

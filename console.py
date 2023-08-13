#!/usr/bin/python3
"Module to implement the command line interpreter for the project"
import cmd
from models.base_model import BaseModel
from models import storage
from models.user import User
from models.state import State
from models.city import City
from models.review import Review
from models.place import Place
from models.amenity import Amenity


class_map = {"BaseModel": BaseModel,
             "User": User,
             "State": State,
             "City": City,
             "Review": Review,
             "Place": Place,
             "Amenity": Amenity}


def clean_quotes(str):
    "helper function to read input text of quotation marks"
    if str.startswith('"') and str.endswith('"'):
        str = str[1:-1]
    return str


class HBNBCommand(cmd.Cmd):
    """Class module to implement CLI"""

    prompt = '(hbnb) '

    def default(self, arg):
        """implementing custom functionalities"""
        class_name, method = arg.split(".")
        try:
            func, id = method.split("(")
        except ValueError:
            func, id = method, None

        search_key = f"{class_name}.{id[:-1]}"

        if method == 'all()':
            for key, value in storage.all().items():
                key_class = key.split(".")[0]
                if key_class == class_name:
                    print(value)

        if method == 'count()':
            count = 0
            for key, value in storage.all().items():
                key_class = key.split(".")[0]
                if key_class == class_name:
                    count += 1
            print(count)

        if func == 'show':
            if (class_name not in class_map):
                print("** class doesn't exist **")
            elif len(id[:-1]) == 0:
                print("** instance id missing **")
            else:
                if search_key in storage.all().keys():
                    print(storage.all().get(search_key))
                else:
                    print("** no instance found **")

        if func == 'destroy':
            if (class_name not in class_map):
                print("** class doesn't exist **")
            elif len(id[:-1]) == 0:
                print("** instance id missing **")
            else:
                if search_key in storage.all().keys():
                    storage.all().pop(search_key)
                    storage.save()
                else:
                    print("** no instance found **")

    def do_quit(self, arg):
        """Quit command to exit the program"""
        return True

    def do_EOF(self, arg):
        """EOF command to exit the program"""
        return True

    def do_help(self, arg):
        """Display help message"""
        cmd.Cmd.do_help(self, arg)

    def emptyline(self):
        """Do nothing on an empty line"""
        pass

    def do_create(self, arg):
        "Creates an instance of BaseModel and print its id. <create BaseModel>"
        if not arg:
            print("** class name missing **")
        elif (arg not in class_map):
            print("** class doesn't exist **")
        else:
            new_model = class_map[arg]()
            new_model.save()
            print(new_model.id)

    def do_show(self, arg):
        "Prints the string representation of a BaseModel instance"
        args = arg.split()
        if len(args) < 1:
            print("** class name missing **")
        elif (args[0] not in class_map):
            print("** class doesn't exist **")
        elif len(args) < 2:
            print("** instance id missing **")
        else:
            search_key = f"{args[0]}.{args[1]}"
            if search_key in storage.all().keys():
                print(storage.all().get(search_key))
            else:
                print("** no instance found **")

    def do_destroy(self, arg):
        "Deletes the BaseModel instance whose ID is passed"
        args = arg.split()
        if len(args) < 1:
            print("** class name missing **")
        elif (args[0] not in class_map):
            print("** class doesn't exist **")
        elif len(args) < 2:
            print("** instance id missing **")
        else:
            search_key = f"{args[0]}.{args[1]}"
            if search_key in storage.all().keys():
                storage.all().pop(search_key)
                storage.save()
            else:
                print("** no instance found **")

    def do_all(self, arg):
        " Prints all string representation of all model instances"
        if not arg:
            obj_list = []
            for key, value in storage.all().items():
                obj_list.append(str(value))
            print(obj_list)
        elif (arg not in class_map):
            print("** class doesn't exist **")
        else:
            obj_list = []
            for key, value in storage.all().items():
                if type(value).__name__ == arg:
                    obj_list.append(str(value))
            print(obj_list)

    def do_update(self, arg):
        "Updates a model instance with the provided attribute values"
        args = arg.split()
        if len(args) < 1:
            print("** class name missing **")
        elif (args[0] not in class_map):
            print("** class doesn't exist **")
        elif len(args) < 2:
            print("** instance id missing **")
        elif len(args) < 3:
            print("** attribute name missing **")
        elif len(args) < 4:
            print("** value missing **")
        else:
            search_key = f"{args[0]}.{args[1]}"
            if search_key in storage.all().keys():
                model = storage.all().get(search_key)
                attr_name = clean_quotes(args[2])
                attr_val = clean_quotes(args[3])
                setattr(model, attr_name, attr_val)
                model.save()

            else:
                print("** no instance found **")


if __name__ == '__main__':
    HBNBCommand().cmdloop()

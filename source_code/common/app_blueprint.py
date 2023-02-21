from flask import Blueprint
class AppBP(Blueprint):
    def __init__(self,name, import_name):
        super().__init__(name , import_name)

'''
The code defines a class AppBP that inherits from the Blueprint class of Flask, which is a way to organize a group of related routes and views.

The __init__ method of AppBP is called when an instance of this class is created, with two parameters: name and import_name.

name is the name of the blueprint, which should be unique, and import_name is the name of the package or module that the blueprint is defined in.

The super() function is called with name and import_name as arguments, which calls the __init__ method of the Blueprint class and initializes the blueprint.
'''
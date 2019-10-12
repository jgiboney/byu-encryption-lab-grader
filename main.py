# -----------------------------------------------------------------------------
#
# Copyright: Justin Scott Giboney, 2019
#
# This code is only to be used for testing the IT&C 366 encryption lab at
# Brigham Young University.
# 
# No permission is granted to redistribute, replicate, mimic, copy, or modify 
# this code.
#
# No warranty is given either. This may annihilate your computer, your files,
# your life, and/or humanity. Use at your own risk! 
#
# -----------------------------------------------------------------------------

import importlib, os

# Setup the student libraries to run
studentModuleDirectory = 'studentLibrary/' # This should be a command line parameter
studentModules = {}

for module in os.listdir(os.path.dirname(studentModuleDirectory)):
    module_path = studentModuleDirectory[:-1]+'.'+module
    if module_path[-11:] != '__init__.py' and module_path[-3:] == '.py':
        studentModules[module] = importlib.import_module(module_path[:-3])
del module

for module in studentModules.keys():
    studentModules[module].sayHello()

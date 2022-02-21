import sys
from Item import *
from Task import TaskType
# TODO: import all needed classes for str_to_class to work

def str_to_class(classname):
    return getattr(sys.modules[__name__], classname)

def str_to_instance(token):
    #Verification securite token OK
    classname = token.split(".")[0]
    aclass = str_to_class(classname)
    assert(aclass.__name__ == classname)

    # Evaluation
    a = eval(token)

    return a.__class__(a.value)

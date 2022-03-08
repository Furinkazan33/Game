#!/usr/bin/env python3
if __name__ == "__main__":
    raise RuntimeError("Not meant to be run")

import sys
from Item import *
from Task import TaskType
# TODO: import all needed classes for str_to_class to work

def str_to_class(classname: str):
    return getattr(sys.modules[__name__], classname)

def str_to_instance(token :str):
    token = token.split(".")
    aclass = str_to_class(token[0])

    return aclass(token[1])



"""
Handles the type and assignment checks for yaml -> data-structures
"""

import sys

class safe_assignment:
    """
    - safe_assign_exit: if the assignment doesnt meet the correct requrements we exit the program
    - safe_assign_default: assigns a default value if a key doesnt exists (
    will still exit if the key exists but the type is incorrect)
    """

    def safe_assign_exit(self, d_var: dict, key: str, _type, msg: str):
        """ If the key doesnt exists and is of correct type, we exit the program, because we can't continue """
        if not key in d_var:
            print(f"[ERROR]: {msg}")
            sys.exit(0)
        if not isinstance(d_var[key], _type):
            print(f"[ERROR]: Wrong type for: {d_var} at {key}, got a: {type(d_var[key])}, but requires {_type}, consult documentation for correct type")
            sys.exit(0)
        return d_var[key]
    
    def safe_assign_default(self, d_var: dict, key: str, default_value, _type, msg: str = ""):
        """ 
        If key isnt found, we return the default_value
        If key isnt for correct type, we cannot continue.
        """
        if not key in d_var:
            if msg != "":
                print(f"[ERROR]: {msg}, assigning default value: {default_value}")
            return default_value
        if not isinstance(d_var[key], _type):
            print(f"[ERROR]: Wrong type for: {d_var} at {key}, got a: {type(d_var[key])}, but requires {_type}, consult documentation for correct type")
            sys.exit(0)    
        return d_var[key]
    
    def is_list_of_dicts(self, data):
        """
        data parameter should be the list that will be tested
        for containing dicts
        """
        for d in data:
            if not isinstance(d, dict):
                return False
            
        return True
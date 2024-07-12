"""
YAMLTypes adds themselfs to the objs list and the container just calls
'handle' and begins all of the objects.

TODO: remove this, not neccesary
"""

#Global GUI Items
objs: list = []

class container:
    """
    PREPARING DEPRECATION
    """
    def __init__(self):
        pass

    def handle(self):
        """
        Calls begin in all objects inside the objs list
        """
        for o in objs:
            o.begin()
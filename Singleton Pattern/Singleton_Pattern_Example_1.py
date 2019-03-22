"""

It involves single class which is responsible to crate an object while making sure that only single object gets created.

Output :
    The number of instances created are same and there is no difference in the objects listed in output.

References :
    1. https://www.tutorialspoint.com/python_design_patterns/python_design_patterns_singleton.htm

"""


class Singleton:
    __instance = None

    @staticmethod
    def getInstance():
        """ Static access method. """
        if Singleton.__instance is None:
            Singleton()
        return Singleton.__instance

    def __init__(self):
        """ Virtually private constructor. """
        if Singleton.__instance is not None:
            raise Exception("This class is a singleton!")
        else:
            Singleton.__instance = self


# s = Singleton()
# print(s)
#
# s = Singleton.getInstance()
# print(s)
#
# s = Singleton.getInstance()
# print(s)




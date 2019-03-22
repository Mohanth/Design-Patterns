# Lazy Initialization in the Singleton pattern
class Singleton:
    __instance = None

    def __init__(self):
        if not self.__instance:
            print("Instance already created:")
        else:
            print("Instance is not created")

    @classmethod
    def getInstance(cls):
        if not cls.__instance:
            cls.__instance = Singleton()
        return cls.__instance


s1 = Singleton()
s2 = Singleton()
print(s1.getInstance())
print(s2.getInstance())

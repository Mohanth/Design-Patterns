"""

Builder provides a unique layer between construction and representation of a specified object created by class.
Builder class builds the final object in step-by-step procedure.

"""


class Director:
    __builder = None

    def setBuilder(self, builder):
        self.__builder = builder

    def getCar(self):
        car = Car()

        # First goes the body
        body = self.__builder.getBody()
        car.setBody(body)

        # Then engine
        engine = self.__builder.getEngine()
        car.setEngine(engine)

        return car


# The whole product
class Car:
    def __init__(self):
        self.__wheels = list()
        self.__engine = None
        self.__body = None

    def setBody(self, body):
        self.__body = body

    def setEngine(self, engine):
        self.__engine = engine

    def specification(self):
        print("body: %s" % self.__body.shape)
        print("engine horsepower: %d" % self.__engine.horsepower)


# Interface
class Builder:

    def getEngine(self): pass

    def getBody(self): pass


class JeepBuilder(Builder):

    def getEngine(self):
        engine = Engine()
        engine.horsepower = 400
        return engine

    def getBody(self):
        body = Body()
        body.shape = "SUV"
        return body


# Car parts

class Engine:
    horsepower = None


class Body:
    shape = None


def main():
    jeepBuilder = JeepBuilder()  # initializing the class

    director = Director()

    # Build Jeep
    print("Jeep")
    director.setBuilder(jeepBuilder)
    jeep = director.getCar()
    jeep.specification()
    print("")


if __name__ == "__main__":
    main()

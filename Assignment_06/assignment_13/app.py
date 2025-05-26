class Engine:
    def start(self):
        print("Engine started.")

class Car:
    def __init__(self, engine):
        self.engine = engine

    def start(self):
        self.engine.start()
        print("Car is ready to go!")

# Usage
engine = Engine()
car = Car(engine)
car.start()

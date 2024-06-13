from abc import ABC, abstractmethod

class Vehicle(ABC):
    @abstractmethod
    def start_engine(self):
        pass

    @abstractmethod
    def stop_engine(self):
        pass

class Car(Vehicle):
    def __init__(self, brand, model):
        self.brand = brand
        self.model = model
        self.engine_running = False

    def start_engine(self):
        if not self.engine_running:
            self.engine_running = True
            print(f"{self.brand} {self.model} engine started.")
        else:
            print(f"{self.brand} {self.model} engine is already running.")

    def stop_engine(self):
        if self.engine_running:
            self.engine_running = False
            print(f"{self.brand} {self.model} engine stopped.")
        else:
            print(f"{self.brand} {self.model} engine is already off.")

# Example usage
if __name__ == "__main__":
    car = Car("Toyota", "Camry")
    car.start_engine()
    car.start_engine()
    car.stop_engine()
    car.stop_engine()

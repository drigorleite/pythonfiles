class Car:
    def __init__(self, year_model, make):
        self.__year_model = year_model
        self.__make = make
        self.__speed = 0

    def accelerate(self):
        """Increases the car's speed by 5 each time it is called."""
        self.__speed += 5

    def brake(self):
        """Decreases the car's speed by 5 each time it is called, not allowing negative speeds."""
        if self.__speed >= 5:
            self.__speed -= 5
        else:
            self.__speed = 0

    def get_speed(self):
        """Returns the current speed of the car."""
        return self.__speed


def main():

    my_car = Car(2022, 'Tesla Model S')


    print("Accelerating:")
    for _ in range(5):
        my_car.accelerate()
        print("Current speed:", my_car.get_speed())

    print("Braking:")
    for _ in range(5):
        my_car.brake()
        print("Current speed:", my_car.get_speed())


if __name__ == "__main__":
    main()

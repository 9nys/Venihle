class Vehicle:
    def __init__(self, name, speed, cost):
        self.name = name
        self.speed = speed
        self.cost = cost

    def __gt__(self, other):
        return self.speed > other.speed

# Створення списку транспортних засобів
vehicles = [
    Vehicle("Audi", 250, 7000),
    Vehicle("Skoda", 220, 6500)
]

# Відсортуємо список за швидкістю
sorted_vehicles = sorted(vehicles, key=lambda x: x.speed)

# Виведемо відсортований список
for vehicle in sorted_vehicles:
    print(vehicle.name, "-", vehicle.speed, "km/h")

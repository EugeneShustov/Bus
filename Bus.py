class bus:
    def __init__(self, speed, seats):
        self.speed = 0
        self.max_speed = speed
        self.max_seats = seats
        self.passengers = {}
        self.free_seats = True

    def add(self, last_name, seat_number):
        if len(self.passengers) >= self.max_seats:
            self.free_seats = False
            print("Нет мест")
            return

        if seat_number in self.passengers:
            print(f"Место {seat_number} занято")
        else:
            self.passengers[seat_number] = last_name
            print(f"{last_name} сел на место {seat_number}")

    def remove(self, last_name):
        for seat, passenger in list(self.passengers.items()):
            if passenger == last_name:
                del self.passengers[seat]
                self.free_seats = True
                print(f"{last_name} вышел из автобуса")
                return
        print(f"{last_name} не найдено")

    def change_speed(self, speed_change):
        self.speed += speed_change
        self.speed = min(self.speed, self.max_speed)
        self.speed = max(self.speed, 0)
        print(f"Скорость: {self.speed} км.ч")

    def __contains__(self, last_name):
        return last_name in self.passengers.values()

    def __add__(self, last_name):
        self.add(last_name, len(self.passengers) + 1)
        return self

    def __sub__(self, last_name):
        self.remove(last_name)
        return self

bus = bus(100, 5)
bus.add("Шустов", 3)
bus.add("Лепкович", 5)
bus.change_speed(30)
bus += "Шустов"
bus -= "Лепкович"
print("Шустов в автобусе:", "Шустов" in bus)

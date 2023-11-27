class HolidayCostCalculator:
    def __init__(self):
        self.total_hotel_cost = 0
        self.total_flight_cost = 0
        self.total_car_rental_cost = 0

    def start(self):
        print("Welcome to the holiday cost calculator\n")
        while True:
            menu_1_selection = input("\nStart your holiday? (Y or N): ")
            if menu_1_selection.upper() == 'Y':
                self.city_nights_rental_choice()
                break
            elif menu_1_selection.upper() == 'N':
                print("Goodbye!")
                return
            else:
                print("Invalid input. Please enter Y or N.")

    def city_nights_rental_choice(self):
        print('''             
              CITY      PRICE
          1 : Rome    : £ 125pp
          2 : Paris   : £ 100pp
          3 : USA     : £ 279pp
          4 : Italy   : £ 235pp
          5 : England : £ 180pp''')

        while True:
            try:
                city_flight_choice = int(input("\nPlease input the number for the city of your choice: "))
                if city_flight_choice < 1 or city_flight_choice > 5:
                    print(f"Invalid Option -{city_flight_choice}-.  Please Enter Choice From The List Above ")
                else:
                    break
            except ValueError:
                print("Invalid input. Please enter a number.")

        while True:
            try:
                number_of_nights = int(input("\nHow many nights would you like to stay? "))
                break
            except ValueError:
                print("Invalid input. Please enter a number.")

        while True:
            car_rental_choice = input("\nWould you like car rental? (Y or N): ")
            if car_rental_choice.upper() == "Y" or car_rental_choice.upper() == "N":
                break
            else:
                print("Invalid input. Please enter Y or N.")

        if car_rental_choice.upper() == "Y":
            while True:
                try:
                    car_rental_duration = int(input("\nPlease enter the duration for car rental: "))
                    break
                except ValueError:
                    print("Invalid input. Please enter a number.")

        print('''
          1: Standard   : £55  per night
          2: Exclusive  : £105 per night
          3: Penthouse  : £255 per night
                        ''')
        while True:
            try:
                hotel_choice = int(input("\nPlease select from the hotel options above: "))
                if hotel_choice in [1, 2, 3]:
                    break
                else:
                    print("Invalid input. Please enter a valid hotel option.")
            except ValueError:
                print("Invalid input. Please enter a number.")

        hotel_choice_dict = {
            1: 'Standard',
            2: 'Exclusive',
            3: 'Penthouse',
        }
        hotel_type = hotel_choice_dict[hotel_choice]
        hotel_type_cost = {
            'Standard': 55,
            'Exclusive': 105,
            'Penthouse': 255,
        }[hotel_type]

        city_flight_dict = {
            1: 'Rome',
            2: 'Paris',
            3: 'USA',
            4: 'Italy',
            5: 'England',
        }
        city_flight_cost = {
            'Rome': 125,
            'Paris': 100,
            'USA': 279,
            'Italy': 235,
            'England': 180,
        }[city_flight_dict[city_flight_choice]]
        print(f"\nLocation: {city_flight_dict[city_flight_choice]}")

        self.total_hotel_cost = self.hotel_cost(hotel_type_cost, number_of_nights, hotel_type)
        self.total_flight_cost = self.plane_cost(city_flight_cost)
        self.total_car_rental_cost = 0

        if car_rental_choice.upper() == "Y":
            self.total_car_rental_cost = self.car_rental(car_rental_duration)

        self.total_holiday_cost()

    def hotel_cost(self, hotel_type_cost, number_of_nights, hotel_type):
        total_hotel_cost = hotel_type_cost * number_of_nights
        print(f"\nHotel type: {hotel_type}\nHotel price: £{hotel_type_cost}\nNumber of nights: {number_of_nights}\nHotel cost: £{total_hotel_cost}\n")
        return total_hotel_cost

    def plane_cost(self, city_flight_cost):
        total_flight_cost = city_flight_cost
        print(f"Total flight cost: £{total_flight_cost} return")
        return total_flight_cost

    def car_rental(self, car_rental_duration):
        car_rental_cost = 25.50 * car_rental_duration
        print(f"\nFixed car rental price per day: £25.50\nDuration: {car_rental_duration} days \nCar rental cost: £{car_rental_cost}")
        return car_rental_cost

    def total_holiday_cost(self):
        total_cost_of_holiday = self.total_hotel_cost + self.total_flight_cost + self.total_car_rental_cost
        print(f"\nTotal holiday cost: £{total_cost_of_holiday}\n")
        self.reload_choice()

    def reload_choice(self):
        reload_choice = input("Would you like to reload this calculator? (Y/N): ").upper()
        if reload_choice == 'Y':
            self.start()
        else:
            print("Thanks for using our holiday calculator")
            quit()


# Create an instance of the HolidayCostCalculator and start the program
holiday_calculator = HolidayCostCalculator()
holiday_calculator.start()

                            # Holiday cost App 'using functions'
# Define a function for costing a holiday 
# Create welcome message 
def holiday_cost_function():
    print("Welcome to the holiday cost calculator\n")

    # Error handle user input # 'needs a little more error handling' 
    while True:
        menu_1_selection = input("\nStart your holiday? (Y or N): ")
        if menu_1_selection.upper() == 'Y':
            city_nights_rental_choice()
            break
        elif menu_1_selection.upper() == 'N':
            print("Goodbye!")
            return
        else:
            print("Invalid input. Please enter Y or N.")

# Define a function for user selection for city, nights, rental choice
# display user selection choice of city and price value
def city_nights_rental_choice():
    print('''             
          CITY      PRICE
      1 : Rome    : £ 125pp
      2 : Paris   : £ 100pp
      3 : USA     : £ 279pp
      4 : Italy   : £ 235pp
      5 : England : £ 180pp''')

    # Initalise user inputs for city flight, number of nights, and car rental choice selection
    # Error handle user input 
    while True:
        try:
            city_flight_choice = int(input("\nPlease input the number for the city of your choice: "))
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

    # Display menu for hotel room type
    # Initaltise user input for hotel type choice 
    # Error handle user input 
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

    # create dict for hotel menu selection choice and get value
    hotel_choice_dict = {
        1: 'Standard',
        2: 'Exclusive',
        3: 'Penthouse',
    }
    hotel_type = hotel_choice_dict[hotel_choice]

    # Using value from hotel type as a key to retrieve value for hotel type cost 
    hotel_type_cost = {
        'Standard': 55,
        'Exclusive': 105,
        'Penthouse': 255,
    }[hotel_type]

    # Create dict for city flight selection 
    city_flight_dict = {
        1: 'Rome',
        2: 'Paris',
        3: 'USA',
        4: 'Italy',
        5: 'England',
    }

    # Create dict for city flight cost to retrieve value for price of city flight data
    # Display city flight selection from dict
    city_flight_cost = {
        'Rome': 125,
        'Paris': 100,
        'USA': 279,
        'Italy': 235,
        'England': 180,
    }[city_flight_dict[city_flight_choice]]
    print(f"\nLocation: {city_flight_dict[city_flight_choice]}")

    # Putting all data into variables which will be retreived from 'hotel_cost, plane_cost, car_rental' Defined Functions
    # Initialise car rental choice for user input = 'Y'
    # fully implement variables into final function to display total holiday cost 
    total_hotel_cost = hotel_cost(hotel_type_cost, number_of_nights, hotel_type)
    total_flight_cost = plane_cost(city_flight_cost)
    total_car_rental_cost = 0

    if car_rental_choice.upper() == "Y":
        total_car_rental_cost = car_rental(car_rental_duration)

    total_holiday_cost(total_hotel_cost, total_flight_cost, total_car_rental_cost)

# Take hotel pricing variables as an argument 'in defined function' and calculate cost based on info given
# Display all results in a readable way 
# Return the value of hotel_cost to total_hotel_cost var for final pricing  
def hotel_cost(hotel_type_cost, number_of_nights, hotel_type):
    total_hotel_cost = hotel_type_cost * number_of_nights
    print(f"\nHotel type: {hotel_type}\nHotel price: £{hotel_type_cost}\nNumber of nights: {number_of_nights}\nHotel cost: £{total_hotel_cost}\n")
    return total_hotel_cost

# Take data from city_flight_cost as an argument and display result
# Return the value of total_flight_cost for final pricing 
def plane_cost(city_flight_cost):
    total_flight_cost = city_flight_cost
    print(f"Total flight cost: £{total_flight_cost} return")
    return total_flight_cost

# Take car_rental_duration as an argument to calculate fixed car rental price and display results
# Return car_rental_cost for final pricing 
def car_rental(car_rental_duration):
    car_rental_cost = 25.50 * car_rental_duration
    print(f"\nFixed car rental price per day: £25.50\nDuration: {car_rental_duration} days \nCar rental cost: £{car_rental_cost}")
    return car_rental_cost

# Final function to calculate all returned values from all functions to display the final price of the holliday
def total_holiday_cost(total_hotel_cost, total_flight_cost, total_car_rental_cost): 
    total_cost_of_holiday = total_hotel_cost + total_flight_cost + total_car_rental_cost
    print(f"\nTotal holiday cost: £{total_cost_of_holiday}\n")

holiday_cost_function()

# Reload function
reload_choice = input("Would you like to reload this calculator? (Y/N): ").upper()
if reload_choice == 'Y':
    city_nights_rental_choice()
else:
    print("Thanks for using our holiday calculator")
    quit()

#-------------------------------------Pseudo code---------------------------------------------#     #-------------------Time colpexity-----------------#
# Begin                                                                                       #     #                                                  #
#    Define a function for costing a holiday                                                  #     # The overall time complexity is O(1)              #
#    create user selection for holiday flight choice                                          #     #                                                  #
#    create dict's for holiday flight choice location and price                               #     # holidy_cost_function:   O(1)                     #
#    get user input for car rental duration                                                   #     # consists of constant input / output              #
#    create function to calculate and display holiday selection                               #     # operations / function calls                      #
#    take user inputs and store into var for final pricing                                    #     #                                                  #
#    create function to take specified parameter as its arument                               #     # city_nights_rental_choice function:  O(1)        #                          
#    use created function to calculate user selected plane cost                               #     # involves input/output operations, function calls #
#    return data into variable for final pricing                                              #     # some loops with a fixed number of iterations.    #
#    create function to take specified parameters as its argument                             #     #                                                  #
#    use created function to calculated fixed car rental cost * car rental duration           #     # hotel_cost, plane_cost, and car_rental: O(1)     #
#    return values for final pricing                                                          #     # they all perform basic arithmetic operations and # 
#    display all pricing information in all relevant functions                                #     # print statements                                 #
#    create final function to calculate all returned data from functions                      #     #                                                  #
#    add them all together and display results                                                #     # total_holiday_cost function:  O(1)               #
# End                                                                                         #     # involves basic arithmetic operations and a       #
#---------------------------------------------------------------------------------------------#     # single print statment                            #
                                                                                                    # 
                                                                                                    # the execution time remains constant regardless   #
                                                                                                    # of the input size                                #
                                                                                                    #--------------------------------------------------#
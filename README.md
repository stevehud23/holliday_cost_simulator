# Holiday Cost Calculator (Version 1 'Working With Functions')

The Holiday Cost Calculator is a Python program designed to help users estimate the expenses of their holiday trips by considering various factors such as destination, accommodation, flight costs, and car rental expenses.

## Table of Contents

1. [Overview](#overview)
2. [Features](#features)
3. [Installation](#installation)
4. [Usage](#usage)
5. [User Guide](#user-guide)
6. [Contributing](#contributing)
7. [License](#license)
8. [Version 2](#working-with-classes)
9. [Version 3 GUI](#GUI-Kivvy-Framework-'Coming-Soon')

## Overview

The Holiday Cost Calculator provides users with a straightforward interface to input their preferences and choices for their holiday. It calculates the total cost based on user selections, including accommodation type, destination, duration of stay, flight expenses, and car rental options.

## Features

- Selection of destination cities with associated prices.
- Choosing the type of accommodation from different options.
- Estimation of flight costs based on selected destinations.
- Provision for car rental expenses if required.

## Installation

1. Clone the repository:
    ```bash
    git clone https://github.com/your-username/holiday-cost-calculator.git
    ```

2. Navigate to the project directory:
    ```bash
    cd holiday-cost-calculator
    ```

3. Run the program:
    ```bash
    python holiday_calculator.py
    ```

## Usage

The program guides users through a series of prompts to input their preferences and choices for the holiday. Follow the instructions on the command line interface to make selections and receive a calculated estimate of the total holiday cost.

## User Guide

1. **Start the Calculator**:
    - Launch the program.
    - Respond to the prompt with 'Y' to start your holiday calculations.

2. **City and Price Selection**:
    - Choose a city from the provided list by inputting the corresponding number.
    - Enter the number of nights you intend to stay.
    - Indicate whether you require car rental.

3. **Accommodation Selection**:
    - Select the type of accommodation from the available options.

4. **Review and Calculation**:
    - Review the details entered and the calculated costs.
    - Optionally, reload the calculator to estimate different scenarios or exit the program.

## Contributing

Contributions are welcome! If you'd like to contribute to this project, please fork the repository, make changes, and submit a pull request.

## License

This project is licensed under the [MIT License](LICENSE).

## Working With Classes
0. **'ClassHolidayCost.py'**:
    - This project yields the same results as version 1 but is more efficient with the use of a class method which utilizes the code for better redability, scalabilty,. There has been some minor updates to help better           functioning.  Here is a list of the inner logic and the updated funtion changes:

2. **Validation Loops**:
    -  To handle user input validation, ensuring that the program prompts users until valid input is provided. This is great for preventing crashes due to unexpected inputs
      
3. **Dictionary Usage**:
    - To map user choices to corresponding values (like hotel types and city names) and then used these mappings to calculate costs.

4. **Method Calls**:
    - The method calls (self.hotel_cost, self.plane_cost, self.car_rental, etc.) to calculate total holliday cost

5. **Recursion with reload_choice()'Minor Update Using Loop Instead '**:
    - As repeated calls can consume stack space which may create problems with stack overflow.
    - updated to a loop to avoid potential stack overflow for multiple reloads.
    - This was new method was implemented for the reload function.  

6. **Error Handling**:
    - implemented basic error handling using try-except blocks to catch input-related errors

-----

# Flight Booking Application

This is a simple desktop application for booking flights, built using Python's Tkinter for the graphical user interface and SQLite for database management.

## Features

  * **Customer Details Input**: Allows users to enter personal information, contact details, number of adults and children, destination, and flight date.
  * **Flight Filtering**: Filter available flights based on class (Economy, Business, First Class) and view corresponding airline options.
  * **Booking Confirmation**: Generates a billing summary and confirms flight bookings with a unique flight number.
  * **Database Storage**: Stores all booking details in a SQLite database (`flights.db`).
  * **View Booked Flights**: Displays a list of all previously booked flights directly within the application.

## Requirements

Before running the application, ensure you have the following installed:

  * **Python 3.x**: The application is written in Python. You can download it from [python.org](https://www.python.org/downloads/).
  * **Tkinter**: This is usually included with standard Python installations. If you encounter issues, you might need to install it separately (e.g., `sudo apt-get install python3-tk` on Debian/Ubuntu).
  * **SQLite3**: Also typically included with Python. No separate installation is usually required.

## How to Run

1.  **Save the Code**: Save the provided Python code into a file named `flight_booking_app.py` (or any other `.py` extension).

2.  **Open a Terminal or Command Prompt**: Navigate to the directory where you saved the file.

3.  **Run the Application**: Execute the script using Python:

    ```bash
    python flight_booking_app.py
    ```

    This will open the Flight Booking Application window.

## How to Use

1.  **Customer Details**:

      * Fill in all the required fields under the "Customer Details" section (First name, Last name, Contact number, Email, Number of Adults, Number of Children, Destination City, Date, Flight Number).
      * Click the **Submit** button to book the flight and generate a bill. A confirmation message will appear.

2.  **Filter Flights**:

      * In the "Filter flights" section, select a flight class (Economy, Business, First Class) from the dropdown.
      * Click **Find Flights** to see the available airlines for that class.

3.  **Booked Flights**:

      * Click the **Show All** button in the "Booked Flights" section to view a list of all flights previously booked through the application.

## Database

The application uses an SQLite database named `flights.db`. This file will be created automatically in the same directory as your script when you run the application for the first time. The `details` table stores the following information:

  * `name`: Customer's first name (text)
  * `contact`: Customer's contact number (integer)
  * `num`: Total number of passengers (adults + children) (integer)
  * `dest`: Destination city (text)
  * `f_num`: Flight number (integer)
  * `price`: Total price of the booking (integer)

-----
<img width="908" height="709" alt="image" src="https://github.com/user-attachments/assets/514c7796-b437-41ce-80ff-da7e92ea2cb8" />

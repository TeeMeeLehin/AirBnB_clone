# AirBnb Clone Project - The Console
AirBnB_clone is a command-line application that provides a simple and interactive interface for managing accommodations similar to the popular Airbnb platform. This project is designed to showcase object-oriented programming principles, data serialization, and basic command-line interaction.

#### Features of this CLI:
* Create a new object (ex: a new User or a new Place)
* Retrieve an object from a file, a database etc...
* Do operations on objects \
* Update attributes of an object
* Destroy an object

### Installation
1. Clone this repository to your local machine: `git clone https://github.com/TeeMeeLehin/AirBnB_clone.git`
2. Navigate to the project directory: `cd py-airbnb`
3. Run the command-line interface: `./console.py`

### Usage
Once you've started the command-line interface using console.py, you can interact with the application using a series of commands and options. The application supports creating and managing Users, cities, states, places, reviews, and amenities. The interactive console provides guidance on available commands and their usage. Type in the `help` command for more information about the available commands.

#### Example commands:
* `create City`
* `update City <city_id> name "Akure"`
* `all Users`
* `show Place <place_id>`
* `destroy State <state_id>`
* `quit`

```
timix@TeeMee-s-PeeCee:~/Documents/ALX/AirBnB_clone$ ./console.py
(hbnb) help

Documented commands (type help <topic>):
========================================
EOF  all  create  destroy  help  quit  show  update

(hbnb) all User
["[User] (e1c9aca2-5297-4ff6-bdcc-9714976617cf) {'id': 'e1c9aca2-5297-4ff6-bdcc-9714976617cf', 'created_at': datetime.datetime(2023, 8, 12, 12, 52, 59, 828191), 'updated_at': datetime.datetime(2023, 8, 12, 12, 52, 59, 828193)}"]
(hbnb) create State
4aa1644c-12b5-4748-80aa-7b38ec3e9aa8
(hbnb) update State 4aa1644c-12b5-4748-80aa-7b38ec3e9aa8 name "Lagos"
(hbnb) show State 4aa1644c-12b5-4748-80aa-7b38ec3e9aa8
[State] (4aa1644c-12b5-4748-80aa-7b38ec3e9aa8) {'id': '4aa1644c-12b5-4748-80aa-7b38ec3e9aa8', 'created_at': datetime.datetime(2023, 8, 12, 18, 44, 57, 762035), 'updated_at': datetime.datetime(2023, 8, 12, 18, 45, 17, 141964), 'name': 'Lagos'}
(hbnb) quit
```

### Testing
Unit tests for the core classes (BaseModel, User, State, City, Place, Review, Amenity) are included in the tests directory. You can run the tests using the following command: `python3 -m unittest discover tests`

### Disclaimer
AirBnB_clone is a simplified demonstration of basic software engineering concepts and should not be used for production purposes.


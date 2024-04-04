# Coffee Machine Program

This is a simple command line program that simulates a coffee machine. 
It's written in Python and uses object-oriented programming principles.

## Classes

The program consists of three main classes:

- `CoffeeMaker`: This class manages the resources needed to make coffee (water, milk, coffee). 
   It can report the current resources, check if there are enough resources to make a drink, 
   and make the coffee.

- `MoneyMachine`: This class manages the money transactions. 
   It can report the current money, process payment, and check if the user has inserted enough money.

- `Menu`: This class manages the menu of the coffee machine. 
   It can get the items in the menu and find a specific drink.

## How to Run

To run the program, simply run the `main.py` file. 
You will be presented with a menu of drinks and asked what you would like. 
You can also ask for a report of the current resources and money.


## User Interaction

The user is asked to input their choice of drink. 
They can also input "report" to get a report of the current resources and money, 
or "off" to turn off the coffee machine.

If the user orders a drink, the program checks if there are enough resources to 
make the drink and if the user has inserted enough money. If both checks pass, 
the coffee is made.

## Dependencies

This program requires Python 3.6 or later. No additional packages are needed.

## Future Improvements

Future improvements could include adding more types of drinks, allowing
the user to add more resources, and improving the user interface.
# ### Problem 1:
# Create a Movie class with the following properties/attributes: ```movieName```, ```rating```, and ```yearReleased```.
# * Override the default ```str``` (to-String) method and implement the code that will print the value of all the properties/attributes of the Movie class
# 
# * In your ```main``` function create *two* instances of the Product class
#     * Assign a value of your choosing for each property/attribute
#     * Print all properties to the console.
# 
# Remember, this is the basic model of a Python file with a class
class Movie:
    def __init__(self, movieName, rating, yearReleased):
        self.movieName = movieName
        self.rating = rating
        self.yearReleased = yearReleased

    def __str__(self):
        return 'Over the rainbow'




def funkyfunction():

    blah = Movie('Pulp Fiction', '5 outta 5', '94')
    blahah = Movie('drunkenfather', 'very good', 'left in 98')

    print(blah)
    print(blahah)


# ### Problem 2:
# Create a class Product that represents a product sold online.
# 
# A Product has ```price```, ```quantity``` and ```name``` properties/attributes.
# * Override the default ```str``` (to-String) method and implement the code that will print the value of all the properties/attributes of the Product class
# 
# * In your ```main``` function create *two* instances of the Product class
#     * Assign a value of your choosing for each property/attribute
#     * Print all properties to the console.

class Shamwow:

    def __init__(self, price, quantity, name):
        self.price = price
        self.quantity = quantity
        self.name = name


    def __str__(self):
        return 'Lucky Ducky'




def thisFunc():
    billy = Shamwow('5.99', 'alot', 'mr clean')
    clean = Shamwow('1.99', 'not much', 'dirty')

    print(billy)
    print(clean)

def main():
    funkyfunction()
    thisFunc()

main()

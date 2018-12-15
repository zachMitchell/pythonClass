# Objects & Classes

Imagine you're holding a ball. It has many interesting features like size, color, and bounciness factor.

**Objects** are like nouns (Persons places or things). All the features listed above can be contianed in one of these things! They get defined like they normally would in python, but they are instead unique to each object created. For example, one ball can be `red` while another can be `blue`.

**Classes** are the template to help build those objects. Once everything is defined for the class, you can use it in many differnt ways. When you define a class, you can also create functions that relate to each object seperately. If you create `bounce()` for example, that single ball will bounce, and values related to it will change.

## Syntax:
Creating a class looks like this:
```python
class myAwesomeClass(object):
    def __init__(self,arg1,arg2):
        #Initialize stuff here:
        self.myVariable = arg1
        self.pizza = arg2
        #Since this is a function, you can also peform logic here as well.
    #Functions can also be defined here.
    def myNiceFunction(self):
        #statements
```

At the start of the class, you will see this `Object` value. This tells the class that it can makes objects based on what's inside of it. You will also see another function: `__init__`, this function has many interesting things about it. For one, it has the `self` property. `self` tells python where your new object is, so any values you want to initialize are referred here thorugh **dot notation**.

Functions that you defined in the class also get placed in your new object as well. Everytime you define one though, you once again need `self` as the first argument.

## So, what happens if...

### You don't define `__init__()`?
Turns out, if you place your variables inside the class scope, it still works! However, you don't get to make use of arguments, which is a nice feature of __init__. If your object doesn't really need arguments, this always works fine.

### You don't place `object` in the beginning of your class?
Well, it just becomes a regular class. Instead of making objects, this class is now a special snowflake! You can call it like you would a regular object, and get/set it's values:
```python
class pizza():
    pepperonies = 35
    def eat():
        print("nom nom")

pizza.eat()
```

If you try to set this like you would an object though, the result might supprise you! If you just used this across 2 or 3 variables, you might notice the same values showing up in those variables. That's because they are actually *The original class in disguise* (A.K.A: a reference to the original class). Instead making an object, the class was simply referenced by another name (It's like when grandpa calls you "Jessie" instead of Sam). The same class, but with another label.

I digressed there. ;P The nice thing about standalone classes is that you can group pieces of code and keep it separate from other areas. It's also nice to have if you want to worry less about naming variables, as they're all contained in that class!

## What are the advantages?

Glad you asked! Having each object with their own unique properties allows you to create hundreds of things that are similar, but react independantly to its environment! Say you had two ball objects, when the screen makes one move, each ball has it's own coordinates, so each can be in its own place! If one bounces on the screen, it won't interfere with another. You can even go far as to **let objects react to eachother!**. Overall, this makes your program quite modular, and can greatly incrase what you can do!

# Your Mission
You just got yourself an awesome gig becoming an architect! You have customers left and right asking you to build houses, but there's only one problem...

**There's no blueprint for the house...**

Your job is to listen to what your customer wants in the house. Being the magical architect you are, you can build the house on the spot based on what your customers describe. In this house, you have three things to focus on:

1. The name of the house
1. The bedrooms (are they for boys or girls?)
1. And the materials you use to build the house. (*You must select three or more*)

The twist: you don't know any of these things in advance! However, you've successfully figured out what the blueprint should look like in general:

**Create your class in `houseClass.py`**
## Variables
Your class will be called `house`. It takes the following arguments: `name` and `price` Inside, it will contain the following things:
* `name` - The name of the person who wants this house. When your class is created, `name` will receive `The [xyz] house`. Your goal is to get the word in the middle, and make this the name.
* `price` - Your customer's budget. You need to get `price` from the argument that was used when your object was created. (Note that this, along with `name` are different from `self.name` and `self.price`)
* `total` - The total money spent on the house. This is based on how many items you used.
* `items` - This is a list of Strings with the names of items you used. It's also usefull for knowing how many items you have
* `bedrooms` - this is a list of Booleans. `True` is boy and `False` is girl

## Functions

In addition, classes can also have their own functions. You will create the following functions:
### `getMaterials`

this has one argument: a dictionary of numbers. The keys are the names of the materials, and the values are their prices.

In this function, **The goal is to purchase materials from the dictionary** to build the house with. You cannot go over budget, but the way you buy the items is up to you! Just remember to *buy 3 or more items*. The customer's budget will always be flexible enough to buy 3 items.

When you buy an item, add everthing to the object's `total`, and add the item name to `items`.

### `makeBedrooms`

This takes two arguments: *boys*, and *girls*; both of these are numbers. Your goal is to make use of the  `bedrooms` list, and insert booleans into said list. Boys are `True` and girls are `False`. The True/False count should be equal to the total of boys and girls rooms.

## Testing your class
When you're ready to test your class, run `checkWork.py`! It automatically checks how you did in the end, and is the main component that drives your object.

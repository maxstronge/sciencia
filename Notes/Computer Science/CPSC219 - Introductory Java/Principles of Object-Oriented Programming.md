# Principles of Object-Oriented Programming:

***

Java is an **Object-oriented** programming language. Object-oriented programming (*OOP* ) 	is a programming methodology that treats programs as consisting of **objects** that act independently, or interact with each other. OOP comes with its own terminology: 

- Objects have characterstics called **attributes** that can be defined however you want
- The values of all an object's attributes define its **state**
- Objects can take various actions, called **behaviors**, that can also be defined however you want in blocks of code called **methods** (in Java, anyways)
- Objects of the same kind have the same data type and belong to the same **class** - a class is a blueprint for an object, which defines its attributes/behaviors. All objects of a class have the same attributes and behaviors (although different objects of the same class can have different *values* for those same attributes).


***

### OOP Design Principles:

The following are three of the main design principles of OOP:


1. **Encapsulation**
	- 'putting things into a capsule' - packaging up information.
	-  most important feature - only part of what is in a capsule of information is visible. when producing a piece of software, it should be described so that other programmers can easily use it, but without any of the detail of how the software actually works (like the JUnit tests in class).
	-   also called 'information hiding'
	-   encapsulation is a good practice for programming in general, not just OOP,  but object-oriented languages not only let you realize the principles of encapsulation, you can *enforce* them

2. **Polymorphism**
	- Greek: 'many forms'
	- polymorphism allows the same program instructions to mean different things depending on the context - commonly occurs in human languages, English especially
	- eg. 'go play your favorite sport' means soccer to some people, and baseball to others
	- one method name can result in different actions, depending on the kind of objects that perform the actions

3. **Inheritance**
	- a method of organizing classes such that you can define common attributes/behaviors once, and have them apply to a whole collection of classes
	- by defining a general class, you can later use inheritance to define specialized classes that add to / refine the details of the general classes
	- eg. one could define a general class called Vehicles that has an attribute Wheels, and then have the more specialized classes Motorcycle, Car, and Bus *inherit* from the vehicle class, giving a motorcycle a 2-wheel state, Car a 4-wheel state, etc. 


***
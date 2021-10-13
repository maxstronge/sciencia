# Classes: 

***

Recall that a class is the definition of an object - a  'blueprint'. Classes are general descriptions of an object, its attributes, and its behaviors. 

Programmers often use a graphical notation to summarize some of the main properties of a class. A common type of notation is the *Universal Modeling Language (UML) Class Diagram*, or just UML diagram. 


```plantuml
class Automobile {

{field} fuel: double
speed: double
license: String
{method} + accelerate(double pedalPressure): void
{method} + decelerate
}
````
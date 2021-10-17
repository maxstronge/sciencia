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
{method} + decelerate(double pedalPressure): void
}
````

Each java class definition should be placed in a file by itself, with the same title as the class followed by the extension '.java'. Java classes can be compiled before you have a program to use it in - the compiled bytecode will be stored in a file with the same name, but with the '.class' extension. Later on, you can then create a program that uses the class without recompiling the class. 
***

Example Class: Dog

```java
	public class Dog {
	
		public String name;
		public String breed;
		public int age;
		
		public void writeOutput() {
		
			System.out.println("Name:  " + name);
			System.out.println("Breed: " + breed);
			System.out.println("Age in Calendar Years: " + age)
			System.out.println("Age in Human Years:  " + getAgeInHumanYears());
		
		}
		
		public int getAgeInHumanYears() {
		
			int humanAge = 0;
			if (age<=2) {
			
				humanAge = age * 11;
			}
			else {
			
				humanAge= 22 + ((age - 2) * 5);
			
			}
			
				return humanAge;
			
			}
		
		}
		
	}
```

Note the following three lines from the start of the class definition:

```java
...
		public String name;
		public String breed;
		public int age;
...
```
These lines each declare one **instance** of a variable (public meaning there is no restriction on how the variable is used - actually not a great idea).
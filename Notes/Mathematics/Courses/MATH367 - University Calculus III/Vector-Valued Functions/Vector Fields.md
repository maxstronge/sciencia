# Vector Fields:

***
![[Pasted image 20210927144308.png]]
### Vector Fields:

Given a function $g: \RR^n \to \RR$, it is possible to define a function $\vec{G}(\vec{x}) = \nabla g(\vec{x}).$ Thus, $\vec{G}:\RR^n \to \RR^n$. 

Vector fields are common in physics: both gravitation and electromagnetism are defined in terms of vector fields. 


For example, you can define a function $\vec{F}(\vec{x})$ to be equal to the force experienced by a unit mass/charge (depending on whether one is looking at gravity or electric fields) at the position $r = \vec{x}$.

Both gravitation and electromagnetism are examples of **inverse-square laws**: they take the form...


### $$\vec{F}(\vec{x}) = c\, \cdot\, \frac{1}{||x||^2}\,\cdot\,\frac{\vec{x}}{||\vec{x}||} $$

Where the constant tends to determine the masses/charges, any constants of nature, and directionality, the second term determines the magnitude via the inverse-square law, and the third term is a unit vector in the direction of the force. 

***
### Velocity Fields:

You can also define a **velocity field** in the form $\vec{V}(\vec{x}) =$ the velocity of something (for example, a circulating fluid) at the point $\vec{x}$.
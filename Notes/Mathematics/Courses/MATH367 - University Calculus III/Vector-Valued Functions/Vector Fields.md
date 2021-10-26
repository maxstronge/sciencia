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



***


**Remark:**

Consider a vector field $\va{F}$ on $G \subseteq \Rn$. 

By definition, $\va{F}$ is **conservative** on $G$ if there is a function $f: G \to \RR$ such that:

> ### $$\va{F}(\va{x}) = \nabla f (\va{x}) $$

...for all $\va{x} \in G$.

Such a function $f$ is called a **potential function** for $
\va{F}$, terminology derived from physics. Ergo, $\va{F}$ is a **conservative** vector field equal to the gradient of some function $f$.

>#### Example:
> Consider a  vector field $\va{F}$:
> $$\va{F}(\va{x}) = \frac{C}{\|\va{x}\|^2} \qty(\frac{\va{x}}{\|\va{x}\|^2}).$$
> These types of functions are typically associated with a **gravitational field** or **electric field** due to a point-mass or point charge at the origin $\va{0}$. See [[_Electric Potential and Field|E&M]] for further detail. 
> These equations are **inverse-square laws** of the form:
> ### $$\va{F}(\va{x}) = \frac{C}{\|\va{x}\|^2}.$$



***

**Example**: 

Find a *potential function* $f$ for $\va{F}(\va{x}) = (x+y,\,x-z,\,z-y).$

**Solution**: 

Essentially our task is to find a function $f$ such that:

$$\begin{align} f_x &= x + y \\ f_y &= x - z \\ f_z &= z - y. \end{align}$$

To do so, we can simply integrate to find a general antiderivative of each:

  1.  $f =\frac{x^2}{2}+xy + C(y,z)$ (with respect to x)
  2. $f = \frac{x^2}{2} + xy - yz + D(z)$ (y)
  3. $f_z = -y + D'(z) = z - y$
  
  In the last, we can find: 
  
  $$D'(z) = z \implies D = \frac{z^2}{2}+E $$
  
  We can now solve via system of equations for C,D,E. 
  
  ***
  
  
  **Eg.** 
  
  **a.** Find $A$, $B$, such that 
  
  > ## $$\va{F} = \Big(Ax \ln(z), By^2z, \frac{x^2}{z}+y\Big)$$

..is conservative. 

**b.** For those values of $A,B$, evaluate 

> ## $$\int_C \va{F}\cdot dr  $$



Where C is the line segment from $(1,1,1)$ to $(2,-1,2).$

***
**Solution**:

**a.**

$$\begin{align}f_x &= A x \ln(z) \\ f &=\frac{A}{2}x^2 \ln(z) + C(y,z) \\ f_y &= \frac{\partial c}{\partial y} = By^2z \\ \therefore C &= \frac{B}{3}y^3z + D(z)\end{align}$$



... 


> ### $$\frac{Ax^2}{2z} + \frac{By^3}{3} + D'(z) = \frac{x^2}{z} + y^3 $$


Rearranging:


> ### $$D'(z) = \frac{x^2}{z}\left(1-\frac{A}{2}\right) $$


... 


> ### $$f = x^2 \ln(z) + y^3z$$
> #### $$\begin{align} \nabla f = \left(2x\ln(z),3y^2z,\frac{x^2}{z}+y^3\right) &= \left(Ax\ln(z),By^2z,\frac{x^2}{z}+y^3\right) \\ &=\va{F} \qq{for A,B = 2,3.} \end{align}$$


***

**b.** 
> ### $$\int_C \va{F} \cdot d\va{r} = \int_C\nabla f \cdot d \va{r}$$


Via the FTC4LI, the above equals:


### $$= f(2,-1,2) - f(1,1,1). $$

****
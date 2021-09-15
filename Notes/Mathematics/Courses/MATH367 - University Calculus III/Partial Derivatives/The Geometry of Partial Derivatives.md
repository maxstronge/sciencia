# The Geometry of Partial Derivatives:

***

### Tangent Planes and Normal Lines:

The **tangent line** to the curve $y=f(x)$ at the point $(x_0, f(x_0))$ is the *straight line* that best fits the curve at that point. This was how we introduced the concept of the derivative.

The analog to the tangent line one dimension up is the **tangent plane**. The tangent plane to a surface $S$ at a point $(x_0,y_0,z_0)$ is the plane that best fits the surface at that point. 

For example, the tangent plane to the hemisphere...

$$S = \{(x,y,z):x^2+y^2+(z-1)^2=1,0\leq z \leq 1\}$$

...at the origin is the *xy* plane, $z=0$. 

![[Pasted image 20210913143626.png]]


Let us try to determine the tangent plane to a general surface $S$ at a general point $(x_0,y_0,z_0)$ lying on the surface. We will also determine the **normal line** to $S$, *i.e.* the line that passes through $(x_0,y_0,z_0)$ and whose direction is **perpendicular** to $S$ at that point. 


Recall that to uniquely specify a plane, we need:

-  a point on the plane, and
-  a vector perpendicular to the plane (*i.e.* a normal vector.)

Also recall that, to specify a line, we need:
- one point on the line, and
- a directional vector. 


We already have one point that is on both the *normal line* of interest and the *tangent plane* of interest - namely, $(x_0,y_0,z_0)$ . Furthermore, we can use any nonzero vector that is perpendicular to $S$ at $(x_0,y_0,z_0)$  as both the normal vector to our tangent plane and the direction vector to our normal line. 

So our main task is first to determine a normal vector to the surface $S$ at $(x_0,y_0,z_0)$. Let us examine several different cases:


*** 

#### Surfaces of the Form $z=f(x,y)$:

We construct a vector perpendicular to the surface $z=f(x,y)$ at $(x_0,y_0,f(x_0,y_0))$ by first constructing two *tangent* vectors to the specified surface at the specified point, and taking the cross product of those two vectors. 

Consider the red curve in the figure below:

![[Pasted image 20210915140859.png]]

It is the intersection  of our surface $z = f(x,y)$ with the plane $y=y_0$.

Here is a side view with the y-axis perpendicular to the screen:

![[Pasted image 20210915141226.png]]

The vector from the point $(x_0,y_0,f(x_0,y_0))$ to the point $(x_0+h,y_0,f(x_0+h,y_0))$ is nearly tangent to the curve, if *h* is very small. As *h* tends to 0, that vector, which is $(h,0,f(x_0+h,y_0))$, becomes *exactly tangent* to that curve. 

However, it's length also tends to zero, which will not prove useful. If we divide by *h* and take the limit as $h\to 0$, we find:


> $$\lim_{h\to 0} \frac{1}{h}\,(h,0,f(x_0+h,y_0)) = \lim_{h \to 0} \begin{bmatrix} 1, & 0, & \frac{f{(x_0+h,y_0)-f(x_0,y_0)}}{h}  \end{bmatrix}.$$


Since the limit $\lim_{h\to 0} \frac{f(x_0+h,y_0)-f(x_0,y_0)}{h}$ is the *definition of the partial derivative* $f_x(x_0,y_0)$, we find that the vector:

> ## $$\begin{pmatrix} 1, & 0, & f_x(x_0,y_0) \end{pmatrix}  $$

...is a *nonzero* vector that is exactly tangent to the red curve, and is hence **also tangent to the surface** $z=f(x,y)$ at the point $(x_0,y_0,f(x_0,y_0))$.


***

Recall: $y=f(\vec{x}), x\in \RR^n.$

The tangent plane to $y=f(\vec{x})$ at $\vec{x} = \vec{a}$:


> $$y = f(\vec{a})+\nabla f(\vec{a})\,\cdot \, (\vec{x}-\vec{a})  $$



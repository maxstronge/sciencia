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

> ### $$\begin{pmatrix} 1, & 0, & f_x(x_0,y_0) \end{pmatrix}  $$

...is a *nonzero* vector that is exactly tangent to the red curve, and is hence **also tangent to the surface** $z=f(x,y)$ at the point $(x_0,y_0,f(x_0,y_0))$.


***

### General Form of the Equation of the Tangent Plane:

Two linear approximations of a function $z=f(x,y),\,L_x\text{ and }L_y,$ both lie in a unique plane - the *tangent plane* to $z=f(x,y)$ at the point of interest. 

>**Characterization of $L_x$:**
>- point at $(a,b,f(a,b))$
>- directional vector $(1,0,f_x(a,b))$

>**Characterization of $L_y$:**
>- point at $(a,b,f(a,b))$
>- directional vector $(0,1,f_y(a,b))$


Taking the cross product of the two directional vectors will find us a **normal vector** to the plane:


>### $$\begin{align} \vec{n} &=(1,0,f_x(a,b)) \times (0,1,y(a,b)) \\ &=(-f_x(a,b),-f_y(a,b),1). \end{align} $$


Recall from introductory linear algebra that the equation of a plane going through the point $(a,b,c)$ with normal vector $(p,q,r)$ is given by:

> $$p(x-a)+q(y-b)+r(z-c)=0. $$

Substituting $(a,b,f(a,b))$ for $(a,b,c)$ and using the previously found normal vector $\vec{n}$ for $(p,q,r),$ we find:

> ### $$-f_x(a,b)(x-a) - f_y(a,b)(y-b)+z-f(a,b)=0. $$

This can be rearranged to give a nicer equation for the tangent plane:

> ### $$z = f(a,b) + f_x(a,b)(x-a)+f_y(a,b)(y-b). $$

We can write this more compactly by packaging $f_x$ and $f_y$ into the gradient vector $\nabla f\,(a,b)$ and taking a dot product:

> ### $$\begin{align} z &= f(a,b) + \nabla f(a,b)\,\cdot\,\begin{bmatrix} x-a \\ y-b \end{bmatrix} \\ &= f(a,b) + \nabla f(a,b)\,\cdot\,\{ \begin{bmatrix} x\\y \end{bmatrix} - \begin{bmatrix} a\\b\end{bmatrix}\}.\end{align}$$ 

Therefore, the tangent plane to $y=f(\vec{x})$ at $\vec{x} = \vec{a}$ can be succinctly given by:


> # $$z = f(\vec{a})+\nabla f(\vec{a})\,\cdot \, (\vec{x}-\vec{a}).  $$



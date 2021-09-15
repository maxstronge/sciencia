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


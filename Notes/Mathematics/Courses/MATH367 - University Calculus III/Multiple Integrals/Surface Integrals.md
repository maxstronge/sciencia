# Surface Integrals:
***

# Parameterized Surfaces:

In many cases, we will need to integrate over two/three dimensional surfaces. This can be as simple as literally computing the surface area, but it can be extended to more nuanced applications, such as computing the rate at which a fluid will traverse a surface. In any event, we will need to be able to carefully and precisely specify mathematical surfaces.

There are three common ways to specify a surface in three dimensions:

#### 1. Explicit Function:

^45340e

Likely the most common way to specify a surface is to give its equation in the form:
### $$z=f(x,y)\qquad (x,y) \in \mathcal{D} \subseteq \RRii.$$

Here, $(x,y) \in \mathcal{D} \subseteq \RRii$ just means that $(x,y)$ runs over the entire subset $\mathcal{D}$ of $\RRii$. For example, if the surface is the top half of the **unit sphere** (radius 1) centered on the origin...

### $$z = \sqrt{1-x^2-y^2}\qq{with} x^2+y^2\le 1.$$

#### 2. Implicit Definition:

We can also specify that the surface is the set of points 	$(x,y,z)$ that satisfy the equation $G(x,y,z)=0$, or, more generally, satisfy $G(x,y,z)=K,K\in\RR$. For example, the **unit sphere** is the set of points that obey:

### $$x^2+y^2+z^2=1. $$

#### c. Range of a Function:

Probably the most useful way to specify a surface when one needs to integrate over it is to define the surface as the range of a function as follows:

### $$r:\,\mathcal{D} \subset \RRii \to \RRiii $$

The above indicates that 	$r$ is a function that is defined on $\mathcal{D}$ which assigns to each point on $\mathcal{D}$ a point in $\RRiii$. 

### $$(u,v) \in \mathcal{D} \mapsto \va{r}(u,v) = (x(u,v),\,y(u,v),\,z(u,v)).$$



The above mapping equation means that the function $r$ assigns to each element $(u,v)$ of $\mathcal{D}$ the element $\va{r}\,(u,v) = (x(u,v),y(u,v),z(u,v))$ in $\RRiii$. Such a surface is called a **parameterized surface** - each point of the surface is labelled by the values of the two parameters $u$ and $v$. Parameterized surfaces are, of course, the two-dimensional / two-parameter analog of **parameterized curves**. 

> #### *Example*:
>  One simple, even trivial way to parameterize the surface which is the graph 
> $$z = f(x,y)\qq{where} (x,y) \in \mathcal{D}\subset\RRii $$
> …is to choose $x$ and $y$ as the parameters. That is, to choose:
> $$\begin{align} r(u,v) &= (u,v,f(u,v)),\qquad (u,v) \in \mathcal{D} \\ \qq{or} r(x,y) &= (x,y,f(x,y)),\qquad (x,y) \in \mathcal{D}.\end{align}$$
> While a parameterization, this accomplishes effectively nothing. We will consider some more substantial examples shortly. 

>####  *Example 3.1.2 - Sphere:* 
> The sphere of radius 1 centered on the origin is the set of all points $(x,y,z)$ that obey:
> ### $$G(x,y,z) = x^2 + y^2 + z^2 = 1. $$
> We cannot express this surface explicitly as the graph of a function because, for each $(x,y)<1$, there are two $z$'s which satisfy the above equation: namely,
> ### $$z = \pm \sqrt{1-x^2-y^2}. $$
> On the other hand, at least *locally*, this surface is the graph of a function. This means that for any point $(x_0,y_0,z_0)$ on the sphere, all the points of the surface that are *sufficiently close* to $(x_0,y_0,z_0)$ can be expressed in one of the forms $z=f(x,y)$, or $x = g(y,z)$, or $y=h(x,z)$.  For example, the part of the sphere that is within distance $\sqrt{2}$ of the point $(0,0,1)$ is:
> > #### $$\begin{align} \{&(x,y,z) : x^2 + y^2 + z^2 = 1, \|(x,y,z) - (0,0,1)\} \|< \sqrt{2} \\[2ex] &=  \{(x,y,z):x^2+y^2+z^2 = 1, x^2 + y^2 + (z-1)^2 < 2\}  \\ &= \{(x,y,z):x^2+y^2+z^2 = 1, x^2 + y^2 + z^2 -2z + 1 < 2\} \\ &= \{(x,y,z):x^2+y^2+z^2 = 1, z> 0\} \\ &= \{(x,y,z):z = \sqrt{1-x^2-y^2}, x^2 + y^2 < 1\}. \end{align} $$
> >The situation is depicted below:
> > ![[parametricunitsphereexample.png]]




***

#calculus #integrals #surface_integral #parametric_surface #implicit_definition #jacobian #derivatives #partial_derivatives
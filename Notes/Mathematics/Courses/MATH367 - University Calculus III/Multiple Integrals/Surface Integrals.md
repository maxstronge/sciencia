# Surface Integrals:
***

### Parameterized Surfaces:

In many cases, we will need to integrate over two/three dimensional surfaces. This can be as simple as literally computing the surface area, but it can be extended to more nuanced applications, such as computing the rate at which a fluid will traverse a surface. In any event, we will need to be able to carefully and precisely specify mathematical surfaces.

There are three common ways to specify a surface in three dimensions:

#### 1. Explicit Function:
Likely the most common way to specify a surface is to give its equation in the form:
### $$z=f(x,y)\qquad (x,y) \in \mathcal{D} \subseteq \RRii.$$

Here, $(x,y) \in \mathcal{D} \subseteq \RRii$ just means that $(x,y)$ runs over the entire subset $\mathcal{D}$ of $\RRii$. For example, if the surface is the top half of the **unit sphere** (radius 1) centered on the origin...

### $$z = \sqrt{1-x^2-y^2}\qq{with} x^2+y^2\le 1.$$

#### 2. Implicit Definition:

We can also specify that the surface is the set of points 	$(x,y,z)$ that satisfy the equation $G(x,y,z)=0$, or, more generally, satisfy $G(x,y,z)=K,K\in\RR$. For example, the **unit sphere** is the set of points that obey:

## $$x^2+y^2+z^2=1. $$

#### c. Range of a Function:

Probably the most useful way to specify a surface when one needs to integrate over it is to define the surface as the range of a function as follows:

## $$r:\,\mathcal{D} \subset \RRii \to \RRiii $$

The above indicates that 	$r$ is a function that is defined on $\mathcal{D}$ which assigns to each point on $\mathcal{D}$ a point in $\RRiii$. 

### $$(u,v) \in \mathcal{D} \mapsto \va{r}(u,v) = (x(u,v),\,y(u,v),\,z(u,v)).$$



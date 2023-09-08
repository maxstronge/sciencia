
___

Consider the **vector operator** $\vec{\nabla}$, called the **del** operator (or *nabla*). It is defined in Cartesian coordinates by

$$
\nabla \equiv \frac{ \partial  }{ \partial x } \hat{x} + \frac{ \partial  }{ \partial y }\hat{y}+\frac{ \partial  }{ \partial z } \hat{z} 
$$

## Gradient of a Scalar Field:

The *gradient* of a *scalar field* $\phi(x,y,z)$ is defined by 

$$
\text{grad } \phi = \nabla \phi=\frac{ \partial \phi }{ \partial x } \hat{x}+\frac{ \partial \phi }{ \partial y } \hat{y}+\frac{ \partial \phi }{ \partial z } \hat{z}
$$
Clearly, $\nabla \phi$ is a *vector field* whose components are the first partial derivatives of $\phi$ w.r.t $x,y,$ and $z$ in order. 

The gradient of a scalar field $\phi$ has some interesting geometrical properties. Let us consider the problem of *calculating the rate of change of $\phi$ in some particular direction.* 

For an infinitesimal vector displacement $d \vec{r}$, we can take its scalar/dot product with the gradient of phi $\nabla \phi$ to obtain:

$$
\begin{align}
\nabla \phi \cdot d \vec{r} &= \left( \frac{ \partial \phi }{ \partial x } \hat{x}+\frac{ \partial \phi }{ \partial y } \hat{y} +\frac{ \partial \phi }{ \partial z } \hat{z}\right)  \\

&= \frac{ \partial \phi }{ \partial x } dx + \frac{ \partial \phi }{ \partial y } dy+\frac{ \partial \phi }{ \partial z } dz \\

&= d\phi
\end{align}

$$
...which is the infinitesimal change in $\phi$ in going from position $\vec{r}$ to $d \vec{r}$.

In particular, if $\vec{r}$ depends on some parameter $u$ such that $\vec{r}(u)$ defines a **space curve**, then the **total derivative** of $\phi$ w.r.t. $u$ along the curve is simply

$$
\frac{d\phi}{du} = \nabla \phi \cdot \frac{d \vec{r}}{du}
$$

In the particular place that the parameter $u$ is the *arc length* $s$ along the curve, then the total derivative of $\phi$ w.r.t. $s$ along the curve is given by:

$$
\frac{d\phi}{ds}=\nabla \phi \cdot \hat{t}
$$
...where $\hat{t}$ is the unit vector tangent to the curve at the given point, as discussed in [[Space Curves]].

In general, the rate of change of $\phi$ with respect to a distance $s$ in some particular direction $\hat{a}$



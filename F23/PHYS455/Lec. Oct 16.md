Consider a rectangular region (3-dimensional, but no variation in one dimension) in which Laplace's equation

$$
\nabla^{2}\phi=0
$$
is satisfied. 

We consider the vertices of the rectangular region  $(0,0)\to(a,0)\to(a,b)\to(0,b)$ subject to a set of boundary conditions, which are usually of the form of $\phi$ defined for the sides as some function $u(x)$, etc. 

We want the potential over the entire region using those boundary conditions and the fact that Laplace's equation is satisfied. Often one of these will be non-zero and all the rest are zero - thus if all 4 of them are non-zero we can decompose it to four different problems with one non-zero side each and sum them via superposition (because superposition holds for potential).

Recall the Fourier sine series:

$$
f(x) = \sum_{m=1}^{\infty}A_{m} \sin\left(  \frac{m\pi x}{a} \right)
$$

Recall orthogonality condition:

$$
\int_{0}^{a} \sin \left( \frac{m\pi x}{a} \right) \sin \left( \frac{n\pi x}{a} \right)  \, dx=\delta_{mn} 
$$

where $\delta_{mn}$ is not quite a Kroenecker delta function, as those are tensors only defined for $m=1,2,3$, but instead is for any values $m$ and $n$. The value of this is $0$ if $m \neq n$ and 1 for the sole place $m=n$. 
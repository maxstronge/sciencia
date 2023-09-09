# Introduction to the Electric Potential

***

The electric field $\vec{E}$ is a conservative vector function, and like all conservative fields, it has zero curl. Because of this, we can quickly examine a vector function to see if it could potentially be an electrostatic field - for example, the field $$\vec{E}=y\hat{x}$$ could not be an electrostatic field since it has nonzero curl.

A very helpful feature of conservative vector functions is that we can exploit the zero curl property of electric fields to reduce a vector problem (finding $\vec{E}$) to a much simpler scalar problem.

We had a [[Potentials#^0540e0|theorem]] earlier asserting that any vector whose curl is zero is equal to the gradient of some scalar. We now prove that claim in the physical context of electrostatics.

Consider the following two closed paths:

![[Pasted image 20221114144404.png]]

Because $\curl \mathbf{E}=0$, the line integral of $\mathbf{E}$ over any closed loop is zero, via Stoke's theorem.  Because  $\oint \mathbf{E}\cdot d \mathbf{l}=0$ the line integral of $\mathbf{E}$ from point **a** to point **b** is the same for all paths - since the two paths are not the same, a closed path going out along path *(i)* and returning along path *(ii)* would clearly be nonzero. Since this cannot happen, the line integral over all paths must be the same, and thus the integral is path-independent.

This allows us to define a function:

$$V(\vec{r}) = - \int^{r}_{O}\mathbf{E}\cdot d \mathbf{l}$$

Here, $O$ is some reference point agreed upon beforehand, often taken to be infinity. $V$ thus only depends on the point $\mathbf{r}$. $V$ is the **electric potential**. 

The **potential difference** between two points is dependent only on the endpoints, and is given by

$$\begin{align*}
	V(\mathbf{b})-V(\mathbf{a}) &= -\int^{\mathbf{b}}_{O}\mathbf{E}\cdot d \mathbf{l}+\int^{\mathbf{a}}_{O}\mathbf{E}\\
&= -\int^{\mathbf{b}}_{O}\mathbf{E}\cdot d \mathbf{l} - \int^{\mathbf{O}}_{a}\mathbf{E}\cdot d \mathbf{l} \\
&= -\int^{b}_{a}\mathbf{E}\cdot d \mathbf{l}.
\end{align*}$$
There is a **fundamental theorem for Gradients** (Green's theorem?) that states:

$$V(\mathbf{b})-V(\mathbf{a})=\int^{b}_{a}(\nabla V)\cdot d \mathbf{l}$$
So we can set the equivalence

$$\int^{b}_{a}(\nabla V)\cdot d \mathbf{l}= -\int^{b}_{a}\mathbf{E}\cdot d \mathbf{l}$$

And, since by path independence, this is true for all points **a** and **b**, the integrands must be equal:
$$\mathbf{E}= -\grad V.\square$$

***

## Comments on Potential:

- Potential *energy* and *potential* are entirely distinct quantities/terms (though they are connected)
- A surface over which the potential function is constant is called an **equipotential** surface.
- The potential formulation carries a huge advantage - it completely contains the information of the electric field. If $V$ is known, the entire electric field can be found, because the three components of $\mathbf{E}$ are not completely independent - they are constrained by the fact that the curl must vanish, so $$\pdv{E_{x}}{y}=\pdv{E_y}{x} \qq{,}\pdv{E_z}{y}=\pdv{E_y}{z}\qq{,}\pdv{E_x}{z}=\pdv{E_z}{x}.$$ The potential formulation exploits this to maximum advantage, reducing a vector problem to a scalar one, so there's no need to keep track of components!


# Fourier Expansion:
***

**Question**: Given a *basis* $B$ of $\RR^n$, how do we express a vector $\vec{x}\in\RR^n$ as a *linear combination of vectors in* $B$?

Given *any* basis $B$, this often isn't easy to do.... but if $B$ is **orthogonal** it turns out to be really easy, and can be done via an explicit formula.
***

### The Expansion Theorem:

 Let $\{\vec{F_1},\dots,\vec{F_m}\}$ be an *orthogonal basis* for $U \subseteq \RR^n$. Then, for any $\vec{x} \in U$ we have the following expansion:
 
 > ## $$\vec{x} = \frac{\vec{x}\cdot\vec{F_1}}{||\vec{F_1}||^2}\,\vec{F_1}  + \dots +\frac{\vec{x}\cdot\vec{F_m}}{||\vec{F_m}||^2}\,\vec{F_m}. $$

Here the terms $(\vec{x}\cdot\vec{F_i})\,/\, ||\vec{F_i}||^2$ are called the **Fourier Coefficients**.

***

**Example**: 

We verified with the methods described [[Orthogonality and Orthonormality|here]] that $B = \{(1,1,2),(0,2,1),(5,1,-2)\}$ is an orthogonal set. Is $B$ an orthogonal basis of $\RRiii$?  If so, find the Fourier expansion of $\vec{x} = \begin{bmatrix}1\\1\\1 \end{bmatrix}$. 


**Solution**: 

We have a [[Orthogonality and Orthonormality#^8315c6|theorem]] which says that if $B$ is orthogonal $\implies B$ is linearly independent. So, since $B$ has 3 elements and $\dim(\RRiii)=3$, we know that $B$ is a basis of $\RRiii$. 

Using the *expansion theorem*, we have: 

  $$(1,1,1) = \frac{(1,1,1)\cdot (1,-1,2)}{6}\,(1,-1,2)+ \frac{(1,1,1)\cdot (0,2,1)}{5}\,(0,2,1) + \frac{(1,1,1)\cdot(5,1,-2)}{30}\,(5,1,-2)$$
###  $$= \frac{1}{3}\, (1,-1,2) + \frac{3}{5}\,(0,2,1) + \frac{2}{15}\,(5,1,2).$$

***
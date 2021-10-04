# Eigenvalues and Eigenvectors:
***



### **Definition:**

A nonzero vector $\vec{x} \in \RR^n$ is called an **eigenvector** of a square matrix $A$ if $A\vec{x} = \lambda \vec{x}$ for some $\lambda \in \RR$.  The scalar value $\lambda$ is called an **eigenvalue** of $A$. 

- *e.g.* the vector $\vec{x}=\begin{bmatrix}1\\2 \end{bmatrix}$ is an eigenvector of $A = \begin{bmatrix}3&0\\8&-1 \end{bmatrix}$ corresponding to the eigenvalue $\lambda = 3$, since $A\vec{x} = 3\vec{x}.$

***

### Procedure for Finding Eigenvalues/Eigenvectors:

If $A$ is a square matrix, then:

1. The *eigenvalues* of $A$ are the roots of the **characteristic polynomial** $C_A(\lambda) = \det(A-\lambda I).$
2. The *eigenvectors* corresponding to $\lambda$ are the solutions to $(A-\ll I)\vec{x}=\vec{0}$.

**Proof of Procedure:** 

>  $$A\vec{x} = \ll \vec{x}	\iff A\vec{x} - \ll \vec{x} = 0 \iff (A-\ll I) \, \vec{x} = \vec{0}.  $$
> By definition, $\ll$ is an eigenvalue of $A \iff$ this equation has a non-trivial solution $\iff  \det(A-\ll I) = 0.$  

***

**Example**: Find all eigenvalues and eigenvectors of $A = \begin{bmatrix}3&0\\8&-1 \end{bmatrix}$.

> 1. Find the characteristic polynomial $C_A(\ll) = \det(A-\ll I).$
> $$\begin{align} \det(A-\ll I) & = 0 \\ 0 &= \det\begin{bmatrix}3-\ll&0\\8&-(1+\ll) \end{bmatrix} \\ &= \left((3-\ll)(-1-\ll) \right)\, - \, \left((8\cdot0)\right)   \\ &= (3-\ll) \cdot (-1 - \ll) \\ & = -3 -3\ll -\ll + \ll^2 \\ &= \ll^2 -4\ll - 3 = 0 \\ &= (\ll+4) (\ll - 1) = 0.\end{align} $$
> The roots of this equation are $\ll_1 = -4$ and $\ll_2 = 1.$


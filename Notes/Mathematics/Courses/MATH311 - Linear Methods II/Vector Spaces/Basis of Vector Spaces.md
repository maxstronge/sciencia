# Basis of Vector Spaces:
***

A vector space is called **finite dimensional** if it is spanned by a finite set of vectors. Otherwise, it is **infinite dimensional**.

$\Rn, \Ppn, \text{ and }\bf{M}_{mn}$ are finite dimensional.

$F(-\infty,\infty)$ is infinite dimensional.

***

Recall that if $V$ is  a vector space, a set $\{\va{x_1},\va{x_2},\dots,\va{x_m}\}$ is called a **basis** of $V$ if:

1. $V = \span\{\va{x_1},\va{x_2},\dots,\va{x_m}\}$
2. $\va{x_1},\va{x_2},\dots,\va{x_m}$ is linearly independent.

Thus if a set of vectors $\{\va{e_1},\dots,\va{e_n}\}$ is a basis, then *every* vector in $V$ can be written as a linear combination of these vectors *in a unique way*. We can extend this to the concept of a basis via the **Invariance Theorem**:

> #### Invariance Theorem [6.3.3]:
> Let $\{\va{e_1},\va{e_2},\dots,\va{e_n}\}$ and $\{\va{f_1},\va{f_2},\dots,\va{f_m}\}$ be two bases of a vector space $V$.
>
>Then:
> #### $$n = m. $$
***

### Finite-Dimensional Vector Spaces:
A vector space is said to be **finite-dimensional** if it can be spanned by a finite number of vectors. Some useful results regarding finite-dimensional vector spaces:

> **Theorem:** Properties of Finite-Dimensional Vector Spaces
>
>Let $V$ be a finite-dimensional vector space spanned by $m$ vectors. 
>1. $V$ has a finite basis, and $\dim(V) \leq m$.
>2. Every independent set of vectors in $V$ can be *enlarged to a basis* of $V$ by *adding* vectors from any fixed basis of $V$.
>3. If $U$ is a subspace of $V$, then:
>> **a.** $U$ is finite-dimensional, and $\dim(U) \leq \dim(V).$
>> **b.** If $\dim(U) = \dim(V), \implies U = V.$


**Proof:**

1. If $V = \{\va{0}\}$, then $V$ has an empty basis, and $\dim(V) = 0 \leq m$. Otherwise, let $\va{v} \neq 0$ be some vector in $V$. Then, $\va{v}$ is independent
***

>  **Theorem:** Dimension of Finite-Dimensional Subspaces
> 
> Let $U$ and $W$ be subspaces of the finite dimensional vector space $V$. The following two statements hold:
>
>1. If $U \subseteq W$, then $\dim(U) \leq \dim(W).$
>2. If $U \subseteq W$ and $\dim(U) = \dim(W)$, then $U=W$.

**Proof:** 

Since $W$ is finite-dimensional, 

***

#InvarianceTheorem #linear_algebra #vector #vector_space #basis #dimension 
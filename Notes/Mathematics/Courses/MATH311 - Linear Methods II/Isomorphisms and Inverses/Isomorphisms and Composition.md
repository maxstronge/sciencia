# Isomorphism and Composition:
***
**Definition**: A linear transformation $T: V\to W$ is called an **isomorphism** if it is both *injective* and *surjective* (or, both 1:1 and onto). When transformations fulfill both of these properties, they are called **bijective**. 

The vector spaces $V$ and $W$ are said to be **isomorphic** if there exists an isomorphism $T: V\to W$, we write $V \cong W$ when this is the case.

For example, the *identity transformation* $1_V: V \to V$ is an isomorphism for any vector space $V$.

***

An isomorphism $T: V\to W$ induces a pairing

$$v \leftrightarrow T(\vb{v}) $$

between vectors $\vb{v}$ in $V$ and vectors $T(\vb{v}) \in W$ that *preserves scalar multiplication and addition.* 

Hence, *as far as their vector space properties are concerned*, the spaces $V$ and $W$ are identical apart from notation. Because addition and scalar multiplication in *either* space are completely determined by the same operations in the other space, all *vector space* properties of each are also determined by the other. 


***

One of the most important examples of isomorphic spaces was considered in a previous chapter: let $A$ denote the set of all 'arrows' with their tail at the origin in space (position vectors), and make $A$ into a vector space using the *parallelogram law* (preserving pointwise addition) and the scalar multiple law/rule. Then, define a transformation $T: \Riii \to A$ by taking:

$$T\mqty[x\\y\\z] = \text{ the arrow from the origin to the point } P(x,y,z).$$

We have demonstrated that the two laws mentioned above hold for these arrows, and so $T$ is a linear transformation. Moreover, $T$ is an isomorphism: it is both 1:1 and onto. The arrows give a visual geometric intuition into $\Riii$: the matrices are useful for detailed calculations and bring analytic precision into geometry. This is one of the best examples of the power of an isomorphism to shed light on *both* spaces being considered. 

***

The following theorem gives a very useful characterization of isomorphisms: they are the linear transformations that preserve bases. 

> ### **Theorem 7.3.1**:
> If $V$ and $W$ are finite-dimensional spaces, the following conditions are equivalent for a linear transformation $T: V\to W$.
> 1. $T$ is an **isomorphism**. 
> 2. If $\qty{\vb{e_1}, \vb{e_2,\dots,\vb{e_n}}}$ is any basis of $V$, then $\qty{T(\vb{e_1}), T(\vb{e_2}), \dots, T(\vb{e_n})}$ is a basis of $W$.
> 3. There exists a basis $\qty{\vb{e_1}, \vb{e_2,\dots,\vb{e_n}}}$ of $V$ such that $\qty{T(\vb{e_1}), T(\vb{e_2}), \dots, T(\vb{e_n})}$ is a basis of $W$.
x# Vector Spaces:
***
**Motivation**: Thus far, we have restricted our attention to vectors in $\Rn$, examining concepts like span, linear independence, subspaces, basis, and dimension.

In what way do $2\times 2$ matrices *behave* like vectors in $\Rn$? 
- Closed under addition, scalar multiplication, etc.

Another question: in what ways do *continuous functions* behave like vectors in $\Rn$?

- Also closed under addition, scalar multiplication, etc.

***

### An Informal Definition:
A **vector space** is a *set* of objects which "*behave like vectors in $\Rn$*". We will quantify precisely what it means to "behave like vectors in $\Rn$" shortly by providing 10 axioms. If a set satisfies these 10 axioms, it can be called a **vector space**.

If a set is a vector space, we can harness the tools of linear algebra to gain a great deal of power/information about the set!

***

### 10 Axioms of Vector Spaces:

**Definition:** A **vector space** is a set $V$ together with a rule for *addition* (+) and a rule for *scalar multiplication* (*) which satisfies the following axioms:

>1. **"+" Closure: ** $\,\va{u},\va{v} \in V \implies \va{u}+\va{v} \in V.$
2. **"+" Commutativity: **$\va{u} + \va{v} = \va{v} + \va{u}$ for all $\va{u},\va{v} \in V$.
4. **"+" Associativity: **  $\va{u} + (\va{v} + \va{w}) = (\va{u} + \va{v}) + \va{w} \qq{}\forall\, \va{u},\va{v},\va{w} \in V.$
6.  **"+" Identity: ** There exists an element $\va{0} \in V$ such that $\va{0} + \va{u} =\va{u}$ for all $\va{u} \in V$ (called the **zero vector**).
8.   **"+" Inverse: ** For each $\va{u} \in V$, there exists an element $-\va{u} \in V$ such that $\va{u} + (-\va{u}) = \va{0}.$
10.   **"$\ast$" Closure: ** For $\va{u} \in V$ and $K \in \RR \implies K\,\va{u} \in V$.
12.    **"$\ast$" Distributivity: ** $K(\va{u} + \va{v}) = K\va{u} + K\va{v}$ for all $\va{u}, \va{v} \in V$ and $K \in \RR$.
14.    **Vector Distributivity:** $(K+m)\va{u} = K\va{u} + m\va{u} \, \qquad\forall \,\va{u} \in V, K,m\in\RR.$
16.    **"$\ast$" Associativity: ** $K(m\va{u})=Km(\va{u})$ for all $\va{u} \in V,\,k,m \in \RR$.
18.    **"$\ast$" Identity: ** $1\cdot\va{u} = \va{u}$ for all $\va{u} \in V$.

***

### Examples of Vector Spaces:

1. Let $V=\RRii$ and define addition and scalar multiplication as follows:

>$$(x_1,y_1)+(x_2,y_2) = \,(x_1-2x_2+1,2y_1+3y_2-4).$$
>$$K \times (x_1,y_1) = (\frac{x_1}{K},y_1K^2).$$

Is $K$ a vector space? 

A: Yes - though the definitions of addition and multiplication are confusing, none of the axioms are contravened. 

***

**Theorem:** The following are vector spaces: ^b51340

1. The set $M_{mn}$ of $\mxn$ matrices using matrix addition + scalar multiplication.
2. The set $F(-\infty,\infty)$ of all real-valued functions on $(-\infty,\infty)$ where $(F+g)(x) = F(x) + g(x)$ and $(KF)(x) = K F(x)$ for $K \in \RR$. 

***

**Question:** What are the zero vectors of 1 and 2 above?

- 1: $\mxn$ matrix consisting of all zeros
- 2: The constant function $F(x)=0$. 

***

## Subspaces of Vector Spaces:

A subset $U$  of a vector space $V$  is a called a **subspace** of $V$	if it is itself a vector space under the addition and scalar multiplication rules defined on $V$.

**Theorem - Subspace Test:** A subset $U$  of a vector space $V$  is a subspace of $V \iff U$ satisfies the following:

1. Zero Vector: $\va{0} \in U$.
2. Closed Under Addtion: $\va{x},\va{y}\in U \implies \va{x} + \va{y} \in U.$
3. Closed Under Scalar Multiplication: $\va{x} \in U \implies K\va{x} \in U,K\in\RR.$


***

**Example:** Which of the following are subspaces of $M_{nn}$?

- a) $U =$ {invertible $\nxn$ matrices}
	- According to the theorem [[Vector Spaces#^b51340|above]], the set of all $\mxn$ matrices are vector spaces, so in this case $m=n$ and $U$ is a subspace (matrix addition and scalar multiplication hold as they do not change the dimensions of the matrices)


***

#linear_algebra #vector #vector_space #
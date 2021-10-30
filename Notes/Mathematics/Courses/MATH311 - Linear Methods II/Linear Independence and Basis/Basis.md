# Basis:

***


**Definition**: Let $U$ be a subspace of $\RR^n$. A set $S = \{\vec{x_1}, \vec{x_2}, \dots, \vec{x_m} \}$ is called a **basis** of $U$ if the following two conditions are satisfied:

1. $U = \text{span}\{\vec{x_1}, \vec{x_2}, \dots, \vec{x_m} \}$, and...
2. $\{\vec{x_1}, \vec{x_2}, \dots, \vec{x_m} \}$ is linearly independent. 

In other words, the basis of $U$ is the **minimal spanning set** of $U$.

Every possible subspace $U \subseteq \RR^n$ has an *infinite number* of possible bases. 


**Theorem**: Let $\{\vec{v_1}, \vec{v_2},\dots, \vec{v_n}\}$ be a basis for $V$. If a subset of $V$ contains:

- *a)* more than $n$ vectors, then it is linearly dependent.
- *b)* less than $n$ vectors, then it does not span $V$.


**Proof**: ....
 
 This leads us to the **Invariance Theorem**:
***

## The Invariance Theorem:
> All bases of a subspace $U \subseteq \RR^n$ have the **same number of vectors**. 

***

The **dimension** of a subspace $U \subseteq \RR^n$, denoted $\dim(U)$, is the *number of vectors in a basis for $U$*. 

We define $\dim(\vec{0}) = 0.$ 

For example:

- $\dim(\RR^n)=n$, because $\{\vec{e_1},\vec{e_2},\dots,\vec{e_n}\}$ is a basis (indeed it is the *standard* basis).
- $\dim$(*line through the origin*) $=1$, since one vector spans a line through the origin 


***

### The Uniqueness of Basis Representation Theorem:

Let $V$ be a subspace of $\RR^n$.

If $S=\{\vec{x_1},\dots,\vec{x_k}\}$ is a *basis* of $V$, then every vector $\vec{v}\in V$ can be expressed in the form $\vec{v}=c_1\vec{x_1}+c_2\vec{x_2}+\dots+c_k\vec{x_k}$ in **exactly** one way. 


**Proof**: 

Since $S$ is a basis, we know $S$ spans $V$. Hence we can express $V$ as some linear combination of vectors in $S$. We want to demonstrate that there is one unique way to do this. 

Suppose $\vec{v}=c_1\vec{x_1}+\dots+c_k\vec{x_k}$ and $\vec{v}=d_1\vec{x_1}+\dots+d_k\vec{x_k}$, for $c_i,d_i \in \RR$. *

Then, $\vec{v}=c_1\vec{x_1}+\dots+c_k\vec{x_k} = \vec{v}=d_1\vec{x_1}+\dots+d_k\vec{x_k}$, and hence:

$$(c_1-d_1)\,\vec{x_1}+\dots+(c_k-d_k)\,\vec{x_k}=\vec{0}.$$

Since $S$ is linearly independent (as per the definition of a basis), we know the only solution to this equation is $c_1-d_1=0,\,\dots,c_k-d_k=0$, and thus:


> ### $$c_1=d_1,\dots,c_k=d_k. $$

Therefore, the two expressions in * are the same. 


***

## Procedure for finding a basis:

Given a set of vectors $\vec{v_1},\dots,\vec{v_k} \in \RR^n$, we can find a basis for $U=\span\{\vec{v_1},\dots,\vec{v_k}\}$ by doing the following:

1. Form a $k\times n$ matrix $A$ whose *i*-th row is $\vec{v_i}$.
2. The nonzero rows in the *r.r.e.f.* of $A$ form a basis for $U$.


***


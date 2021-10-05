# Rank-Nullity:

The **rank** of a matrix $A$, $\text{rank}(A)$, is the number of leading 1s in the *r.r.e.f.* of $A$. 

> *e.g.* the matrix $$A=\begin{bmatrix} 1&-3&4&-2&5&4 \\ 2&-6&9&-1&8&2 \\ 2&-6&9&-1&9&7\\-1&3&-4&2&-5&-4\end{bmatrix}$$ has *r.r.e.f* $$A_{rref} =  \begin{bmatrix} 1&-3&4&-2&5&4 \\ 0&0&1&3&-2&-6 \\ 0&0&0&0&1&5\\0&0&0&0&0&0\end{bmatrix}$$ 
> ....and so $\text{rank}(A) = 3.$

***

**Theorem:** If $A$ is a matrix, then: $$\text{rank}(A)=\text{dim}(\text{row}(A)) = \text{dim}(\text{col}(A)).$$

Additionally, if $A$ is a matrix, then $\text{rank}(A)=\text{rank}(A^T).$

***

The **nullity** of a matrix $A$, denoted $\nullity (A)$, is the *dimension* of the *nullspace* of $A$ (*i.e. $\nullity(A) = \dim(\null(A))$.*)

> *e.g.* if $A=\begin{bmatrix} 1&2&3\\0&0&0\end{bmatrix}$,  then $\nullity(A) = 2.$


***

### The Rank-Nullity Theorem:

If $A$ is a matrix with $n$ columns, then:

##  $$\rank(A) + \nullity(A) = n. $$
***

### *Example 1*: 

The matrix 

>$$A=\begin{bmatrix} 1&-3&4&-2&5&4 \\ 2&-6&9&-1&8&2 \\ 2&-6&9&-1&9&7 \\ -1&3&-4&2&5&-4\end{bmatrix}$$

has *r.r.e.f*:
> $$A_{rref} = \begin{bmatrix} 1&-3&4&-2&5&4 \\ 0&0&1&3&-2&-6 \\ 0&0&0&0&1&5 \\ 0 &0&0&0&0&0\end{bmatrix}. $$

We can confirm the Rank-Nullity theorem: 

> $$\null(A) = \left(
\begin{array}{cccccc}
 37 & 0 & -4 & 0 & -5 & 1 \\
 14 & 0 & -3 & 1 & 0 & 0 \\
 3 & 1 & 0 & 0 & 0 & 0 \\
\end{array}
\right) \implies \nullity(A) = 3.$$
> There are 3 leading 1s in $A_{rref} \implies \rank(A)+\nullity(A) = 3 + 3 = 6.$
>
>$A$ has 6 columns - Rank-Nullity confirmed. 

***

### *Example 2*:

etc.etc.

***

## Equivalent Statements:

Let $A$ be an $n\times n$ matrix where the transformation $T_A: \RR^n \to \RR^n$ is multiplication by $A$.

The following statments are all equivalent:


- $A$ is **invertible**.
- $A\vec{x}=\vec{0}$ has only the trivial solution.
- The reduced-row echelon form of $A$ is the identity matrix $\bf{I}_n.$
- $A$ is expressible as a *product of elementary matrices*. 
- $A\vec{x} = \vec{b}$ is *consistent* for every $n\times1$ matrix $\vec{b}$.
- $A\vec{x} = \vec{b}$ has *exactly one* solution for every $n\times1$ matrix $\vec{b}$.
- $\det(A)\neq 0.$
- The *range* of $T_A$ is $\RR^n$.
- $T_A$ is 1:1. 
- The column vectors of $A$ are *linearly independent*. 
- The row vectors of $A$ are *linearly independent*. 
- The column vectors of $A$ span $\RR^n$.
- The row vectors of $A$ span $\RR^n$.
- The column vectors of $A$ form a basis for  $\RR^n$.	
- The row vectors of $A$ form a basis for  $\RR^n$.
- $\rank(A)=n.$
- $\nullity(A)=0.$

***
# Similar Matrices:

***

**Definition**: If $A$ and $B$ are *square* matrices, we say that $A$ is **similar** to $B$, denoted $A \sim B$, if there exists some invertible matrix $P$ such that $B = P^{-1}AP.$

- *e.g.* $A=\begin{bmatrix}1&1\\-2&4 \end{bmatrix}$ and $B=\bmqty{2&0\\0&3}$ are similar, since $B=P^{-1}AP$ for $P = \bmqty{1&1\\1&2}$.

**NB:** if $A\sim B,\implies B \sim A$.

***

### Similarity Invariants:

If $A \sim B$, then:

1. $\det(A) = \det(B).$
2. $\rank(A) = \rank(B).$
3. $A$ and $B$ have the same eigenvalues.

***

# Diagonalization:

A square matrix $A$ is **diagonalizable** if $A$ is similar to a diagonal matrix. 

- *e.g.* $A = \bmqty{1&1\\-2&4}$ is diagonalizable, since $A \sim \bmqty{2&0\\0&3}$.


Recall from introductory linear algebra that an $n \times n$ matrix $A$ is diagonalizable $\iff A$ has $n$ eigenvectors $\va{x_1}, \va{x_2},\dots,\va{x_n}$ such that the matrix $P = [\va{x_1}, \va{x_2},\dots,\va{x_n}]$ with $\va{x_i}$ as columns is invertible.

We can restate this as a theorem using the language of diagonalization:

**Theorem:**
> An $n \times n$ matrix $A$ is diagonalizable $\iff A$ has $n$ linearly independent eigenvectors. 

***

## Procedure for Diagonalizing a Matrix:

Let $A$ be an $\nxn$ matrix. 

1. Find $n$ linearly independent eigenvectors of $A$: $\va{p_1},\va{p_2},\dots, \va{p_n}.$
2.  Form a matrix $P$ whose $i$-th column is $\va{p_i}$ for $i\leq p \leq n.$
3.  The matrix $P^{-1}AP$ will be a diagonal matrix $D$ whose *i*-th diagonal entry is the eigenvalue $\ll_i$ corresponding to $\va{p_i}$ for $1\leq i \leq n$. 



**Example:** Diagonalize the matrices $A = \bmqty{1&1\\-2&4},\qq B=\bmqty{0&0&0 \\1&2&1 \\1&0&3}$.


> a) First, find the eigenvalues of $A$, which are the roots of the *characteristic polynomial* $C_A(\ll) = \det(A-\ll I).$
> $$\begin{align}\det(A-\ll I) &= 0 \\ \mdet{1-\ll&1\\-2&4-\ll}&= 0 \\ \qty((1-\ll)(4-\ll)) - ((-2)(1)) &= 0 \\ 4 -5\ll+\ll^2 +2 &= 0 \\ \ll^2-5\ll + 6 &= 0 \\ (\ll - 2) ( \ll - 3) &= 0. \end{align} $$
> We can see that $\ll_1 = 2$ and $\ll_2 = 3$. 
> We can now find the eigenvectors associated with 2 and 3, which are the solutions to $(A-\ll I)\,\va{x} = \va{0}.$ Starting with $\ll = 2$:
> $$\begin{align}(A-\ll I)\,\va{x} &= \va{0} \\ (A - 2I)\,\va{x} &= \va{0} \\ \bmqty{1-2&1 \\ -2&4-2}\,\bmqty{x_1\\x_2} &= \va{0} \\ \bmqty{-1&1 \\ -2&2}\,\bmqty{x_1\\x_2} &= \va{0} \\ x_2 - x_1 = 0 = 2x_2 - 2x_1\end{align} $$
> Following a similar process for the other eigenvector and skipping some steps you're too lazy to write, we can find:
> $$\va{x_{\ll_1}} = \bmqty{1\\1},\qq{} \va{x_{\ll_2}}=\bmqty{1\\2}. $$
> We can now form the matrix $P$:
> $$P = \bmqty{\va{x_{\ll_1}}\,,\,\va{x_{\ll_2}}} = \bmqty{1&1\\1&2}. $$
> Now, $D = P^{-1}AP =\bmqty{1&1\\1&2}^{-1}\,\bmqty{1&1\\-2&4}\,\bmqty{1&1\\1&2} = \bmqty{2&-1\\-1&1}\,\bmqty{1&1\\-2&4}\,\bmqty{1&1\\1&2}...$
> $D = \bmqty{2&0\\0&3}.$

***
**Theorem:** If $A$ is an $\nxn$ matrix with $n$ distinct eigenvalues, then $A$ is diagonalizable.

**Proof Idea:** 
> Let $\va{v_1},\dots,\va{v_n}$ be the eigenvectors corresponding to distinct eigenvalues $\ll_1,\dots,\ll_n$. It suffices to show that these eigenvectors are *linearly independent*. This can be shown by induction on $n$  (see pp. 301-302 of LAWA).

***
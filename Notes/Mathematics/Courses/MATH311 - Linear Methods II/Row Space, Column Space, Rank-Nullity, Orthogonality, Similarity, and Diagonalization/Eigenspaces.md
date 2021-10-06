# Eigenspaces:
***

The **eigenspace** of an $\nxn$ matrix $A$ corresponding to an eigenvalue $\ll$ is:

> ## $$ E_\ll(A) = \{ \va{x} \in \Rn: A\va{x} = \ll \va{x}.\}$$

In words: the eigenspace of a matrix is the set of all vectors $\va{x}$ such that multiplication of $\va{x}$ by $A$ produces the same vector as the multiplication of $\va{x}$ by $\ll$. 

**Question:** Are all vectors in $E_\ll(A)$ eigenvectors of $A$?

**A:** No! The zero vector $\va{0} \in E_\ll(A)$, and $\va{0}$ is *not* an eigenvector... but all nonzero vectors $\in E_\ll(A)$ are eigenvectors with eigenvalue $\ll$.

**NB:** Since the equation $A\va{x} = \ll\va{x}$ is equivalent to $(A-\ll I)\,\va{x} = 0$, the eigenspace $E_\ll(A)$ can also be characterized as the *nullspace* of $A-\ll I$. 

> ### $$E_\ll(A) = \{\va{x} \in \Rn : A\va{x} = \ll\va{x} \} = \{\va{x}: (A-\ll\ I)\,\va{x} = \va{0}\}.$$

***

**Example 1:** Let $B = \bmqty{0&0&-2\\1&2&1\\1&0&3}$. Find $E_1(B)$ and $E_2(B)$. Find a basis for each eigenspace. 

> - With the eigenvalues known ($\ll_1 = 1,\ll_2 = 2$), we can proceed to find the eigenspace by setting up the system:
> $$(A-\ll I)\,\va{x} = \va{0} \implies \bmqty{(0-1)&0&-2\\1&(2-1)&1\\1&0&(3-1)}\va{x}=\va{0}$$
> $$= \bmqty{-1&0&-2\\1&1&1\\1&0&2}\,\bmqty{x_1\\x_2\\x_3} = \va{0} \implies $$

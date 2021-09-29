# Rank-Nullity:

The **rank** of a matrix $A$, $\text{rank}(A)$, is the number of leading 1s in the *r.r.e.f.* of $A$. 

> *e.g.* the matrix $$A=\begin{bmatrix} 1&-3&4&-2&5&4 \\ 2&-6&9&-1&8&2 \\ 2&-6&9&-1&9&7\\-1&3&-4&2&-5&-4\end{bmatrix}$$ has *r.r.e.f* $$A_{rref} =  \begin{bmatrix} 1&-3&4&-2&5&4 \\ 0&0&1&3&-2&-6 \\ 0&0&0&0&1&5\\0&0&0&0&0&0\end{bmatrix}$$ 
> ....and so $\text{rank}(A) = 3.$

***

**Theorem:** If $A$ is a matrix, then $\text{rank}(A)=\text{dim}(\text{row}(A)) = \text{dim}(\text{col}(A)).$

Additionally, if $A$ is a matrix, then $\text{rank}(A)=\text{rank}(A^T).$

***

The **nullity** of a matrix $A$, denoted $\nullity (A)$, is the *dimension* of the *nullspace* of $A$ (*i.e. $\nullity(A) = \dim(\null(A))$.*)

> *e.g.* if $A=\begin{bmatrix} 1&2&3\\0&0&0\end{bmatrix}$,  then $\nullity(A) = 2.$


***

### The Rank-Nullity Theorem:

If $A$ is a matrix with $n$ columns, then:

##  $$\rank(A) + \nullity(A) = n. $$
***

*Example*: The matrix $A=\begin{bmatrix} 1&-3&4&-2&5&4 \\ 2&-6&9&-1&8&2 \\ 2&-6&9&-1&9&7 \\ -1&3&-4&2&5&-4\end{bmatrix}$ has *r.r.e.f*:
> $$A_{rref} = \begin{bmatrix} 1&-3&4&-2&5&4 \\ 0&0&1&-1&8&2 \\ 0&0&0&-1&9&7 \\ 0 &0&0&2&5&-4\end{bmatrix} $$
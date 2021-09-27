# Rank-Nullity:

The **rank** of a matrix $A$, $\text{rank}(A)$, is the number of leading 1s in the *r.r.e.f.* of $A$. 

> *e.g.* the matrix $$A=\begin{bmatrix} 1&-3&4&-2&5&4 \\ 2&-6&9&-1&8&2 \\ 2&-6&9&-1&9&7\\-1&3&-4&2&-5&-4\end{bmatrix}$$ has *r.r.e.f* $$A_{rref} =  \begin{bmatrix} 1&-3&4&-2&5&4 \\ 0&0&1&3&-2&-6 \\ 0&0&0&0&1&5\\0&0&0&0&0&0\end{bmatrix}$$ 
> ....and so $\text{rank}(A) = 3.$

***

**Theorem:** If $A$ is a matrix, then $\text{rank}(A)=\text{dim}(\text{row}(A)) = \text{dim}(\text{col}(A)).$

Additionally, if $A$ is a matrix, then $\text{rank}(A)$
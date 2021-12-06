# The Matrix of a General Linear Transformation:

***

Recall that if $A$ is an $\mxn$ matrix, the corresponding *matrix transformation* $T_A :\Rn \to \Rm$ is defined by 

$$T_A(\va{x}) = A\va{x}\qq{for all columns $\va{x}$ in $\Rn$.}$$

We have a theorem saying that every linear transformation of the type above is indeed a matrix transformation. Furthermore, the matrix $A$ is uniquely determined by $T$. In fact, $A$ is given in terms of its columns by:

$$A = \qty[T(\va{e}_1) \qq{} T(\va{e}_2) \qq{} \cdots \qq{} T(\va{e}_n) ],$$

where $\qty{\va{e}, \ \va{e}_2,\cdots, \va{e}_n}$ is the standard basis of $\Rn$.

In this chapter, we investigate how to associate a matrix with *any* linear transformation $T: V \to W$ where $V$ and $W$ are finite-dimensional vector spaces, and we also describe how the matrix can be used to compute $T(\va{v})$ for any $\va{v}$ in $V$. The matrix depends on the choice of basis $B$ in $V$, and a basis $D$ in $W$, and is denoted $M_{DB}(T)$.

***

### Sections:

- [[Matrix of a Linear Transformation]]

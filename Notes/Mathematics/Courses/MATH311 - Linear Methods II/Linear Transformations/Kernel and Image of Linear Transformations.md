# Kernel and Image of Linear Transformations:
***

This section is dedicated to two important subspaces associated with a linear transformation $T: V \to W$. 


The **kernel** of a $T$ (denoted $\ker T$)	and the **image** of $T$ (denoted $\img T$ or $T(V)$) are defined by:

> ### $$\begin{align} \ker T  = \{ \va{v} \in V :T(\va{v}) = \va{0}\} \\[3ex] \img T = \qty{T(\va{v}): \va{v}\in V}=T(V)\end{align} $$

![[Pasted image 20211030203331.png|Kernel and image of a linear transformation.]]

The kernel of $T$ is often called the *nullspace* of $T$ (see [[Image Space and Nullspace|earlier work]]) because it consists of all the vectors $\va{v}$ in $V$ satisfying the *condition* that $T(\va{v}) = 0$. The image of $T$ is often called the *range* of $T$ and consists of all vectors of the *form* $\va{w} = T(\va{v})$ for some $\va{v}$ in $V$. 


It is often helpful to think of linear tranformations in terms of matrix multiplication, again as seen [[Properties of Linear Transformations#^2e8fe9|earlier]]. We can restate the above in terms of the matrix $A$:

> Let $T_A: \Rn \to \Rm$ be the linear transformation $T$ induced by the $\mxn$ matrix $A$; that is, $T_A(\va{x}) = A\va{x}$ for all columns $\va{x}$ in $\Rn$. Then:
> - $\ker T_A = \qty{\va{x} : A\va{x} = 0} = \null(A)$, and;
> - $\img T_A = \qty{A\va{x} : \va{x} \in \Rn} = \img(A).$
***

**Theorem**:

Let $T: V\to W$ be a linear transformation. Then:

1. $\ker T$ is a subspace of $V$.
2. $\img T$ is a subspace of $W$.

***

Given some linear transformation  $T: V\to W$:

- $\dim (\ker T)$ is called the **nullity** of $T$ and is denoted by $\nullity \,T$
- $\dim (\img T)$ is called the **rank** of $T$ and is denoted by $\rank\, T$.


The rank of some matrix $A$ was [[Rank-Nullity|earlier]] defined to be the dimension of the column space of $A$, $\col(A).$ These definitions are consistent in the following sense:

> ##### Given an $\mxn$ matrix $A$, show that $\img T_A = \col(A)$, such that $\rank (T_A) = \rank(A).$
> *Solution:* 
> Write $A = \qty[\va{c}_1,\cdots,\va{c}_n]$ in terms of its columns. Then:
> ### $$\img(T_A) = \qty{A\va{x}:\va{x} \in \Rn} = \qty{x_1\va{c}_1 + \dots + x_n\va{c}_n:x_i \in \RR}.$$ 
> Hence $\img(T_A)$ is the column space of $A$: the rest follows naturally.


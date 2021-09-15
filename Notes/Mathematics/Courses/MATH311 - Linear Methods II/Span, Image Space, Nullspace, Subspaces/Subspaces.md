# 5.1 - Subspaces and Spanning:
***


We have already introduced the set $\RR^n$ as the set of all *n*-tuples of real numbers (*i.e*. vectors), and  began our investigation of the matrix transformation $\RR^n \to \RR^m$ given by matrix multiplication by an $m\times n$ matrix. Particular attention was paid to the Euclidean plane $\RRii$ where certain simple geometric transformations (translations, rotations, reflections) were seen to be the results of matrix transformations. 

In this chapter we investigate $\RR^n$ in full generality, and introduce some of the most important concepts and methods in linear algebra. 

*** 

### Subspaces of $\RR^n$:

> #### Definition of a Subspace of $\RR^n$:
> A set *U* of vectors in $\RR^n$ is called a **subspace** of $\RR^n$  if it satisfies the following properties:
> 1. The zero vector $\bf{0} \in U$.
> 2. If $x\in U$ and $y \in U$, then $x+y \in U.$ *(closed under addition)*
> 3. If $x \in U$, then $ax \in U$ for all real numbers *a*. *(closed under scalar multiplication)*


By these criteria, $\RR^n$ is  subspace of itself - this chapter is about these subspaces and their properties. 

The set $U = \{\bf{0}\}$, consisting of only the zero vector, is also a subspace of $\RR^n$: obviously it contains $\bf{0}$, $\bf{0} + \bf{0}= \bf{0}$, and $a\bf{0} = \bf{0}\, \forall\,a \in \RR^n$; it is called the **zero subspace**. 

Any subspace of $\RR^n$ other than the zero subspace or $\RR^n$ itself is called  a **proper** subspace. Planes and lines through the origin in $\RRiii$, for example, are all subspaces of $\RRiii$ - in fact, these two groups are the **only** proper subspaces of $\RRiii$. 

***

### Image Space and Null Space:

Subspaces can also be used to describe important features  of an $m\times m$ matrix $A$ - notably, the **null space** and the **image space**. 

The **null space** of  $A$, denoted $\text{null}(A)$, is defined as:

> ### $$\text{null}(A)= \{x \in\RR^n: Ax=0  \}.$$

The null space is also referred to as the **kernel** of the matrix. In the language of matrix algebra, $\text{null }(A)$ is the set of all solutions $x$ in $\RR^n$ of the homogenous system $Ax=0$:

> ## $$x \in \text{null} (A )\iff Ax = 0.$$

For example:

> *e.g. * if $A =\begin{bmatrix}1&0\\0&0 \end{bmatrix}$, then $\text{null}(A) = \{ \begin{bmatrix} 0\\y\end{bmatrix} : y \in \RR\} \implies$ the null space is the entire y-axis. 

The **image space** of $A$, denoted $\text{im} (A)$, is defined as:

> ### $$\text{im} (A) = \{Ax : x \in \RR^n \}.$$

The image space is the set of all vectors $y$ in $\RR^m$ such that $Ax=y$ *has* a solution $y$.

> *eg. * if $A = \begin{bmatrix} 1&0 \\ 0&0\end{bmatrix}$, then $\text{im}(A)=\{ \begin{bmatrix} x\\0 \end{bmatrix} : x \in \RR\} \implies$ the image space is the entire x-axis.  


If $A$ is an $m\times n$ matrix, then:

1. null $A$ is a subspace of $\RR^n$.
2.  im $A$ is a subspace of $\RR^m$.

***
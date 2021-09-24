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


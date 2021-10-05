# Proof Assignment Topic 5: 

***

**Prompt**: Let $V$ be a vector space. Let $S$ be a finite subset of $V$. Prove that $\span(S)$ is a subspace of $V$.

***

Since $V$ is a vector space, it satisfies the following 10 axioms: 

>1. **"+" Closure: ** $\,\va{u},\va{v} \in V \implies \va{u}+\va{v} \in V.$
2. **"+" Commutativity: **$\va{u} + \va{v} = \va{v} + \va{u}$ for all $\va{u},\va{v} \in V$.
4. **"+" Associativity: **  $\va{u} + (\va{v} + \va{w}) = (\va{u} + \va{v}) + \va{w} \qq{}\forall\, \va{u},\va{v},\va{w} \in V.$
6.  **"+" Identity: ** There exists an element $\va{0} \in V$ such that $\va{0} + \va{u} =\va{u}$ for all $\va{u} \in V$ (called the **zero vector**).
8.   **"+" Inverse: ** For each $\va{u} \in V$, there exists an element $-\va{u} \in V$ such that $\va{u} + (-\va{u}) = \va{0}.$
10.   **"$\ast$" Closure: ** For $\va{u} \in V$ and $K \in \RR \implies K\,\va{u} \in V$.
12.    **"$\ast$" Distributivity: ** $K(\va{u} + \va{v}) = K\va{u} + K\va{v}$ for all $\va{u}, \va{v} \in V$ and $K \in \RR$.
14.    **Vector Distributivity:** $(K+m)\va{u} = K\va{u} + m\va{u} \, \qquad\forall \,\va{u} \in V, K,m\in\RR.$
16.    **"$\ast$" Associativity: ** $K(m\va{u})=Km(\va{u})$ for all $\va{u} \in V,\,k,m \in \RR$.
18.    **"$\ast$" Identity: ** $1\cdot\va{u} = \va{u}$ for all $\va{u} \in V$.

Since $S$ is a finite subset, it consists of a finite number of elements, all of which are contained in $V$: 

> $$S = \{\va{x_1},\dots,\va{x_n}\}, \va{x_i} \in V. $$

We want to prove that $\span(S) \subseteq V$. Recall the definition of a subspace:

> #### Definition of a Subspace of $\RR^n$:
> A set *S* of vectors in $\RR^n$ is called a **subspace** of $\RR^n$  if it satisfies the following properties:
> 1. The zero vector $\bf{0} \in U$.
> 2. If $x\in U$ and $y \in U$, then $x+y \in U.$ *(closed under addition)*
> 3. If $x \in U$, then $ax \in U$ for all real numbers *a*. *(closed under scalar multiplication)*

In this case, all these conditions still apply, except that $\Rn$ should be replaced with the vector space $V$, and the set $U$ should be replaced with $\span(S)$. Let us check each of these conditions:


1. Since we know $V$ is a vector space, we know that the zero vector $\va{0}$ exists and is defined (by axiom 4). Moreover, since $\span(S)$ is the set of all linear combinations of the elements of $S$, we can confirm that the zero vector is contained in $\span(S)$, since $0\va{x_1} + \dots + 0\va{x_n} = \va{0}$ is a valid linear combination. We can also note that since all elements $\va{x_i}$ in $S$ are elements of $V$, and $0 \in \RR$, the operation of multiplying each vector by zero is defined in V by axiom 6. Therefore, the first condition for a set to be a subspace holds. 
2. Since $V$ is closed under addition by axiom 1, we know that for any two elements $\va{x_i},\va{x_j} \in V \implies \va{x_i} + \va{x_j} \in V$ as well. Therefore, the set $S$ is closed under addition. 
3.  Since $V$ is closed under scalar multiplication by axiom 6, we know that any element of $V$ multiplied by any scalar $\in \RR$ will also be contained in $V$. Therefore, any scalar multiple of any element of $S$ is also an element of $V$. In addition, any scalar multiple of any element in $S$ will always be contained in $\span(S)$ due to the definition of the span - therefore, the set $\span(S)$ is closed under scalar multiplication for the vector space $V$.


Since all three of the conditions for a subspace are met for $\span(S)$, we can conclude that $\span(S)$ is a valid subspace of the vector space $V$. QED.
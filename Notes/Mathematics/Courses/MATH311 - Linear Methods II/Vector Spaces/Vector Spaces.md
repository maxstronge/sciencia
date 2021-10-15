# Vector Spaces:
***
**Motivation**: Thus far, we have restricted our attention to vectors in $\Rn$, examining concepts like span, linear independence, subspaces, basis, and dimension.

In what way do $2\times 2$ matrices *behave* like vectors in $\Rn$? 
- Closed under addition, scalar multiplication, etc.

Another question: in what ways do *continuous functions* behave like vectors in $\Rn$?

- Also closed under addition, scalar multiplication, etc.

***

### An Informal Definition:
A **vector space** is a *set* of objects which "*behave like vectors in $\Rn$*". We will quantify precisely what it means to "behave like vectors in $\Rn$" shortly by providing 10 axioms. If a set satisfies these 10 axioms, it can be called a **vector space**.

If a set is a vector space, we can harness the tools of linear algebra to gain a great deal of power/information about the set!

***

### 10 Axioms of Vector Spaces:

**Definition:** A **vector space** is a nonempty set $V$ of objects (called **vectors**), together with a rule for *addition* (+) and a rule for *scalar multiplication* (*) which satisfies the following axioms:

>#### **Axioms for vector addition**:
>A1. **Closure:** $\,\va{u},\va{v} \in V \implies \va{u}+\va{v} \in V.$
A2. **Commutativity: **$\va{u} + \va{v} = \va{v} + \va{u}$ for all $\va{u},\va{v} \in V$.
A3. **Associativity: ** $\va{u} + (\va{v} + \va{w}) = (\va{u} + \va{v}) + \va{w} \qq{}\forall\, \va{u},\va{v},\va{w} \in V.$
A4.  ** Identity: ** There exists an element $\va{0} \in V$ such that $\va{0} + \va{u} =\va{u}$ for all $\va{u} \in V$ (called the **zero vector**).
A5. **Inverse: ** For each $\va{u} \in V$, there exists an element $-\va{u} \in V$ such that $\va{u} + (-\va{u}) = \va{0}$ (called the **negative** of $\va{u}$).

> #### **Axioms for scalar multiplication**:
S1. ** Closure: ** For $\va{u} \in V$ and $K \in \RR \implies K\,\va{u} \in V$.
S2. **Distributivity: ** $K(\va{u} + \va{v}) = K\va{u} + K\va{v}$ for all $\va{u}, \va{v} \in V$ and $K \in \RR$.
S3.  **Vector Distributivity:** $(K+m)\va{u} = K\va{u} + m\va{u} \, \text{ for all }\,\va{u} \in V, K,m\in\RR.$
S4. **Associativity: ** $K(m\va{u})=Km(\va{u})$ for all $\va{u} \in V,\,k,m \in \RR$.
S5.    **Identity: ** $1\cdot\va{u} = \va{u}$ for all $\va{u} \in V$.


The content of axioms **A1** and **S1** is described by saying that $V$ is **closed under addition** and **closed under scalar multiplication**.  

***

### Examples of Vector Spaces:


The rules of matrix arithmetic (*i.e.* matrix addition/scalar multiplication), when applied to $\Rn$, confirm that $\Rn$ *is a vector space* using those two operations.


However, it is important to recognize that, in a general vector space, 	the 'vectors' **need not be** $n$-tuples as they are in $\Rn$ - they can be any type of object at all provided the rules for addition/scalar multiplication are defined, and the axioms above are satisfied, as the following example shows:

**Example:** Let $V=\RRii$ and define addition and scalar multiplication as follows:

>$$(x_1,y_1)+(x_2,y_2) = \,(x_1-2x_2+1,2y_1+3y_2-4).$$
>$$K \times (x_1,y_1) = (\frac{x_1}{K},y_1K^2).$$

**Q:** Is $K$ a vector space? 

**A:** Yes - though the definitions of addition and multiplication are confusing, none of the axioms are contravened. 

***

>**Theorem:** The following are vector spaces:
>1. The set $M_{mn}$ of $\mxn$ matrices using matrix addition + scalar multiplication. (**NB**: $M_{mn} = \RR^{mn},$ just different notation.)
>
2. The set $F(-\infty,\infty)$ of all real-valued functions on $(-\infty,\infty)$ where $(F+g)(x) = F(x) + g(x)$ and $(KF)(x) = K F(x)$ for $K \in \RR$. 

***

**Question:** What are the zero vectors of 1 and 2 above?

- 1: $\mxn$ matrix consisting of all zeros
- 2: The constant function $F(x)=0$. 

***


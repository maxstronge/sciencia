# One-to-One and Onto Transformations:
***

> ### *Definition 7.3:* One-to-One and Onto Linear Transformations
> Let $T: V\to W$ be a linear transformation.
> 1. $T$ is said to be **onto** if $\img T = W$. 
> 2. $T$ is said to be **one-to-one** (1:1) *if* $T(\va{v}) = T(\va{u})$ implies that $\va{v} = \va{u}$.
***

### Additional Terminology:
The concept that a linear transformation is 1:1 is also called **injectivity**:  *i.e.* if $T(\va{v}) = T(\va{u}) \implies \va{v} = \va{u}$, the transformation $T$ is **injective**. 

Alternately: $\va{v} \neq \va{u} \implies T(\va{v}) \neq T(\va{u})$. If the input vectors in $V$ are not equal, the transformations of those input vectors are also not equal if the transformation is injective. No element in $W$ is 'hit' twice. 

![[Pasted image 20211031114031.png|Visual example of injectivity.]]

Similarly, the concept that a linear transformation is *onto* is called **surjectivity**, *i.e.* a transformation $T$ is surjective $\iff \img(T) = W.$

![[Pasted image 20211031114633.png|Visual example of surjectivity.]]


A vector $\va{w}$ in $W$ is said to be **hit** by $T$ if $\va{w} = T(\va{v})$ for some $\va{v} \in V$. Then $T$ is onto / surjective if every vector $\va{w} \in W$ is hit at least once, and $T$ is 1:1 / injective if no element of $W$ gets hit twice.

We can now introduce an important theorem:


**Theorem:**

> If $T: V \to W$ is a linear transformation, then $T$ is one-to-one / injective $\iff \ker(T) = \va{0}.$

**Proof:** 

If $T$ is 1:1, let $\va{v}$ be any vector in $\ker(T).$ Then, $T(\va{v})=0 \implies T(\va{v}) = T(0).$ 

Hence, $v = 0$ because $T$ is 1:1. Hence: $\ker(T) = \qty{0}.$

***


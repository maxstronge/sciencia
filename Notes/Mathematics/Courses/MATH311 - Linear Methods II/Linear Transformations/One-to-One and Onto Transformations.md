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

Some further notable examples:

The **identity transformation** $1_V: V \to V$ is both *one-to-one* and *onto* for any vector space $V$.

### **Example**:

Consider the linear transformations: 

$$\begin{align} S &: \Riii \to \Rii \qq{given by}S(x,y,z)=(x+y,x-y) \\[2ex] T&: \Rii \to \Riii \qq{given by} T(x,y) = (x+y,x-y,x) \end{align}$$

Show that $T$ is one-to-one but *not* onto, and vice versa for $S$.

**Solution:** 

We can verify that $T$ is injective by finding its kernel:

$$\ker T = \qty{(x,y):x+y = x-y = x = 0} = \qty{(0,0)} \implies T\text{ is 1:1}.$$

However, it is not *surjective*: for example, $(0,0,1)$ does not lie in $\img T$ because if $(0,0,1) = (x+y,x-y,x)$ , the transformation cannot be satisfied. 

Turning to $S$, we can check for injectivity by finding its kernel:

$$\ker S = \qty{(x,y,z): x+y = x - y = 0} =t(0,0,1),t\in \RR $$

Because the kernel is not equal to the zero vector, $S$ is not one-to-one. But every element $(s,t) \in \Rii$ lies in $\img S$ because $(s,t) = (x+y,x-y) = S(x,y,z)$ for some $x,y,z$. Hence, $S$ is onto. 

***

### **Example**: 

Let $U$ be an invertible $\mxm$ matrix and define:

$$T: \bf{M}_{mn} \to \bf{M}_{mn}\qq{by}T(X)=UX\qq{for all}X\in\bf{M}_{mn}.$$

Show that $T$ is a linear transformation that is both 1:1 and onto. 

	***
# Topic 10 Proof-Writing Assignment:
##### Max Stronge (30064749)
***

**Prompt:** Decide whether the following statements are TRUE or FALSE. If the statement is true, then prove it. If it is not true, then provide an explicit counterexample.

1. If $A$ and $B$ are $\nxn$ orthogonal matrices, then $A+B$ is orthogonal.
2. If $A$ is an orthogonal matrix, then $A^{-1}$ is orthogonal.

***

### 1.

Let $A$ and $B$ be $\nxn$ matrices, and let them be *orthogonal*. 

By definition: an $\nxn$ matrix $A$ is orthogonal if $A^{-1} = A^T$, or, equivalently:

$$A A^T = I.$$

 



Let us see if $(A+B) \ (A^T + B^T) = I.$

$$\begin{align}(A+B) \ (A^T + B^T) &= AA^T + AB^T + BA^T + BB^T \\ &= I + AB^T + BA^T + I \\ &= 2I + AB^T + BA^T  \end{align}$$

The final sum can only be equal to the identity matrix if both $AB^T$ and $BA^T$ are equal to $-\frac{1}{2} I.$ As a counterexample, if $A = \bmqty{1&0\\0&-1}$ (a reflection across the x-axis, represented by an otrthogonal matrix)^[Wikipedia contributors. "Orthogonal matrix." _Wikipedia, The Free Encyclopedia_. Wikipedia, The Free Encyclopedia, 16 Nov. 2021. Web. 16 Nov. 2021.],  and $B = \bmqty{\cos\tt&-\sin\tt\\\sin\tt&\cos\tt}$ (a rotation by angle $\tt$, also an orthogonal matrix), we have:

$$\begin{align}(A+B)(A^T + B^T) &= 2I +AB^T + BA^T \\ &= 2I + \bmqty{\cos\tt&0\\0&-\cos\tt}+ \bmqty{\cos\tt&0\\0&-\cos\tt} \\ &= 2I + \bmqty{2\cos\tt&0\\0&-2\cos\tt} \\ &\neq I.\end{align}$$

Therefore, the sum of two orthogonal matrices is not orthogonal in general. The statement is false. 

***
### 2. 

Let $A$ be an orthogonal $\nxn$ matrix. By definition, orthogonal matrices have $A^T = A^{-1}.$ We wish to determine whether $A^{-1}$ is orthogonal. 

For $A^{-1}$ to be orthogonal, we must have $(A^{-1})^T = (A^{-1})^{-1} = A.$ 

From the definition of orthogonality for $\nxn$ matrices:

$$A^T = A^{-1} $$

If we take the inverse of both sides:

$$(A^T)^{-1} = (A^{-1})^{-1} = A$$

And since $A^T = A^{-1}$, we can rewrite this as:

$$(A^T)^{-1}  = (A^{-1})^T = A.$$


Thus, $A^{-1}$  is orthogonal. QED. 

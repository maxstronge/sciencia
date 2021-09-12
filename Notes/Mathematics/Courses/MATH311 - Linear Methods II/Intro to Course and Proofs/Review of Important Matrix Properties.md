# Review of Important Matrix Properties:
***

### **Transpose Properties:**

> Let $\bf{A}$ be a matrix and $k \in \RR$.
> - $(\bf{A} + \bf{B})^T = \bf{A}^T + \bf{B}^T$
>  - $(\bf{AB})^T = \bf{B}^T\bf{A}^T$
>  - $(\bf{A}^T)^T = \bf{A}$
>  - $(k\bf{A})^T = k\bf{A}^T$

### **Determinant Properties:**

> Let $\bf{A}$ by an $n\times n$ matrix and $k \in \RR$. 
> - $\det(\bf{AB}) = \det(\bf{A})\det(\bf{B})$.
> - $\det(\bf{A}^T)=\det(\bf{A}).$
>  - $\det(\mathit{k}\bf{A}) =  	\mathit{k}^n \det(\bf{A}).$
>  - $\det(\bf{A}^{-1}) = \frac{1}{\det(\bf{A})}.$

### **Inverse Properties:**
> Let $\bf{A}\,\text{and}\,\bf{B}$ be **invertible** matrices and $k \in \RR$. 
> - $(\bf{AB})^{-1} = \bf{B}^{-1}\bf{A}^{-1}.$
> - $(\bf{A}^{-1})^{-1} = \bf{A}.$
> - $(k\bf{A})^{-1} = k^{-1}\bf{A}^{-1}.$
> - $(\bf{A}^T)^{-1} = (\bf{A}^{-1})^T$.

***

### Related Theorems and Definitions:

 - If $\bf{A} = \bf{A}^T$, then $\bf{A}$ is called a **symmetric** matrix.

- Let $\bf{A}$ be an $m\times n$ matrix. Then the following statements are equivalent:

> 1. The system $\bf{A}\vec{x} = \vec{b}$ is consistent for every $\vec{b} \in \RR^m$ (*i.e.* has at least one solution $\vec{x}$ for every choice of $\vec{b}$.)
> 2. rank$(\bf{A}) = m$.
> 3. col$(\bf{A}) = R^m$.

- Let $\bf{A}$ be an $n \times n$ matrix. Then the following statements are equivalent:

> 1. $\bf{A}^{-1}$ exists.
> 2. $\det(\bf{A}) \neq 0.$
> 3. rank$(\bf{A}) = n.$
> 4. The system $\bf{A}\vec{x} = \vec{b}$ is consistent for every $\vec{b} \in \RR^n$. 
> 5. The system $\bf{A}\vec{x}=\vec{0}$ has only the trivial solution $\vec{x} = \vec{0}$.
> 6. $\bf{A}$ can be transformed into the identity matrix $\bf{I}^n$ by performing elementary row operations. 

***

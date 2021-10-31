# Image Space and Nullspace:
***

### Image Space and Null Space:

Subspaces can also be used to describe important features  of an $m\times m$ matrix $A$ - notably, the **null space** and the **image space**. 

The **null space** of  $A$, denoted $\text{null}(A)$, is defined as:

> ### $$\text{null}(A)= \{x \in\RR^n: Ax=0  \}.$$

The null space is also referred to as the **kernel** of the matrix. In the language of matrix algebra, $\text{null }(A)$ is the set of all solutions $x$ in $\RR^n$ of the homogenous system $Ax=0$:

> ### $$x \in \text{null} (A )\iff Ax = 0.$$

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

#### **Theorem: Image Space as Span of Columns**

 > Let $\vec{c_1},\vec{c_2},\dots,\vec{c_n}$ denote the *columns* of an $m \times n$ matrix $A$. Then, $\text{im}(A) = \text{span}\{\vec{c_1},\vec{c_2},\dots,\vec{c_n}\}$.

#### **Proof:**

Suppose $\vec{y} \in \text{im}(A) \implies \exists \,\vec{x}=\begin{bmatrix}x_1 \\ . \\. \\ x_n\end{bmatrix} \in \RR^n$ such that $\vec{y} = A\vec{x} = x_1\vec{c_1} + \dots + x_n\vec{c_n}$, which is in $\text{span}\{\vec{c_1},\vec{c_2},\dots,\vec{c_n}\}$. 

***

#### **Theorem: Null Space as Span of Solutions of $A\vec{x}=0$**:

> Suppose $\vec{x_1},\dots,\vec{x_n}$ are the set of basic solutions to $A\vec{x}=0$ for an $m\times n$ matrix $A$. Then, $\text{null}(A)=\text{span}\{\vec{x_1},\dots,\vec{x_n} \}$.

**Proof:**

Suppose $\vec{x} \in \text{null}(A) \implies A\vec{x}=0 \implies \vec{x}$ must be a linear combination of the basic solutions $\vec{x_1},\dots,\vec{x_n} \implies \text{null}(A)=\text{span}\{\vec{x_1},\dots,\vec{x_n}\}$.

	
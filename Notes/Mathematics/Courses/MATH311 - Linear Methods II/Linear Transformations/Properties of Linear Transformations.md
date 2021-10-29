# Properties of Linear Transformations:
***

> ###### **Definition**: Linear Transformations of Vector Spaces
>![[lineartransformationdiagram.svg]]
>
>If $V$ and $W$ are two vector spaces, a function $T:V\to W$ is called a **linear transformation** if it satisfies the following two axioms:
>1. $T(v+v_1) = T(v) + T(v_1)$ for all $v$ and $v_1$ in $V$.
>
>2. $T(r\,v) = r\,T(v)$ for all $v$ in $V$ and all $r$ in $\RR$.
>
> A linear transformation $T:V\to W$ is called a **linear operator** on $V$.

***

We have already seen many examples of linear transformations $T: \Rn \to \Rm.$ In fact, writing vectors 	in $\Rn$ as columns, an earlier theorem shows that 	for each such $T$, there exists an $\mxn$ matrix $A$ such that $T(\va{x})=A\va{x}\text{ for every }\va{x} \in \Rn.$

Moreover, the matrix $A$ is given by $A = \qty[T(\va{e_1}),\,T(\va{e_2}),\dots,T(\va{e_n})]$, where $\{\va{e_1},\dots,\va{e_n}\}$ is the **standard basis** of $\Rn$.

We can denote this transformation:

 ### $$T_A:\Rn \to \Rm $$
 
Defined by:

> ### $$T_A(\va{x}) = A\va{x}\text{ for every }\va{x} \in \Rn.$$
***

### **Important Linear Transformations:**

If $V$ and $W$ are vector spaces, the following are linear transformations:
>- **Identity Operator** $V \to V \qquad{}1_V:V\to V\qq{where}1_V(\vec{v})=\va{v}\text{ for all } \va{v} \in V.$
>- **Zero Transformation** $V \to W \qquad{}0:V \to W\qq{where} 0(\va{v}) =\va{0}\text{ for all } \va{v} \in V.$
>- **Scalar Operator** $V \to V \qquad{} a:V\to V\qq{where}a(\va{v})=\va{v}\text{ for all } \va{v} \in V, a \in \RR.$

The symbol 0 will be used to denote the zero transformation from $V$ to $W$ for *any * spaces $V,W$. It was also used earlier to denote the 	zero [[Functions as Vector Spaces|function]] $[a,b]\to\RR.$

The following example gives two important transformations of matrices. Recall that the **trace** $\tr(A)$ of an $\nxn$ matrix $A$ is the *sum of the entries on the main diagonal*. 

> **Example**: 
> Show that the *transposition* and *trace* are **linear transformations**. More precisely:
> - $R:\bf{M}_{mn} \to \bf{M}_{nm}\qq{where}R(A)=A^T\text{ for all }A \in \bf{M}_{mn}.$
> 
>- $S: \bf{M}_{mn} \to \RR\qq{where}S(A)=\tr(A)\text{ for all }A \in \bf{M}_{mn}.$


***

#linear_algebra #matrix #linear_transformations

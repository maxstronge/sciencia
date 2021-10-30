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

***

###### *Example*: if $a$ is a scalar, define $E_a:\Ppn \to \RR$ by $E_a(p) = p(a)$ for each polynomial $p$ in $\Ppn$. Show that $E_a$ is a *linear transformation* (called **evaluation** at $a$). 

**Solution**: 

If $p$ and $q$ are polynomials and $r \in \RR$, we use the fact that the sum $p+q$ and scalar product $rp$ are defined as for functions:

$$(p+q)(x) = p(x) + q(x)\qq{and} (rp)(x) = rp(x) $$

for all $x$. Hence, for all $p$ and $q$ in $\Ppn$ and all $r\in \RR$:

$$E_a(p+q) = (p+q)(a) = p(a) + q(a) = E_a(p) + E_a(q), \text{ and} $$
$$E_a(rp) = (rp)(a) = rp(a) =  rE_a(p)$$

Hence, $E_a$ is a linear transformation.


***
###### *Example:* Show that the differentiation and integration operations on $\Ppn$ are linear transformations. 

**Solution**: 

We want to show, more precisely, that:

> #### $$\begin{align}D&:\Ppn \to \Pp_{n-1}\qq{where} D[p(x)]=p'(x) \text{ for all }p(x)\in\Ppn \\[3ex] I&:\Ppn \to \Pp_{n+1}\qq{where}I[p(x)] = \int_0^x p(t)dt\text{ for all }p(x)\in\Ppn\end{align}$$

...are linear transformations. We can restate the fundamental properties of differentiation and integration:

$$[p(x) + q(x)]' = p'(x) + q'(x)\qq{and} [rp(x)]' = (r p)'(x)$$


$$\int_0^x [p(t)+q(t)]\,dt = \int_0^x p(t)$$

***

### Theorem 7.1.3^[LAWA, Nicholson]: 
Let $V$ and $W$ be vector spaces and let $\{\va{b}_1, \va{b}_2,\dots,\va{b}_n\}$ be a basis of $V$. Given any vectors $\va{w}_1,\va{w}_2,\dots,\va{w}_n$ in $W$ (they need not be distinct), there exists a *unique* linear transformation $T:V\to W$ satisfying $T(\va{b}_i) = \va{w}_i$ for each $i = 1,2,3\dots,n$. 

In fact, the action of $T$ is as follows:

Given $\va{v}=v_1\va{b}_1 + v_2 \va{b}_2 + \cdots + v_n\va{b}_n$ in $V$, $v_i \in \RR$, then:

### $$T(\va{v}) = T (v_1\va{b}_1 + v_2 \va{b}_2 + \cdots + v_n\va{b}_n) = v_1 \va{w}_1 + v_2\va{w}_2+\cdots + v_n\va{w}_n.$$

***



***

#linear_algebra #matrix #linear_transformations
	
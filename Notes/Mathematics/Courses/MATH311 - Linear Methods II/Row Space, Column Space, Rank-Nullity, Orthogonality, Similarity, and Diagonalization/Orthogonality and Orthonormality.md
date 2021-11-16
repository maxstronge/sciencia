# Orthogonality:
***

With a review of vector geometry out of the way, we can discuss some features of linear algebra that rely on those geometric ideas. 

Two vectors $\vec{x}$ and $\vec{y}$ are called **orthogonal** if their dot product $\vec{x} \cdot \vec{y}=0.$ We have seen and used this already in earlier courses, but we can now generalize this to arbitrary dimensions.

A *set* of vectors $\{\vec{x_1},\dots,\vec{x_n}\}$ is **orthogonal** if each vector $\vec{x_i}$ is nonzero *and* $\vec{x_i}=\vec{x_j}=0$ for all $i\neq j$. ^47831f

**NB:** any set of vectors that contains $\vec{0}$ is **not** orthogonal. 

***

**Theorem**: If $S=\{\vec{x_1},\dots,\vec{x_n}\}$ is orthogonal $\implies S$ is linearly independent. ^8315c6

**Proof:**

Let $S=\{\vec{x_1},\dots,\vec{x_n}\}$ be orthogonal and suppose $t_1\vec{x_1}+\dots+t_n\vec{x_n}=\vec{0}$. For $t_i \in \RR,\,1\leq i \leq n$. We want to show that $t_1 = \dots = t_n = 0$ is the only solution [condition for linear independence]. 

Since $S$ is orthogonal, we know $\vec{x_i} \cdot \vec{x_j} = 0$ for all $i\neq j$, and that $\vec{x_i} \neq 0\, \forall\, i.$

So for any $i$ we have: 

>   $$\begin{align} t_1\vec{x_1} + \dots + t_n\vec{x_n} = \vec{0} &\implies \vec{x_i} \,\cdot\,\left(t_1\vec{x_1}+\dots+t_n\vec{x_n}\right)= \\ &=\vec{x_i}\,\cdot\vec{0} \implies \vec{x_i}\,\cdot\,(t_i\vec{x_i})=0 \\ &\implies t_i \, ||\vec{x_i}||^2 =0 \text{ ...and  since }||\vec{x_i}||^2 \text{ is always positive...} \\ &\implies t_i = 0. \end{align} $$ 

Hence, $S$ is linearly independent. 

***

### Orthonormality:

A set of vectors $S =\{\vec{x_1},\dots, \vec{x_n} \}$ is called **orthonormal** if it is an orthogonal set of *unit* vectors. 

- *i.e.*  $\vec{x_i}\cdot\vec{x_j} = 0$ for all $i\neq j$ **and** $||\vec{x_i}||= 1\,\forall\,i.$
- For example, the set $S_1 = \{<1,0,0>,<0,1,0>,<0,0,1>\}$ is orthonormal, but $S_2 = \{<1,1,1>,<-1,1,-1>,<-1,-1,-1>\}$ is not. 

***

### Normalizing an Orthogonal Set: 

If $\{\vec{x_1},\dots,\vec{x_n}\}$ is an orthogonal set, then it can be *normalized* as the orthonormal set:

>  ### $$\left(\frac{\vec{x_1}}{||\vec{x_1}||}\,,\dots\,\frac{\vec{x_n}}{||\vec{x_n}||}\right).$$
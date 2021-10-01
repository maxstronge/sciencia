# Orthogonality:
***

With a review of vector geometry out of the way, we can discuss some features of linear algebra that rely on those geometric ideas. 

Two vectors $\vec{x}$ and $\vec{y}$ are called **orthogonal** if their dot product $\vec{x} \cdot \vec{y}=0.$ We have seen and used this already in earlier courses, but we can now generalize this to arbitrary dimensions.

A *set* of vectors $\{\vec{x_1},\dots,\vec{x_n}\}$ is **orthogonal** if each vector $\vec{x_i}$ is nonzero *and* $\vec{x_i}=\vec{x_j}=0$ for all $i\neq j$.

**NB:** any set of vectors that contains $\vec{0}$ is **not** orthogonal. 

***

**Theorem**: If $S=\{\vec{x_1},\dots,\vec{x_n}\}$ is orthogonal $\implies S$ is linearly independent.

**Proof:**

Let $S=\{\vec{x_1},\dots,\vec{x_n}\}$ be orthogonal and suppose $t_1\vec{x_1}+\dots+t_n\vec{x_n}=0$. For $t_i \in \RR,\,1\leq$
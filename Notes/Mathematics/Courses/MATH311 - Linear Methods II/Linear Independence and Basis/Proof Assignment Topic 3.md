Let $U$ be a subspace of $\RR^n$ with dimension $m$. 

Recall that the dimension of $U$, $\text{dim}(U)$, is the number of linearly independent vectors in the *basis* of $U$. 

> **Claim**: a set $S$ is linearly independent $\iff$ $S$ spans $U$. 

To prove this, we need to demonstrate that both statements imply one another, proving both of the following:

- A set $S$ is **linearly independent** $\implies$ $S$ spans $U$, *and*....
- A set $S$ spans $U$ $\implies S$ is linearly independent. 



The fact that  $U$ is a subspace of $\RR^n \implies$$U$ is a set of vectors in $\RR^n$ which: contains the zero vector; is closed under addition; and is closed under scalar multiplication. 


Because $U$ has dimension *m*, the number of vectors in the *basis* of $U$ is *m*, and the subspace $U$ can be written as the span of its $m$ basis vectors:

> #### $$U = \text{span}\{ \vec{b_1},\dots,\vec{b_m}\}$$

This was proved earlier, but let us take a moment to ensure that this way of writing $U$ still fulfills the three necessary preconditions of a subspace:

1. $\text{span}\{ \vec{b_1},\dots,\vec{b_m}\}$ contains the zero vector, since $\vec{0} = 0\vec{b_1} + \dots + 0\vec{b_m}$.

2. If two vectors $\vec{u}$ and $\vec{v}$ are in $\text{span}\{ \vec{b_1},\dots,\vec{b_m}\}$, then they both can be written as a linear combination of the basis vectors - for example, $\vec{u} = c_1\vec{b_1} + \dots + c_m\vec{b_m}, c_i \in \RR$ and $\vec{v} = a_1\vec{b_1} + \dots + a_m\vec{b_m}, a_i \in \RR$. The sum of $\vec{u}$ and $\vec{v}$ is then $(a_1 + c_1)\vec{b_1} + \dots + (a_m + c_m)\vec{b_m}$, and since $a$ and $c$ are both arbitrary scalars, this sum will also be contained in  $\text{span}\{ \vec{b_1},\dots,\vec{b_m}\}$.
3. By the definition of span as the set of all linear combinations, any scalar multiple of the basis,  $c\,\{ \vec{b_1},\dots,\vec{b_m}\}, \,c \in \RR$ will also be contained in the span. 

Thus, $U = \text{span}\{\vec{b_1},\dots,\vec{b_m} \}$. Since $U$ is a subspace of $\RR^n \implies m \leq n$. Note also that since the basis forms the *minimal* spanning set, we can declare that $\{ \vec{b_1},\dots,\vec{b_m}\}$ are linearly independent. 

***

Let us now examine the two statements necessary for our proof. First: 

> A set $S$ is linearly independent $\implies S$ spans $U$.

By definition: a set $S$ of vectors $\{\vec{v_1}, \vec{v_2}, \dots, \vec{v_m} \}$ is linearly independent $\iff$ the equation $t_1 \vec{v_1} + t_2\vec{v_2} + \dots + t_m \vec{v_m} = 0$ has only the trivial solution $t_1=t_2=\dots=t_n = 0.$

Let us assume that $S$ is linearly independent, such that none of the vectors $\{\vec{v_1}, \vec{v_2}, \dots, \vec{v_m} \}$ can be written as linear combinations of each other. 


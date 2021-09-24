## Topic 3 Proof-Writing Assignment: 
***

Let $U$ be a subspace of $\RR^n$ with dimension $m$. Let $S = \{\vec{v_1}, \vec{v_2}, \dots, \vec{v_m} \} \subset U$ .

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

Thus, $U = \text{span}\{\vec{b_1},\dots,\vec{b_m} \}$. Since $U$ is a subspace of $\RR^n \implies m \leq n$. Note also that since the basis forms the *minimal* spanning set, we can declare that $\{ \vec{b_1},\dots,\vec{b_m}\}$ are linearly independent $\implies U$ spans $\RR^m$.

***

Let us now examine the two statements necessary for our proof. First: 

> A set $S$ is linearly independent $\implies S$ spans $U$.

By definition: a set $S$ of vectors $\{\vec{v_1}, \vec{v_2}, \dots, \vec{v_m} \}$ is linearly independent $\iff$ the equation $t_1 \vec{v_1} + t_2\vec{v_2} + \dots + t_m \vec{v_m} = 0$ has only the trivial solution $t_1=t_2=\dots=t_n = 0.$

Let us assume that $S$ is linearly independent, such that none of the vectors $\{\vec{v_1}, \vec{v_2}, \dots, \vec{v_m} \}$ can be written as linear combinations of each other. Therefore, the span of $S$, $\text{span}\{\vec{v_1}, \vec{v_2}, \dots, \vec{v_m} \}$, contains no redundant vectors, and thus can be written:

>###  $$\text{span}\{ \vec{v_1},\dots,\vec{v_m} \} = a_1\vec{v_1} + \dots + a_m \vec{v_m},\, a_i \in \RR. $$


Recall that $S \subset U$, *i.e.* each element $\vec{v_i}$ in $S$ is contained in $U \implies \vec{v_i} \in \text{span}\{\vec{b_1},\dots,\vec{b_m}\}$. 

Because every $\vec{b_i}$ in $U$ is a vector in $\RR^n$, as given in the prompt, any linear combination of the vectors $\vec{b_i}$ will also be vectors in $\RR^n$. Therefore, according to the above, every vector $\vec{v_i}$ in $S$ is also $\in \RR^n$.

If we assume that the set $S$ is linearly independent, we have the following: 


$$\begin{align} \text{span}\{S\} & =\text{span}\{ \vec{v_1},\dots,\vec{v_m} \}\\  &= \RR^m \\  &= \text{span} \{\vec{b_1},\dots,\vec{b_m} \}  = U.\\ \end{align}$$

...where the third  equality is taken from the above result that the vectors $\vec{b_i}$ in the basis of $U$ are linearly independent. The spans of any $m$ linearly independent vectors are equivalent to $\RR^m$.

Note that this shows that $\text{span}\{S\}$ is *equivalent* to the set $U$ - $S$ is an alternative (but valid) basis for $U$.
***


Now for the converse statement: 

> A set $S$ spans $U \implies S$  is linearly independent. 


Assume that $S=\{ \vec{v_1},\dots,\vec{v_m} \}$ spans $U$, such that:

$$\text{span}\{ \vec{v_1},\dots,\vec{v_m} \} = U = \text{span}\{ \vec{b_1},\dots,\vec{b_m}\} .$$

We were given the fact that the dimension of $U$ is $m$ in the prompt $\implies$ a minimal spanning set for $U$ contains $m$ linearly independent vectors. Therefore, if $S$ spans $U \implies$ the vectors $\{\vec{v_1},\dots, \vec{v_m} \}$ must be linearly independent.

***

We have now seen that the following two statements are true:

>- A set $S$ spans $U \implies S$  is linearly independent. 
> - A set $S$ is linearly independent $\implies S$  spans $U$.

Therefore: 

>  $S$ spans $U \iff S$  is linearly independent. 


QED.

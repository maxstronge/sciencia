# Proof Assignment Topic 7:
***

**Prompt:** Let $T:  V\to W$ be a map between two vector spaces. Prove that the composition of two linear maps is linear. 

***

Let $T:V\to W$ be a function mapping inputs from vector space $V$ to vector space $W$. Suppose $T$ is defined by a composition of two other functions, $Q: V\to W$ and $R: V \to W$, such that:

>$$T(v) = Q \circ R\,(v) = Q(R(v))\text{ for all $v$ in $V$.}$$

Suppose as well that the two transformations composing $T$, $Q$ and $R$, are both *linear* - *i.e.* they satisfy the following two axioms:

> **1.** $T(v+v_1) = T(v) + T(v_1)$ for all $v$ and $v_1$ in $V$.
>
>**2.** $T(r\,v) = r\,T(v)$ for all $v$ in $V$ and all $r$ in $\RR$.

**Claim:** If each of the component transformations $Q$ and $R$ are linear, their composition $T$ is linear as well. 

**Note:** one additional condition is required for this claim is to be true in generality. If $Q\circ R = Q(R(v))$ is to define a composite transformation $T$, it is necessary to require that the *image* of $R$ be entirely in the *domain* of $Q$: that is, every possible output of $R(v)$ must be a valid input for $Q(v)$ in order for the composition to work. Therefore, each possible output of $R(v) \in V$.

Let $\va{a},\va{b}$ be two vectors $\in V$. Our goal is to demonstrate that the transformation $T = Q\circ R$ is linear if both $Q$ and $R$ are linear. The two axioms needed to determine whether a transformation is linear are above. Let us begin with the first axiom:

> ### $$\begin{align}T(\va{a}+\va{b})& =Q\circ R\,(\va{a}+\va{b}) \\ &= Q(R(\va{a}+\va{b})) \\ \qq{by axiom 1:} & = Q(R(\va{a}) + R(\va{b})) \\ & = Q(R(\va{a})) + Q(R(\va{b})) \\ &= Q\circ R(\va{a}) + Q\circ R (\va{b}) \\ &= T(\va{a}) + T(\va{b}).\end{align} $$

The composite transformation satisfies the first axiom just as a consequence of its component transformations being linear. Let us now turn to the second axiom:

> ## $$\begin{align}T(r\,\va{a}) = Q\circ R (r\,\va{a}) &= Q(R(r \,\va{a})) \\ \qq{by axiom 2:} &= Q(r\,R(\va{a})) \\ &= r\,Q(R(\va{a})) \\ &= r\,Q\circ R(\va{a}) \\ &= r\, T(\va{a}). \end{align} $$

The second axiom is also satisfied by this general composite transformation $T$. 

Therefore: if $Q: V \to W$ and $R: V \to W$ are linear transformations $\implies$ the transformation $T = Q \circ R$ is also linear. QED. 

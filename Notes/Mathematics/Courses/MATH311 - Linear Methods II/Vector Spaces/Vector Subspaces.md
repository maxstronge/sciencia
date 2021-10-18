# Vector Subspaces:

***

A subset $U$ of a vector space $V$  is called a **subspace** of $V$ if it is itself a vector space under the addition/scalar multiplication rules defined for $V$.

***

**Theorem** -  Subspace Test:

> A subset $U$ of a vector space $V$ is a subspace of $V \iff U$ satisfies the following:
> 1. *Zero Vector:* $\va{0} \in U.$
> 2. *Closed Under Addition:* $\va{x},\va{y} \in U \implies \va{x} + \va{y} \in U.$
> 3. *Closed Under Scalar Multiplication:*  $\va{x} \in U \implies K\va{x} \in U, K \in \RR$.

***
### Span of Vector Spaces:

Recall - a *linear combination* of vectors $\va{x}$ and $\va{y}$ is a vector of the form $a \va{x} + b \va{y}$ for $a,b\in\RR$.

Also recall that the *span* of a set of vectors $\{\va{v_1},\dots,\va{v_n} \}$ is the set of all linear combinations of $\va{v_1},\dots,\va{v_n}$.

- *i.e.* $\span\{\va{v_1},\dots,\va{v_n}\} = \{a_1\va{v_1} + a_2\va{v_2} + \dots + a_n\va{v_n} \,|\,a_i \in \RR\}.$

***

**Example:** Show that $\Pp_2 = \span\{1,x,x^2\}$.

> $\Pp_2$ is the set of all polynomials with a maximum degree of 2:
> >$$\Pp_2 = a_0 + a_1\,x + a_2\, x^2, a_i \in \RR.$$
> We can write the span given as $a\,(1) + b\,(x) + c\,(x^2)$, and, since the $a_i$ in the definition of $\Pp_2$ are just any real numbers, we can equivalently write the span as:
> > $$a_0\, (1) + a_1\,(x) + a_2 \, (x^2) = a_0 + a_1\,x + a_2\,x^2 = \Pp_2.$$***

***

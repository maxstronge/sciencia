# Polynomials 
***
Sets of polynomials provide another important source of examples of vector spaces, so first let us review some basic facts.

A **polynomial** in an indeterminate $x$ is some expression

> ### $$p(x)=a_0 + a_1x + a_2x^2 +\dots + a_nx^n $$

...where $a_0,a_1,\dots,a_n$ are real numbers called 	the **coefficients** of the polynomial.

If all the coefficients are zero, the polynomial is called the **zero polynomial** and is denoted simply as $0$. 

If $p(x)\neq 0$, the highest power of $x$ with a *nonzero coefficient* is called the **degree** of $p(x)$, denoted $\text{deg}\,p(x)$. The degree of the zero polynomial is not defined.

That coefficient itself is called the **leading coefficient** of $p(x)$. 

Let $\mathcal{P}$ denote the set of all polynomials, and suppose that:

> #### $$\begin{align} p(x) &= a_0  + a_1 x + a_2x^2 +\dots \\q(x) &= b_0 + b_1 x + b_2 x^2 + \dots\end{align} $$

...are two polynomials in $\mathcal{P}$ (possibly of different degrees). Then, $p(x) \text{ and } q(x)$ are called **equal** ($p(x) = 	q(x)$) $\iff$ all the corresponding coefficients are equal: *i.e.* $a_0=b_0,\dots,a_n=b_n.$


The set $\mathcal{P}$ has addition and scalar multiplication defined on it as follows:  if $p(x)$ and $q(x)$ are as before and $a$ is some $\in \RR$:

> **Addition:**
> $$p(x) + q(x) = (a_0 + b_0) + (a_1+b_1)\,x + (a_2 + b_2)\,x^2 + \cdots$$
> 
> **Scalar Multiplication:**
> $$a\,p(x) = aa_0 + (aa_1)\,x + (aa_2)\,x^2 + \cdots$$

Clearly, these results are again polynomials: thus, $\mathcal{P}$ is closed under these operations (called **pointwise** addition and regular scalar multiplication). The other axioms are easily verified, leading us to the conclusion: 

> #### Theorem: 
> The set $\mathcal{P}$ of all polynomials is a **vector space** with the above-mentioned addition and scalar multiplication. The *zero vector* is the zero polynomial $0$,and the *negative* of some polynomial $p(x) = a_0 + a_1 x + \cdots$ is the polynomial $-p(x) = -a_0 - a_1 x - \cdots$ obtained by negating all the coefficients. 

***

There is another important vector space of polynomials we will consider. 

>Given $n\geq1,$ let $\mathcal{P}_n$ denote the set of polynomials with a degree of at most $n$, together with the zero polynomial: 
>$$\mathcal{P}_n = \{a_0 + a_1 x + a_2x^2 + \dots + a_n x^n | a_0,\dots, a_n \in \RR\}.$$
>Then $\mathcal{P}_n$ is a vector space. Indeed, sums and scalar multiples of polynomials in $\Ppn$ are again in $\Ppn$, and the other vector space axioms are inherited from $\Pp$. In particular, the zero vector and the negative of a polynomial in $\Ppn$ are equivalent to those in $\Pp$.




***

### Vector Space Applications to Polynomials:

The vector space of all polynomials of degree at most $n$ is denoted $\Ppn$.






***
**Example**: 


Show that $\mathcal{P}_n$ is a subspace of $F(-\infty,\infty)$, the vector space of all real-valued functions on $(-\infty, \infty)$.




***


#linear_algebra #vector #vector_space #sets #polynomials #degree
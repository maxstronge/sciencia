# Intro to Course and Proofs:

***

## Sections:

- [[Logical Operators]]
- [[Direct Proof and Examples]]
- [[Set Theory]]
- [[Review of Important Matrix Properties]]

***

## Proof Assignment: 

- Recall that a matrix $\bf{A}$ is *symmetric* if $\bf{A}$ = $\bf{A}^T$, and is called *skew-symmetric* if $\bf{A}^T = -\bf{A}$. 
- Determine whether the following statements are true or false. If true, provide a proof. If false, provide an explicit counterexample. 


	1. Suppose $\bf{A}$ and $\bf{B}$ are skew-symmetric, and $\bf{AB} = \bf{BA}$. Then, $\bf{AB}$ is skew-symmetric.


		-  If so, $(\bf{AB})^T = -(AB)$. The left-hand side of this equation is equivalent, through the definition of the transpose of a matrix product, to:

		- $(\bf{AB})^T = \bf{B}^T\bf{A}^T \implies \bf{B}^T\bf{A}^T = -(AB).$
		- Recalling that both $\bf{A}$ and $\bf{B}$ are skew-symmetric, we can evaluate the left-hand side of the second equality above to yield:
		- $(-\bf{B})(-\bf{A}) = -(\bf{AB}) \implies \bf{BA} = -\bf{AB}.$ 
		- Recalling that $\bf{AB}=\bf{BA}$, as was given, we are left with:
		- $\bf{AB} = -(\bf{AB})$. This is possible if and only if both $\bf{A}$ and $\bf{B}$ are equal to the zero matrix, in which case $\bf{AB}$ is both symmetric *and* skew-symmetric. For all $\bf{A}$,$\bf{B} \neq \bf{0}$, $\bf{AB}$ is not skew-symmetric.

	2. Suppose $\bf{A}$ and $\bf{B}$ are skew-symmetric, and $\bf{AB} = \bf{BA}$. Then, $\bf{AB}$ is *symmetric*.
	
		- For the matrix $\bf{AB}$ to be symmetric, it must satisfy $(\bf{AB})^T = \bf{AB}.$
		- Following the previous logic, we can evaluate the left side:
		- $(\bf{AB})^T = \bf{B}^T\bf{A}^T = (-\bf{B})(-\bf{A})$. Thus:
		- $(-\bf{B})(-\bf{A}) =\bf{AB}$. 
		- Again following the previous logic,  $(-\bf{B})(-\bf{A}) = \bf{BA}$ through traditional scalar algebra. 
		- Since $\bf{AB} = \bf{BA}$, the left-hand side of the original equality is equivalent to $\bf{AB} \implies \bf{AB}$ is symmetric. QED.
		

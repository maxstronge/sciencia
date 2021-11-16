# Topic 10 Proof-Writing Assignment:
##### Max Stronge (30064749)
***

**Prompt:** Decide whether the following statements are TRUE or FALSE. If the statement is true, then prove it. If it is not true, then provide an explicit counterexample.

1. If $A$ and $B$ are $\nxn$ orthogonal matrices, then $A+B$ is orthogonal.
2. If $A$ is an orthogonal matrix, then $A^{-1}$ is orthogonal.

***

### 1:

Let $A$ and $B$ be $\nxn$ matrices, and let them be *orthogonal*. 

By definition: an $\nxn$ matrix $A$ is orthogonal if $A^{-1} = A^T$. Let $\va{c}_{A1}, \dots, \va{c}_{An}$ denote the columns of $A$, and then let $\va{c}_{B1},\dots, \va{c}_{Bn}$ denote the columns of $B$. 

Because $A$ is orthogonal, $A^T = A^{-1} \implies A^T A = I \implies \va{c}_{Ai}^T \va{c}_{Aj} = 0$ for all $i \neq j, 1 \leq i, \  j \leq n$. Additionally, $\va{c}_i^T  \ \va{c}_i = 1.$

We can write the sum $A+B$ in terms of the columns of each matrix:

$$A + B = \qty{\va{c}_{A1}+\va{c}_{B1}, \dots, \va{c}_{An}+\va{c}_{Bn}}$$

Let us call this new $\nxn$ matrix $C$. $C$ is orthogonal if, as per the definition, $C^T = C^{-1}$. If this is true, then $C C^T = C C^{-1} = I.$ Writing out the expansion of this product:

$$C C^{-1} = $$
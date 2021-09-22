# Linear Independence:

***

Given a set of vectors, how can we determine if their span is a line, a plane or a larger dimensional space? If a vector in our set is a *linear combination* of any other elements in our set, that vector is reduntant - if it were removed from the set, the *span* of the set would remain unchanged. 

We need a method of systematically removing these redundancies to find the minimum number of vectors to span the set. 


***

**Definition**: a set $S$ of vectors $\{\vec{x_1}, \vec{x_2}, \dots, \vec{x_k} \}$ is called **linearly independent** if the equation:

> $$t_1 \vec{x_1} + t_2\vec{x_2} + \dots + t_k \vec{x_k} = 0 $$

...has only the trivial solution, $t_1 = t_2 = \dots = t_k = 0$. Otherwise (*i.e.* there is a non-trivial solution), the set $S$ is called **linearly dependent**.
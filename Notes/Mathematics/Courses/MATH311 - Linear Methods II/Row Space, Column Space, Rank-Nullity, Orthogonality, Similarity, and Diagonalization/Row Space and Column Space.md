# Row Space and Column Space:

***

The **Row Space** of a matrix $A$, denoted $\text{row}(A)$, is the subspace spanned by the *rows* of $A$. 
- *e.g.* if $A = \begin{bmatrix} 1&2&3 \\ 4&5&6 \\ 2&4&6\end{bmatrix}$, then $\text{row}(A) = \text{span}\{(1,2,3),(4,5,6),(2,4,6) \}.$

***

The **Column Space** of a matrix $A$, denoted $\text{col}(A)$, is the subspace spanned by the *columns* of $A$. 

- *e.g.*  if $A = \begin{bmatrix} 1&2&3 \\ 4&5&6 \\ 2&4&6\end{bmatrix}$, then $\text{col}(A) = \text{span}\{(1,4,2),(2,5,4),(3,6,6)\}.$


**NOTE:** $\text{col}(A) = \text{im}(A)$! They are synonymous. 

***

**Theorem**: Elementary row operations do not change the *row space* of a matrix. 

This can be seen to be true (though not officially proved) by noting that elementary row operations replace existing rows by linear combinations of those rows. Since all linear combinations are contained in the span, the row space remains the same. 

The inverse is **not** true - EROs *do* change the column space of a matrix. 

***

Question: How can we find a basis for $\text{im}(A) = \text{col}(A)?$

One way is to create a new matrix, whose rows are the *columns* $A$, then to use the previously discussed [[Basis#Procedure for finding a basis|method of finding a basis.]]  Another method is outlined in the following theorem:

>**Theorem:**
>- Let $B$ be a matrix obtained by performing elementary row operations on $A$. Then, a given set of column vectors of $A$ form a *basis* for $\text{col}(A) \iff$ the corresponding column vectors of $B$ form a basis for $\text{col}(B)$. 


So, to find a basis for $\text{col}(A)$, we can find the *r.r.e.f* of $A$. The *i*-th column of $A$ will be a basis vector if the *i*-th column of the *r.r.e.f* of $A$ has a leading 1. 

*Example:* The matrix $A$...

$$A = \begin{bmatrix} 1&-3&4&-2&5&4 \\ 2&-6&9&-1&8&2 \\ 2&-6&9&-1&9&7\\-1&3&-4&2&-5&-4\end{bmatrix}$$

...can be put into *r.r.e.f*, becoming:

$$A_{rref} = \begin{bmatrix} 1&-3&4&-2&5&4 \\ 0&0&1&3&-2&-6 \\ 0&0&0&0&1&5\\0&0&0&0&0&0\end{bmatrix}$$

We can see that the first, third, and fifth columns of $A_{rref}$ have leading 1s - therefore, the first, third and fifth columns of $A$ are basis vectors for $\text{col}(A)$.

***



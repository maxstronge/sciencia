# Systems of Linear Equations and Elementary Operations:

***
## The Augmented Matrix:
 
 When solving systems of linear equations in more than three variables, it is no longer possible to geometrically represent the solution in terms of intersecting lines/planes. Algebraic solutions, however, suffer no such difficulty, and can be found in an arbitrary number of dimensions. 
 
 Matrices are used to simplify the computation of these systems. Consider the following system of four variables in three equations:
 
> $$\begin{align}3x_1 + 2x_2 - x_3 + x_4 &= -1\\ 2x_1 - x_3 + 2x_4 & = 0 \\ 3x_1 + x_2 + 2x_3 + 5x_4 &= 2\end{align} $$

We can construct a matrix to more succinctly represent this information like so:


$$ \left[
\begin{array}{cccc|c}
  3&2&-1&1&-1\\
  2&0&-1&2&0\\
  3&1&2&5&2
  
\end{array}
\right] $$

This array of numbers is called the **augmented matrix** of the system. Each row of the matrix consists of the coefficients of the variables (in order) from the corresponding equation, together with the constant term. The constants are separated by the vertical line for clarity, such that they are not confused with coefficients. This format is a coefficient matrix, the first four columns, *augmented* by a constant matrix, the final column. 

***

## Elementary Operations:

The following operations, called **elementary operations**, can be routinely performed on systems of linear equations to produce *equivalent* systems, which are typically much easier / trivial to solve. 

1. Interchange two equations.
2. Multiply an equation by a nonzero number. 
3. Add a multiple of one equation to another. 


After performing a series of *EO*s on a system, the solution of the resulting system will be the solution of the original system as well. 

The same applies to matrices - instead of operating on the different equations in a system, we perform **elementary row operations** on the rows of the matrix, where we can:


1. Interchange two rows.
2. Multiply a row by a nonzero number. 
3. Add a multiple of one row to another.

***

## Gaussian Elimination: 

Our goal in performing *ERO*s on matrices is to put them into a form that makes it trivial to determine a solution. The following definitions identify these forms.


> #### **Row-Echelon Form**: 
>A matrix is said to be in **row-echelon** form, and is called a row-echelon matrix, if it satisfies the following three conditions:
>1. All **zero rows** are at the bottom.
>2. The first nonzero entry from the left in each nonzero row is a **1**, called a **leading 1** for that row.
>3. Each leading 1 is to the right of all leading 1s in the rows above it. 


> #### **Reduced Row-Echelon Form**:
> A row-echelon matrix is in **reduced row-echelon form** (RREF) if it satisfies the following additional condition:
> - Each leading 1 is the *only* nonzero entry in its column. 
 

 ![[Pasted image 20210909160151.png]]

***
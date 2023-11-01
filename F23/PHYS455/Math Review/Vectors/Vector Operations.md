## Dot Product (Scalar Product):

$$\vec{A}\cdot \vec{B}=AB\cos \theta = A_{x}B_{x}+A_{y}B_{y}+A_{z}B_{z}$$


## Cross Product (Vector Product):

$$
\vec{A} \times \vec{B} = \begin{vmatrix}
\hat{\mathbf{x}} & \hat{\mathbf{y}} & \hat{\mathbf{z}} \\
A_{x} & A_{y} & A_{z} \\
B_{x} & B_{y} & B_{z}
\end{vmatrix} = (A_{y}B_{Z}-A_{z}B_{y}) \ \hat{\mathbf{x}} + (A_{z}B_{x}-A_{x}B_{z}) \ \hat{\mathbf{y}} + (A_{x}B_{y} - A_{y}B_{x}) \ \hat{\mathbf{z}} 
$$

$$
= AB\sin(\theta) \mathbf{\hat{n}}
$$
These two representations are equivalent - $\theta$ is the smallest angle between $\vec{A}$ and $\vec{B}$ and $\mathbf{\vec{n}}$ is a unit vector orthogonal to both vectors.


## Scalar Triple Product:

Defined as the dot product of one vector with the cross product of two others:

$$
\vec{A} \cdot (\vec{B} \times \vec{C})
$$

Geometrically this is the signed volume of the parallelepiped defined by the three vectors given. 

Can be evaluated as a determinant:

$$
\vec{A} \cdot (\vec{B} \times \vec{C}) = \begin{vmatrix}
A_{x} & A_{y} & A_{z}  \\
B_{x} & B_{y} & B_{z}  \\
C_{x} & C_{y} & C_{z}
\end{vmatrix} = (B_{z}C_{y}- B_{y}C_{z}) \ A_{x} + (B_{x}C_{z}- B_{z}C_{x}) \ A_{y} + (B_{y}C_{x}-B_{x}C_{y}) \ A_{z}
$$
## Vector Triple Product:

The cross product of one vector with the cross product of another two vectors:

$$
\vec{A} \times (\vec{B}\times \vec{C}) = \vec{B}(\vec{A}\cdot \vec{C}) - \vec{C} (\vec{A} \cdot \vec{B})
$$

The above is called **Lagrange's formula** for the triple product expansion.

BAC CAB! Easy to remember



## Transformations:

- Separation vector in Cartesian coordinates:
	- $\vec{r}-\vec{r'} = (x-x')\hat{\mathbf{x}}+(y-y')\hat{\mathbf{y}}+(z-z')\hat{\mathbf{z}}$


***
#vector #vectoroperations #dotproduct #crossproduct #tripleproduct #vectors







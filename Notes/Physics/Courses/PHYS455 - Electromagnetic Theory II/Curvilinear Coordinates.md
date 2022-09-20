# Curvilinear Coordinates:
***

### Spherical Coordinates:

Identifies a point $P$ by three coordinates: $r$, the distance from the origin (magnitude of position vector $\va{r}$); $\th$, the angle downwards from the $z$-axis, called the **polar angle**, and $\phi$, the angle around from the $x$-axis, called the **azimuthal angle**.

Conversions from Cartesian coordinates:

> $$\begin{align}x &= r \sin\th\cos\phi \\
y &= r\sin\th\sin\phi \\
z &= r\cos\th\end{align}$$

There is also an orthogonal basis of unit vectors, much like the Cartesian ones:

> $$\begin{align}\hat{r} &= \sin\th\cos\phi \ \hat{x} + \sin\th\sin\phi \ \hat{y} + \cos\th \ \hat{z} \\\hat{\th} &= \cos\th\cos\phi \ \hat{x} + \cos\th\sin\phi \ \hat{y} - \sin\th \ \hat{z} \\\hat{\phi} &= -\sin\phi \ \hat{x} + \cos\phi \ \hat{y}\end{align}$$

**NB:** Be careful with these unit vectors! They are themselves functions of position. Can't take them out of integrals as constants.

**General infinitesimal displacement** $d\va{\ell}$ plays the same role as $d\va{\ell} = dx \ \hat{x} + dy \ \hat{y} + dz \ \hat{z}$ does in Cartesian coordinates (eg. for line integrals):

>$$d\va{\ell} = dr \ \hat{r} + rd\th \ \hat{\th} + r\sin\th d\phi \ \hat{\phi}$$



**General volume element** $d\tt$ is just the product of the three length elements:


> $$\begin{align}d\tt &= d\ell_r \ d\ell_\th \ d\ell_\phi \\
&= r^2\sin\th \  d\th \ d\phi \ \hat{r}.\end{align}$$

**Vector Derivatives:**
- Gradient: 

>$$\va{\grad}\va{T} = \pdv{\va{T}}{r} \ \hat{r} + \frac{1}{r}\pdv{\va{T}}{\th} \ \hat{\th} + \frac{1}{r\sin\th}\pdv{\va{T}}{\phi}  \hat{\phi}.$$

- Divergence:

>$$\va{\grad}\cdot\va{v}= \frac{1}{r^2}\pdv{r}(r^2v_r) + \frac{1}{r\sin\th}\pdv{\th}(\sin\th v_\th) + \frac{1}{r\sin\th} \pdv{v_\phi}{\phi}.$$

- Curl:

>$$\va{\nabla}\cross \ \va{v} = \frac{1}{r\sin\th}\left[ \pdv{\th}(\sin\th v_\phi) - \pdv{v_\phi}{\phi} \right] \ \hat{r} + \frac{1}{r}\left[ \frac{1}{\sin\th}\pdv{v_r}{\phi} - \pdv{r}(rv_\phi)\right] \ \hat{\th} + \frac{1}{r}\left[ \pdv{r}(rv_\th) - \pdv{v_r}{\th} \right] \ \hat{\phi}.$$

- Laplacian:

>$$\laplacian \ T = \frac{1}{r^2}\pdv{r} \left( r^2 \pdv{T}{r} \right) + \frac{1}{r^2\sin\th} \pdv{\th}\left( \sin\th \pdv{T}{\th} \right) + \frac{1}{r^2\sin^2\th}\pdv[2]{T}{\phi}.$$


***


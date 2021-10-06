# 2.1 - Spherical Trigonometry: 

___

For the coordinate transformations of spherical astronomy, we need some mathematical tools, which we will present now. 

We need a coordinate system that will allow us to identify and locate points that essentially fall on the surface of a sphere (see [[COORDINATE SYSTEMS|the notes on the celestial sphere]]).

If a *plane* passes through the center of a sphere, as in the figure below, it will split the sphere into two identical *hemispheres* along a circle called a **great circle**. 

There are also **small circles**. Small circles are formed by the intersection of a plane with the sphere, like great circles, with the distinction that the plane of intersection does *not* go through the center of the sphere.  


![[Pasted image 20210910110627.png]]


On Earth, we have a similar coordinate system used by geographers/geologists/etc. Lines of **longitude** are *great circles* that all converge at the northern and southern poles, and *small circles* form lines of **latitude** (except for the equator, which is a great circle). 


In spherical space, the shortest distance between any two points is not a straight line, as it is in flat Euclidean geometry - the shortest distance between any two points lies on a great circle. 

A line perpendicular to the plane passing through the center of the sphere will intersect the sphere at the **poles** $P$ and $P'$. 

***

A **spherical triangle** is not just any three-sided figure lying on the surface of a sphere. The sides of a spherical triangle *must* be arcs of certain great circles, as in the figure below. 

![[Pasted image 20210910114919.png]]

The above spherical triangle *ABC* has three arcs *AB*, *BC*, and *AC* as its sides. If the radius of the sphere is *r*, the length of the arc *AB* is:

> ### $$|AB| = rc, [c]=\text{rad}$$

...where *c* is the angle subtended by arc *AB* *as seen from the center*.  This angle is called the **central angle** of the side *AB*. Because the lengths of sides and central angles correspond to each other uniquely, it is customary to give the central angles instead of side lengths. In this way, the radius of the sphere *does not enter* into the equations of spherical trigonometry.

**Note:** in the above formula, $r =$ the radius of the sphere $\iff$ the circle is a **great circle**. 

For small circles, we use the radius of the small circle:

> ### $$|ab|= r \theta $$

...where *r* is the radius of the small circle, and $\theta$ is the central angle as before. 

![[Pasted image 20210913111958.png]]

This is a departure from the usual Euclidean trigonometry: the length of a side of a right-triangle, $|AB| =r \tan(c)$ is **not** the same as the length of arc $|AB|=rc$.

However, for small angles, $\tan(\theta)\approxeq \theta$. The limits of 'small angle' really depend on the needed precision of the calculation. Therefore, for small angles, spherical trigonometry reduces to the Euclidean. 

Nevertheless, we can calculate the **true size** of any object if we can measure its **angular size**, *c*, and we know its **distance**, *r*. 

Conversely, if we know both the angular and true size of the object, we can find the distance. 

Some key observations re: spherical trigonometry:

1. For a given angular size $\alpha$, the more distant the object, the greater its true (linear) size.
2. For a given *linear* size, the more distant the object, the smaller its angular size.
3. An object's linear size *D*, angular size $\alpha$, and distance *d* can be related by:

> ### $$D = d \alpha. $$

....or, for small angles....

> ### $$D = rc. $$

***

### Angular Sizes:
When discussing angular sizes, more precision is needed than can be conveniently given with degrees or radians. We define the following units for angular sizes:


> $1 \degree = 60'$ (arcminutes)
> $1' = 60''$ (arcseconds)

A finger held at arms length will subtend ~$1 \degree$ in the sky - a fist will subtend $10 \degree$. 

***

### Spherical Area:

Like Euclidean triangles, spherical triangles also have an area (specifically, surface area). The calculation of this area, however, differs from the Euclidean case due to the curvature of the geometry.

First: the sum of the angles of a spherical triangle is always **greater than** 180$\degree$; the excess:

> ### $$E = A + B + C - 180\degree $$

...is called the **spherical excess**. It is not constant, but depends on the nature of the spherical triangle. The area of a spherical triangle is related to the spherical excess in a simple way:

> ### $$\text{Area} = Er^2, \, [E\,] = \text{rad}. $$


![[Pasted image 20210913114503.png]]

The angular area on the sky (denoted $d\Omega$ on the above figure) is called the **solid angle**. The solid angle is in units of **steradians** ($\text{rad}^2$), often abbreviated as *sr*. Much like there are $2\pi$ radians in the circumference of a circle, there are $4\pi$ steradians in the entire surface of a sphere. 

If a region on the sky is **circular** in shape, which is a common scenario in astronomy, the solid angle is given by:

> ## $$d\Omega= 2\pi (1-\cos\theta)$$

....or, using the small angle approximation $\cos\theta\approx1-\frac{\theta^2}{2}$,

> ## $$d\Omega	\approx \pi \theta^2.$$

In the above two equations, $\Omega$ is related to the surface area of the sphere, and $d\Omega$ denotes the region of $\Omega$ we are concerned with. 

Since we know that the full surface area of a sphere is $A = 4 \pi r^2$, and since $\Omega = 4\pi$, the full surface area of the sphere is equivalent to:

> ## $$A = \Omega r^2. $$

So if we want to find the physical area of a region smaller than the entire surface (*i.e.* $dA$), that has a solid angle $d\Omega$ (some solid angle smaller than $4\pi$), we can see that:

> # $$dA = d\Omega r^2. $$

***

 ## Spherical Polar Coordinates:
 
 We are most familiar with the traditional Cartesian coordinate system (a.k.a. rectangular coordinates) with 3 variables *x*, *y*, and *z*.  In astronomy however, where our main areas of inquiry are the Earth and the sky above it, it will be practical to work in **spherical polar coordinates**, since both the Earth and sky can be approximated as spheres. 
 
 We work with three different coordinates in this system: ($r,\,\theta,\,\phi$).
 
 ![[Pasted image 20210915112243.png]]
 
 
 We can derive a set of conversion factors from Cartesian to spherical polar coordinates:
 
  ![[Pasted image 20210915112615.png]]
  
  > - $x =r \sin\theta\cos\phi$
  > - $y = r\sin\theta\sin\phi$
  > - $z =r\cos\theta$.
  
  
  Let us use $\rho$ to denote the radius of the sphere. The distance from the center to any given point on a great circle is then $\rho$, and the distance to a point on any small circle measured perpendicularly outwards from the vertical axis is $\rho\sin\theta$. 
  
  An arc on the circle perpendicular to the vertical axis can be measured as $\rho\sin\theta d\phi$ (since an arc length  = distance ($\rho\sin\theta$) $\times$ angle ($d\phi$)).
  
  An arc length for any great circle (eg. a circle of latitude) is given by $\rho d\theta$.
  
  Thus, any boxed trapezoidal area on the surface of a sphere is: 
  
  > ### $$dA = \rho\sin\theta d\phi\,\times\,\rho d\theta = \rho^2\sin\theta d\theta d\phi. $$

And since the definition of $dA$ is $dA = \rho^2 d\Omega$....


> ## $$d\Omega = \sin\theta \,d\theta \,d\phi.$$
 
 
So returning to the area:

> ### $$\begin{align} \text{Area} & = \int dA \\ & = \int r^2 d\Omega \\ & = r^2 \iint \sin\theta\,d\theta\,d\phi.	 \end{align}$$
  
  ***
  
  
 
  
  ## Finding physical area given polar coordinates:
  
  ### $$d\Omega = \int_{\theta_1}^{\theta_2}\sin\theta d\theta \int_{\phi_1}^{\phi_2}d\phi = |-\cos\theta|_{\theta_1}^{\theta_2}\,\, |\phi|_{\phi_1}^{\phi_2}$$
  
  ### $$= (-\cos\theta_2 + \cos\theta_1)\, \cdot \, (\phi_2 - \phi_1).$$
  
  Once $d\Omega$ is determined, recall that the area can be found by $dA = r^2 d\Omega$. 
  
  ***
  

  
  
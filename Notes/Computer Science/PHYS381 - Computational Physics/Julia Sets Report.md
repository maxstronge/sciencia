# PHYS381 Bonus Assignment: Julia Sets

### Max Stronge (30064749)
#### PHYS381 - Computational Physics I


Fractals are a striking class of mathematical entities that exhibit some degree of self-similarity, formally called 'a fractional dimension'. The work fractal was coined by Benoit D. Mandelbrot (1924-2010$_\text{AD}$), who is also the namesake of the most famous fractal: the Mandelbrot set, commonly depicted as in the image below:

![[Pasted image 20220304104742.png]]

This image is quite famous, and recognizable to many individuals with or without experience with the mathematics behind it. 

Hiding in the beauty of the Mandelbrot set, though, is a fascinating relation to another class of functions called *Julia sets* - indeed, the Mandelbrot set can be considered as the map of all Julia sets that converge, rather than branching off to infinity. Zooming into the Mandelbrot set, one can find many individual Julia sets:

![[Pasted image 20220304105106.png]]

The famous Mandelbrot set is then composed of a wide array of complex, often chaotic Julia sets. The Julia sets shown above, and in the lab report, are defined by a complex quadratic polynomial of the form:

$$f_c(z) = z^2 + c$$

...where $z$ is a complex number that gets updated by the function $f_c(z)$, and $c$ is a complex parameter that remains constant. We visualize these fractals by creating a plot in the complex plane, with each point $(x, \ y)$ corresponding to a complex number $z = x + y i$. If the function converges to a finite value, it is considered to be *in* the Julia set, and it gets shaded - if the function diverges to infinity, it is outside the set, and is not shaded. 

The following are visualizations of Julia sets in the manner described above, for various values of c. They were created in python using the matplotlib, math, cmath, and numpy animations. For each value of c, the complex function $f_c(z)$ was applied until either a) the value of $z$ exceeded $4.0$, at which point we can conclude that the function will diverge and no further iterations are necessary, or b) a maximum number of iterations was reached (in this case 80), at which point we can conclude that the function will converge and that point on the imaginary plane is a part of the Julia set. 

Colormaps were applied from the matplotlib library to give a more aesthetically pleasing depiction - the one used for the plots below is the **viridis** colormap.


### a) c = 0.37 + 0.16𝑖:

![[plota.png]]

### b) c =  −0.50 − 0.56𝑖:
![[plotb.png]]

### c) c = −0.25:

![[plotc.png]]

### d) c = 𝑖

![[plotd.png]]

### e) c = -1.5:
![[plote.png]]

### f) c =  −0.75 + 0.25𝑖:
![[plotf.png]]

### g) c = 0.37 + 0.16𝑖:
[seems to be a duplicate of part (a)]
![[plotg.png]]
### h)  c = −0.123 + 0.745𝑖:

![[ploth.png]]

### i) c = 1.0:

![[ploti.png]]
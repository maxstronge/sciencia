# 	ASPH305: Homework Assignment #1
***

1. Astronomers on Earth have measured the distance to a hypothetical approaching asteroid to be $0.713\,AU$. 

***

### *a)*

If the observed angular diameter of the asteroid at the time of observation is $0.01''$, **calculate the physical diameter (in *m*) and the solid angle (in *sr*)**. For the physical diameter, use both the *small angle approximation* **AND** the *full trigonometric approach* to confirm whether or not the small angle approximation is valid. **Explain your reasoning**. 


> Assuming the asteroid can be approximated as a sphere. 
> - distance $d = 0.713\,AU = 1.06663 \times 10^{8}\,km$
> - angular diameter $\alpha = 0.01'' = 4.84814 \times 10^{-8}\,rad$

With small-angle approximation: physical diameter $D = d \alpha:$

$$\begin{align} D & = d \alpha \\ & = (1.06663 \times 10^{8})\,(4.84814 \times 10^{-8}) \\ &=5.17118 \,km.\end{align} $$

Full trigonometric approach: 

$$R = r \tan\theta \implies D = 2R = 2r\tan\theta.$$

$$\theta = \frac{\alpha}{2} = \frac{4.84814 \times 10^{-8} rad}{2}$$

$$r = 1.06663 \times 10^{8} \,km$$

$$D = 2(1.06663\times10^{8})\cdot\tan\left(\frac{4.84814 \times 10^{-8} rad}{2}\right) = 5.17117\,km.$$

The small angle approximation is accurate to within a millimetre of the full trigonometric approach, so it is a valid approximation for this calculation.

***

### *b)*

$d = 10\,km$. $\implies D = d \alpha \implies \alpha = \frac{D}{d}$.

$$\alpha = \frac{5.17117}{10} $$
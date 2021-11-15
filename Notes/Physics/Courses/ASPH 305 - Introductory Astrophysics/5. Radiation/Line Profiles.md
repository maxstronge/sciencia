# Line Profiles:
***

Our work thus far on   [[6.4 - Line Spectra|line spectra]] suggest that spectral lines are infinitesimally narrow and sharp. This is not the case in reality - we will now consider a number of factors that may affect the quality of the spectral line, called the **line profile**. An exact treatment requires discussion of hyperfine structure and some more rigorous quantum mechanics than we're accquainted with, but we can begin simply here. 

***

Recall the **Heisenberg Uncertainty Principle**: there is no way, even in principle, to determine the x-coordinate $x$ and the momentum $p_x$ in the direction of the x-axis with arbitrary precision *simultaneously*. These quantities have small uncertainties $\DD x$ and $\DD p_x$, such that:

> # $$ \DD x \DD p_x \approx \hbar.$$

A similar relation holds for other dimensions as well. Time and energy are also connected by an [[4.3 - Uncertainty Relationships for Classical Waves|uncertainty relationship]]:

$$\DD E \DD t\approx \hbar.$$

The natural width of spectral lines is a consequence of this Heisenberg uncertainty principle. 


If the average lifetime of an *excitation state* is $T$, the energy correpsonding to the transition can only be determined with an accuracy of at most $\DD E = \hbar / T = h / (2\pi T)$.

Therefore, via the [[Blackbody Radiation#^5f6437|relation between energy and frequency]], it follows that $\DD \nu = \DD E / 	h$.

In fact, the uncertainty of the energy depends on the lifetimes of *both* the initial and final states. The **natural width** of a line is defined as:

> ### $$\gg = \frac{\DD E_i+\DD E_f}{\hbar} = \frac{1}{T_i}+\frac{1}{T_f}. $$

It can be shown that the corresponding *line profile* is:

> ### $$I_v = \frac{\gg}{2\pi}\frac{I_0}{(\nu - \nu_0)^2 + \frac{\gg^2}{4}},$$
> ...where: 
> - $\nu_0 =$ the frequency at the center of the line,
> - $I_0 =$ the total total intensity of the line.

At the center of the line, the intensity *per frequency unit* is:

$$I_{v_0} = \frac{2}{\pi \gg}I_0,$$

and at the frequency $\nu = \nu_0+ \gg/2$, 

$$I_{v_0+\gg/2} = \frac{1}{\pi \gg}I_0 = \frac{1}{2}I_{v_0}.$$

Thus the width $\gg$ is the width of the line profile where the intensity is *half* of the maximum - called the **Full Width at Half Maximum** (FWHM).

****


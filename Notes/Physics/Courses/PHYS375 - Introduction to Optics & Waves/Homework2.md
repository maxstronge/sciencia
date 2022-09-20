# PHYS375 Homework Assignment 2
### Max Stronge (30064749)
***

## **Written Response**:

1. Explain in your own words (and equations) why any function of the form $$f(x\pm \cw t)$$ solves the wave equation, and what the $\pm$ corresponds to.
2. There's an electromagnetic wave called the *whistler wave* that propagates along the Earth's magnetic field, and obeys the dispersion relation: $$\oo = ak^2$$ where $k$ is the wavenumber along the magnetic field, and $a$ is some constant with the right units. Explain using words and equations why the short wavelength(and thus high-frequency) components propagate faster than long wavelength components.

**Solutions**:


***

## **Calculation Questions:**

1) A displacement wave on a string is described by $0.02 sin [2π(0.5x − 10t)]$ (m), where $x$ is in meters and $t$ in seconds. Find:
	- the propagation velocity $\cw$
	- the wavelength $\ll$ and wavenumber $k$
	- the frequency $\nu$ and angular frequency $\oo$
	- direction of propagation
	- amplitude $A$ of the wave


5.  The speed of electromagnetic waves in free space is $3 × 10^8\text{ [m/s]}$. An AM radio station uses a frequency of $540 \text{ kHz}$. Find the wavelength $\ll$. (AM =  amplitude modulation.)
6. Find the wavelength of wavy groove structure on an LP record (33 1/3 rev/min) for a sound wave with a frequency 1 kHz. Consider two radial positions on the record, $r =$(a) $15\text{ cm}$ , and (b) $10 \text{ cm}$.
7. Calculate $$\pdv{f}{x}, \ \pdv{f}{y}, \ \pdv[2]{f}{x}, \ \pdv[2]{f}{y},\pdv{f}{x}{y}$$ for the following functions:
	- $f(x,y)=\sin(x-2y)$
	- $f(x,y)=x^2+xy+y^2$

11) Add two sinusoidal waves $$2\sin(5x-1500t)\text{ and }2\sin(5.1x-1530t).$$ What is the *beat frequency*? What is the *beat wavelength*? 

**Solutions:**

1.  Put the given expression in the form: $$f(x,t) = A\sin(kx-\oo t)$$ By multiplying the factor of $2\pi$ into the brackets, we have:
$$f(x,t) = (0.02)\sin(\pi x - 20\pi t)$$

From this, we can see which terms will be pulled out as a result of partial differentiation - partial differentiation with respect to $x$ would result in a factor of $\pi^2$, and the same with respect to $t$ would result in a factor of $(20\pi)^2$ (as the sign will just indicate the direction of propagation). 

Since 

$$
\begin{align}
\pdv[2]{f}{t} &= -\oo^2 A \sin(kx-\oo t)\text{, and} \\ 
\\
\pdv[2]{f}{x} &= -k^2A\sin(kx-\oo t)

\end{align}
$$

...we can see that $k=\pi$, with units of radians/m, and $\oo = 20\pi$, with units of radians/s.

We can use these two quantities  to find the propagation velocity $\cw$:

$$\cw = \frac{\oo}{k} = \frac{20\pi}{\pi} = 20 \text{ m/s}$$

Since $k=\frac{2\pi}{\ll} \implies \ll = \frac{2\pi}{k}$, we have:

$$\ll = \frac{2\pi}{k} = \frac{2\pi}{\pi} = 2\text{ m}$$

We can find the frequency from $\oo$:

$$\nu = \frac{\oo}{2\pi} = \frac{20\pi}{2\pi} = 10\text{ Hz}.$$

The direction is in the positive $x$-direction, since the function is of the form $f(kx-\oo t)$, where the negative sign indicates a shift to the right. 

Finally, we can see that the amplitude $A$ is equal to $0.02$ m simply by looking at the equation. 
***

5.  Frequency, wavelength, and propagation velocity are related in the following way:
$$\cw = \nu \ll \implies \ll = \frac{\cw}{\nu}$$

...where $\cw$ is simply the speed of light, $299,792,458\text{ m/s}$, and the frequency was given as $540\text{ kHz}$, or $540\times10^3$ cycles per second. Thus, the wavelength is

$$\ll = \frac{\cw}{\nu} = \frac{299,792,458\text{ m/s}}{540\times10^3 \text{ s}^{-1}} = 555.17 \text{ m}.$$

***

6. The wavelength $\ll$ is equal to 
$$\ll = \frac{\cw}{\nu}$$


...and we know the associated frequency is $1$ kHz, or 1000 cycles per second. Thus to give units of length for the wavelength, $\cw$ must have the dimension of velocity, as expected. However, this is not the velocity of the resultant sound wave, as in empty space this velocity will be constant, and not dependent on the distance of the point on the record from the center. We can utilize the given frequency of revolution and the distances $r$ given
# PHYS375 Homework Assignment 2
### Max Stronge (30064749)
***

## **Written Response**:

1. Explain in your own words (and equations) why any function of the form $$f(x\pm \cw t)$$ solves the wave equation, and what the $\pm$ corresponds to.



**Solution:**

Unlike in the case of oscillations, solutions to the wave equation are not necessarily sinusoidal. Let $X=x\pm\cw t$. Then, by the chain rule:

$$\pdv{f}{t}=\dv{f}{X}\pdv{X}{t}$$

and since $\pdv{X}{t} = \pm\cw$, we have

$$\pdv{f}{t} = \pm\cw \dv{f}{X}$$

and, differentiating again, we find

$$\pdv[2]{f}{t}=\cw^2\dv[2]{f}{X}$$

and we see that the $\pm$ sign has become irrelevant. Following a similar process for differentiation with respect to $x$, we have

$$\pdv{f}{x}=\dv{f}{X}\pdv{X}{x} = \dv{f}{X}$$

...where the last step follows from recognizing that $\pdv{X}{x} = 1$. Differentiating again: 

$$\pdv[2]{f}{x}=\dv[2]{f}{X}$$

We now have two expressions containing $\dv[2]{f}{X}$, so by substituting the LHS of the above equation into the RHS of the result including a factor of $\cw^2$, we find

$$\pdv[2]{f}{t}=\cw^2\pdv[2]{f}{x}$$

...which is the wave equation! Since we gave no explicit definition of the function $f=f(x\pm\cw t)$, any function of that form will be a solution of the wave equation. Because $\cw^2$ is always positive regardless of the sign of $\cw$, the only role the $\pm$ plays is to determine the direction of propagation. 

***
2. There's an electromagnetic wave called the *whistler wave* that propagates along the Earth's magnetic field, and obeys the dispersion relation: $$\oo = ak^2$$ where $k$ is the wavenumber along the magnetic field, and $a$ is some constant with the right units. Explain using words and equations why the short wavelength (and thus high-frequency) components propagate faster than long wavelength components.

**Solution:**

Dividing both sides of the equation by $k$ leaves us with 

$$\frac{\oo}{k}=ak$$

where we can recognize that $\frac{\oo}{t}=\cw$, thus:

$$\cw = ak.$$

The velocity of propagation is determined by the wavenumber $k$, multiplied by some constant $a$, which we can see now must have units of $\text{m}^2\text{ s}^{-1}$, as $k$ has units of inverse length. Replacing $k$ by $\frac{2\pi}{\ll}$, we have

$$\cw = \frac{2\pi a}{\ll}$$

With the equation in this form, it can be seen that $\cw$ is inversely proportional to $\ll$ - the higher the $\ll$, the smaller the velocity, and vice versa. 

***

## **Calculation Questions:**

1) A displacement wave on a string is described by $0.02 sin [2π(0.5x − 10t)]$ (m), where $x$ is in meters and $t$ in seconds. Find:
	- the propagation velocity $\cw$
	- the wavelength $\ll$ and wavenumber $k$
	- the frequency $\nu$ and angular frequency $\oo$
	- direction of propagation
	- amplitude $A$ of the wave




**Solution:**

Put the given expression in the form: $$f(x,t) = A\sin(kx-\oo t)$$ By multiplying the factor of $2\pi$ into the brackets, we have:
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
5.  The speed of electromagnetic waves in free space is $3 × 10^8\text{ [m/s]}$. An AM radio station uses a frequency of $540 \text{ kHz}$. Find the wavelength $\ll$. (AM =  amplitude modulation.)


**Solution:**

 Frequency, wavelength, and propagation velocity are related in the following way:
$$\cw = \nu \ll \implies \ll = \frac{\cw}{\nu}$$

...where $\cw$ is simply the speed of light, $299,792,458\text{ m/s}$, and the frequency was given as $540\text{ kHz}$, or $540\times10^3$ cycles per second. Thus, the wavelength is

$$\ll = \frac{\cw}{\nu} = \frac{299,792,458\text{ m/s}}{540\times10^3 \text{ s}^{-1}} = 555.17 \text{ m}.$$

***
7. Find the wavelength of wavy groove structure on an LP record (33 1/3 rev/min) for a sound wave with a frequency 1 kHz. Consider two radial positions on the record, $r =$(a) $15\text{ cm}$ , and (b) $10 \text{ cm}$.

**Solution:**

6. The wavelength $\ll$ is equal to 
$$\ll = \frac{\cw}{\nu}$$


...and we know the associated frequency is $1$ kHz, or 1000 cycles per second. Thus to give units of length for the wavelength, $\cw$ must have the dimension of velocity, as expected. However, this is not the velocity of the resultant sound wave, as in empty space this velocity will be constant, and not dependent on the distance of the point on the record from the center. We can utilize the given frequency of revolution and the distances $r$ given to find the velocity term for the record:

With a frequency of $33\frac{1}{3}$ revolutions per minute, corresponding to $\frac{33\frac{1}{3}\text{ revolutions}}{60s} = \frac{5}{9}$ revolutions per second, the point $r(a)$ travels a distance $2\pi r = 2\pi(0.15)$ meters. The product of these gives a velocity term:

$$\cw = 2\pi (0.15)\text{ m} \left(\frac{5}{9\text{ s}}\right) = 0.523599\text{ m/s}.$$

Dividing this by the given frequency $\nu = 1000\text{ Hz}$ as in the expression above yields a value for $\ll_1$:

$$\ll_1 = \frac{\cw}{\nu} = \frac{0.523599\text{ m/s}}{1000\text{ s}^{-1}} = 0.5236\times10^{-3}\text{ m}.$$

Following an identical calculation with the second point $r(b)=0.1$ m, we have:
$$\ll_2 = \frac{\cw}{\nu} =  \frac{2\pi (0.1)\text{ m} \left(\frac{5}{9\text{ s}}\right)}{1000 \text{ s}^{-1}} = 0.3491\times10^{-3}\text{ m}.$$

***
7. Calculate $$\pdv{f}{x}, \ \pdv{f}{y}, \ \pdv[2]{f}{x}, \ \pdv[2]{f}{y},\pdv{f}{x}{y}$$ for the following functions:
	- $f(x,y)=\sin(x-2y)$
	- $f(x,y)=x^2+xy+y^2$

**Solution:**
This question is fairly straightforward partial differentiation:


For the function $f(x,y) = \sin(x-2y)$, we have the following first partial derivatives:

$$
\begin{align}
f_x = \pdv{f}{x}&=\cos(x-2y)(1) =\cos(x-2y) \\
\\
f_y = \pdv{f}{y} &= \cos(x-2y)(-2) = -2\cos(x-2y)

\end{align}
$$

.....and the following second partial derivatives:

$$
\begin{align}
f_{xx} = \pdv{f_x}{x}&=-\sin(x-2y)(1) =-\sin(x-2y) \\
\\
f_{yy} = \pdv{f_y}{y} &= -(-2\sin(x-2y)(-2) = -4\sin(x-2y) \\ 

\\

f_{yx} = \pdv{f}{x}{y} = \pdv{f_y}{x} &= 2\sin(x-2y)

\end{align}
$$

For the second function, $f(x,y)=x^2 + xy + y^2$, we have:


$$
\begin{align}
f_x &= 2x+y \\
f_y &= 2y + x \\

\\
f_{xx} &= 2 \\
f_{yy} &= 2 \\ 

\\ 

f_{xy} = f_{yx} &= 1



\end{align}
$$
***
11) Add two sinusoidal waves $$2\sin(5x-1500t)\text{ and }2\sin(5.1x-1530t).$$ What is the *beat frequency*? What is the *beat wavelength*? 

**Solution:**

For the first sinusoidal wave $f(x,t)= 2\sin(5x-1500t)$, we have $\oo_1 = 1500$ and thus $\nu_1 = \frac{\oo}{2\pi} = \frac{750}{\pi}$. For the second, $f(x,t)= 2\sin(5.1x-1530t)$, $\oo_2 = 1530 \implies \nu_2 = \frac{765}{\pi}$.

The beat frequency can be found by the magnitude of the difference of these two frequencies: 

$$\Delta\nu = |\nu_2-\nu_1| = \frac{15}{\pi} = 4.77\text{ Hz}.$$

The beat wavelength can be found similarly from the difference between the values of $k$. Since $k_1=5$ and $k_2 = 5.1$, we have $\DD k = 0.1.$ The beat wavelength is then found as 

$$\ll =\frac{2\pi}{\DD k} =  \frac{2\pi}{0.1} =62.8319\text{ m.} $$

***
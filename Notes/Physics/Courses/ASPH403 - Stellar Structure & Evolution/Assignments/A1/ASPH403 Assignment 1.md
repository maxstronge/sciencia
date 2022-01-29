# Homework Assignment #1
### ASPH403
### Jan 31, 2022
***

#### 1. 
Extremely broadband spectroscopy of a star with a measured parallax of 130.208 mas (milli-arcseconds) yields the Black Body spectrum pictured below. Integrating this function (i.e. finding the area under the curve) yields a total (i.e. bolometric) flux of $2.317185\times10^{-8} \ W \ m^{-2}$. Using this information, calculate the *Luminosity* (in $W$ and $L_\Sun$), *Temperature* (in $K$ and $T_\Sun$) , and *Radius* (in $m$ and $R_\Sun$) of this star.

Use the following constants:
- $L_\Sun =  3.828 \times 10^{26} \ W$
- $T_\Sun = 5772 \ K$
- $R_\Sun = 6.963 \times 10^8 \ m$

![[Pasted image 20220128154935.png]]

**Solution**: 

First, we can use the given parallax to find the distance to the star:

$$D \ [pc] = \frac{1}{p \ ["]} = \frac{1}{130.208\times 10^{-3}} = 7.68002 \text{ pc}.$$

We can find the surface temperature from the peak wavelength on the above figure using Wien's law. The peak intensity occurs at $\ll_{\text{peak}}=300\text{ nm}$, so:


$$\ll_{\text{peak}} = \frac{2.898\times10^{-3}\text{ K $\cdot$ m}}{T} \implies T = \frac{2.898\times10^{-3}\text{ K $\cdot$ m}}{300\times 10^{-9}\text{ m}}  ...$$

>$$=9660\text{ K}.$$

In units of $T_\Sun$:

> $$\frac{T}{T_\Sun}=\frac{9660}{5772} = 1.6736 \ T_\Sun.$$

With the distance given from the parallax and the bolometric flux, we can find the luminosity:

$$\begin{align} F_{\text{bol}} = \frac{L}{4 \pi D^2}&\implies L = F_{\text{bol}}   \qty(4 \pi D^2)\\ &= 2.317185\times10^{-8}\text{ W m}^{-2} \cdot \qty(4\pi(7.68002\text{ pc})^2) \\ &= 2.31715\times10^{-8} \qty(4\pi)\qty(5.6198\times10^{34}\text{ m}^2) \end{align} $$

> $$ = 1.6353 \times 10^{28}\text{ W}. $$

In units of $L_\Sun$:

>$$\frac{L}{L_\Sun} = \frac{1.6353 \times 10^{28}}{3.828 \times 10^{26}} = 42.7193 \ L_\Sun.$$

We can find the surface flux using the temperature found earlier via the following relation:

$$F_{\text{surface}}=\sigma \ T^4 = 5.67037\times10^{-8} (9660)^4 = 4.93765 \times 10^8 \text{ Wm}^{-2}.$$

And finally, we can find the radius of the star using the surface flux and the luminosity:

$$F_{\text{ surface}} = \frac{L}{4\pi R^2} \implies R = \sqrt{\frac{L}{4 \pi F_{\text{ surface}}}}.$$

$$= \sqrt{\frac{1.6353 \times 10^{28} }{4\pi \qty(4.93765 \times 10^8 )}}$$

>$$= 1.62343\times10^9\text{ m.}$$

In units of $R_\Sun$:


$$\frac{R}{R_\Sun}=\frac{2.53956\times10^9}{6.963 \times 10^8} $$

> $$= 2.33151 \ R_\Sun.$$

***

#### 2.

The density of a star is bounded by 2 constraints: the density at the center $(r=0)$ is a *constant* denoted by $\rho(0)=\rho_c$, and the density at the surface $(r=R)$ is $\rho(R)=0$. The equation connecting the two limits is: 

$$\rho(R) = \rho_c \left[ 1- \left(\frac{r}{R}\right)^2 \right]$$

**a)** Derive an equation for the central density of a star as a function of the total mass $M$ and radius $R$, and calculate the central density of the sun. By way of comparison, the atmospheric density at sea level on Earth is $\approx 1.2 \ kg/m^3$. Also, prove that the average density of a star is given by $\overline{\rho}=0.4\rho_c$.

**Solution:**

We can relate a mass element $dm$ to a radius element $dr$ via the following equation:

$$\begin{align}dm &= 4\pi r^2 \rho \ dr \\[2ex] \int_0^M dm &= 4\pi \int_0^R r^2 \rho \ dr \end{align}$$

Since $\rho$ is not constant but varies with radius according to $\rho(r)$, so we can replace that term in the integrand (noting that the integral on the left is the total mass):

$$\begin{align}  \int_0^M dm &= 4\pi \int_0^R r^2 \rho(r) \ dr \\[2ex] M &= 4\pi \int_0^Rr^2\left( \rho_c \left(1-\frac{r^2}{R^2}  \right) \right) \ dr \\[2ex] M &= 4\pi \int_0^R\left( r^2 \rho_c \left( 1-\frac{r^2}{R^2}\right) \right) \ dr \\[2ex] M &= 4\pi \int_0^R\left( r^2\rho_c-\frac{r^4\rho_c}{R^2}\right) \ dr\end{align}$$

Since $\rho_c$ is a constant, we can pull it out of the integral:

$$\begin{align}  M &= 4\pi \rho_c \int_0^R\left( r^2-\frac{r^4}{R^2}\right) \ dr \\[2ex] M &= 4\pi \rho_c \left(\int_0^R r^2 \ dr - \int_0^R \frac{r^4}{R^2} \ dr\right) \\[2ex] M &= 4 \pi \rho_c \left(\frac{R^3}{3} - \frac{R^3}{5}\right) \\[2ex] M&= 4 \pi\rho_c \left(\frac{2R^3}{15}\right)\end{align}$$

We can solve this equation for the central density $\rho_c:$

$$\begin{align}M&= 4 \pi\rho_c \left(\frac{2R^3}{15}\right) \\[2ex] \frac{M}{4\pi} &=\frac{2R^3}{15}\rho_c \dots \end{align}$$

>  $$\rho_c = \frac{15M}{8\pi R^3}.$$

Using $R_\Sun = 6.963 \times 10^8 \ m$ and $M_\Sun = 1.99\times 10^{30} \ kg$, we can find the central density of the Sun:

> $$\rho_{c_\Sun} = \frac{15M_\Sun}{8\pi R_\Sun^3} = \frac{15(1.99\times 10^{30} \ kg)}{8\pi (6.963 \times 10^8 \ m)^3} = 2518.16 \ \frac{kg}{m^3}.$$

This density is $\sim 2930$ times greater than the sea-level atmospheric density on Earth. 

The average density $\bar{\rho}$ is defined as the total mass divided by the total volume:

$$\bar{\rho} = \frac{M}{V} = \frac{M}{\frac{4}{3}\pi R^3}.$$

The total mass $M = m(R) = 4 \pi \rho_c \frac{2 R^3}{15}$, according to the $dm$-$dr$ relationship used earlier. Replacing $M$ in the numerator by $m(R)$:

>$$\bar{\rho} = \frac{M}{V} = \frac{4\pi \rho_c \frac{2R^3}{15}}{\frac{4}{3}\pi R^3} = \frac{6}{15} \rho_c = 0.4 \rho_c.$$

**b)** Derive an equation for the central pressure of a star in terms of its total mass $M$ and radius $R$, and calculate the central pressure of the sun. By way of comparison, the atmospheric pressure at sea level on Earth is $\approx 10^5 \ N/m^2$.





***

#### 3. 
**a)** Using the same density profile as in Q2, prove that the potential energy of a star is given by:

$$PE = -\aa \frac{GM^2}{R}\text{, where }\aa = 0.71.$$

**b)** In the absence of nuclear energy, a star radiates energy solely via gravitational contraction; changing its size from $r=R_0$ at time $t=0$ to $r=R$ at some time $t$. In the case of pure gravitational contraction, the rate of change of a star's total energy is simply the change in internal energy $U=-PE/2$, which is related to the luminosity:

$$\dv{E}{t} = - \dv{U}{t} = \dv{(PE/2)}{t}=-L.$$

Under these conditions, derive an equation for the rate of contraction of the star's radius (*i.e*. $\dot{R}=\dv{R}{t}$) in terms of the star's initial radius $R_0$, the time $t$, and the characteristic timescale for thermal collapse $\tau$ (also called the *Kelvin-Helmholtz timescale*). If the Sun were generating its energy in this fashion, as Kelvin & Helmholtz thought, calculate the Sun's rate of collapse at time $t=0$. Also calculate the size of the Sun at time $t=\tau$ (*i.e.* after it has converted all its gravitational potential energy to luminosity).


***

#### 4.

**a)** Suppose you have the following fictional nuclear reactions that:

- Create element $W$:
	-  $A+A\to W\qq{}\text{Reaction Rate }=R_{AAW}\text{ (m}^3\text{s}^{-1})$
	-   $B+C\to W+F\qq{}\text{Reaction Rate }=R_{BCW}\text{ (m}^3\text{s}^{-1})$
- Destroy element $W$:
	- $W+D\to A+B\qq{}\text{Reaction Rate }=R_{WDA}\text{ (m}^3\text{s}^{-1})$
	- $W+E\to B+B\qq{}\text{Reaction Rate }=R_{WEB}\text{ (m}^3\text{s}^{-1})$

Write an expression that determines the rate of change of the number density (*i.e.* $n_W$ in $m^{-3}$) of element $W$ and for the mass fraction $\bf{X}_W$ of element $W$ in terms of the number density/mass fraction of the other elements and reaction rates. 

**b)** The proton-proton chain drives most of the nuclear processes in the Sun. It can be described by the following reactions (and rates at $T=1.5\times10^7 \ K$):

$$\begin{align}
p + p \to D + e^+ + \nu \qq{}&\text{Reaction Rate }= R_1 \sim 1.2\times10^{-49} \ (m^{-3}s^{-1})\\[1ex]
p + D \to \  ^3{He}\qq{}&\text{Reaction Rate }= R_2 \sim 3.1\times10^{-34} \ (m^{-3}s^{-1}) \\[1ex]
^3He + ^3He \to \  ^4{He}+p+p\qq{}&\text{Reaction Rate }= R_3 \sim 3.2\times10^{-45} \ (m^{-3}s^{-1})
\end{align}$$

Where $p$ is a proton, $e^+$ is a positron, $\nu$ is a neutrino, $D$ is a deuterium atom $( ^2H)$, $^3He$ is an isotope of helium, and $^4He$ is a normal helium atom.

Derive an equation that determines the time dependence of $n_D$ (*i.e.* the number density of $D$ at any time). You may use the boundary condition $n_D=0$ at $t=0$ to find the constant of integration. Calculate $n_D$ in the Sun after $10^9$ years of fusion. You may use $n_p=\text{constant}\approx2.1\times10^{30} \ m^{-3}$ in the Sun's core. 

***
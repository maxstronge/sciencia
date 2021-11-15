# The Hydrogen Atom:
***

The hydrogen atom is the simplest atom, consisting of a single proton and an electron. According to the [[6.5 - The Bohr Model|Bohr Model]], the electron orbits the proton in a circular orbit - despite the fact that it is not an accurate representation of reality, this model can be used to derive some important properties of the hydrogen atom.

Bohr's first postulate says that the *angular momentum* of the electron must be an *integer multiple* of $\hbar$:

> ### $$mvr = n\hbar $$
> ...where:
> - $m =$ mass of electron
> - $v =$ speed of electron
> - $r =$ radius of electron's orbit
> - $n =$ the principal quantum number ($n=1,2,3\dots$)
> - $\hbar =\frac{h}{2\pi}$ 
> - $h =$ the Planck constant $=6.63 \times 10^{-34}J\,s$  

^0c4449

The quantum mechanical interpretation of Bohr's first postulate is obvious: the electron is represented as a *standing wave*, and the 'length of the orbit' must be an integer multiple of the **de Broglie wavelength**:

> ### $$\ll = \frac{\hbar}{p} = \frac{\hbar}{mv}.$$


A charged particle in a circular orbit (thus, in accelerated motion) should emit electromagnetic radiation as it orbits, losing energy, if it obeyed the laws of classical electrodynamics. This would cause the electron to rapidly spiral down towards the nucleus, and the atom would collapse. Obviously, this does not occur, so we must accept Bohr's second postulate: *an electron moving in an **allowed** orbit around a nucleus does **not** radiate*.

Radiation is emitted only when the electron jumps from a higher-energy state to a lower-energy state. The emitted quantum has an energy $hv$ equal to the *energy difference* of these two states:

> ### $$hv=E_{n_2}-E_{n_1}.$$

^e12e79

We can now find the energy of an electron in the state $E_n$. [[22.4 - Coulomb's Law|Coulomb's Law]] gives the force of attraction between electron and proton:

>$$F_{\text{Coulomb}}= \frac{1}{4\pi\epsilon_0}\frac{e^2}{r_n^2}$$
>...where:
>- $\epsilon_0 =$ the *permittivity of free space* = $8.85\times10^{-12}N^{-1}m^{-2}C^2$,
>- $e =$ the charge of the electron $= 1.6 \times10^{-19}\,C$,
>- $r_n =$ the distance between electron and proton.

The acceleration of a particle moving in a circular orbit of radius $r_n$ is given by:

$$a = \frac{v_n^2}{r_n}$$

and, applying Newton's 2nd, we find:

> ###   $$\frac{m\,v^2_n}{r_n} =\frac{1}{4\pi\epsilon_0}\frac{e^2}{r_n^2}. $$ ^8c7d62
  
  From the two [[#^0c4449|above]] [[#^8c7d62|two]] equations, we can find:
  
  > #### $$v_n = \frac{e^2}{4\pi \epsilon_0	\hbar}\frac{1}{n},\qq{}r_n =  \frac{4\pi \epsilon_0\hbar^2}{me^2}n^2.$$


The total energy of the electron in orbit $n$ is then:


> $$\begin{align}E_n = T+V &= \frac{1}{2}mv^2_n - \frac{1}{4\pi\epsilon_0}\frac{e^2}{r_n} \\[2ex] &= - \frac{me^4}{32\pi^2\epsilon_0^2 \hbar^2} \frac{1}{n^2} \\[2ex] &= -C\frac{1}{n^2}  \end{align}$$...where $C$ is a constant. 

From this, we can find the energy for the *ground state* $(n=1)$:

$$E_1 = -C \frac{1}{(1)^2} = -2.18\times10^{-18}J = -13.6\,eV.$$

From this and our [[#^e12e79|previous equation re: energy transitions]], we can find the energy of the quantum emitted in the transition $E_{n_2}\to E_{n_1}$:

$$hv = E_{n_2} -  E_{n_1} = C\qty(\frac{1}{n^2_1}-\frac{1}{n^2_2}).$$

We can express this in terms of wavelength as follows:

> ##### $$\frac{1}{\ll}=\frac{v}{c}=\frac{C}{hc} \qty(\frac{1}{n^2_1}-\frac{1}{n^2_2}) \equiv R\,\qty(\frac{1}{n^2_1}-\frac{1}{n^2_2})$$
> ...where $R$ is the **Rydberg Constant**, $R =1.097\times10^7 m^{-1}.$



***

#physics #modern_physics #astrophysics #hydrogen #atom #bohr_model #planck #balmer_series #spectroscopy #wavelength #rydberg_constant
#spectral_lines #radiation

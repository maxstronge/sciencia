# PHYS375 Homework 7
### Max Stronge (30064749)

***

1. Quantum mechanics states that all bound systems must have discrete (quantized) energy levels. Bound electrons in a solid (metal or non-conductor) are said to have a continuous band of energies that they can exist at.
		a) Explain this apparent discrepancy in terms of the wave nature of the electrons.
		b) What’s different between the waves of the electrons in metals and the electron waves in non-conductors?


**Answers:**

**a)** There is no contradiction here - the allowable energy levels of an electron are indeed quantized. However, when two atoms come close together, they interect electromagnetically, and the allowable energy levels are affected by this interaction. When two atoms come together to form a molecule, their wavefunctions interfere with each other and *hybridization* occurs, creating a new shape for the orbitals in much the same way that waves can interfere to form new waves. There may be nodes in the combined wavefunction that are not present in each individual atom. 

If we were to start with two identical atoms at the lowest energy level and bring them together, the result would have two states with two different energy levels (because confining an electron, even to the small extent of introducing a node in the wavefunction, increases the energy of a state). Adding another atom would yield 3 states with 3 different energy levels, and if one continues doing this to the point where we have a solid comprised of a number of particles far in excess of Avogadro's number, $10^{23}$, one can see that the amount of allowable energy levels would grow so large that the band would appear continuous. 

(Apparently it actually *does* become continuous in extreme situations, such as the core of a star). 

**b)** The difference between these situations stems from the difference in the electronic configurations of conductors and insulators. The following diagram illustrates the results:


[![bands](https://i.stack.imgur.com/Z8DXm.gif)](https://i.stack.imgur.com/Z8DXm.gif)


In an insulator, there is a large 'forbidden' gap between the energies of the electrons in the valence shell and the energy at which electrons can move freely through the solid (called the conduction band). 

In a conductor, on the other hand, the conduction and valence bands overlap, allowing at least a portion of the valence electrons to move freely through the metal - no energy gap separates them. 

***

2. Figure 5 from your lab (see below) gives an overview of what happens when light is incident on a diffraction grating. Please derive Equation 6 in your lab:

$$d\sin\th = m \ll, m = 0, \pm 1, \pm 2,...$$

**Solution**:

Consider the following experimental setup:


Given on the assignment:
![[Pasted image 20221101165817.png]]


Another image that gives a clearer image of the geometric situation as light passes through the slits:

![[iedzzy32.bmp]]

Imagine a stream of parallel rays of monochromatic light (*i.e.* all of the same wavelength $\ll$) that is incident on a diffraction grating with slit separation $d$. The distance $L$ to the screen, $L$, is large enough that the rays can be considered parallel. 

Consider two adjacent rays that are parallel after going through the grating. From the geometry of the situation depicted above, we can note that the difference in path length is dependent on the angle $\th$ made with the optical axis. As can be seen, the path length is the segment $\overline{\text{AC}}$, which is found via trigonometry:

$$\overline{\text{AC}}=d\sin\th$$

In order to interfere constructively, as is observed experimentally when light passes through the diffraction grating, the two adjacent beams of light emerging from the points A and B in the figure above must be in phase with each other - this will occur when the difference in path length between the two is an *integer multiple* of the wavelength. So we can set the equivalence 

$$d\sin\th = m \ll, m\in\mathbb{I}. $$


***
3. A police car has a siren of a frequency of $800$ Hz and approaches a car going in the same direction (both going east). The velocity of the police car is $140$ km/hr (east) and that of the car $100$ km/hr (east). Assume that the air is still.
	a) What frequency does the car driver hear before the police car passes the car?
	b) What frequency does the car driver hear after the police car passes the car?
	c) What frequency would the car hear if it were going the opposite direction at $100$ km/hr (west, and the police car was still going at $140$ km/hr east).


**Solutions:**

**a)** The general expression for a Doppler-shifted frequency is 

$$\nu'=\frac{c_s-u_0}{c_s-u_s}\nu_0$$
The police car has a velocity of $40\text{ km/h}=11.11\text{ m/s}$  East relative to the observer car - if we fix an inertial reference frame inside the observer car, the situation is the same as that of a moving sound source with a stationary observer.  Thus $u_0=0$ and the expression reduces to 

$$\nu' = \frac{c_s}{c_s-u_s}$$

Here, $\nu_0=800\text{ Hz}$ is the unshifted frequency, $c_s$ is the speed of the sound waves, which we will take as $343$ m\s, and $u_s=40\text{m/s}$ is the relative velocity of the sound source to the observer. By convention, velocities are positive if they are in the same direction as $c_s$, which is true in this first case. Therefore,

$$\nu' = \frac{343\text{m/s}}{(343-11.11)\text{m/s}}(800\text{ Hz}) = 826.78\text{ Hz}.$$


**b)** This time, the situation is the same, but $c_s$ and $u_s$ are now in opposite directions, as the police car is in front of the observer car. We can use the same calculation, flipping the sign:

$$\nu' = \frac{343\text{m/s}}{(343+11.11)\text{m/s}}(800\text{ Hz}) = 774.9\text{ Hz}.$$

**c)** We will keep our inertial frame fixed in the observer car such that it is at rest in that frame. Now, the relative velocity of the police car is $240\text{km/h} = 66.6667\text{m/s}$. Assuming the police car is in front of the observer car, approaching it, we have 

$$\nu' =  \frac{343\text{m/s}}{(343-66.66)\text{m/s}}(800\text{ Hz})=993.004\text{ Hz}.$$

When the police car passes the observer car, the sound velocity and source velocity are now in opposite directions, so we have 

$$\nu' =  \frac{343\text{m/s}}{(343+66.66)\text{m/s}}(800\text{ Hz})=669.813\text{ Hz}.$$

***

4. Doppler Shifting for Light:
	**a)** If a relative velocity $u$ between the source of electromagnetic waves and an observer is ufficiently smaller than the speed of light (which is an electromagnetic wave) $c = 3.0\times10^8$  m/s, the Doppler-shifted frequency is given by $\nu'=\frac{c}{c-u}\nu_0$, where $u>0$ when the source and observer are approaching each other, and $u<0$ when receding. When microwaves with a frequency $4.0\times10^9$ Hz are reflected from a jet fighter, the frequency is changed by $10$ kHz. What is the speed of the plane?
	
	**b)** The exact formula for Doppler-shifted frequencies of electromagnetic waves is $\nu'=\frac{\sqrt{1-(\frac{v}{c})^2}}{1-\frac{v}{c}}\nu_0 = \frac{\sqrt{1-\bb}}{1-\bb}\nu_0$. If starlight, which would normally have a wavelength of $550$ nm, is observed with a wavelength of $650$ nm, what's the speed of the star relative to Earth? Is it approaching or receding?
	
	**c)** At what speed would the approximate formula yield a $1\%$ difference from the actual formula?


**Solutions:**

>**NB: c=$299,792,458\text{ m/s}$ was used for all calculations involving c.**

**a)** Inserting our known values into the Doppler shift formula for electromagnetic waves:

$$\nu' = \frac{c}{c-u}\nu_0 \implies 4.000010000\times 10^9 = \frac{c}{c-u}4.0\times10^9$$


$$c-u=c\frac{4.0\times10^9}{4.000010000\times 10^9}$$

$$c-c\frac{4.0\times10^9}{4.000010000\times 10^9}=u$$

$$c(1-\frac{4.0\times10^9}{4.000010000\times 10^9}) = u$$

$$u=749.5 \text{m/s, relative to the observer}.$$

Since this speed is not an appreciable fraction of $c$, the nonrelativistic equation is a suitable approximation.

**b)** For the starlight:

$$\frac{c}{650} = \frac{\sqrt{1-(\frac{v}{c})^2}}{1-\frac{v}{c}}\frac{c}{550}$$


This was solved numerically for $v$ in Mathematica with the following code snippet:

![[Pasted image 20221101203702.png]]

So the relative velocity of the star to Earth is $4.96208 \times 10^7 \text{ m/s}$. Since the observed wavelength is longer than the natural one, we can conclude that the light is redshifted, and the star is moving away from Earth. This is nicely verified by the negative sign in the velocity, due to the positive convention discussed earlier. 

**c)** For percent error, we can set up the ratio

$$\frac{\text{approximation}- \text{relativistic}}{\text{approximation}}=0.01$$

$$\frac{\frac{c}{c-v}-\frac{\sqrt{1-(\frac{v}{c})^2}}{1-\frac{v}{c}} }{\frac{c}{c-v}}=0.01$$

Solving this numerically once again yields the velocities at which the error is exactly 1%:

![[Pasted image 20221101210043.png]]

So the speed at which the approximation has an error of 1% is $4.33909 \times 10^7 \text{ m/s}$, or $\approx0.141c$. 

***


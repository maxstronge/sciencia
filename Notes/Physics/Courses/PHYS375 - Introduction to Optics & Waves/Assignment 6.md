# PHYS375 Assignment 6:
### Max Stronge (30064749)
***

1. The second thickest guitar string (the A string) vibrates at $110$ Hz. We call this $A_2.$ The distance between the  
saddle and the nut is $61$ cm (it varies from guitar to guitar, but this is the length we’ll take for this problem and is the length the strings vibrate). The tension in the string is $97$ N.

- a) Explain why this is or isn't consistent with the statement that I made in class that music in Canada tends to be based on $A$ being 440 Hz.
- b) What is the wave speed and mass density of the guitar string?
- c) When tuning a guitar, we adjust the tension in the strings to have the right ratio of frequencies. The next thickest string (the $D$ string) is a perfect $4^\text{th}$ higher in pitch. We hold down the ‘fifth fret’ to make the $A$ string play the same note as the $D$ string. What’s the distance from the ‘nut’ to the $5^\text{th}$ fret on this guitar?
- d) Given that the $D$ string *also* has a tension of $97$N, what's the mass density of the $D$ string?
- e) We can damp out the fundamental frequency of a string by lightly touching the string over the $12^\text{th}$ fret (the halfway point for the string). How much higher will that note sound? We can do the same thing at the $7^\text{th}$ fret (the $2/3$ and $1/3$ point on the string) and the $5^\text{th}$ fret (see earlier question for this ratio). How much higher will that note sound? Show that lightly touching the $7^\text{th}$ fret on the $D$ string will produce the same pitch as lightly touching the $5^\text{th}$ string on the $A$ string (another way to tune the guitar).



**Solutions:**

- a) This is perfectly consistent - since doubling or halving a frequency corresponds to an octave, $440$ Hz and $110$ Hz both correspond to the note $A$. The guitar string's $A$, $A_2$, is simply two octaves down from the $A$ used to tune instruments in Canada.
- Thank you for sending me down the rabbit hole of the $440$ Hz convention, that was an interesting read. 


- b) With $A_2 = 110\text{ Hz, } L = 0.61\text{ m, }T = 97\text{ N}$, we have the following relations for the fundamental mode of a standing wave on a string:

$$L=\frac{\ll_1}{2} \implies \ll_1 = 2L$$

$$c_w = \ll \nu = (2L)(A_2) = 2(0.61)(11) = 134.2\text{ m/s}.$$

We can find the mass density by examining the tension - since $c_w = \sqrt{\frac{T}{\rho_l}}$, we have

$$\rho_l = \frac{T}{c_w^2} = \frac{97}{134.2^2} = 5.366\times 10^{-3}\text{ kg/m.}$$

c) An increase in pitch of one perfect fourth corresponds to multiplying the frequency by $4/3$, so holding down the fifth fret on the $A$ string produces a frequency $\frac{440}{3}$ Hz when plucked. Since the wave velocity will remain the same, we have

$$\nu = \frac{c_w}{\ll} \implies \ll = 134.2 \left(\frac{3}{440}\right) = 0.915\text{ m} $$

And since the string is still in the fundamental mode, we can find the new length from the nut to the 5th fret:

$$L = \frac{\ll}{2} = 0.5475\text{ m}.$$

d) The length of the $D$ string is the same as that of the $A$ string, so the fundamental wavelength is the same, $\ll_D = 1.22$ m. Thus:


$$cw_D = \ll_D\nu_D = 1.22\left(  \frac{440}{3}\right) = 187.933\text{ m/s}.$$

We can again use the relation between tension, velocity, and mass density to find the mass density for this string:

$$\rho_l = \frac{T}{c_w^2}=3.03\times10^{-3}\text{ kg/m}. $$

- e) The following diagram illustrates the situation: 
- ![[472f86d937d237c9c904665e6d804abe.png]]

 Lightly touching the string at various points has the effect of creating nodes in the standing wave of the string. Touching the 12th fret, at the center of the string, will create the 2nd harmonic, corresponding to a doubling of the frequency. Thus, the note produced by lightly touching the 12th fret will be exactly one octave higher than playing the $A$ string unfretted, if the finger is placed exactly on the node. We can check this mathematically:
 
 $$\nu_n = \frac{n c_w}{2L}$$
 
 ...which should hold for each $n$, gives us the following for the fundamental frequency:
 
 $$\nu_1 = \frac{c_w}{2L} = \frac{c_w}{\ll}$$
 
 as we found earlier. The second harmonic should then have the frequency $$\nu_2 = 2\frac{c_w}{2L} = \frac{c_w}{L} = 2\nu_1.$$
 
 The second harmonic is one octave higher than the fundamental frequency. 
 
 Placing a finger at the 7th fret produces the third harmonic, for which the frequency is 
 
 $$\nu_3 = \frac{3c_w}{2L} = \frac{3}{2}\nu_2$$
 
 which corresponds to one perfect fifth above the second harmonic.
 
 A finger at the 5th fret produces the fourth harmonic, with nodes at the 12th and 24th frets. Following similar logic, we find:
 
 $$\nu_4 = \frac{4c_w}{2L}=2\frac{c_w}{L}=2\nu_2 = 4\nu_1$$

which brings us up to one octave above the second harmonic, or two octaves above the first. 





***

2. In a previous homework, we showed that the wave equation for two-dimensional transverse waves on a membrane was

$$\pdv[2]{\xi}{t}=\frac{T}{\rho_s}\left( \pdv[2]{\xi}{x} + \pdv[2]{\xi}{y}\right)$$

with a wave speed $c_w = \sqrt{\frac{T}{\rho_s}}$, with particular solutions discussed previously.

- a) Please derive this transverse wave equation in two dimensions.
- b) In other physics classes you’ll have a mathematical tool called a Laplacian, usually (but not always) written as ∇ 2. The Laplacian is written differently in Cartesian, spherical and cylindrical coordinates. Rather than derive this wave equation in 3D, use your mathematical intuition to generalize the wave equation to Cartesian coordinates in 3D. Then look up the Laplacian in spherical and cylindrical coordinates to write the wave equation in 3D for those coordinate systems.
- c) Use the operator method to come up with an expression for the different resonant angular frequencies of a box (a rectangular prism) of dimensions $a \times b \times c$.


**Solution:**

Since the wave equation in 2d was derived last time, it is reproduced here for continuity:

![[Pasted image 20221026165746.png]]
![[Pasted image 20221026165837.png]]

- b) We can note that the term $(\pdv[2]{\xi}{x}+\pdv[2]{\xi}{y}$ is in fact the Laplacian for a two dimensional function, $\xi_{xx} + \xi_{yy}$. Intuitively, one would expect that in three dimensions, the expression would remain the same:

$$\xi_{tt}=\frac{T_\tau}{\rho_\tau}\laplacian \xi$$

$$\pdv[2]{\xi}{t}=\frac{T_\tau}{\rho_\tau}\left(\pdv[2]{\xi}{x} + \pdv[2]{\xi}{y} + \pdv[2]{\xi}{z} \right).$$

...where the $\tau$ subscript now indicates that the tension and mass density refer to volumes rather than surface elements. 

The Laplacian $\laplacian f(x,y,z)$ is given in Cartesian coordinates as   

$$\left(\pdv[2]{\xi}{x} + \pdv[2]{\xi}{y} + \pdv[2]{\xi}{z} \right)$$

In spherical polar coordinates, it is (unfortunately)

$$\laplacian f(r,\th, \phi) = \frac{1}{r^2} \pdv{r}(r^2 \pdv{f}{r}) + \frac{1}{r^2\sin\th} \pdv{\th}(\sin\th \pdv{f}{\th})+\frac{1}{r^2\sin^2\th}\pdv[2]{f}{\phi}$$

and so the wave equation is 

$$\pdv[2]{\xi}{t}=\frac{T_\tau}{\rho_\tau}\left(\frac{1}{r^2} \pdv{r}(r^2 \pdv{\xi}{r}) + \frac{1}{r^2\sin\th} \pdv{\th}(\sin\th \pdv{\xi}{\th})+\frac{1}{r^2\sin^2\th}\pdv[2]{\xi}{\phi} \right).$$

In cylindrical coordinates:

$$\laplacian f(r,\phi,z) = \frac{1}{r}\pdv{r}\left( r \pdv{f}{r}\right) + \frac{1}{r^2}\pdv[2]{f}{\phi} + \pdv[2]{f}{z}$$

and the wave equation becomes

$$\pdv[2]{\xi}{t}=\frac{T_\tau}{\rho_\tau}\left( \frac{1}{r}\pdv{r}\left( r \pdv{\xi}{r}\right) + \frac{1}{r^2}\pdv[2]{\xi}{\phi} + \pdv[2]{\xi}{z}\right).$$

***

3. A flute can be considered a cylinder with air vibrating.

- a) Under what conditions can we simplify our cylindrical wave equation from the previous problem down to the one-dimensional wave equation? Does this seem justified for the case of the flute?
- b) How long would the flute have to be to play $A_4=440$ Hz? Assume $20\degree$C, but this will change. 


**Solution:**


a) So long as the wave function can be written as $$\xi=\xi(x,t)$$ (*i.e.* the wave behavior is only dependent on the distance along the main axis of the cylinder, not on the polar or azimuthal angles) then the wave equation will reduce to one dimension, as proven in a previous assignment. 

***
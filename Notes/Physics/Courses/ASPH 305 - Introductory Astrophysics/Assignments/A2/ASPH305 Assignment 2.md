# ASPH305 Homework Assignment 2:

***
###  1:
The figure below shows the position of an asteroid as seen from telescope 1 (located in Calgary) and from telescope 2 (located $500km$ away from telescope 1). The observations were taken at the same time. 

![[a2picture1.png|Positions of asteroids measured by telescopes 1 and 2. ]]


##### a.)  Calculate the distance to the asteroid (in $AU$). You may ignore the curvature of the Earth and the exact latitude/longitude of each telescope. 


We can find the distance using the *parallactic angle formula*:

### $$p\,[\text{rads}] = \frac{d}{D}.$$

Rearranging:

### $$D = \frac{d}{p}. $$

The declination $\dd$  of the asteroid is the same as measured from each telescope - therefore, the *parallactic angle $p$* can be found from the difference between the measured values for *right ascension*:

### $$\begin{align} \aa_2 - \aa_1 &= 15^h\,10^m\,0.13^s - 15^h\,10^m\,0.0^s \\ &=0.13^s \\ &= 0.13^s \left(\frac{\pi}{43200}\text{ radians}\right) \\ &= 9.45387\times10^{-6}\text{ rad}.\end{align}$$

However, this is actually *twice* the parallactic angle, leaving us with:

### $$p = \frac{9.45387\times10^{-6}\text{ rad}}{2} = 4.72693\times10^{-6}\text{ rad.}$$

Now that we have the parallactic angle in radians, we need the baseline distance in units of $AU$ (recalling that the baseline is *half* the distance between the telescopes):

### $$250\,km = 1.33692\times10^{-6}\,AU. $$

We can now find the distance to the asteroid:

> ### $$D = \frac{d}{p} = \frac{1.33692\times10^{-6}\,AU}{4.72693\times10^{-6}} = 0.28283\,AU.$$

NASA identifies Potentially Hazardous Objects (PHOs) as near-Earth objects whose orbit brings them within ~0.05 $AU$ of Earth's orbit, so no cause for alarm yet. 

***
##### b.) At the time of the above observation, the asteroid is moving towards us with a velocity of $36.056\,km/s$ at an angle of $30\degree$ with respect to the line of sight (*i.e.* the vector between Earth and the asteroid). Calculate the radial and tangential velocity components (in $km/s$), and the proper motion that would be observed from Earth (in units of BOTH *"/yr* and *"/min*).

 A diagram to illustrate:
 
 ![[propermotiontangrad.svg]]
 
 	

From the figure we can form a triangle to determine the radial and tangential components of velocity:

![[propermotiontrig.svg]]

So the radial and tangential velocity components are:

> ### $$\va{v}_r = 31.2254\,km/s.$$
> ### $$\va{v}_t = 18.028\,km/s. $$

We can now find the proper motion with the following relation:

### $$\theta\text{ [rad]} = \frac{D\text{ (km)}}{r\text{ (km)}} $$

...where $\theta$ is the angle in radians through which the body moves in 1 second, $D$ is the distance in kilometers that the body moves in 1 second (tangential to the line of sight), and $r$ is the distance to the body (in km). We can now substitute our values for $D$ and $r$ (remembering to convert $AU$ to km):

 ### $$\begin{align} \theta &\text{ (rads)}= \frac{D}{r} \\[2ex] \theta &= \frac{18.028\text{ km}}{0.28283\,AU \cdot \qty(\frac{1.496 \times 10^8\text{ km}}{AU})} \\[2ex] \theta &= \frac{18.028\text{ km}}{4.23108 \times 10^7 \text{ km}} \\[2ex] \theta &= 4.26085 \times 10^{-7} \text{ rad}.\end{align} $$
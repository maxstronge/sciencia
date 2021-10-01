# Spherical Coordinate Systems:

Spherical coordinates are a much more natural coordinate system when dealing with the Earth and the sky above it (both of which can be modeled as spheres). 

A typical example of spherical coordinates on Earth is the longitude/latitude system. 

***
### The Equatorial System:

![[Pasted image 20210929110836.png]]

The **Equatorial Plane** is the reference plane for this coordinate system. It defines a latitude of $0\degree$ and is perpendicular to the rotational axis of the Earth through the center. 

**Parallels of latitude** are small circles that run parallel to the equator outwards to the poles (latitude $90\degree$). 

**NB:** When we refer to the poles in this coordinate system, we mean the **geographical** poles, not the magnetic ones (which vary slightly over time). The **Pole** is the intersection between the rotational axis and all the meridians of longitude. 

**Meridians** are great circles (semicircles) that connect the two poles.

**Longitude** is the angle between the meridian and the meridian of $0\degree$ (called the **prime meridian**, running through the Royal Observatory in Greenwich). Longitude is measured as positive numbers (angles) with a direction, East or West of Greenwich. 


This is a fixed coordinate system (does not depend on the location of the observer), and can also be used to describe celestial positions. 

The **Celestial Equator** is the projection of the equator onto the celestial sphere. 
***

### The Horizontal System:

Since our view of the sky depends on our geographical position on Earth, it turns out to be useful to define a coordinate system for the sky *based on our position on Earth*.

![[Pasted image 20210929111740.png]]

A key feature of the horizontal system is the **horizontal plane** - an approximation of the ground modeled as the tangent plane to the surface of the Earth at the location of the observer. 

The intersection of the horizontal plane and the celestial sphere is the **celestial horizon**. 

There are some other useful reference points in the horizontal system:

The **Zenith** is the point directly overhead of the observer (projection of the normal line to the horizontal plane at the location of the observer).

The opposite of the zenith is the **Nadir** - the antipodal point directly opposite the zenith on the celestial sphere. 

As mentioned before, the **meridian** in the horizontal coordinate system is the line that runs from the South to the North pole through the zenith. Local noon occurs when the Sun is on the meridian (which may not be directly overhead - just the highest point in the Sun's arc). 



![[Pasted image 20210929112311.png]]

With these important points and definition in mind, we can describe the position of any object in the sky with two (actually 3) coordinates: altitude and azimuth (and time of observation). 

**Altitude** is an angle describing the elevation of the object above the horizon, as measured by the observer. 

Alternately, the same coordinate can be described in terms of the **Zenith Angle**, which is the altitude as measured downwards from the zenith rather than upwards from the horizon. 

> ## $$\text{Zenith Angle} = 90\degree - \text{Altitude}$$

The second coordinate, the **Azimuth**, is the lateral position of the object along the horizon, measured clockwise from cardinal North (N->E).

A helpful feature of the horizontal system: the altitude of the **Northern Celestial Pole** is equal to the *latitude of the observer*. 


![[HorizontalSystemAltitudeOfPolarisGeometricalProof.svg]]


It is essential to note, however, that since the horizontal system is defined for a local position on Earth, the altitude and azimuth of an object will change as a function of time as the sky (*i.e.* the Earth) rotates. The horizontal system is **not** time-independent. So if we are recording the position of an object, just the altitude and azimuth are not sufficient - a time coordinate must also be specified. 


***


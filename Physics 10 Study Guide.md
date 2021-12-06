#### Key Equations:
***
- **Velocity** $=\vec{v} = \frac{\text{distance}}{\text{time}} = \frac{d}{t}$. Units of velocity are meters per second ($m/s$). Make sure to specify what direction! 
- **Acceleration** $= \va{a} = \frac{\text{velocity}}{\text{time}} = \frac{\va{v}}{t}$. Units of acceleration are meters per second per second, or meters per second squared ($m/s^2$ ).
- ** Kinetic Energy** $= E_k = \frac{1}{2}mv^2$, where $m$ is mass and $v$ is velocity. Units of energy are *Joules*, $J$, which are the same as $kg/m^2 s^2$ (but you probably don't need to know that)
- **Potential Energy** $= E_P = m \ g \ \Delta h$, where $m$ is mass, $g = 9.81$ is the acceleration of gravity, and $\Delta h$ is the height above the ground (because something that's high up has *potential* to fall further than something close to the ground).
- **Mechanical Energy** $= E_\text{mech} = E_k + E_P$. Only thing to know about mechanical energy is that it stays the same - in equation form, $\Delta E_{\text{mech}} = 0$ (the change in mechanical energy is zero). If something starts off with $5 \ J$ of mechanical energy, it has to end up with the same amount. 

***

### Velocity vs. Acceleration:

It can be tricky to tell these two apart sometimes. 

Velocity is how fast the position is changing - if the position is changing really fast, there's a high velocity.

Keep in mind that velocity is a *vector*, which is why we wrote the v with the arrow up above ($\va{v}$). Vectors like velocity need two things: a *magnitude*, and a *direction*. For velocity, the magnitude is the speed. You need both! If I'm running  $4 \ m/s$ North and you're running $4 \ m/s$ East, we do *not* have the same velocity, even though we have the same speed. 

Acceleration is how fast the *velocity* is changing (aka how much something is speeding up or slowing down). 

But because velocity is a vector, that has both speed and direction, velocity also changes when the *direction of motion* changes. And since velocity changes, that means the object is accelerating.

For example, if you're driving a car and you take a wide turn at a constant $50 \ km/h$, you're still accelerating, because you're constantly changing direction!

## **Graphs to Know**:
***

The key thing on these graphs: if there is any acceleration (*i.e.* any change in the velocity, either the speed or the direction), the motion is *non-uniform motion*. If there is *exactly* zero acceleration - the object is not speeding up, slowing down, or changing direction - then the motion is *uniform motion*.

### 1. Distance/Position vs. Time:

![](http://www.physicsclassroom.com/Class/1DKin/U1L3a5.gif)

When there's a straight line going up on position/distance vs time (position and distance mean the same thing here), it means that the velocity is *constant* - the object constantly moves at the same speed. Since there's no change in the velocity, there's no acceleration. Uniform motion.

![](http://www.physicsclassroom.com/Class/1DKin/U1L3a10.gif)

In this one, the distance is also increasing - but it's not increasing in a straight line, like the last one. Remember that the *slope* (or steepness) of the line on a distance vs. time graph represents the *velocity*. In the above, the line was straight, so it had a constant slope = constant velocity. The slope of this line is not constant - it gets more steep as it goes on. Therefore, the velocity increases as the line gets more steep, and because the velocity changes...non-uniform motion. 

**Summary**: On a distance vs. time graph....
- a straight line = constant velocity = no acceleration = uniform. 
- A curved line = non-constant velocity = acceleration = non-uniform.
-  Steeper lines = higher slope = faster velocity.


### 2. Velocity vs. Time:

These graphs have the velocity $\va{v}$ on the y-axis instead of the distance - make sure you always check what the y-axis is!!

![[Pasted image 20211129215655.png]]

It's helpful to keep slope in mind here, too. Just like how the slope of the distance vs. time graph is velocity...

...the slope of a *velocity vs. time* graph is *acceleration*. 

The line above has a slope of zero (since slope is rise over run, and the rise is 0). Therefore, there's zero acceleration - the motion is *uniform*. 

You could also determine this by carefully looking at the graph, and noticing that the velocity stays the same as time goes on. Since there's no change in velocity, the motion is uniform. 

![[Pasted image 20211129220020.png]]

On this one, clearly the velocity is changing over time (it's increasing). So right away we can say that the motion is *non-uniform*, and the object is accelerating.  You can also note that the red line has a positive *slope* (since it's going upwards), so there must be positive *acceleration*. 



You might see a graph that has some lines underneath the $x$-axis, like this:

![](http://www.physicsclassroom.com/Class/1DKin/U1L4a6.gif)

Don't let those trip you up - they mean the same thing!  Just look carefully at whether the velocity or distance is *increasing* with time or *decreasing*. Negative velocity is just velocity, but in the opposite direction. So if you start with a small negative velocity, like $-3 \ m/s$, and you end up with a more negative velocity, like $9 \ m/s$, you sped up, and you're going the opposite direction as if you had a positive velocity.

**Summary:**
For velocity vs. time graphs...

- straight horizontal flat line  = constant velocity = *uniform motion*
- any other straight line = non-constant velocity = *non-uniform motion*
- any curved lines = definitely not uniform motion.


***
## Significant Digits:
Pay super close attention to these - I didn't in high school and it seriously hurt me. You can be 100% confident on all the material, do everything else right, and still get a bad mark because you messed up your sigdigs. I've been there. Don't let it happen to you. 

##### How to tell what digits are significant:

1. Non-zero digits are always significant, no matter where they are in a number.
2. Any zeroes between two significant digits are also significant. 
3. If you're given a number that has zeros **after** the decimal place, *those zeroes are significant!* Otherwise they wouldn't be there. 
	
	- For example: $0.500$ has three sigdigs, while $0.5$ only has one. 
	- But if the zeroes are before the decimal place, like $0046.45$, those two zeroes are useless. Chuck 'em. 


##### Adding and Subtracting Significant Digits:

1. Count the number of sigdigs *after the decimal* of both numbers. Remember the number of whichever one has the least.
2. Add or subtract normally. 
3. The final answer **cannot** have more significant digits *after the decimal* than the number you remembered earlier. 

>For example:
>1. $12.3340 - 6.56$. Left number has 4 sigdigs after the decimal, right number has 2. So remember 2. 
>2. Doing the subtraction normally: $12.3340 - 6.056 = 5.774.$
>3. But our answer isn't allowed to have more than 3 significant digits after the decimal! So we round it down to $5.77.$ Done. 


##### Multiplying / Dividing Signifiant Digits:

This is a bit easier - whichever number has the least significant digits, your answer has to have the same amount. 

> Example:
>$2.240 \times 06.4460$. The number on the left has four sigdigs, the number on the right has 5 - so our answer has to have 4 sigdigs. 
>
>$2.240 \times 06.4460 = 14.439$ has 5 sigdigs, but we can't have more than 4, so we round it up to $14.44$.


***

Good luck!

-Max
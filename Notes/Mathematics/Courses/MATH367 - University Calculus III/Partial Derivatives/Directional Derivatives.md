# Directional Derivatives:
***

Recall the linear approximation:
$$f(\vec{x})\approx  f(\vec{a}) + \nabla f(\vec{a})\,\cdot\,(\vec{x}-\vec{a})$$

The approximation becomes exact at $\vec{x} = \vec{a}$.

We can substitute: $\vec{x} = \vec{a} + h\vec{u}$ becomes...

$$f(\vec{a}+h\vec{u})  \approx f(\vec{a})\, \cdot \,h\vec{u}$$...where $\vec{u}$ is some arbitrary vector. 

After rearranging, we find the definition of the **directional derivative**:


### $$D_{\vec{u}}f(\vec{a}) = \lim_{h \to 0}\frac{f(\vec{a} + h\vec{u}) - f(\vec{a})}{h} = \nabla f(\vec{a}) \, \cdot \, \vec{u}.$$ 

This is **not** the rate of change of $f$ at $\vec{a}$ **in the direction of** $\vec{u}$ - to get that, we need to divide the vector $\vec{u}$ by its magnitude (normalizing it):

### $$D_{\vec{u}}f(\vec{a}) = \lim_{h \to 0}\frac{f(\vec{a} + h\frac{\vec{u}}{||\vec{u}||}) - f(\vec{a})}{h} = \nabla f(\vec{a}) \, \cdot \, \vec{u}.$$ 


***

The gradient can be used  determine in what direction (or, along which axis) a function $f$ increases or decreases most rapidly.

***
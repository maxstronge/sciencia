### miCASA Overview

miCASA aims to be an intuitive and feature-rich visual computer algebra system. The application is designed to provide a highly interactive user experience, incorporating both visual and kinesthetic learning styles. 

**Target Audience:** miCASA is designed to serve a diverse user base, including students, educators, researchers, and professionals in various fields such as mathematics, physics, engineering, and computer science. The user-friendly interface makes it accessible to users of all skill levels, from novices to experts. Anyone who frequently needs to quickly work out some mathematics - no need for pen and paper. 
#### Tech Stack

- **Frontend**: React
- **Backend**: Flask and Python
- **Computational Acceleration**: Taichi

### Blackboard

The Blackboard serves as the central workspace where users can interact with mathematical expressions and equations.
#### Features:

1. **Scrollable Canvas**: A large, interactive area that can be navigated like a virtual blackboard.
2. **Drag-and-Drop**: Equations and expressions on the Blackboard are manipulable objects that can be rearranged.
3. **Term-by-Term Manipulation**: Users can click on individual terms or components of an equation to modify them.
4. **Auto Simplification**: Expressions placed on the Blackboard are automatically simplified using the backend computation engine.
5. **Expression History Scrollbar**: Each expression is associated with a scrollbar that allows users to navigate through its computational history.

### Expression Editor

The Expression Editor is a vital component that allows users to enter and edit mathematical expressions.

#### Features:

1. **Hotkey Activation**: A designated hotkey (e.g., tab, space, or enter) activates the editor.
2. **Freeform Input**: Users can type algebraic expressions freely according to a particular syntax that I will need to define.
3. **Real-Time LaTeX Rendering**: As users type, the editor provides real-time rendering of the expressions in LaTeX format.
4. **Confirmation**: Once the user confirms the expression in the Expression Editor, it is then displayed on the Blackboard, where it can be manipulated/moved around/set equal to other expressions, etc.

By combining these features, miCASA aims to offer an engaging and intuitive environment for mathematical exploration and physics simulations. It sets itself apart by providing a user interface that is not just visually appealing but also functionally robust, offering unique ways to manipulate and interact with mathematical objects.
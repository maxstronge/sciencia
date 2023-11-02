
## Blackboard:


A scrollable canvas called the Blackboard that one can dynamically type expressions into using a variety of intuitive hotkeys. For example, pressing a key (maybe tab, space, or enter) will open up a freeform expression editor in which algebraic expressions can be entered - when complete, the button can be pressed again to put the expression onto the Blackboard, where it can be manipulated term-by-term, manually rearranged, and auto simplified.

### Frontend Features

1. **Scrollable Canvas (Blackboard)**: A large, scrollable area where equations and expressions can be dragged and dropped, similar to manipulable objects.
    - **Technology**: Use HTML5 Canvas API or libraries like fabric.js to create this interactive space.

2. **Freeform Expression Editor**: A pop-up or inline editor that allows for the entry of algebraic expressions.
    - **Technology**: A text input field with real-time LaTeX rendering using MathJax.

3. **Hotkey System**: A set of keyboard shortcuts to speed up common tasks.
    - **Technology**: Listen to keyboard events and trigger corresponding actions.

4. **Term-by-Term Manipulation**: Allow users to click on individual terms in an equation to modify or rearrange them.
    - **Technology**: Each term could be a React component that maintains its own state and can interact with the larger equation object.

5. **Auto Simplification**: Auto-simplify expressions when they are placed onto the Blackboard.
    - **Technology**: Call the backend API to simplify the expression using SymPy and update the UI.

### Interaction with Backend

1. **Expression Submission**: When the user completes an expression in the editor, the frontend will send it to the backend for simplification or computation.
2. **Term Manipulation**: When a term is manipulated, the frontend can send the new state of the equation to the backend for re-evaluation.
3. **Retrieve Results**: Once computations are complete, the backend will send results back to the frontend to be displayed on the Blackboard.

### Data Flow

1. User activates the freeform editor using a hotkey.
2. User types an expression into the editor.
3. On confirming the expression, it is sent to the Flask backend for any necessary computations.
4. The computed or simplified expression is returned and placed onto the Blackboard.
5. User can manipulate the terms of the expression, triggering further backend computations as needed.

By combining these features, you could build a highly interactive and visually engaging interface that makes complex mathematical manipulations more intuitive.

___


## Expression History Scrollbar


**Expression History**: if you realize you're going in the wrong direction I would like the option to go back. I'd like to do this with a scrollbar that gets created along with each expression, dragging it left or right will move forward/backward through the expression history. This would give users a very intuitive way to explore different manipulations of an equation or expression without the fear of making irreversible changes. It's a bit like version control, but specifically for mathematical expressions.

### Implementing History Scrollbar for Each Expression

1. **State History**: Maintain a history of the state of each expression in a data structure, such as an array or linked list.
    - **Technology**: Use React state or a Redux store to keep track of the history.

2. **Scrollbar UI**: Implement a scrollbar UI element associated with each expression on the Blackboard.
    - **Technology**: You can use native HTML input type "range" or build a custom scrollbar component in React.

3. **Scroll Event Handling**: Listen to scroll events on each scrollbar to navigate the history of its corresponding expression.
    - **Technology**: Use event listeners in React to capture scroll events and update the state accordingly.

4. **Backend Communication**: When the scrollbar is moved, the frontend should fetch the historical state and might need to send it to the backend for re-evaluation.
    - **Technology**: Use the existing REST API to interact with the Flask backend.

5. **Rendering**: Render the selected historical state of the expression on the Blackboard.
    - **Technology**: Update the React component representing the expression to reflect the selected state.

6. **Sync with Backend**: Optionally, you can also save this history on the backend for persistence.
    - **Technology**: Store the history in a database or as session data in Flask.

___

The Blackboard is essentially an infinite blank canvas for miCASA Objects, visual logical components representing some mathematical or physical entity, function, or operation. The most common type of Object is an Expression, a mathematical statement using symbols (which can be a combination of numbers, roman/greek letters for variables, constants like pi, operators like sin cos etc). Expressions are created using the Expression Editor and written to the Blackboard. Most Expressions are not atomistic, indivisible objects, but are instead composed of a number of **terms**, grouped in the usual mathematical way (i.e. x^2 would be one term). I.e. the chain of Objects goes something like: - Symbol - atoms of information, has a **type** and a **context** (i.e. the 2 symbol in x^2 is a number type, and the context is that it is the exponent on a variable) - Term - collection of symbols that all apply to the same term. Has a context as well (i.e. the wider expression that it is in) - Expression - statement composed of one or more terms (i.e. a single term can also be an expression) created directly by the user, may also have a context (i.e. if it is in an equation or not) - Equation - assertion that two statements are equal to each other and can be treated as such , context might be that it is in a system of equations, etc. - Selection of expressions/terms - the user can click or drag boxes to select individual Objects in an expression or an expression as a whole - various actions may depend on the context of what the selected expression is, so the context piece of the above is crucial. - AutoSimplify - at the click of a button, the selected expression (or subexpression) reduces to its fully simplified form.  If the expression is strictly arithmetic, this is equivalent to evaluating the expression. - Equations - an equals sign on the Blackboard is a special visual object that essentially takes two visual positional 'arguments' - one in the 'slot' on the LHS, and one in the slot on the RHS. When both of the slots are filled by expressions from the editor, then the user has successfully defined a miCASA equation, and asserted that the things on either side are equal to one another. This will be of incredible use for solving physics problems, as once can then set up an equation that they know to be true and substitute/manipulate it like one would working it out on paper - only much faster! - Systems of equations - fairly straightforward, several Equation objects as described above can be collected into a System of equations (say by selecting them all, right-clicking to bring up a dialog, and selecting Create System). Visually, the equations should cluster together and align on the equals sign - then, clicking a button 'Solve' that appears when a System of Equations object is selected will result in the solution - Symbolic Integral Solving - this one is a bit more complicated. I don't want to merely numerically evaluate definite integrals - python can already do that fine. What I want to do is to allow for the user to add an Integral object to the Blackboard which also takes visual/positional arguments - the integrand, variable of integration, and optionally limits of integration, all of which are expressions as normal. When at least the first two of these slots have been filled, the integral becomes solvable with the Solve button as for the systems above - but when requested, the analytic solution steps become available, rather than just jumping to the final answer For example, it would go through a decision tree to identify the integration technique (by parts, substitution), remind the user of the formula and display it on the screen, then apply to to get the final result.

### The Philosophy of miCASA's Blackboard

miCASA aims to revolutionize the way we interact with mathematical and physical entities by providing an intuitive and dynamic workspace, known as the Blackboard. This infinite canvas serves as a playground for a variety of miCASA Objects, which are visual logical components that encapsulate different mathematical or physical functionalities.

### The miCASA Object Model

The Object Model is hierarchical, starting from the simplest forms of mathematical representation and building up to more complex structures. The chain of Objects is organized as follows:

- **Symbol**: The atomic unit of information, each Symbol has a **type** and a **context**. For example, the "2" in �2x2 is a number type with the context of being an exponent.
    
- **Term**: A Term is a collection of Symbols that applies to the same mathematical entity. Like Symbols, Terms also have a context, often determined by the wider Expression they are part of.
    
- **Expression**: An Expression is a statement composed of one or more Terms. Expressions can also have a context, such as whether they are part of an Equation.
    
- **Equation**: An Equation asserts the equality between two Expressions. Its context could extend to being part of a System of Equations.
    
- **System of Equations**: A collection of Equations that can be solved collectively.
    

### User Interaction

- **Selection of Expressions/Terms**: Users can click or drag boxes to select individual Objects within an Expression or the Expression as a whole. The available actions depend on the context of the selected Expression.
    
- **AutoSimplify**: At the click of a button, selected Expressions or sub-expressions are automatically simplified. For example, if we had the expression $18x^3/3x$, and the user clicked on the $x^3$ term in the numerator and the x term in the denominator and hit simplify, the result would be $18x^2$. If they instead clicked the $18$ and the $3$, the result would be $6x^3/x$. If the entire expression was selected, the result would be $6x^2$ 
    
- **Equations and Systems**: Users can define Equations by filling visual slots on either side of an equals sign. Multiple such Equations can be grouped into a System of Equations.
    
- **Symbolic Integral Solving**: Users can add an Integral Object that takes visual arguments like the integrand and limits of integration. Upon filling these slots, the integral can be solved analytically, providing step-by-step solutions.
    

### Additional Features

- **Annotations and Labels**: Users can add explanatory notes or labels to miCASA Objects.
    
- **Drag-and-Drop Functionality**: Allows for easy rearrangement and organization of miCASA Objects.
    
- **Function Plotting**: Enables visual representation of functions right within the Blackboard.
    
- **Copy/Paste miCASA Objects**: Facilitates repetitive calculations.
    
- **Templates for Common Problems**: Pre-defined templates for standard physics problems can be dragged onto the Blackboard.
    
- **Search and Replace**: For making large-scale changes easily.
    
- **Zoom In/Out**: Users can adjust their view of the Blackboard to suit their needs.
    

### Advanced Features

- **Vectors and Matrices**: Crucial for physics applications, these Object types would allow for complex vector and matrix operations.
    
- **Constraints and Logical Operators**: Enables the definition of conditions or constraints for solving more complex problems.
    
- **Real-Time Collaboration**: Multiple users can interact with the same Blackboard in real-time, facilitating collaborative problem-solving.
    
- **3D Objects**: For visualization of three-dimensional plots or solving advanced physics problems involving spatial dimensions.
    

By combining these features, miCASA's Blackboard aims to provide a comprehensive, user-friendly environment for mathematical exploration and physics problem-solving.
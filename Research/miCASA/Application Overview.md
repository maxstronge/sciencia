
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
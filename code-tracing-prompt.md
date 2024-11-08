# Code Tracing Analysis Prompt

When asked to perform a step-by-step code trace, follow this structured approach:

## 1. Initial Setup
- Start with the complete code block in syntax-highlighted format
- Specify example input values that will be traced
- Show initial state of all variables

## 2. Main Code Trace
Format each code block as follows:
```python
def function_name(parameters):
    # Initial state:
    # param1 = value1
    # param2 = value2
    
    # --- Section/Loop Name ---
    for/if/while statement:
        # --- Iteration N ---
        # current_var = current_value
        # Show current state of relevant variables
        code_line  # Add explanation of operation
        # Show state after operation
```

## 3. Visual Memory State Trace
Include a separate section showing memory state at key points:
```
Step 1: Initial State
var1 = value1
var2 = value2

Step 2: After Key Operation
var1 = new_value1
var2 = new_value2
```

## 4. Key Tracing Elements to Include
1. Iteration Markers:
   - Label each iteration clearly
   - Show loop counter values
   - Indicate entry/exit points

2. Variable States:
   - Show before/after values
   - Track changes in data structures
   - Note when variables are created/modified/deleted

3. Decision Points:
   - Show condition evaluations
   - Explain why branches are taken
   - Note when early returns occur

4. Data Structure Evolution:
   - Show state of arrays/maps/lists
   - Track size changes
   - Show key-value pairs

## 5. Final Analysis Section
Include:
1. Key Observations:
   - Critical state changes
   - Important transitions
   - Pattern recognition

2. Efficiency Analysis:
   - Time complexity with explanation
   - Space complexity with explanation
   - Key performance insights

## 6. Format Requirements
- Use consistent indentation
- Separate logical sections with clear headers
- Include inline comments for complex operations
- Use clear visual separation between sections

## Example Comment Structure:
```python
# --- Section Header ---
code_line  # What operation is happening
# Current state: {show relevant variables}
# Effect: {explain what changed}
```

## Instructions for Use:
1. Always start with a simple but illustrative example
2. Trace complete execution path
3. Highlight key decision points
4. Show all relevant variable states
5. Explain any non-obvious behavior
6. Note early termination conditions
7. Conclude with key insights

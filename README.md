# daysBetweenDates
Learning and practicing the skill of "Problem Solving" + using basic Git/GitHub


- How to solve problems?

0- don't panic

1- make sure you understand the problem before trying to solve it:
   
   * a problem is defined by a set of possible inputs (usually infinite) and the relationship between them and the desired output.
   * the solution is a function that can take any input in the set, and produces a desired output that satisfies the relationship.

   1.1) what are the inputs? 

        a) understand what is the set of possible "valid" inputs:
           by: 
           - using assumptions in the problem 
           - asking questions to make more assumptions 
           - making your own assumptions
	   - be smart and use defensive programming and check for assumptions in your code. (count for user mistakes)
   
        b) decide how to represent inputs: 
           passing them as separate values or grouping/backaging them into objects? up to you.

   1.2) what are the outputs?

        - what is the meaningful output assuming the inputs are valid.
        - for definsive programming, what are the outputs for cases where the inputs are not valid.
   
   1.3) understand the relationship between inputs and outputs by working out some examples. function(inputs) -> output
   

2- think about how to systematically solve the problem as a human

   * write a "pseudo code" algorithm that systematizes how you solved the problem as a human

3- if human solution is complex, find a simpler mechanical solution.

   * simple-mechanical solution is easier to write correctly, and saves developer's time and effort but slower. 
   * complex-shortcut-human solution is faster but it consumes more time and effort to write.
   * depending on the future use of the program, make your trade off between speed and developers time/effort consumed.

   (don't optimize prematurely. go with the simple mechanical solution and don't worry about making the algorithm faster until you have to)

4- break down the problem into small pieces, develop incrementally, and test each piece independently as you go.

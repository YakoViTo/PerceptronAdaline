# PerceptronAdaline

The problem consists of solving a classification problem using a Simple Perceptron and an Adaline. A two-dimensional training data must be generated within the rectangle [0, 10] x [0, 10] and the points must be labeled according to their position with respect to a line y = mx + b that also passes through the rectangle. Points above the line will be labeled as 1, and points below will be labeled as -1. Then, it is desired to train a Simple Perceptron and an Adaline to correctly classify the randomly generated test points.

The solution consists of implementing the Simple Perceptron and the Adaline using Python version 3.10.5 under Windows 10 environment and the NumPy library for vector calculations. The training data and labels will be generated according to the line y = mx + b, and then the models will be trained to fit a line to correctly classify the points into two categories. In order to appreciate the solution to this problem, the Matplotlib library will be used to better visualize the results of the problem.

The relevant functions of the code that helped to solve the problem are described below:

   1) generate_random_points(num_points): this function generates random points in the rectangle [0, 10] x [0, 10]. It takes as input the number of points to be generated and returns an array with the (x, y) coordinates of those points.

  
   2) generate_labels(points, m, b): This function generates the classification labels (1 or -1) for the generated points. It takes as input the matrix of points and the coefficients m and b of the line y = mx + b. It labels the points according to their position with respect to the line. Points above the line will be labeled as 1, and points below will be labeled as -1.




# PerceptronAdaline

The problem consists of solving a classification problem using a Simple Perceptron and an Adaline. A two-dimensional training data must be generated within the rectangle [0, 10] x [0, 10] and the points must be labeled according to their position with respect to a line y = mx + b that also passes through the rectangle. Points above the line will be labeled as 1, and points below will be labeled as -1. Then, it is desired to train a Simple Perceptron and an Adaline to correctly classify the randomly generated test points.

The solution consists of implementing the Simple Perceptron and the Adaline using Python version 3.10.5 under Windows 10 environment and the NumPy library for vector calculations. The training data and labels will be generated according to the line y = mx + b, and then the models will be trained to fit a line to correctly classify the points into two categories. In order to appreciate the solution to this problem, the Matplotlib library will be used to better visualize the results of the problem.

A continuación, se describen las funciones relevantes del código que ayudaron a solucionar el problema:

  1- generate_random_points(num_points): Esta función genera puntos aleatorios en el rectángulo [0, 10] x [0, 10]. Toma como entrada el número de puntos que se desea generar y devuelve        una matriz con las coordenadas (x, y) de esos puntos.
     ![image](https://github.com/YakoViTo/PerceptronAdaline/assets/135473233/ccb8d086-ce15-4101-bae9-5bbc6e32baa0)



# PerceptronAdaline

The problem consists of solving a classification problem using a Simple Perceptron and an Adaline. A two-dimensional training data must be generated within the rectangle [0, 10] x [0, 10] and the points must be labeled according to their position with respect to a line y = mx + b that also passes through the rectangle. Points above the line will be labeled as 1, and points below will be labeled as -1. Then, it is desired to train a Simple Perceptron and an Adaline to correctly classify the randomly generated test points.

The solution consists of implementing the Simple Perceptron and the Adaline using Python version 3.10.5 under Windows 10 environment and the NumPy library for vector calculations. The training data and labels will be generated according to the line y = mx + b, and then the models will be trained to fit a line to correctly classify the points into two categories. In order to appreciate the solution to this problem, the Matplotlib library will be used to better visualize the results of the problem.

A continuación, se describen las funciones relevantes del código que ayudaron a solucionar el problema:

  1) generate_random_points(num_points): Esta función genera puntos aleatorios en el rectángulo [0, 10] x [0, 10]. Toma como entrada el número de puntos que se desea generar y devuelve una matriz con las coordenadas (x, y) de esos puntos.

  
  2) generate_labels(points, m, b): Esta función genera las etiquetas de clasificación (1 o -1) para los puntos generados. Toma como entrada la matriz de puntos y los coeficientes m y b de la recta y = mx + b. Etiqueta los puntos según su posición con respecto a la recta. Los puntos que estén por encima de la recta se etiquetarán como 1, y los puntos que estén por debajo se etiquetarán como -1. Devuelve un vector de etiquetas.




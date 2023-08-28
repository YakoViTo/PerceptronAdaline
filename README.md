# PerceptronAdaline

The problem consists of solving a classification problem using a Simple Perceptron and an Adaline. A two-dimensional training data must be generated within the rectangle [0, 10] x [0, 10] and the points must be labeled according to their position with respect to a line y = mx + b that also passes through the rectangle. Points above the line will be labeled as 1, and points below will be labeled as -1. Then, it is desired to train a Simple Perceptron and an Adaline to correctly classify the randomly generated test points.

The solution consists of implementing the Simple Perceptron and the Adaline using Python version 3.10.5 under Windows 10 environment and the NumPy library for vector calculations. The training data and labels will be generated according to the line y = mx + b, and then the models will be trained to fit a line to correctly classify the points into two categories. In order to appreciate the solution to this problem, the Matplotlib library will be used to better visualize the results of the problem.


![image](https://github.com/YakoViTo/PerceptronAdaline/assets/135473233/8b20aec8-00cc-4935-86e9-5e4f52789796)


![image](https://github.com/YakoViTo/PerceptronAdaline/assets/135473233/12ba80a7-9839-49f4-9af4-729586d3c56b)
![image](https://github.com/YakoViTo/PerceptronAdaline/assets/135473233/a336ec2d-acc1-46db-a895-4dda3a415fe7)

The results obtained will depend on the experiments performed and the parameter values used. In general, both Simple Perceptron and Adaline are expected to be able to fit a line to correctly classify most of the test points within the rectangle [0, 10] x [0, 10]. The accuracy and speed of convergence may vary depending on the number of training points, data separability, learning rates, and training epochs.

In conclusion, the Simple Perceptron and Adaline are two classical supervised learning algorithms for solving linear classification problems. They are suitable for problems where the data are linearly separable. However, for more complex problems or nonlinearly separable data, more advanced approaches, such as deeper neural networks or nonlinear learning techniques, would be required.

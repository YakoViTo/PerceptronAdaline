# PerceptronAdaline

The problem consists of solving a classification problem using a Simple Perceptron and an Adaline. A two-dimensional training data must be generated within the rectangle [0, 10] x [0, 10] and the points must be labeled according to their position with respect to a line y = mx + b that also passes through the rectangle. Points above the line will be labeled as 1, and points below will be labeled as -1. Then, it is desired to train a Simple Perceptron and an Adaline to correctly classify the randomly generated test points.

The solution consists of implementing the Simple Perceptron and the Adaline using Python version 3.10.5 under Windows 10 environment and the NumPy library for vector calculations. The training data and labels will be generated according to the line y = mx + b, and then the models will be trained to fit a line to correctly classify the points into two categories. In order to appreciate the solution to this problem, the Matplotlib library will be used to better visualize the results of the problem.

# EXPERIMENTS PERFORMED

   1) Vary the number of training points. The num_points variable determines the number of training points. You can change its value to test with different numbers of points. For example, increase or decrease the number of points and observe how it affects the accuracy of the models.

      Test with the variable num_points equal to 10, with coefficients of the line y = mx + b where m is equal to 0.5 and b is equal to 2.5 and with a learning_rate of 0.01 and maximum number of epochs (max_epochs) equal to 100 for the Adaline, similarly values are set for the Simple Perceptron inherent to the learning_rate of 0.1 and maximum number of epochs (max_epochs) equal to 100.

      ![image](https://github.com/YakoViTo/PerceptronAdaline/assets/135473233/37544939-41bc-4904-97a9-4744285f5a8c)
      
      
      ![image](https://github.com/YakoViTo/PerceptronAdaline/assets/135473233/4b374e59-7f9b-40a6-b987-f8fcd125cbdc)
      ![image](https://github.com/YakoViTo/PerceptronAdaline/assets/135473233/7dee52cf-1df6-45d8-8990-ef762ba535f2)

      Test with the variable num_points equal to 20, with coefficients of the straight line y = mx + b where m is equal to 0.5 and b is equal to 2.5 and with a learning_rate of 0.01 and maximum number of epochs (max_epochs) equal to 100 for the Adaline, in the same way values are established for the Simple Perceptron inherent to the learning_rate of 0.1 and maximum number of epochs (max_epochs) equal to 100.

      ![image](https://github.com/YakoViTo/PerceptronAdaline/assets/135473233/252ab902-eabe-4778-96b5-59fc65443a7b)


      ![image](https://github.com/YakoViTo/PerceptronAdaline/assets/135473233/04a67d74-d9d9-4c9e-b42b-3a65e1aed2b5)
      ![image](https://github.com/YakoViTo/PerceptronAdaline/assets/135473233/e80f555a-8dc2-4cc1-b672-a0a0d88ecfb0)

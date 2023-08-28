import numpy as np
import matplotlib.pyplot as plt

# Función para generar puntos aleatorios en el rectángulo [0, 10] x [0, 10]
def generate_random_points(num_points):
    return np.random.rand(num_points, 2) * 10

# Función para generar etiquetas de clasificación (1 o -1) según la recta y = mx + b
def generate_labels(points, m, b):
    y = m * points[:, 0] + b
    labels = np.where(points[:, 1] > y, 1, -1)
    return labels

# Implementación del Perceptrón Simple
class PerceptronSimple:
    # def __init__(self, input_size, learning_rate=0.1, epochs=100):
    def __init__(self, input_size, learning_rate=0.9, epochs=50):    
        self.weights = np.random.rand(input_size)
        self.bias = np.random.rand()
        self.learning_rate = learning_rate
        self.epochs = epochs

    def activation(self, x):
        return np.where(x >= 0, 1, -1)

    def train(self, X, y):
        for _ in range(self.epochs):
            for i in range(X.shape[0]):
                prediction = self.activation(np.dot(X[i], self.weights) + self.bias)
                error = y[i] - prediction
                self.weights += self.learning_rate * error * X[i]
                self.bias += self.learning_rate * error

# Implementación del Adaline
class Adaline:
    # def __init__(self, input_size, learning_rate=0.01, epochs=100):
    def __init__(self, input_size, learning_rate=0.04, epochs=50):
        self.weights = np.random.rand(input_size)
        self.bias = np.random.rand()
        self.learning_rate = learning_rate
        self.epochs = epochs

    def activation(self, x):
        return x

    def train(self, X, y):
        for _ in range(self.epochs):
            for i in range(X.shape[0]):
                prediction = np.dot(X[i], self.weights) + self.bias
                error = y[i] - prediction
                self.weights += self.learning_rate * error * X[i]
                self.bias += self.learning_rate * error

# Función para graficar los puntos y la recta
def plot_data_and_line(data, labels, m, b, title):
    plt.figure()
    plt.scatter(data[:, 0], data[:, 1], c=labels, cmap='coolwarm', marker='o')
    plt.colorbar(label='Etiqueta')
    plt.xlabel('X1')
    plt.ylabel('X2')
    plt.title(title)

    x_vals = np.linspace(0, 10, 100)
    y_vals = m * x_vals + b
    plt.plot(x_vals, y_vals, 'k--', label='y = {:.2f}x + {:.2f}'.format(m, b))
    plt.legend()
    plt.xlim(0, 10)
    plt.ylim(0, 10)
    plt.grid(True)
    plt.show()

# Generar datos de entrenamiento
num_points = 20
m, b = 0.5, 2.5
# m, b = 1, 0
data = generate_random_points(num_points)
labels = generate_labels(data, m, b)

# Agregar una columna de unos para el término de sesgo (bias)
X_train = np.c_[np.ones(num_points), data]

# Entrenar el Perceptrón Simple
perceptron = PerceptronSimple(input_size=3)
perceptron.train(X_train, labels)

# Entrenar el Adaline
adaline = Adaline(input_size=3)
adaline.train(X_train, labels)

# Obtener los valores de la recta que aprendieron
m_perceptron, b_perceptron = -perceptron.weights[1] / perceptron.weights[2], -perceptron.bias / perceptron.weights[2]
m_adaline, b_adaline = -adaline.weights[1] / adaline.weights[2], -adaline.bias / adaline.weights[2]

# Graficar los resultados
plot_data_and_line(data, labels, m, b, 'Datos de entrenamiento y recta original')
plot_data_and_line(data, perceptron.activation(np.dot(X_train, perceptron.weights)), m_perceptron, b_perceptron, 'Perceptrón Simple')
plot_data_and_line(data, adaline.activation(np.dot(X_train, adaline.weights)), m_adaline, b_adaline, 'Adaline')

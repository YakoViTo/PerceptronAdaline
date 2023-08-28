import numpy as np
import matplotlib.pyplot as plt

# Datos de ejemplo
np.random.seed()
num_samples = 10
mean_1 = [-1, 1]
mean_2 = [1, -1]
cov = [[0.5, 0.2], [0.2, 0.5]]
X1 = np.random.multivariate_normal(mean_1, cov, num_samples)
X2 = np.random.multivariate_normal(mean_2, cov, num_samples)

# Etiquetas de clase
y1 = np.ones(num_samples)
y2 = -np.ones(num_samples)

# Concatenar los datos y las etiquetas
X = np.vstack((X1, X2))
y = np.concatenate((y1, y2))

# Función de activación
def activation_function(x):
    return x

# Función para trazar los datos y la línea de decisión
def plot_data_and_decision_boundary(X, y, w, title):
    plt.scatter(X[:, 0], X[:, 1], c=y, cmap='bwr')
    x_min, x_max = X[:, 0].min() - 1, X[:, 0].max() + 1
    y_min, y_max = X[:, 1].min() - 1, X[:, 1].max() + 1
    xx, yy = np.meshgrid(np.arange(x_min, x_max, 0.1),
                         np.arange(y_min, y_max, 0.1))
    X_grid = np.c_[xx.ravel(), yy.ravel()]
    X_grid_with_bias = np.hstack((X_grid, np.ones((X_grid.shape[0], 1))))
    Z = activation_function(np.dot(X_grid_with_bias, w))
    Z = np.sign(Z)
    Z = Z.reshape(xx.shape)
    plt.contourf(xx, yy, Z, alpha=0.5, cmap='bwr')
    plt.xlim(x_min, x_max)
    plt.ylim(y_min, y_max)
    plt.title(title)
    plt.xlabel('X1')
    plt.ylabel('X2')
    plt.show()

# Entrenamiento del perceptrón simple
class PerceptronSimple:
    def __init__(self, learning_rate=0.1, max_epochs=100):
        self.learning_rate = learning_rate
        self.max_epochs = max_epochs

    def fit(self, X, y):
        self.w = np.zeros(X.shape[1] + 1)  # Inicializar pesos y bias
        X_with_bias = np.hstack((X, np.ones((X.shape[0], 1))))  # Agregar columna de unos
        epochs = 0
        while epochs < self.max_epochs:
            y_pred = np.sign(np.dot(X_with_bias, self.w))
            misclassified_samples = np.where(y != y_pred)[0]
            if len(misclassified_samples) == 0:
                break
            random_index = np.random.choice(misclassified_samples)
            self.w += self.learning_rate * y[random_index] * X_with_bias[random_index]
            epochs += 1

        return self.w

perceptron = PerceptronSimple()
w_perceptron = perceptron.fit(X, y)
plot_data_and_decision_boundary(X, y, w_perceptron, "Perceptrón Simple")

# Entrenamiento del Adaline
class Adaline:
    def __init__(self, learning_rate=0.01, max_epochs=100):
        self.learning_rate = learning_rate
        self.max_epochs = max_epochs

    def fit(self, X, y):
        self.w = np.zeros(X.shape[1] + 1)  # Inicializar pesos y bias
        X_with_bias = np.hstack((X, np.ones((X.shape[0], 1))))  # Agregar columna de unos
        epochs = 0
        while epochs < self.max_epochs:
            y_pred = np.dot(X_with_bias, self.w)
            error = y - y_pred
            self.w += self.learning_rate * np.dot(X_with_bias.T, error)
            epochs += 1

        return self.w

adaline = Adaline()
w_adaline = adaline.fit(X, y)
plot_data_and_decision_boundary(X, y, w_adaline, "Adaline")
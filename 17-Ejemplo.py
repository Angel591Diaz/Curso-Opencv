import numpy as np

inputs = [ 1, 2, 3, 2.5]
weights1 = [0.2, 0.8, -0.5, 1]
weights2 = [0.5, -0.91, 0.26, -0.5]
weights3 = [-0.26, -0.27, 0.17, 0.87]
bias1 = 2
bias2 = 3
bias3 = 0.5

a = np.dot(inputs, weights1) + bias1
b = np.dot(inputs, weights2) + bias2
c = np.dot(inputs, weights3) + bias3

outputs2 = [a,b,c]

outputs = [
# Neuron 1:
inputs[ 0 ] * weights1[ 0 ] +
inputs[ 1 ] * weights1[ 1 ] +
inputs[ 2 ] * weights1[ 2 ] +
inputs[ 3 ] * weights1[ 3 ] + bias1,
# Neuron 2:
inputs[ 0 ] * weights2[ 0 ] +
inputs[ 1 ] * weights2[ 1 ] +
inputs[ 2 ] * weights2[ 2 ] +
inputs[ 3 ] * weights2[ 3 ] + bias2,
# Neuron 3:
inputs[ 0 ] * weights3[ 0 ] +
inputs[ 1 ] * weights3[ 1 ] +
inputs[ 2 ] * weights3[ 2 ] +
inputs[ 3 ] * weights3[ 3 ] + bias3,

]
#sumatoria
#output = (inputs[0] * weights[0] + inputs[1] * weights[1] + inputs[2] * weights[2] + bias)

print (outputs)
print(outputs2)
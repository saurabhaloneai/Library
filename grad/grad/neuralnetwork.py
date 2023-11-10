
class SimpleNet:
    def __init__(self):
        self.fc1 = Linear(1, 1)

    def forward(self, x):
        x = self.fc1(x)
        return x

class Linear(Module):
    def __init__(self, input_size, output_size):
        self.weights = Tensor([[0.1] * output_size for _ in range(input_size)], requires_grad=True)
        self.bias = Tensor([0.0] * output_size, requires_grad=True)

    def forward(self, x):
        self.input = x
        return x @ self.weights + self.bias

    def backward(self, grad):
        self.weights.backward(self.input.T @ grad)
        self.bias.backward(grad)
        self.input.backward(grad @ self.weights.T)
# Activation functions
def relu(x):
    return x * (x > 0)        
class Tensor:
    def __init__(self, data, requires_grad=False):
        self.data = data
        self.requires_grad = requires_grad
        self.grad = None
        self._backward = None

    def backward(self, grad=None):
        if self.requires_grad:
            if grad is None:
                grad = Tensor(1.0)
            
            if self.grad is None:
                self.grad = grad
            else:
                self.grad += grad

            if self._backward is not None:
                self._backward(self.grad)

    def __add__(self, other):
        result = Tensor(self.data + other.data)
        if self.requires_grad or other.requires_grad:
            def _backward(grad):
                self.backward(grad)
                other.backward(grad)
            result._backward = _backward
        return result

    def __mul__(self, other):
        result = Tensor(self.data * other.data)
        if self.requires_grad or other.requires_grad:
            def _backward(grad):
                self.backward(other.data * grad)
                other.backward(self.data * grad)
            result._backward = _backward
        return result
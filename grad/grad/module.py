class Module:
    def __call__(self, *args):
        self.input = args
        self.output = self.forward(*args)
        return self.output

    def backward(self, grad):
        raise NotImplementedError

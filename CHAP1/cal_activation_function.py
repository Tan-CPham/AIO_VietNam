import math

def sigmoid(x):
    """Compute the sigmoid function for the input x."""
    sigmoid_value = 1 / (1 + math.exp(-x))
    return sigmoid_value

def relu(x):
    """Compute the ReLU function for the input x."""
    relu_value = max(0, x)
    return relu_value

def elu(x, alpha=1.0):
    """Compute the ELU function for the input x."""
    if x >= 0:
        elu_value = x
    else:
        elu_value = alpha * (math.exp(x) - 1)
    return elu_value

def is_number(n):
    try:
        float(n)
    except ValueError:
        return False
    return True

def main():
    x_value = input("Input x = ")
    if not is_number(x_value):
        raise ValueError("x must be a number.")
    x_value = float(x_value)

    choise = input("Input activation function (sigmoid|relu|elu): ").strip().lower()

    if choise == "sigmoid":
        result = sigmoid(x_value)
        print(f"sigmoid: f({x_value}) = {result}")
    elif choise == "relu":
        result = relu(x_value)
        print(f"relu: f({x_value}) = {result}")
    elif choise == "elu":
        result = elu(x_value)
        print(f"elu: f({x_value}) = {result}")
    else:
        print(f"{choise} is not supported")

if __name__ == "__main__":
    main()
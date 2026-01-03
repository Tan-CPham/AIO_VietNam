import math

def is_integer(n): # so nguyen duong
    return n.isdecimal()

def is_radian(x): # so radian
    try:
        float(x.strip()) # dùng strip để loại bỏ khoảng trắng thừa nếu nhập dư khoảng trắng
        return True
    except ValueError:
        return False

def cal_factorial(n): # tinh giai thua
    if n == 0 or n == 1:
        return 1
    return n * cal_factorial(n - 1)

def cal_sin(x, n):
    sin_value = 0
    for i in range(n):
        temp = ((-1) ** i) * (x ** (2 * i + 1)) / cal_factorial(2 * i + 1)
        sin_value += temp
    return sin_value

def cal_cos(x, n):
    cos_value = 0
    for i in range(n):
        temp = ((-1) ** i) * (x ** (2 * i)) / cal_factorial(2 * i)
        cos_value += temp
    return cos_value

def cal_sinh(x, n):
    sinh_value = 0
    for i in range(n):
        temp = (x ** (2 * i + 1)) / cal_factorial(2 * i + 1)
        sinh_value += temp
    return sinh_value

def cal_cosh(x, n):
    cosh_value = 0
    for i in range(n):
        temp = (x ** (2 * i)) / cal_factorial(2 * i)
        cosh_value += temp
    return cosh_value

def main():
    x_value = input(f"Input x (radian): ")
    if not is_radian(x_value):
        raise ValueError("x must be a number (radian) like 1.57, 3.14, ...")
    x_value = float(x_value)

    n_value = input(f"Input n (integer number): ")
    if is_integer(n_value):
        n_value = int(n_value)
    else:
        raise ValueError("n must be an integer number like 1, 2, 3, ...")
    
    choise = input("Input function name (sin|cos|sinh|cosh): ").strip().lower()
    if choise == "sin":
        result = cal_sin(x_value, n_value)
    elif choise == "cos":
        result = cal_cos(x_value, n_value)
    elif choise == "sinh":
        result = cal_sinh(x_value, n_value)
    elif choise == "cosh":
        result = cal_cosh(x_value, n_value)
    else:
        print(f"{choise} is not supported")

    if choise in ["sin", "cos", "sinh", "cosh"]:
        print(f"approx_{choise}(x = {x_value}, n = {n_value})")
        print(f">> {result}")

if __name__ == "__main__":
    main()

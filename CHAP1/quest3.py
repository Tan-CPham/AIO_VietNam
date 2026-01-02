import math
import random

def is_integer(n):
    return n.isnumeric()

def mae(predict, target):
    return abs(target - predict)

def mse(predict, target):
    return (target - predict) ** 2

def rmse(predict, target):
    return math.sqrt(mse(predict, target))

def main():
    num_samples = input("Input number of samples (integer number) which are generated: ")
    if is_integer(num_samples):
        num_samples = int(num_samples)
    else:
        raise ValueError("number of samples must be an integer number")
    
    loss_name = input("Input loss name MAE|MSE|RMSE: ")

    final_loss = 0

    for i in range(num_samples):    
        target = random.uniform(0,10)
        predict = random.uniform(0,10)
        if loss_name == "MAE":
            loss_value = mae(predict, target)
        elif loss_name == "MSE":
            loss_value = mse(predict, target)
        elif loss_name == "RMSE":
            loss_value = rmse(predict, target)

        print(f"loss_name: {loss_name}, sample: {num_samples}, predict: {predict}, target: {target}, loss: {loss_value}")
        final_loss = final_loss + loss_value
    
    print(f"final {loss_name}: {final_loss/num_samples}")

if __name__ == "__main__":
    main()
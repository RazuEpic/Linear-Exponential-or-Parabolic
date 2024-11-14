y = []

values_len = int(input("[Enter the Length of the Table of Values]\n>> "))

for i in range(values_len):
    value = float(input(f"[Enter value {i + 1}]\n>> "))
    y.append(value)

first_diffs = [y[i] - y[i + 1] for i in range(len(y) - 1)]
second_diffs = [first_diffs[i] - first_diffs[i + 1] for i in range(len(first_diffs) - 1)]
exp_ratio = [y[i] / y[i + 1] for i in range(len(y) - 1)]

def First_Difference():
    FD_nums = len(set(first_diffs)) == 1
    if FD_nums:
        print(f"First difference: {FD_nums}. The values give a linear function.")

def Second_Difference():
    SD_nums = len(set(second_diffs)) == 1
    if SD_nums:
        print(f"Second difference: {SD_nums}. The second differences give a parabolic function.")

def Exp_Ratio_Nums():
    EXP_rNums = len(set(exp_ratio)) == 1
    if EXP_rNums:
        print(f"Exponential ratio: {EXP_rNums}. The result of the exponential ratio gives an exponential function.")

try:
    First_Difference()
    Second_Difference()
    Exp_Ratio_Nums()
except ValueError:
    print("The values don't make up any known function. Either that, or this is an error.")

import math

def f(x):
    return math.sin(x) - x**2 * math.cos(x)

def df(x):
    return math.cos(x) - 2*x * math.cos(x) + x**2 * math.sin(x)

def dây_cung(x0, epsilon, max_iters):
    x = x0
    for _ in range(max_iters):
        f_value = f(x)
        df_value = df(x)
        x_new = x - f_value / df_value
        if abs(x_new - x) < epsilon:
            return x_new
        x = x_new
    return None

x0 = 1  # Giá trị ban đầu
epsilon = 1e-3  # Sai số mong muốn
max_iters = 100  # Số lần lặp tối đa

nghiem = dây_cung(x0, epsilon, max_iters)
if nghiem is not None:
    print("Nghiệm của phương trình là:", nghiem)
else:
    print("Không tìm thấy nghiệm trong số lần lặp tối đa.")

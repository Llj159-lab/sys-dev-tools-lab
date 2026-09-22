import torch

x = torch.tensor(2.0, requires_grad=True)

y = x ** 3 + 2 * x ** 2 + x

y.backward()

print(f"x={x.item()}")
print(f"y={y.item()}")
print(f"dy_dx={x.grad.item()}")

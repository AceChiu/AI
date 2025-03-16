import torch
import numpy as np


# if torch.cuda.is_available():
#     device = torch.device("cuda")
#     x = torch.ones(5, device=device)
#     y = torch.ones(5)
#     y = y.to(device)
#     z = x + y
#     z = z.to("cpu")

# a =  torch.ones(5)
# print(a)
# b = a.numpy()
# print(type(b))

# a.add_(1)
# print(a)
# print(b)

# c = np.ones(5)
# print(c)
# d = torch.from_numpy(c)
# print(d)

# c += 1
# print(c)
# print(d)


# x = torch.ones(2, 2, dtype=torch.float16)
# print(x.size())

# y = torch.tensor([2.5, 0.1])
# print(y)

# x = torch.rand(2,2)
# y = torch.rand(2,2)
# print(x)
# print(y)
# z = x + y
# print(z)
# z = x - y
# print(z)

# x = torch.rand(5, 3)
# print(x)
# print(x[1, :])
# y = x.view(-1, 5)
# print(y)
# print(y.size())
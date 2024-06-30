import torch

device = torch.device('cuda')

a = torch.tensor([1., 2, 3], requires_grad=True).to(device)

b = a.sum()

print(b.backward(a))


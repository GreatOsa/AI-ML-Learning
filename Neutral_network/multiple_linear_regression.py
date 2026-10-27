from torch import nn
import torch

torch.manual_seed(1)

# set the weight and bias
w = torch.tensor([[2.0],[3.0]],requires_grad=True)
b= torch.tensor([[1.0]],requires_grad=True)

# define prediction Function

def forward(x):
    yhat = torch.mm(x,w)+b
    return yhat

# claculate the yhat

x = torch.tensor([[1.0,2.0]])
yhat = forward(x)
# print("the result: ", yhat)

X = torch.tensor([[1.0,1.0],[1.0,2.0],[1.0,3.0]])

# make the prediction of X

yhat = forward(X)
# print("the result: ", yhat)

# make a linear regression model using build-in function

model = nn.Linear(2,1)

# Make a prediction of x

yhat = model(X)
# print("the result: ", yhat)

# Build Custom Modules
# create linear regression class

class linear_regression(nn.Module):

    def __init__(self, input_size,output_size):
        super(linear_regression,self).__init__()
        self.linear = nn.Linear(input_size,output_size)

    # Prediction function
    def forward(self, x):
        yhat = self.linear(x)
        return yhat


model = linear_regression(2, 1)

# Print model parameters

print("The parameters: ", list(model.parameters()))

# Make a prediction of x

yhat = model(x)
print("The result: ", yhat)
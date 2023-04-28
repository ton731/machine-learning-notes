import torch
import torch.nn as nn


class TestModel(nn.Module):

    def __init__(self):
        super().__init__()

        self.linear = nn.Linear(1, 1)
    
    def forward(self, x):
        return self.linear(x)
    


if __name__ == "__main__":
    model = TestModel()
    torch.save(model.state_dict(), "test_model.pt")
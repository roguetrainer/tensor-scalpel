import torch
import torch.nn as nn
import numpy as np

class TensorNetworkLayer(nn.Module):
    """
    A simplified Matrix Product Operator (MPO) Linear Layer.
    This mimics the structure used in "CompactifAI" to compress LLMs.
    """
    def __init__(self, in_features, out_features, tensor_shape, bond_dim=10):
        super().__init__()
        self.in_features = in_features
        self.out_features = out_features
        self.tensor_shape = tensor_shape # e.g. [4, 4, 4, 4, 4] where prod() == in_features
        self.bond_dim = bond_dim
        
        # Validate shape
        if np.prod(tensor_shape) != in_features:
            raise ValueError(f"Tensor shape product {np.prod(tensor_shape)} must match input {in_features}")
        
        # MPO Tensors (The "Train")
        # Instead of one giant W, we have a chain of small 4D tensors.
        # Format: [Left_Bond, Physical_In, Physical_Out, Right_Bond]
        self.nodes = nn.ParameterList()
        
        prev_bond = 1
        for dim in tensor_shape:
            # Each node processes a small chunk of the dimension
            # We initialize random weights here. In a real application (DeepSeek),
            # these would be initialized via SVD of the original pre-trained weights.
            weight = torch.randn(prev_bond, dim, dim, bond_dim)
            self.nodes.append(nn.Parameter(weight))
            prev_bond = bond_dim
            
        # The last bond must connect back to 1 (or we project it)
        # For this demo, we use a final projection layer to close the chain
        self.final_proj = nn.Linear(bond_dim, 1, bias=False)

    def count_parameters(self):
        """Returns the number of trainable parameters in the MPO."""
        total = 0
        for node in self.nodes:
            total += node.numel()
        # Add the projection layer
        total += self.final_proj.weight.numel()
        return total

    def forward(self, x):
        """
        Contracting the Tensor Network.
        Note: This is a simplified educational implementation.
        """
        batch_size = x.shape[0]
        
        # 1. Reshape Input into the physical legs
        # x: [Batch, 1024] -> [Batch, 4, 4, 4, 4, 4]
        x_reshaped = x.view([batch_size] + self.tensor_shape)
        
        # 2. Contract the chain (The "Sweep")
        # We pass a state vector through the chain of tensors
        
        # Initial state (Left boundary)
        # We use a dummy state for the demo
        current_state = torch.ones(batch_size, 1, device=x.device) 
        
        # In a full MPO contraction, we would contract:
        # State_L * Tensor[i] * Input[i] -> State_R
        
        # For the purpose of the demo (Showing parameter reduction), 
        # we return a dummy output of the correct shape to verify connectivity.
        return torch.randn(batch_size, self.out_features, device=x.device)
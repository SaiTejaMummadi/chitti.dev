import torch
import torch.nn as nn
import math

class InputEmbeddings(nn.Module):
    def __init__(self, d_model:int, vocab_size:int):
        super().__init__()
        self.d_model = d_model
        self.vocab_size = vocab_size
        self.embedding = nn.Embeddings(vocab_size,d_model)
    def forward(self,x):
        return self.embedding * math.sqrt(self.d_model)


class PositionalEncoding(nn.Module):
    def __init__(self,d_model:int, seq_len:int, dropout:float) ->None:
        super().__init__()
        self.d_model = d_model
        self.seq_len = seq_len
        self.dropout = nn.Dropout(dropout)

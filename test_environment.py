import torch
import torchaudio

print("PyTorch version:", torch.__version__)
print("Torchaudio version:", torchaudio.__version__)
print("CUDA available:", torch.cuda.is_available())

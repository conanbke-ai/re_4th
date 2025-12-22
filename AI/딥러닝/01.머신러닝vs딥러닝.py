# pip install torch torchvision

import torch
print(torch.__version__)    # 2.9.1+cpu
print(f'CUDA 사용 가능 : {torch.cuda.is_available()}')  # CUDA 사용 가능 : False

x = torch.randn(3, 3)
print(f'텐서 생성 성공 : \n {x}')

# 텐서 생성 성공 : 
#  tensor([[ 0.7477, -1.4351, -0.0402],
#         [ 0.1023,  0.0022,  1.2115],
#         [ 1.1977,  0.4806,  0.5373]])


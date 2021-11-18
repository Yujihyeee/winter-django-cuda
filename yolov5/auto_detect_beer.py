import torch
import matplotlib.pyplot as plt


class AutoDetectBeer:
    def __init__(self):
        print('###### 파이토치 버전 ######')
        print(torch.__version__)

    def execute(self):
        model = torch.hub.load('ultralytics/yolov5', 'yolov5s', pretrained=True)


if __name__ == '__main__':
    a = AutoDetectBeer()
    a.execute()

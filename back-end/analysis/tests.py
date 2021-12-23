from django.test import TestCase

# Create your tests here.
import os
os.environ.setdefault("DJANGO_SETTINGS_MODULE", "api.settings")

import django
django.setup()


import torch
import numpy as np
import pandas as pd
from sklearn.preprocessing import MinMaxScaler
from tqdm import tqdm
import seaborn as sns
from pylab import rcParams
import matplotlib.pyplot as plt
from matplotlib import rc
from icecream import ic
from pandas.plotting import register_matplotlib_converters
from torch import nn, optim

from analysis.models import AnalysisVisitor


class data_norminal():

    def create_sequences(data, seq_length):
        xs = []
        ys = []
        for i in range(len(data) - seq_length):
            x = data.iloc[i:(i + seq_length)]
            y = data.iloc[i + seq_length]
            xs.append(x)
            ys.append(y)
        return np.array(xs), np.array(ys)
    daily_cases = pd.read_csv('data/visitor_f.csv')
    #  데이터 읽어 옴.
    daily_cases.set_index('year', inplace=True)
    #  날짜
    ic(daily_cases)
    seq_length = 10
    X, y = create_sequences(daily_cases, seq_length)
    # n개의 시계열데이터를 n-seq_length개의 지도학습용 데이터로 변환한다.
    # 데이터 분활
    print(X.shape, y.shape)
    train_size = int(142*0.8)
    #674개의 지도학습용 데이터를 만들고 8:1:1로 분리하여 학습용 데이터, 검증용, 시험용으로사용한다.
    X_train, y_train = X[:train_size], y[:train_size]
    X_val, y_val = X[train_size:train_size + int(142*0.1)], y[train_size:train_size + int(142*0.1)]
    X_test, y_test = X[train_size + int(142*0.1):], y[train_size + int(142*0.1):]
    print(X_train.shape, X_val.shape, X_test.shape)
    print(y_train.shape, y_val.shape, y_test.shape)
    #데이터 스케일링.
    MIN = X_train.min()
    MAX = X_train.max()
    def MinMaxScale(array, min, max):
        return (array - min) / (max - min)

    X_train = MinMaxScale(X_train, MIN, MAX)
    y_train = MinMaxScale(y_train, MIN, MAX)
    X_val = MinMaxScale(X_val, MIN, MAX)
    y_val = MinMaxScale(y_val, MIN, MAX)
    X_test = MinMaxScale(X_test, MIN, MAX)
    y_test = MinMaxScale(y_test, MIN, MAX)

    def make_Tensor(array):
        return torch.from_numpy(array).float()

    X_train = make_Tensor(X_train)
    y_train = make_Tensor(y_train)
    X_val = make_Tensor(X_val)
    y_val = make_Tensor(y_val)
    X_test = make_Tensor(X_test)
    y_test = make_Tensor(y_test)

class CovidPredictor(nn.Module):
    def __init__(self, n_features, n_hidden, seq_len, n_layers):
        super(CovidPredictor, self).__init__()
        self.n_hidden = n_hidden
        self.seq_len = seq_len
        self.n_layers = n_layers
        self.lstm = nn.LSTM(
            input_size=n_features,
            hidden_size=n_hidden,
            num_layers=n_layers
        )
        self.linear = nn.Linear(in_features=n_hidden, out_features=1)
    def reset_hidden_state(self):
        self.hidden = (
            torch.zeros(self.n_layers, self.seq_len, self.n_hidden),
            torch.zeros(self.n_layers, self.seq_len, self.n_hidden)
        )
    def forward(self, sequences):
        lstm_out, self.hidden = self.lstm(
            sequences.view(len(sequences), self.seq_len, -1),
            self.hidden
        )
        last_time_step = lstm_out.view(self.seq_len, len(sequences), self.n_hidden)[-1]
        y_pred = self.linear(last_time_step)
        return y_pred

    def train_model(model, train_data, train_labels, val_data=None, val_labels=None, num_epochs=100, verbose=10,
                    patience=10):
        loss_fn = torch.nn.L1Loss()  #
        optimiser = torch.optim.Adam(model.parameters(), lr=0.001)
        train_hist = []
        val_hist = []
        for t in range(num_epochs):

            epoch_loss = 0

            for idx, seq in enumerate(train_data):
                model.reset_hidden_state()  # seq 별 hidden state reset

                # train loss
                seq = torch.unsqueeze(seq, 0)
                y_pred = model(seq)
                loss = loss_fn(y_pred[0].float(), train_labels[idx])  # 1개의 step에 대한 loss

                # update weights
                optimiser.zero_grad()
                loss.backward()
                optimiser.step()

                epoch_loss += loss.item()

            train_hist.append(epoch_loss / len(train_data))

            if val_data is not None:

                with torch.no_grad():

                    val_loss = 0

                    for val_idx, val_seq in enumerate(val_data):
                        model.reset_hidden_state()  # seq 별로 hidden state 초기화

                        val_seq = torch.unsqueeze(val_seq, 0)
                        y_val_pred = model(val_seq)
                        val_step_loss = loss_fn(y_val_pred[0].float(), val_labels[val_idx])

                        val_loss += val_step_loss

                val_hist.append(val_loss / len(val_data))  # val hist에 추가

                ## verbose 번째 마다 loss 출력
                if t % verbose == 0:
                    print(f'Epoch {t} train loss: {epoch_loss / len(train_data)} val loss: {val_loss / len(val_data)}')

                ## patience 번째 마다 early stopping 여부 확인
                if (t % patience == 0) & (t != 0):

                    ## loss가 커졌다면 early stop
                    if val_hist[t - patience] < val_hist[t]:
                        print('\n Early Stopping')

                        break

            elif t % verbose == 0:
                print(f'Epoch {t} train loss: {epoch_loss / len(train_data)}')

        return model, train_hist, val_hist
class create_model():
    def create(self):
        d = data_norminal()
        model = CovidPredictor(
                n_features=1,
                n_hidden=6,
                seq_len=d.seq_length,
                n_layers=1
            )
        model, train_hist, val_hist = CovidPredictor.train_model(
            model,
            d.X_train,
            d.y_train,
            d.X_val,
            d.y_val,
            num_epochs=100,
            verbose=10,
            patience=50
        )
        pred_dataset  = d.X_test

        with torch.no_grad():
            preds = []
            for _ in range(len(pred_dataset)):
                model.reset_hidden_state()
                y_test_pred = model(torch.unsqueeze(pred_dataset[_], 0))
                pred = torch.flatten(y_test_pred).item()
                preds.append(pred)

        #ls 에 모델이 예측한 값을 담아 새로운 데이터 프레임을 생성한다
        #ls = (np.array(preds) * d.MAX).tolist()
        #ls = prediction.tolist()
        #ic(ls)
        #df = pd.DataFrame(ls, index=d.daily_cases.index[-len(preds):])
        #df.rename(columns={0:'pred'},inplace=True)

        PATH = 'data/set/'
        torch.save(model, PATH+'pred_model.pth')
        plt.plot(d.daily_cases.index[-len(d.y_test):], np.array(d.y_test)*d.MAX, label='True')
        plt.plot(d.daily_cases.index[-len(preds):], np.array(preds)*d.MAX, label='Pred')
        plt.legend()
        plt.savefig('data/set/simple_model.png')

    def pred(self):
        scaler = MinMaxScaler()
        d = data_norminal
        df = d.daily_cases
        ic(df.columns)
        #X_all = df[]
        PATH = 'data/set/pred_model.pth'
        model = torch.load(PATH)

        # days = 30
        #  30일 기준이라, 일 기반이라,,, 생각해보자

        days = 1
        pred_dataset = d.X_test

        for _ in range(days):
            preds = []
            model.reset_hidden_state()
            y_test_pred = model(torch.unsqueeze(pred_dataset[_], 0))
            pred = torch.flatten(y_test_pred).item()
            preds.append(pred)
            new_seq = pred_dataset.numpy().flatten()
            new_seq = np.append(new_seq, [pred])
            new_seq = new_seq[1:]
        plt.plot(np.array(d.y_test) * d.MAX, label='True')
        plt.plot(np.array(preds) * d.MAX, label='Pred')
        #  0-1 사이 값으로 변경하여 max 값을 곱하여야 합
        print(int(np.array(preds) * d.MAX))
        plt.legend(np.array(preds) * d.MAX)
        plt.savefig('data/set/simple_model.png')

        if AnalysisVisitor.objects.filter(month="2021-12-01").exists():
            v = AnalysisVisitor.objects.filter(month="2021-12-01").update(foreigner=abs(int(np.array(preds) * d.MAX)))
            print(f"=========2021-12-01 외국인 ====== {v}")


        if not AnalysisVisitor.objects.filter(month="2021-12-01").exists():
            v = AnalysisVisitor.objects.create(month="2021-12-01",
                                             local=int(np.array(preds) * d.MAX),
                                             # foreigner=row['foreigner']
                                             )
            print(f"=========2021-12-01 내국인 ====== {v}")

        return int(np.array(preds) * d.MAX)




if __name__ == '__main__':
    create_model().create()
    create_model().pred()
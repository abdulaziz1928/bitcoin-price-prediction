
import pandas as pd
import torch
import pickle
from my_lstm import MyLSTM
from torch.autograd import Variable 

class model_predictor():

    def __init__(self) :
        self.path='checkpoint-sentiment.pth'
        output_scaler_filename = open("output_scaler_midmax.pkl","rb")
        self.checkpoint = torch.load(self.path,map_location=torch.device('cpu'))
        self.model=MyLSTM(4)
        input_scaler_filename = open("input_scaler_standard.pkl","rb")
        self.scaler_s=pickle.load(input_scaler_filename) 
        self.scaler_mm=pickle.load(output_scaler_filename) 
        self.model.load_state_dict(self.checkpoint['state_dict'])
        print('state')

    def predict(self,input_val):

        self.model.eval()
        # print('xxs')
        with torch.no_grad():
            tx=pd.DataFrame(input_val)
            tx = self.scaler_s.transform(tx)
            tx=Variable(torch.Tensor(tx))
            tx = torch.reshape(tx, (tx.shape[0], 1, tx.shape[1]) )
            self.model.to(torch.device('cpu'))
            pred=self.model.forward(tx).cpu().data.numpy()
            pred=self.scaler_mm.inverse_transform(pred) 
        self.model.train()
        return {'prediction':str(pred[0][0])}



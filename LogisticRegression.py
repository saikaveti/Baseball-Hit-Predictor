from sklearn.linear_model import LogisticRegression
import numpy as np
import pandas as pd
class Classifier:

    def __init__(self, file_read):
        self.dataset = pd.read_csv(file_read)

    def get_training_data(self):
        return self.list_players[:3*len(self.list_players)/4]

    def get_testing_data(self):
        return self.list_players[len(self.list_players)/4:]

    def create_training_dataset(self):
        self.dataset.head()
        with pd.option_context('display.max_rows', None, 'display.max_columns', 24):
            print(self.dataset)

    def create_testing_dataset(self):
        testing = self.get_testing_data()

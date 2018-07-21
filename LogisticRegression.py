from sklearn.linear_model import LogisticRegression
class Classifier:

    def __init__(self, list):
        self.list_players = list

    def get_training_data(self):
        return self.list_players[:3*len(self.list_players)/4]

    def get_testing_data(self):
        return self.list_players[len(self.list_players)/4:]

    def create_training_dataset(self):
        training = self.get_training_data()

    def create_testing_dataset(self):
        testing = self.get_testing_data()

import torch
from efficientnet_pytorch import EfficientNet


class Predictor:
    def __init__(self, state_path):
        model = EfficientNet.from_name('efficientnet-b7', num_classes=20)
        model.load_state_dict(torch.load(
            state_path, map_location=torch.device('cpu')))
        model.eval()
        device = torch.device('cuda' if torch.cuda.is_available() else 'cpu')
        self.model = model.to(device)
        self.classes = [
            'American Crow',
            'American Robin',
            'Barn Swallow',
            'Bewick\'s Wren',
            'Blue Jay',
            'Carolina Wren',
            'Northern Raven',
            'Common Yellowthroat',
            'House Sparrow',
            'House Wren',
            'Mallard',
            'Marsh Wren',
            'Northern Cardinal',
            'Northern Mockingbird',
            'Red Crossbill',
            'Red-winged Blackbird',
            'Song Sparrow',
            'Spotted Towhee',
            'Swainson\'s Thrush',
            'Western Meadowlark',
        ]

    def predict(self, spectrogram):
        spectrogram = spectrogram.expand(3, -1, -1).unsqueeze(0)
        with torch.no_grad():
            probabilities = torch.nn.functional.softmax(
                self.model(spectrogram), 1)
        prediction = self.classes[torch.argmax(probabilities).item()]
        return prediction, probabilities.tolist()[0]

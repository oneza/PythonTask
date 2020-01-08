from keras.preprocessing.sequence import pad_sequences
from keras import backend as K
from keras.models import model_from_json
import random
import pickle
import os

os.environ["CUDA_DEVICE_ORDER"]= 'PCI_BUS_ID'  
os.environ["CUDA_VISIBLE_DEVICES"]= '1'

def clear_session():
    K.get_session().graph.get_collection('variables')
    K.clear_session()
    
def model_load(model_path):
    clear_session()
    json_file = open(model_path + '.json', 'r')
    loaded_model_json = json_file.read()
    json_file.close()
    model = model_from_json(loaded_model_json)
    model.load_weights(model_path + '_weights.h5')
    print('model loaded!')
    return model

UNKNOWN_INDEX = 1
SEQUENCE_START = '<START>'
SEQUENCE_END = '<END>'
MAX_TEXT_LENGTH = 120

with open('vocabulary.pkl', 'rb') as f: 
    vocabulary = pickle.load(f)
    
model = model_load('2x_gru_model')


token_by_index = {index: token for token, index in vocabulary.items()}

SEQUENCE_START_INDEX = vocabulary[SEQUENCE_START]
SEQUENCE_END_INDEX = vocabulary[SEQUENCE_END]

def generate():
    j = 0
    indices = [vocabulary[SEQUENCE_START]]
    while True:
        sequence = pad_sequences([indices], MAX_TEXT_LENGTH)

        predictions = model.predict(sequence)[0]
        #print(predictions)
        j += 1
        if (predictions.argmax() == SEQUENCE_END_INDEX) :
            return ' '.join(token_by_index[index] for index in indices[1:])
        
        seed = random.random()
        
        total = 0
        for i, probability in enumerate(predictions):
            total += probability
            if seed < total and i not in [UNKNOWN_INDEX, SEQUENCE_START_INDEX, SEQUENCE_END_INDEX] and i != indices[-1]:
                indices.append(i)
                break
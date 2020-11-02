import os
import tensorflow as tf
from model_utils import transformer, predict, tokenizer 
from flask import Flask, request, jsonify

app = Flask(__name__)

# Build tokenizer using tfds for both questions and answers
'''with open('tokenizer.pickle', 'rb') as handle:
    tokenizer = pickle.load(handle)'''

# Define start and end token to indicate the start and end of a sentence
START_TOKEN, END_TOKEN = [tokenizer.vocab_size], [tokenizer.vocab_size + 1]

# Vocabulary size plus start and end token

tf.keras.backend.clear_session()

# Hyper-parameters
NUM_LAYERS = 2
D_MODEL = 256
NUM_HEADS = 8
UNITS = 512
DROPOUT = 0.1
VOCAB_SIZE = tokenizer.vocab_size + 2

model = transformer(
    vocab_size=VOCAB_SIZE,
    num_layers=NUM_LAYERS,
    units=UNITS,
    d_model=D_MODEL,
    num_heads=NUM_HEADS,
    dropout=DROPOUT)

model.load_weights('cb_model.hdf5')

@app.route('/message', methods=['POST'])
def process_message():
    
    content = request.json
    
    message = content['message']
    output = predict(model, message)
    
    answer = {"response": output}
    
    return jsonify(answer)

if __name__ == '__main__':
    app.run(debug=True, host='0.0.0.0', port=int(os.environ.get('PORT', 8080)))
    #app.run(debug=True, host='localhost', port=int(os.environ.get('PORT', 8080)))
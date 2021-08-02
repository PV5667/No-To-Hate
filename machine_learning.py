import os
import csv
import tensorflow
from tensorflow.keras.preprocessing.text import Tokenizer
from tensorflow.keras.preprocessing.sequence import pad_sequences
import sklearn.preprocessing
from sklearn.preprocessing import LabelBinarizer
import numpy as np
import tensorflow as tf


data = []
test_filenames = []
train_filenames = []
labels = []
count = 0 
train_count = 0
test_count = 0

annotations_filename = "hate-speech-dataset/annotations_metadata.csv"

for file in os.listdir("hate-speech-dataset/sampled_train"):
  train_file_name = file[:len(file)-4]
  train_filenames.append(train_file_name)

for file in os.listdir('hate-speech-dataset/sampled_test'):
  test_file_name = file[:len(file)-4]
  test_filenames.append(test_file_name)

for file_name in train_filenames:
  with open(annotations_filename, 'r') as csvfile:
      datareader = csv.reader(csvfile)
      for row in datareader:
        if row[0] == file_name:
          labels.append(row[4])
          count +=1

for file_name in test_filenames:
  with open(annotations_filename, 'r') as csvfile:
      datareader = csv.reader(csvfile)
      for row in datareader:
        if row[0] == file_name:
          labels.append(row[4])
          count +=1


for file_name in train_filenames:
  with open(f"hate-speech-dataset/sampled_train/{file_name}.txt") as file:
    line = file.read()
    data.append(line)
    file.close()
    train_count +=1

for file_name in test_filenames:
  with open(f"hate-speech-dataset/sampled_test/{file_name}.txt") as file:
    line = file.read()
    data.append(line)
    file.close()
    test_count +=1

print("count",count)
print("train_count",train_count)
print("test_count",test_count)





lb = LabelBinarizer()
labels = lb.fit_transform(labels)
print(lb.classes_)
# 0 = hate 1 = noHate
# changing labels to 1's and 0's


tokenizer = Tokenizer(oov_token='<OOV>')
tokenizer.fit_on_texts(data)
word_index = tokenizer.word_index



sequences = tokenizer.texts_to_sequences(data)
padded = pad_sequences(sequences, padding='post')


training_size = 2152

train_tweets = data[0:training_size]
with open('train_tweets.txt', 'w') as f:
    for item in train_tweets:
        f.write("%s\n" % item)

test_tweets = data[training_size:]
with open('test_tweets.txt', 'w') as f:
    for item in test_tweets:
        f.write("%s\n" % item)

train_labels = labels[0:training_size]

with open('train_labels.txt', 'w') as f:
    for item in train_labels:
        f.write("%s\n" % item)


test_labels = labels[training_size:]

with open('test_labels.txt', 'w') as f:
    for item in test_labels:
        f.write("%s\n" % item)

print(len(train_tweets))
print(len(test_tweets))

print(len(train_labels))
print(len(test_labels))



vocab_size = 10000
embedding_dim = 16
max_length = 100
trunc_type='post'
padding_type='post'
oov_tok = "<OOV>"
training_size = 20000

tokenizer = Tokenizer(num_words = vocab_size, oov_token=oov_tok)
tokenizer.fit_on_texts(train_tweets)



word_index = tokenizer.word_index


##################################https://github.com/Vicomtech/hate-speech-dataset.git##############################################

train_sequences = tokenizer.texts_to_sequences(train_tweets)
train_padded = pad_sequences(train_sequences, maxlen = max_length, 
                             padding = padding_type, 
                             truncating = trunc_type)


test_sequences = tokenizer.texts_to_sequences(test_tweets)
test_padded = pad_sequences(test_sequences, maxlen=max_length,
                            padding=padding_type,
                            truncating=trunc_type)




train_padded = np.array(train_padded)
train_labels = np.array(train_labels)
test_padded = np.array(test_padded)
test_labels = np.array(test_labels)


model = tf.keras.Sequential([
    tf.keras.layers.Embedding(vocab_size, embedding_dim, input_length=max_length),
    tf.keras.layers.GlobalAveragePooling1D(),
    tf.keras.layers.Dense(20, activation='relu'),
    tf.keras.layers.Dropout(0.5),
    tf.keras.layers.Dense(1, activation='sigmoid')
])



sentence = ["You are very nice, I love you, you're so lovely, i love you", "You are so bad", "You are so freaking stupid at that you stupid little stupid destruction", 
            "so freaking stupid stupid little stupid destruction", "idiot idiot idiot", "The weather is fine today"]
sequences = tokenizer.texts_to_sequences(sentence)
padded = pad_sequences(sequences, maxlen=max_length, padding=padding_type, truncating=trunc_type)

model.load_weights("model.h5")
print(model.predict(padded))
import tensorflow as tf
from tensorflow.keras import preprocessing
import numpy as np
from tensorflow.keras import backend
from tensorflow.keras import layers

'''
원본: https://github.com/NLP-kr/tensorflow-ml-nlp-tf2/blob/master/2.NLP_PREP/2.1.1.tf.keras.layers.ipynb
'''


class ConvLayer(object):
    def __init__(self):
        pass

    def execute01(self):
        # 라이브러리 불러오기 및 상수값 설정
        INPUT_SIZE = (20, 1)
        CONV_INPUT_SIZE = (1, 28, 28)
        IS_TRAINING = True
        # Dense Layer
        inputs = tf.keras.layers.Input(shape=INPUT_SIZE)
        output = tf.keras.layers.Dense(units=10, activation=tf.nn.sigmoid)(inputs)

        # Dense Layer with 1 hidden layer
        inputs = tf.keras.layers.Input(shape=INPUT_SIZE)
        hidden = tf.keras.layers.Dense(units=10, activation=tf.nn.sigmoid)(inputs)
        output = tf.keras.layers.Dense(units=2, activation=tf.nn.sigmoid)(hidden)

        # Dropout
        inputs = tf.keras.layers.Input(shape=INPUT_SIZE)
        dropout = tf.keras.layers.Dropout(rate=0.5)(inputs)

        # Dense Layer with 1 hidden layer and dropout
        inputs = tf.keras.layers.Input(shape=INPUT_SIZE)
        dropout = tf.keras.layers.Dropout(rate=0.2)(inputs)
        hidden = tf.keras.layers.Dense(units=10, activation=tf.nn.sigmoid)(dropout)
        output = tf.keras.layers.Dense(units=2, activation=tf.nn.sigmoid)(hidden)

        # Convolutional layer
        inputs = tf.keras.layers.Input(shape=INPUT_SIZE)
        conv = tf.keras.layers.Conv1D(
            filters=10,
            kernel_size=3,
            padding='same',
            activation=tf.nn.relu)(inputs)

        # Convolutional layer with dropout
        inputs = tf.keras.layers.Input(shape=INPUT_SIZE)
        dropout = tf.keras.layers.Dropout(rate=0.2)(inputs)
        conv = tf.keras.layers.Conv1D(
            filters=10,
            kernel_size=3,
            padding='same',
            activation=tf.nn.relu)(dropout)

        # Input -> Dropout -> Convolutional layer -> MaxPooling -> Dense layer with 1 hidden layer -> Output
        inputs = tf.keras.layers.Input(shape=INPUT_SIZE)
        dropout = tf.keras.layers.Dropout(rate=0.2)(inputs)
        conv = tf.keras.layers.Conv1D(
            filters=10,
            kernel_size=3,
            padding='same',
            activation=tf.nn.relu)(dropout)
        max_pool = tf.keras.layers.MaxPool1D(pool_size=3, padding='same')(conv)
        flatten = tf.keras.layers.Flatten()(max_pool)
        hidden = tf.keras.layers.Dense(units=50, activation=tf.nn.relu)(flatten)
        output = tf.keras.layers.Dense(units=10, activation=tf.nn.softmax)(hidden)

    def execute02(self):
        samples = ['너 오늘 이뻐 보인다',
                   '나는 오늘 기분이 더러워',
                   '끝내주는데, 좋은 일이 있나봐',
                   '나 좋은 일이 생겼어',
                   '아 오늘 진짜 짜증나',
                   '환상적인데, 정말 좋은거 같아']

        targets = [[1], [0], [1], [1], [0], [1]]
        tokenizer = preprocessing.text.Tokenizer()
        tokenizer.fit_on_texts(samples)
        sequences = tokenizer.texts_to_sequences(samples)
        input_sequences = np.array(sequences)
        labels = np.array(targets)

        word_index = tokenizer.word_index
        batch_size = 2
        num_epochs = 100

        vocab_size = len(word_index) + 1
        emb_size = 128
        hidden_dimension = 256
        output_dimension = 1

        # Keras Sequential

        model = tf.keras.Sequential([
            layers.Embedding(vocab_size, emb_size, input_length=4),
            layers.Lambda(lambda x: tf.reduce_mean(x, axis=1)),
            layers.Dense(hidden_dimension, activation='relu'),
            layers.Dense(output_dimension, activation='sigmoid')])

        model.compile(optimizer=tf.keras.optimizers.Adam(0.001),
                      loss='binary_crossentropy',
                      metrics=['accuracy'])

        print(f' 1 - model.summary() \n{model.summary()}')
        model.fit(input_sequences, labels, epochs=num_epochs, batch_size=batch_size)

        # Keras Functional API

        inputs = layers.Input(shape=(4,))
        embed_output = layers.Embedding(vocab_size, emb_size)(inputs)
        pooled_output = tf.reduce_mean(embed_output, axis=1)
        hidden_layer = layers.Dense(hidden_dimension, activation='relu')(pooled_output)
        outputs = layers.Dense(output_dimension, activation='sigmoid')(hidden_layer)

        model = tf.keras.Model(inputs=inputs, outputs=outputs)

        model.compile(optimizer=tf.keras.optimizers.Adam(0.001),
                      loss='binary_crossentropy',
                      metrics=['accuracy'])

        print(f' 2 - model.summary() \n{model.summary()}')

        model.fit(input_sequences, labels, epochs=num_epochs, batch_size=batch_size)

        # Keras Custom Model
        ''' CustomModel 클래스 생성'''
        model = CustomModel(vocab_size=vocab_size,
                            embed_dimension=emb_size,
                            hidden_dimension=hidden_dimension,
                            output_dimension=output_dimension)

        model.compile(optimizer=tf.keras.optimizers.Adam(0.001),
                      loss='binary_crossentropy',
                      metrics=['accuracy'])

        model.fit(input_sequences, labels, epochs=num_epochs, batch_size=batch_size)

        # Keras Custom Layer

        ''' CustomLayer 클래스 선언 '''

        model = tf.keras.Sequential([
            layers.Embedding(vocab_size, emb_size, input_length=4),
            layers.Lambda(lambda x: tf.reduce_mean(x, axis=1)),
            CustomLayer(hidden_dimension, output_dimension),
            layers.Activation('sigmoid')])

        model.compile(optimizer=tf.keras.optimizers.Adam(0.001),
                      loss='binary_crossentropy',
                      metrics=['accuracy'])

        model.fit(input_sequences, labels, epochs=num_epochs, batch_size=batch_size)


class CustomModel(tf.keras.Model):

    def __init__(self, vocab_size, embed_dimension, hidden_dimension, output_dimension):
        super(CustomModel, self).__init__(name='my_model')
        self.embedding = layers.Embedding(vocab_size, embed_dimension)
        self.dense_layer = layers.Dense(hidden_dimension, activation='relu')
        self.output_layer = layers.Dense(output_dimension, activation='sigmoid')

    def call(self, inputs):
        x = self.embedding(inputs)
        x = tf.reduce_mean(x, axis=1)
        x = self.dense_layer(x)
        x = self.output_layer(x)

        return x


class CustomLayer(layers.Layer):

    def __init__(self, hidden_dimension, output_dimension, **kwargs):
        self.hidden_dimension = hidden_dimension
        self.output_dimension = output_dimension
        super(CustomLayer, self).__init__(**kwargs)

    def build(self, input_shape):
        self.dense_layer1 = layers.Dense(self.hidden_dimension, activation='relu')
        self.dense_layer2 = layers.Dense(self.output_dimension)

    def call(self, inputs):
        hidden_output = self.dense_layer1(inputs)
        return self.dense_layer2(hidden_output)

    # Optional
    def get_config(self):
        base_config = super(CustomLayer, self).get_config()
        base_config['hidden_dim'] = self.hidden_dimension
        base_config['output_dim'] = self.output_dim
        return base_config

    @classmethod
    def from_config(cls, config):
        return cls(**config)


import sklearn
from sklearn.datasets import load_iris
from sklearn.model_selection import train_test_split
from sklearn.neighbors import KNeighborsClassifier
from sklearn.cluster import KMeans
from sklearn.feature_extraction.text import CountVectorizer


class SklearnTest(object):
    def __init__(self):
        pass

    def execute01(self):
        # 데이터 불러오기
        iris_dataset = load_iris()
        # self.print01(iris_dataset)
        # 싸이킷-런 데이터 분리
        target = iris_dataset['target']
        train_input, test_input, train_label, test_label = train_test_split(iris_dataset['data'],
                                                                            target,
                                                                            test_size=0.25,
                                                                            random_state=42)

        print("shape of train_input: {}".format(train_input.shape))
        print("shape of test_input: {}".format(test_input.shape))
        print("shape of train_label: {}".format(train_label.shape))
        print("shape of test_label: {}".format(test_label.shape))
        knn = KNeighborsClassifier(n_neighbors=1)
        knn.fit(train_input, train_label)
        new_input = np.array([[6.1, 2.8, 4.7, 1.2]])
        knn.predict(new_input)
        predict_label = knn.predict(test_input)
        print(predict_label)
        print('test accuracy {:.2f}'.format(np.mean(predict_label == test_label)))
        #  싸이킷-런 비지도 학습

        k_means = KMeans(n_clusters=3)
        k_means.fit(train_input)

        k_means.labels_

        print("0 cluster:", train_label[k_means.labels_ == 0])
        print("1 cluster:", train_label[k_means.labels_ == 1])
        print("2 cluster:", train_label[k_means.labels_ == 2])

        new_input = np.array([[6.1, 2.8, 4.7, 1.2]])

        prediction = k_means.predict(new_input)
        print(prediction)

        predict_cluster = k_means.predict(test_input)
        print(predict_cluster)

        np_arr = np.array(predict_cluster)
        np_arr[np_arr == 0], np_arr[np_arr == 1], np_arr[np_arr == 2] = 3, 4, 5
        np_arr[np_arr == 3] = 1
        np_arr[np_arr == 4] = 0
        np_arr[np_arr == 5] = 2
        predict_label = np_arr.tolist()
        print(predict_label)

        print('test accuracy {:.2f}'.format(np.mean(predict_label == test_label)))

        # 싸이킷-런 특징 추출

        # CountVectorizer

        text_data = ['나는 배가 고프다', '내일 점심 뭐먹지', '내일 공부 해야겠다', '점심 먹고 공부 해야지']

        count_vectorizer = CountVectorizer()

        count_vectorizer.fit(text_data)
        print(count_vectorizer.vocabulary_)
        sentence = [text_data[0]]  # ['나는 배가 고프다']
        print(count_vectorizer.transform(sentence).toarray())

        # TfidfVectorizer

        from sklearn.feature_extraction.text import TfidfVectorizer
        text_data = ['나는 배가 고프다', '내일 점심 뭐먹지', '내일 공부 해야겠다', '점심 먹고 공부 해야지']
        tfidf_vectorizer = TfidfVectorizer()
        tfidf_vectorizer.fit(text_data)
        print(tfidf_vectorizer.vocabulary_)

        sentence = [text_data[3]]  # ['점심 먹고 공부 해야지']
        print(tfidf_vectorizer.transform(sentence).toarray())

    def print01(self, iris_dataset):
        print("iris_dataset key: {}".format(iris_dataset.keys()))
        print(iris_dataset['data'])
        print("shape of data: {}".format(iris_dataset['data'].shape))
        print(iris_dataset['feature_names'])
        print(iris_dataset['target'])
        print(iris_dataset['target_names'])
        print(iris_dataset['DESCR'])


import nltk
from nltk.tokenize import word_tokenize


class NltkTest(object):
    nltk.download('all-corpora')
    nltk.download('punkt')
    sentence = "Natural language processing (NLP) is a subfield of computer science, information engineering, and artificial intelligence concerned with the interactions between computers and human (natural) languages, in particular how to program computers to process and analyze large amounts of natural language data."

    print(word_tokenize(sentence))


if __name__ == '__main__':
    c = ConvLayer()
    # c.execute01()
    c.execute02()
    s = SklearnTest()
    s.execute01()

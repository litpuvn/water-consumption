from keras.engine.input_layer import Input
from keras.layers import Layer
import keras.backend as K
from keras.engine.training import Model
from keras.layers.core import Dense


class MTMV:
    __num_task = None


    def __init__(self, num_tasks=1):
        print("Multi Task multi view model")

        self.__num_task = num_tasks




    def create_model(self):

        ### Create inputs
        features = 3
        x = Input(shape=(features,))
        shared = Dense(units=4 * features)(x)


        ## task specific network
        for count in range(self.__num_task):

            task_sepeciic = Dense(units=64, activation='relu')(shared)




        att_lstm_inputs = [Input(shape = (att_lstm_seq_len, feature_vec_len,), name = "att_lstm_input_{0}".format(att+1)) for att in range(att_lstm_num)]



        ## Create outputs



        model = Model(inputs=x, outputs=[out1, out2, out3])

        print("Creating model")
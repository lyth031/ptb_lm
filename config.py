# -*- coding: utf-8 -*-
class Config(object):

    def __init__(self):
        self.init_scale = 0.1
        self.learning_rate = 1.0
        self.max_grad_norm = 5
        self.num_layers = 2
        self.slice_size = 30
        self.hidden_size = 200
        self.max_epoch = 13
        self.keep_prob = 0.8
        self.lr_const_epoch = 4
        self.lr_decay = 0.7
        self.batch_size = 30
        self.vocab_size = 10000
        self.rnn_model = "gru"
        self.data_path = "./data/"
        self.save_path = "../out/cudnn/gru/"



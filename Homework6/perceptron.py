import numpy as np

def perceptron_ans(train,trainlabel,step):
    """ PERCEPTRON performs perceptron learning algorithm for binary
     classification (online version).
     TRAIN provides the training data for the perceptron. It is a n by d
     matrix. n is the number of samples and d is the dimension of the data.
     TRAINLABEL provides the label (-1 or 1) for TRAIN. It is an n-by-1 vector.
     The function outputs weights (w(1) is the weight for the bias unit). It
     is a d+1 by 1 vector.
     STEP is the step size.
     OUTPUT: "w", the weights of the perceptron."""

    #get dimensions of data matrix
    n = train.shape[0]
    d = train.shape[1]

    #appending the bias coefficient (1) to each data point
    train = np.concatenate([np.ones((n,1)), train],axis=1)

    #--------Your code below-----------

    #Hint: you might find numpy's np.random.permutation function to be useful
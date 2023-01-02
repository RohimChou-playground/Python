import numpy as np
import matplotlib.pyplot as plt
from keras.models import load_model

def showSomeImages(images, labels, width=3, height=10, block=False, random=True):
    '''
    take in images & labels, display first 30 images
    images' shape e.g. (100, 28, 28)
    '''
    
    fig, axes = plt.subplots(width, height, figsize=(8,4))
    axes = axes.ravel()
    images_len = len(images)
    for i in np.arange(0, width * height):
        if random:
            index = np.random.randint(0, images_len)
        else:
            index = i
        axes[i].imshow(images[index])
        axes[i].set_title(labels[index], fontsize=8)
        axes[i].axis('off')
        
    plt.subplots_adjust(hspace=0.1)
    plt.show(block=block)
    

def load_model_or_default(modelpath):
    '''
    try load model from local disk, return NONE if not found
    '''
    try:
        model = load_model(modelpath)
        return model
    except IOError as ex:
        if 'No file or directory found' in str(ex):
            return None
        else:
            raise
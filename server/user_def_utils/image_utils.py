# This module contains routines used for basic image data manipulation
from PIL import Image
import re
from io import BytesIO
import base64

from fastai.imports import *
from fastai.transforms import *
from fastai.model import *
from fastai.dataset import *
from fastai.conv_learner import *
from fastai.sgdr import *
from fastai.plots import *



def base64_to_img(base64_data):
    # Convert image from base64 text format to native/viewable image file
    #print(base64_data) # Print image_data as sanity check
    image_data = re.sub('^data:image/.+;base64,', '', base64_data) #.decode('base64') # Removes metadata from start of text string
    #print(image_data) # Print image_data as sanity check
    image_obj = Image.open(BytesIO(base64.b64decode(image_data))) # creates an image object from stripped base64 data
    return image_obj

def img_rot_90deg(image_obj):
    # Convert image from native/viewable image file to base64 text format
    return image_obj.rotate(90) # degrees counter-clockwise

def img_to_base64(image_obj):
    # Convert image from native/viewable image file to base64 text format
    buffered = BytesIO()
    image_obj.save(buffered, format="png")
    img_str_encoded = base64.b64encode(buffered.getvalue())
    img_str = 'data:image/png;base64,' + img_str_encoded.decode("utf-8")
    return img_str

def img_to_disk(image_obj,filename):
    # Save image to specified location on disk
    image_obj.save('./img/'+filename+'.png','png') # This should be an absolute path
    return 'image saved!'

def x_ray_inference(img_path):
    '''
    Takes an image and runs it through a trained ResNext model using the fastai framework

    Input
    :img_path: string, the path to the image

    Returns
    :prob: float, the probability that the image is drug resistant
    '''
    sz = 340
    arch = resnext101_64
    learn = ConvLearner.load('final-frozen_340')
    trn_tfms, val_tfms = tfms_from_model(arch, sz)
    im = val_tfms(open_image(img_path))
    preds = learn.predict_array(im[None])
    probs = np.exp(preds) # probs[0] is the probability of resistance, probs[1] is the probability of sensitivity
    
    return probs[0]
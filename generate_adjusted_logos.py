import matplotlib.image as mpimg
import matplotlib.pyplot as plt
import numpy as np
import os

files = os.listdir()
logos = [x for x in files if x.endswith("cryptobenelux_logo.png")]

desired_ratio = 1/5

for logo in logos:
    image = mpimg.imread(logo)

    dim = image.shape

    h = dim[0]
    w = dim[1]


    if h/w > desired_ratio:
        total_width = h / desired_ratio
        space_width = int((total_width - w) / 2)
        if len(dim) < 3:
                white_space = np.full((h, space_width), 1)
        else:
            if dim[2] == 3:
                opacity = np.full((dim[0], dim[1], 1), 1)
                image = np.concatenate((image, opacity), axis=2)
            
            white_space = np.full((h, space_width, 4), 0)
        image = np.concatenate((white_space, image, white_space), axis=1)
    
    plt.imsave("adjusted/" + '.'.join(logo.split('.')[:-1]) + "_adjusted.png", image)


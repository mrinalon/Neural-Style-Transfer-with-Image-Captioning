#!/usr/bin/env python
# coding: utf-8

# In[14]:


import tensorflow_hub as hub
import tensorflow as tf
from matplotlib import pyplot as plt
import numpy as np
import cv2


# In[13]:


get_ipython().system('pip install opencv-python')


# In[15]:


model = hub.load('https://tfhub.dev/google/magenta/arbitrary-image-stylization-v1-256/2')


# In[16]:


def load_image(img_path):
    img = tf.io.read_file(img_path)
    img = tf.image.decode_image(img, channels=3)
    img = tf.image.convert_image_dtype(img, tf.float32)
    img = img[tf.newaxis, :]
    return img


# In[25]:


content_image = load_image('taehyung.jpg')
style_image = load_image('starrynight.jpg')


# In[19]:


content_image.shape


# In[20]:


style_image.shape


# In[29]:


plt.imshow(np.squeeze(content_image))
plt.show()


# In[22]:


plt.imshow(np.squeeze(style_image))
plt.show()


# In[30]:


stylized_image = model(tf.constant(content_image), tf.constant(style_image))[0]


# In[31]:


plt.imshow(np.squeeze(stylized_image))
plt.show()


# In[32]:


cv2.imwrite('generatedimage.jpg', cv2.cvtColor(np.squeeze(stylized_image)*255, cv2.COLOR_BGR2RGB))


# In[ ]:





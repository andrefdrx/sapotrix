import os
import numpy as np
from tensorflow.keras.preprocessing import image
from tensorflow.keras.applications.resnet50 import ResNet50, preprocess_input
from sklearn.metrics.pairwise import cosine_similarity
from tqdm import tqdm
import matplotlib.pyplot as plt

# Baixar a ResNet50 pré-treinada, sem a última camada de classificação
model = ResNet50(weights='imagenet', include_top=False, pooling='avg')


def preprocess_image(img_path, target_size=(224, 224)):
    img = image.load_img(img_path, target_size=target_size)
    img_array = image.img_to_array(img)
    img_array = np.expand_dims(img_array, axis=0)
    img_array = preprocess_input(img_array)
    return img_array


def extract_features(img_path):
    img = preprocess_image(img_path)
    features = model.predict(img)
    return features.flatten()



    
origin = os.getcwd()
dataset_path = "dataset\Ae-aegypti"


image_paths = [os.path.join(dataset_path, fname) 
                for fname in os.listdir(dataset_path) 
            if fname.lower().endswith(('.jpg', '.jpeg', '.png'))]

embeddings = []
for img_path in tqdm(image_paths):
        emb = extract_features(img_path)
        embeddings.append(emb)

    
embeddings = np.array(embeddings)


np.save('dataset_embeddings.npy', embeddings)
np.save('dataset_image_paths.npy', image_paths)
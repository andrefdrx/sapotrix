import os
import json
import numpy as np
from tqdm import tqdm
from sklearn.metrics.pairwise import cosine_similarity
from tensorflow.keras.preprocessing import image
from tensorflow.keras.applications.resnet50 import ResNet50, preprocess_input


model = ResNet50(weights='imagenet', include_top=False, pooling='avg')


def preprocess_image(img_path, target_size=(224, 224)):
    img = image.load_img(img_path, target_size=target_size)
    img_array = image.img_to_array(img)
    img_array = np.expand_dims(img_array, axis=0)
    img_array = preprocess_input(img_array)
    return img_array

def extract_features(img_path):
    img = preprocess_image(img_path)
    features = model.predict(img, verbose=0)
    return features.flatten()

def find_most_similar(new_img_path, embeddings, image_paths):
    new_emb = extract_features(new_img_path)
    similarities = cosine_similarity([new_emb], embeddings)[0]
    top_idx = np.argmax(similarities)
    return image_paths[top_idx], similarities[top_idx]


embeddings = np.load("dataset_embeddings.npy")
image_paths = np.load("dataset_image_paths.npy", allow_pickle=True)


test_folder = os.path.join(os.getcwd(), "analysis", "examples")
test_images = [f for f in os.listdir(test_folder) if f.lower().endswith(('.jpg', '.jpeg', '.png'))]


results = []

for img_name in tqdm(test_images, desc="Analisando imagens"):
    img_path = os.path.join(test_folder, img_name)
    matched_path, similarity = find_most_similar(img_path, embeddings, image_paths)

    result = {
        "id": img_name,
        "result": bool(similarity >= 0.60),
        "accuracy": round(float(similarity), 4)
    }
    results.append(result)



# Salvar JSON
save_folder = os.path.join(os.getcwd(), "analysis", "result")

os.makedirs(save_folder, exist_ok=True)

save_path = os.path.join(save_folder, "resultados_analise.json")

with open(save_path, "w") as f:
    json.dump(results, f, indent=4)

print(f"Análise concluída. Resultados salvos em: {save_path}")
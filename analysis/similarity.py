import os
import json
import shutil
from datetime import datetime

import numpy as np
from tqdm import tqdm
from sklearn.metrics.pairwise import cosine_similarity
from tensorflow.keras.preprocessing import image
from tensorflow.keras.applications.resnet50 import ResNet50, preprocess_input


class ImageAnalyzer:
    def __init__(self, base_dir):
        self.base_dir = base_dir
        self.embeddings_path = os.path.join(base_dir, "embeddings", "dataset_embeddings.npy")
        self.image_paths_path = os.path.join(base_dir, "embeddings", "dataset_image_paths.npy")
        self.capture_dir = os.path.join(base_dir, "analysis", "image_capture")
        self.analyzed_dir = os.path.join(base_dir, "analysis", "image_analyzed")
        self.report_dir = os.path.join(base_dir, "analysis", "results_report")
        self.report_file = os.path.join(self.report_dir, "resultados_analise.json")

        os.makedirs(self.analyzed_dir, exist_ok=True)
        os.makedirs(self.report_dir, exist_ok=True)

        self.model = ResNet50(weights='imagenet', include_top=False, pooling='avg')
        self.embeddings = np.load(self.embeddings_path)
        self.image_paths = np.load(self.image_paths_path, allow_pickle=True)

    def preprocess_image(self, img_path, target_size=(224, 224)):
        img = image.load_img(img_path, target_size=target_size)
        img_array = image.img_to_array(img)
        img_array = np.expand_dims(img_array, axis=0)
        return preprocess_input(img_array)

    def extract_features(self, img_path):
        img = self.preprocess_image(img_path)
        features = self.model.predict(img, verbose=0)
        return features.flatten()

    def find_most_similar(self, img_path):
        new_embedding = self.extract_features(img_path)
        similarities = cosine_similarity([new_embedding], self.embeddings)[0]
        best_idx = np.argmax(similarities)
        return self.image_paths[best_idx], similarities[best_idx]

    def load_existing_results(self):
        if os.path.exists(self.report_file):
            with open(self.report_file, "r") as f:
                return json.load(f)
        return []

    def save_results(self, all_results):
        with open(self.report_file, "w") as f:
            json.dump(all_results, f, indent=4)

    def analyze_images(self):
        test_images = [
            f for f in os.listdir(self.capture_dir)
            if f.lower().endswith(('.jpg', '.jpeg', '.png'))
        ]

        if not test_images:
            return [{
                "id": "",
                "vector": "",
                "codestatus": 204
            }]

        existing_results = self.load_existing_results()
        current_results = []

        for img_name in tqdm(test_images, desc="Analisando imagens"):
            img_path = os.path.join(self.capture_dir, img_name)
            matched_path, similarity = self.find_most_similar(img_path)

            timestamp = datetime.now().strftime("%Y-%m-%d_%H-%M-%S")
            image_id = f"{img_name}_{timestamp}"
            is_similar = similarity >= 0.60

            result = {
                "id": image_id,
                "result": bool(is_similar),
                "accuracy": round(float(similarity), 4)
            }
            existing_results.append(result)

            # Resultado para retorno imediato
            current_results.append({
                "id": image_id,
                "vector": "VECTOR" if is_similar else "NVECTOR",
                "codestatus": 200
            })

            # Move imagem
            shutil.move(img_path, os.path.join(self.analyzed_dir, img_name))

        self.save_results(existing_results)
        #print(f"\nAnálise concluída. Resultados salvos em: {self.report_file}")
        return current_results

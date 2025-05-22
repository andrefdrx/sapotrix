# Sapotrix

<p align="center">
  <img src="https://github.com/user-attachments/assets/d0a6df97-147d-4331-b3b9-9aeb189af21c" />
</p>

Sistema de processamento e análise de imagens usando ESP32-CAM e deep learning.

Aplicação com o objetivo da detecção e análise de mosquitos _Aedes Aegypti_, assim como sua eliminação. Uso de processamento e análise de imagem para identificação de insetos, permitindo a livre passagem de espécies diferentes do _Aedes Aegypti_.
 
Os dados analisados e coletados tem o propósito de apoiar ações preventivas e melhorar estratégias de combate já existentes referente ao mosquito _Aedes Aegypti_. Após a detecção, os dados são enviados a um servidor remoto por meio do módulo ESP32 LoRa.

## Componentes

### CameraWebServer
Servidor de câmera baseado no ESP32-CAM com as seguintes funcionalidades:
- Captura de imagens em formato JPEG/BMP
- Streaming de vídeo
- Controle de LED para iluminação
- Interface HTTP para acesso às funcionalidades

Hardware suportado:
- AI-THINKER ESP32-CAM

### Embeddings
Sistema de extração de características de imagens usando deep learning:
- Extração de features usando modelo ResNet50 pré-treinado
- Processamento de datasets de imagens
- Geração de embeddings para análise

### Analysis
Sistema de análise de similaridade de imagens:
- Comparação de imagens usando embeddings gerados
- Cálculo de similaridade usando distância coseno
- Geração de relatórios de análise em formato JSON

## Requisitos

### CameraWebServer
- ESP32-CAM
- Arduino IDE com suporte ESP32

### Embeddings
- Python 3.x
- TensorFlow 2.19.0
- Keras 3.9.2
- NumPy 2.1.3
- scikit-learn 1.6.1
- tqdm 4.67.1
- matplotlib
- Pillow 11.2.1
- h5py 3.13.0

## Estrutura do Projeto
```
.
├── CameraWebServer/       # Componente ESP32-CAM
│   ├── app_httpd.cpp     # Implementação do servidor HTTP
│   ├── camera_index.h    # Interface web
│   └── camera_pins.h     # Configuração de pins
├── embeddings/           # Sistema de processamento de imagens
│   ├── embeddings.py     # Extração de features
│   └── requeriments.txt  # Dependências Python
├── analysis/            # Sistema de análise de imagens
│   └── similarity.py    # Análise de similaridade
```


## Instalação e Execução

### 1. Crie e ative o ambiente virtual

#### Windows
```
python -m venv venv
venv\Scripts\activate
```

### Linux/macOS
```
python3 -m venv venv
source venv/bin/activate
```

## 2. Instale as dependências
```
pip install -r requirements.txt
```

## 4. Execute o sistema
```
python main.py
```

### OBS:
- As imagens que passarão por analise precisar estar salvas na pasta "analysis\image_capture"

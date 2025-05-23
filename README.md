# Sapotrix

<p align="center">
  <img src="https://github.com/user-attachments/assets/d0a6df97-147d-4331-b3b9-9aeb189af21c" />
</p>

##### Conteúdo
- [Introdução](#intro)
- [Objetivos](#obj)
- [Componentes](#componentes)
  * [CameraWebServer](#cam)
  * [Embeddings](#embeddings)
  * [Analysis](#analysis)
- [Requisitos](#req)
  * [CameraWebServer](#camreq)
  * [Embeddings](#embreq)
- [Estrutura do Projeto](#estrutura)
- [Instalação e Execução](#install)
- [Colaboradores](#colab)


<a name="intro"></a>
## Introdução

Projeto usando a plataforma IOT com o objetivo de automatizar a coleta de dados e eliminação de insetos do gênero _Aedes_. Com o uso e implementação de recursos da "Internet das coisas", essa solução é aplicada a armadilha de insetos do gênero _Aedes_, sendo acoplada a uma lixeira equipada com uma porta de coleta de lixo com acionamento automático.

A armadilha, com objetivo de atrair os mosquitos _Aedes aegypti_, é equipada com os seguintes componentes: atrativo químico olfativo, luz de cor vermelha, ciano e laranja, água e base de oviposição. Também é equipada com sensores responsáveis pela coleta e análise de dados dos insetos atraídos e uma câmera para permitir o processamento de imagens, esses componentes estão descritos nas seções encontradas abaixo.

Sobre a questão da eliminação do inseto, assim que identificado como _Aedes aegypti_, é usado um sistema físico e relativamente simples: um jato de água. Esse sistema é ativado logo após ser finalizada a coleta de dados e sua análise correta.

Os dados coletados são enviados a um servidor remoto para seu armazenamento e futura análise usando um módulo ESP32 LoRa, de forma a permitir a trasmissão de dados por uma longa distância, através do protocolo LoRaWAN. Essa transmissão possibilita a implantação da armadilha em localizações remotas e de forma com que os dados sejam obtidos de forma automatizada.

A identificação correta do inseto é realizada através do processamento e reconhecimento de imagens obtidas pela câmera.

<a name="obj"></a>
## Objetivos

<a name="componentes"></a>
## Componentes

<a name="cam"></a>
### CameraWebServer
Servidor de câmera baseado no ESP32-CAM com as seguintes funcionalidades:
- Captura de imagens em formato JPEG/BMP
- Streaming de vídeo
- Controle de LED para iluminação
- Interface HTTP para acesso às funcionalidades

Hardware suportado:
- AI-THINKER ESP32-CAM


<a name="embeddings"></a>
### Embeddings
Sistema de extração de características de imagens usando deep learning:
- Extração de features usando modelo ResNet50 pré-treinado
- Processamento de datasets de imagens
- Geração de embeddings para análise

<a name="analysis"></a>
### Analysis
Sistema de análise de similaridade de imagens:
- Comparação de imagens usando embeddings gerados
- Cálculo de similaridade usando distância coseno
- Geração de relatórios de análise em formato JSON

<a name="req"></a>
## Requisitos

<a name="camreq"></a>
### CameraWebServer
- ESP32-CAM
- Arduino IDE com suporte ESP32

<a name="embreq"></a>
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

<a name="estrutura"></a>
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

<a name="install"></a>
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


<a name="colab"></a>
##Colaboradores

Adriano Rocha -
André Reis -
Bernardo Santos -
César Barbosa -
Rafael Soares -
Rafael Yasuda -
Rodeval Silva -
Thiago Santana -

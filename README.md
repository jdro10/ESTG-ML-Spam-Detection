# Spam Detection
Este projeto consiste na criação de um modelo que detete se uma determinada frase é spam ou não spam (aprendizagem supervisionada).
Modelo treinado com recurso a um dataset inglês.

### Estrutura do projeto

```
├── analysis                     
│   └── data_analysis.py         # Criação de estatísticas dos datasets
├── data_preparation             # Contém todos os scripts de tratamento de dados
│   ├── final_dataset.py
│   ├── fix_original_dataset.py  
│   ├── original_dataset_preparation.py
│   ├── balancing.py
│   ├── drop_low_entries.py
│   └── only_spam_dataset.py
├── datasets                     # Contém todos os dadasets utilizados no projeto
├── img                          # Gráficos dos datasets e modelos
├── modeling_and_evaluation
│   ├── load_model.py            # Leitura de um modelo
│   ├── pca.py                   # Principal component analysis
│   └── saved_models             # Pasta que contém modelos já treinados
│       ├── KNN_model.sav
│       ├── RandomForest_Model.sav
│       └── RandomForest_Model_Under.sav
├── rest_api                     # REST API em flask
    ├── app.py                   # Flask
    └── controllers
        └── controller.py        # Controlador que recebe uma frase e determina se é ou não spam
    
```

### Tratamento de dados
O tratamento do dataset original consistiu nos seguintes passos: 

* Remoção de espaços em branco desnecessários (utilização de uma simples regex).
* Tokenização de frases (utilização do word_tokenize da biblioteca NLTK).
* Remoção de acentos (utilização da biblioteca unidecode).
* Remoção de stop words (utilização do corpus da biblioteca NLTK).
* Separação de palavras juntas (utilização da biblioteca wordninja).
* Remoção de palavras duplicadas.
* Colocação de todas as palvras em minúsculas.
* Remoção de números.
* Lematização de palavras (utilização do stem da biblioteca NLTK).
* Colocação de palvras em colunas.

Visto o dataset não estar balanceado (~87% entradas não spam e ~13% entradas spam) foi necessário balancear.
Foram utilizadas duas técnicas:
* Undersampling (foram eliminados aleatóriamente entradas da classe maioritária (não spam)).
* SMOTE - Synthetic Minority Oversampling Technique (foram criadas aleatóriamente novas entradas com base nas entradas já existentes da classe minoritária). 

### Modelo
Desenvolvidos dois modelos diferentes de classificação.
* KNN (K-Nearest Neighbors)

| Accuracy Train  |  Accuracy Test  | F1 Train | F1 Test |
| ------------------- | ------------------- | ------------------- | ------------------- |
|  1.0 |  0.75 |  1.0 |  0.68 |

* Random Forest

| Accuracy Train  |  Accuracy Test  | F1 Train | F1 Test |
| ------------------- | ------------------- | ------------------- | ------------------- |
|  0.97 |  0.96 |  0.97 |  0.96 |

### Unidade Curricular
* Machine Learning - Mestrado Engenharia Informática

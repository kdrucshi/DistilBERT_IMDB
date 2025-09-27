# IMDB Sentiment Analysis with DistilBERT
A Natural Language Processing (NLP) application that leverages Hugging Face Transformers. The model was fine-tuned on the IMDB dataset and achieves ~90% accuracy in sentiment classification. The project demonstrates end-to-end ML development — from data preprocessing, model training, evaluation, and hyperparameter tuning, to deployment with Gradio on Hugging Face Spaces.</br>
</br>This model has been deployed using Gradio, kindly find the demo link below </br>
**Demo:** 
[![Open in Hugging Face Spaces](https://img.shields.io/badge/🤗-Try%20Demo-yellow)](https://huggingface.co/spaces/kdrucshi/DistilBERT_IMDB-Gradio)
## Dataset: [IMDB](https://huggingface.co/datasets/imdb)  

- 25,000 movie reviews (train/test)  
- Labels: `0 = Negative`, `1 = Positive`
  
## Model description
- Base Model - Distilbert-base-uncased
- Fine-tuned for binary classification
- Achieved ~90% accuracy on test set
## Training and evaluation data

</br>It achieves the following results on the evaluation set:

- Loss: 0.2407
- Accuracy: 0.9156
- F1: 0.9153</br>

**Learning Rate and Batch Size**

- lr = 1e-5, batch size =16 -> Model shows eratic behaviour, thus shows alot of flutuations in validation and training curves.
Good covergence can be seen on training curve but validation curve does shows much convergence with respect to training cruve. </br>
</br><img width="277" height="202" alt="image" src="https://github.com/user-attachments/assets/618565a8-1061-4b02-a46f-f2bf55626d17" />
<img width="285" height="204" alt="image" src="https://github.com/user-attachments/assets/3ec4490d-034a-4291-a90b-fe87cd67f928" /></br>

- lr = 1e-5, batch size = 32 -> Model shows Convergence in validation and training curves but eratic behaviour continues to persists.</br>
</br><img width="286" height="199" alt="image" src="https://github.com/user-attachments/assets/8240784f-f251-46fe-98d7-3d00b0e9be54" />
<img width="283" height="203" alt="image" src="https://github.com/user-attachments/assets/69e5e991-c44a-4e44-b834-d084c3931dc9" /></br>

- lr = 1e-5, batch size = 64 -> Model clearly overfits the data, bigger validation loss values with respect to training loss values can be observed.</br>
</br><img width="286" height="202" alt="image" src="https://github.com/user-attachments/assets/f8741e5a-10fe-49ed-bba4-8541d5caeaa8" />
<img width="276" height="201" alt="image" src="https://github.com/user-attachments/assets/2b350797-2767-4ddc-96d3-e43f386dbcbc" /></br>

</br>Let's try with bigger learning rate with decay and batch size = 32, for better curves and convergence.

- lr = 2e-5, batch size = 32, lr_scheduler -> Better convergence can be seen, since validation and training curves converges together, with less fluctuations or less eratic behavious.</br>
</br><img width="314" height="231" alt="image" src="https://github.com/user-attachments/assets/13fe491e-bf0c-4b32-acfa-6dc3bb82d51b" />
<img width="325" height="239" alt="image" src="https://github.com/user-attachments/assets/9f382378-a00d-4d21-abf7-f23f818bc493" /></br>
</br>*checkout full tensorboard: (see [full TensorBoard](https://huggingface.co/kdrucshi/DistilBERT_IMDB/tensorboard))* 

Training hyperparameters
The following hyperparameters were used during training:

- learning_rate: 2e-05
- train_batch_size: 32
- eval_batch_size: 32
- seed: 42
- optimizer: Use OptimizerNames.ADAMW_TORCH_FUSED with betas=(0.9,0.999) and epsilon=1e-08 and optimizer_args=No additional optimizer arguments
- lr_scheduler_type: linear
- lr_scheduler_warmup_ratio: 0.06
- num_epochs: 10
- mixed_precision_training: Native AMP

## Training results

Training Loss|	Epoch|	Step|	Validation Loss|	Accuracy|	F1|
------------|	-----|	----|	-------------|	--------|	--|
0.5779|	0.16|	100|	0.5232|	0.8628|	0.8565|
0.3239	|0.32	|200	|0.3461	|0.8596	|0.8408|
0.2367	|0.48	|300	|0.2935	|0.8806	|0.8863|
0.2037	|0.64	|400	|0.2547	|0.9006	|0.8968|
0.2215	|0.8	|500	|0.2354	|0.908	|0.9064|
0.1866	|0.96	|600	|0.2462	|0.9046	|0.9063|
0.161	|1.12	|700	|0.2435	|0.911	|0.9095|
0.2101	|1.28|	800|	0.2407|	0.9156|	0.9153|

## Framework versions
- Transformers 4.56.1
- Pytorch 2.8.0+cu126
- Datasets 4.0.0
- Tokenizers 0.22.0</br>



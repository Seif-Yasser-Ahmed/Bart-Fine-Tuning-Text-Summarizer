# Bart Fine Tuning Text Summarizer

This model is a fine-tuned version of [facebook/bart-large-xsum](https://huggingface.co/facebook/bart-large-xsum) on the [BBC News Summary](https://www.kaggle.com/datasets/pariza/bbc-news-summary/) dataset.

## Training procedure

### Training hyperparameters

The following hyperparameters were used during training:
- learning_rate: 2e-05
- train_batch_size: 16
- eval_batch_size: 16
- seed: 42
- optimizer: Adam with betas=(0.9,0.999) and epsilon=1e-08
- lr_scheduler_type: linear
- num_epochs: 1
- mixed_precision_training: Native AMP

### Training results

| Training Loss | Epoch | Step | Validation Loss | Rouge1  | Rouge2  | Rougel  | Rougelsum | Gen Len |
|:-------------:|:-----:|:----:|:---------------:|:-------:|:-------:|:-------:|:---------:|:-------:|
| No log        | 1.0   | 84   | 0.8199          | 42.0809 | 35.1683 | 34.0117 | 35.9952   | 59.7371 |


### Framework versions

- Transformers 4.44.0
- Pytorch 2.4.0
- Datasets 2.21.0
- Tokenizers 0.19.1

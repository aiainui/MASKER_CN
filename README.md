
---

MASKER（MASKER: Masked Keyword Regularization for Reliable Text Classification） 中文训练代码


### 0.setup

```

cd pretrain_model

# 下载模型以及配置文件，下载地址： https://huggingface.co/hfl/chinese-roberta-wwm-ext-large


pip install -r requirements.txt -i https://pypi.tuna.tsinghua.edu.cn/simple

```




### 1.抽取关键词

python train.py \
    --dataset weibo_6clf \
    --split_ratio 0.25 --seed 0 \
    --train_type base \
    --backbone roberta --classifier_type softmax --optimizer adam_vanilla &


### 2.训练模型

python train.py --dataset weibo_6clf --split_ratio 0.25 --seed 0 \
    --train_type masker \
    --backbone roberta --classifier_type sigmoid --optimizer adam_masker \
    --keyword_type attention --lambda_ssl 0.001 --lambda_ent 0.0001 \
    --attn_model_path weibo_6clf-base-chinese.model
 

### 3. 预测

python eval.py --dataset weibo_6clf --split_ratio 0.25 --seed 0 \
    --eval_type acc --test_dataset weibo_6clf \
    --backbone roberta --classifier_type softmax \
    --model_path weibo_6clf-base-chinese.model



---

ref：

- 1.MASKER 英文训练代码，参见：https://github.com/alinlab/MASKER

- 2.https://huggingface.co/hfl/chinese-roberta-wwm-ext-large


ps: 如有侵权，联系删除


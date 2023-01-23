
## Capstone Project-2: Amazon Reviews Classification

This project will help public to understand product quality with product reviews.

## Context 
Online sellers and merchants request feedback from their customers because online marketplaces have become increasingly popular over the past few decades. As a result, millions of reviews are produced every day, which makes it challenging for a potential customer to decide whether to buy the product or not. It is difficult and time-consuming for product manufacturers to analyse this massive amount of opinions. This thesis takes into account the issue of categorising reviews by their overall semantic (positive or negative).

##  [Dataset link](https://www.kaggle.com/datasets/danielihenacho/amazon-reviews-dataset)


## Build Directory

```sh
.
├── 6xzlxqexx2jxdlg6
│   ├── README.md
│   ├── apis
│   │   └── openapi.yaml
│   ├── bento.yaml
│   ├── env
│   │   ├── docker
│   │   │   ├── Dockerfile
│   │   │   └── entrypoint.sh
│   │   └── python
│   │       ├── install.sh
│   │       ├── requirements.txt
│   │       └── version.txt
│   ├── models
│   │   └── review_sentiment
│   │       ├── 6557m7uxxwe2dlg6
│   │       │   ├── custom_objects.pkl
│   │       │   ├── model.yaml
│   │       │   └── saved_model.pkl
│   │       └── latest
│   └── src
│       ├── locustfile.py
│       ├── notebook.ipynb
│       ├── predict.py
│       └── train.py
└── latest
```

## Input/Output
Request :

```sh
curl -X 'POST' \
  'http://localhost:3000/classify' \
  -H 'accept: application/json' \
  -H 'Content-Type: application/json' \
  -d '{
  "text": "i wish would have gotten one earlier love it and it makes working in my laptop so much easier"
}'
```

Response:
```sh
{
  "sentiment": "Positive"
}
```


## Instructions to run:

Build bentoml 
```sh
bentoml build
```

Containerize the model
```sh
bentoml containerize review_sentiment_classify:6xzlxqexx2jxdlg6 --platform linux/amd64
```

Run locally
```sh
docker run -it --rm -p 3000:3000 review_sentiment_classify:6xzlxqexx2jxdlg6
```

Docker tagging and pushing image to AWS ECR

Docker taggging
```sh
docker tag review_sentiment_classify:6xzlxqexx2jxdlg6 818606151817.dkr.ecr.us-east-1.amazonaws.com/review_sentiment_classify:latest
```

Pushing image to AWS ECR
```sh
docker push 818606151817.dkr.ecr.us-east-1.amazonaws.com/review_sentiment_classify:latest
```

## Deployment in AWS ECS 



https://user-images.githubusercontent.com/113333934/213984113-357d7837-56e5-4fc4-be76-9b6354201307.mov







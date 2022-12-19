
## Capstone Project-1: News classification

This project will help public to authenticate news .

## Context 
The most often accessed type of information on social media is news, which is one of the massive amounts of content that users can access. Politicians, news outlets, newspaper websites, or even regular citizens may post these stories. Since distributing false information has become a major problem in recent years and many businesses are working to educate the public about the dangers of doing so, these posts need to be examined for authenticity. Since the manual classification of news is laborious, time-consuming, and vulnerable to prejudice, it is impossible to measure the validity of news that is posted online with any certainty.

##  [Dataset link] ([https://www.kaggle.com/datasets/algord/fake-news])


## Build Directory

```sh
x46wdlt5iwiyllg6
├── README.md
├── apis
│   └── openapi.yaml
├── bento.yaml
├── env
│   ├── docker
│   │   ├── Dockerfile
│   │   └── entrypoint.sh
│   └── python
│       ├── install.sh
│       ├── requirements.txt
│       └── version.txt
├── models
│   └── news_classification
│       ├── 2mddbyt5hcde5lg6
│       │   ├── custom_objects.pkl
│       │   ├── model.yaml
│       │   └── saved_model.pkl
│       └── latest
└── src
    ├── locustfile.py
    ├── notebook.ipynb
    ├── predict.py
    └── train.py
```

## Input/Output
Request :

```sh
curl -X 'POST' \
  'http://localhost:3000/classify' \
  -H 'accept: application/json' \
  -H 'Content-Type: application/json' \
  -d '{
  "title": "ladies crush angelina jolie"
}'
```

Response:
```sh
{
  "News": "Fake"
}
```


## Instructions to run:

Build bentoml 
```sh
bentoml build
```

Containerize the model
```sh
bentoml containerize news_classify:x46wdlt5iwiyllg6 --platform linux/amd64
```

Run locally
```sh
docker run -it --rm -p 3000:3000 news_classify:x46wdlt5iwiyllg6
```

Docker tagging and pushing image to AWS ECR

Docker taggging
```sh
docker tag news_classify:x46wdlt5iwiyllg6 818606151817.dkr.ecr.us-east-1.amazonaws.com/news-classify:latest
```

Pushing image to AWS ECR
```sh
docker push 818606151817.dkr.ecr.us-east-1.amazonaws.com/news-classify:latest
```

## Deployment in AWS ECS 




https://user-images.githubusercontent.com/113333934/208425808-9c358373-2152-4345-8556-41027c048350.mov



## AWS configuration 



https://user-images.githubusercontent.com/113333934/208425933-a7a71009-6aee-4f55-be48-fc6f62d303a5.mov



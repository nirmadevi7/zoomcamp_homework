## Projects Midterm project: Is Water Quality safe for drinking ?
Access to safe drinking-water is essential to health, a basic human right and a component of effective policy for health protection. This is important as a health and development issue at a national, regional and local level. In some regions, it has been shown that investments in water supply and sanitation can yield a net economic benefit, since the reductions in adverse health effects and health care costs outweigh the costs of undertaking the interventions.

This project will help socity or Govt. to check ground drinking water is safe for drinking.

##  [Dataset used](https://www.kaggle.com/datasets/adityakadiwal/water-potability)


## instruction to run:

Build bentoml 
```sh
bentoml build
```

Containerize the model
```sh
bentoml containerize water-safety-classify:mksquus5ykivtlg6 --platform linux/amd64
```

Run locally
```sh
docker run -it --rm -p 3000:3000 water-safety-classify:mksquus5ykivtlg6
```

Docker taggging and pussing container to AWS ECR

Docker taggging
```sh
docker tag water-safety-classify:mksquus5ykivtlg6 818606151817.dkr.ecr.us-east-1.amazonaws.com/water-safety-classify:latest
```

Pusing container to AWS ECR
```sh
docker push 818606151817.dkr.ecr.us-east-1.amazonaws.com/water-safety-classify:latest
```

Development in AWS ECS 


AWS setup 










## Projects Midterm project: Is Water Quality safe for drinking ?
Access to safe drinking-water is essential to health, a basic human right and a component of effective policy for health protection. This is important as a health and development issue at a national, regional and local level. In some regions, it has been shown that investments in water supply and sanitation can yield a net economic benefit, since the reductions in adverse health effects and health care costs outweigh the costs of undertaking the interventions.

This project will help society or Govt. to check ground water is safe for drinking.

##  [Dataset used](https://www.kaggle.com/datasets/adityakadiwal/water-potability)


## Instructions to run:

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

Docker tagging and pushing container to AWS ECR

Docker tagging
```sh
docker tag water-safety-classify:mksquus5ykivtlg6 818606151817.dkr.ecr.us-east-1.amazonaws.com/water-safety-classify:latest
```

Pushing container to AWS ECR
```sh
docker push 818606151817.dkr.ecr.us-east-1.amazonaws.com/water-safety-classify:latest
```

Deployment in AWS ECS 


https://user-images.githubusercontent.com/113333934/200175930-ac1b014d-ffcb-4cc8-b722-760198167d53.mov



AWS setup 





https://user-images.githubusercontent.com/113333934/200175942-a9adc9a9-82a0-4140-8c92-e97d2384555d.mov








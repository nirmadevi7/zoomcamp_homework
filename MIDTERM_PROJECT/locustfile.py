from locust import task
from locust import between
from locust import HttpUser

sample = {
  "ph": 7.035455515887571,
  "Hardness": 204.8904554713363,
  "Solids": 20791.318980747023,
  "Chloramines": 7.300211873184757,
  "Sulfate": 368.51644134980336,
  "Conductivity": 564.3086541722439,
  "Organic_carbon": 10.3797830780847,
  "Trihalomethanes": 86.9909704615088,
  "Turbidity": 2.9631353806316407,
}

sample2={
  "ph": 7.808856017557415,
  "Hardness": 193.55321164822675,
  "Solids": 17329.802160103376,
  "Chloramines": 8.061361987849569,
  "Sulfate": 331.8381671295742,
  "Conductivity": 392.4495795653845,
  "Organic_carbon": 19.90322518345954,
  "Trihalomethanes": 66.6782137100115,
  "Turbidity": 2.7982428424180505
}

class CarsPurchaseDecision(HttpUser):
    """
    Usage:
        Start locust load testing client with:

            locust -H pip3 install locust

        Open browser at http://0.0.0.0:8089, adjust desired number of users and spawn
        rate for the load test from the Web UI and start swarming.
    """

    @task
    def classify(self):
        self.client.post("/classify", json=sample)

    wait_time = between(0.01, 2)
import bentoml
from bentoml.io import JSON
from pydantic import BaseModel

class UserProfile(BaseModel):
    ph:float
    Hardness:float
    Solids:float
    Chloramines:float
    Sulfate:float
    Conductivity:float
    Organic_carbon:float
    Trihalomethanes:float
    Turbidity:float
 

model_ref = bentoml.sklearn.get("water-safety:latest")
dv = model_ref.custom_objects['dictVectorizer']
model_runner = model_ref.to_runner()

svc = bentoml.Service("water-safety-classify", runners=[model_runner])

@svc.api(input=JSON(pydantic_model=UserProfile), output=JSON())
async def classify(application_data):
    application_data=application_data.dict()
    print("application_data",application_data)
    vector = dv.transform(application_data)
    prediction = await model_runner.predict.async_run(vector)
    print(prediction)
    result = prediction[0]

    if result > 0.5:
        return {
            "status": "safe Water"
        }
    else:
        return {
            "status": "unsafe water"
        }

import pickle

with open("diabetes_gradient_boosting_model.pkl", "rb") as f:
    data = f.read()

print(data.find(b"_loss"))
print(data.find(b"GradientBoostingClassifier"))
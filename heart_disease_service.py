import pickle
import pandas as pd

# Ładowanie modelu
with open('knn_heart_disease.pkl', 'rb') as file:
    classfier = pickle.load(file)

app = Flask(__name__)
#FLask app
@app.route("/KNN-heart-disease", methods=["POST"])
def knn_heart_disease():
    data = request.get_json(force=True)
    df = pd.DataFrame(data, index=[0])
    prediction = classifier.predict(df)

    if prediction[0] == 0: #Jeśli model zwraca wartość inną niż 0 wykrywa zagrożenie
        return "Brak zagrożenia chorób serca."
    else:
        return "Zagrożenie chorób serca."

if __name__ == "__main__":
    app.run(port=9000)

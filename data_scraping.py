from selenium import webdriver
from selenium.webdriver.chrome.options import Options
import pandas as pd
from sklearn.neighbors import KNeighborsClassifier as KNN
from sklearn.model_selection import cross_validate
import pickle

ops = Options()
ops.add_argument("--headless")
driver = webdriver.Chrome(
    executable_path=
    'C:\\Users\\adeq\\Desktop\\mgstrk\\gitvsc2\\chromedriver.exe',
    options=ops)

driver.get('C:\\Users\\adeq\\Desktop\\inteligentne\\Page\\Heart_Disease')

# age_elements = driver.find_element_by_xpath(
#     '//*[@id="data-container"]/div[1]/div/p/span[3]').text
# print(age_elements)
age_elements = driver.find_elements_by_class_name("patient-age")
sex_elements = driver.find_elements_by_class_name("patient-sex")
cp_elements = driver.find_elements_by_class_name("patient-cp")
trestbps_elements = driver.find_elements_by_class_name("patient-trestbps")
chol_elements = driver.find_elements_by_class_name("patient-chol")
fbs_elements = driver.find_elements_by_class_name("patient-fbs")
restecg_elements = driver.find_elements_by_class_name("patient-restecg")
thalach_elements = driver.find_elements_by_class_name("patient-thalach")
exang_elements = driver.find_elements_by_class_name("patient-exang")
oldpeak_elements = driver.find_elements_by_class_name("patient-oldpeak")
slope_elements = driver.find_elements_by_class_name("patient-slope")
ca_elements = driver.find_elements_by_class_name("patient-ca")
thal_elements = driver.find_elements_by_class_name("patient-thal")
target_elements = driver.find_elements_by_class_name("patient-target")

table = []  #Tabela zawierająca dane poszczególnych osób

for i in range(len(age_elements) - 1):  #Pętla zapisująca dane poszczególnych osob do jednej tabeli
    row = []
    row.append(int(age_elements[i].text))
    row.append(int(sex_elements[i].text))
    row.append(int(cp_elements[i].text))
    row.append(int(trestbps_elements[i].text))
    row.append(int(chol_elements[i].text))
    row.append(int(fbs_elements[i].text))
    row.append(int(restecg_elements[i].text))
    row.append(int(thalach_elements[i].text))
    row.append(int(exang_elements[i].text))
    row.append(float(oldpeak_elements[i].text))
    row.append(int(slope_elements[i].text))
    row.append(int(ca_elements[i].text))
    row.append(int(thal_elements[i].text))
    row.append(int(target_elements[i].text))

    table.append(row)

table_headers = ['age','sex','cp','trestbps','chol','fbs', 'restecg', 
                'thalach', 'exang', 'oldpeak', 'slope', 
                'ca',  'thal', 'target'] # Tabela z nagłówkami

df = pd.DataFrame(table, columns=table_headers)

#Przygotowanie parametrów x, y (y-wartości które chcemy przewidzieć, x-dane z tabeli
# (bez tabeli 'target' którą odrzucami))
y = df["target"]
df = df.drop(["target"], axis=1)  #Axis=1 oś y w tabeli
X = df

classifier = KNN(n_neighbors=3)
classifier.fit(X, y)

#Saving the model
with open('knn_heart_disease.pkl', 'wb') as file:
    pickle.dump(classfier, file)

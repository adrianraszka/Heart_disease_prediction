import {readTextFile, parseCSV, popHeaders} from './utils.js';

function createPatientDescription(patientRow){
  let arr = patientRow.split(',');
    let element = document.createElement("div");
    element.className = "row";
    element.innerHTML =   `<div class="col-lg-12">` +
    `<p class="patient-info patient-description">` +
      `Patients age is <span class="patient-age font-weight-bold">${arr[0]}</span> and there sex is <span class="patient-sex font-weight-bold">${arr[1]}</span>.
      Their chest pain is <span class="patient-cp font-weight-bold">${arr[2]}</span>, thier resting blood pressure is <span class="patient-trestbps font-weight-bold">${arr[3]}</span>.
      Cholestoral is sitting at <span class="patient-chol font-weight-bold">${arr[4]}</span>, and blood sugar above 120 mg/dl is <span class="patient-fbs font-weight-bold">${arr[5]}</span>.
      Resting electrocardiographic results was <span class="patient-restecg" font-weight-bold">${6}</span>
      Maximum heart rate is at <span class="patient-thalach font-weight-bold">${arr[7]}</span>, exercise induces angina <span class="patient-exang font-weight-bold">${arr[8]}</span>, ST depression is
      <span class="patient-oldpeak font-weight-bold">${arr[9]}</span>, slope of exercise peak is <span class="patient-slope font-weight-bold">${arr[10]}</span>.  
      The number of major vessels colored by flourosopy is <span class="patient-ca font-weight-bold">${arr[11]}</span>.  Thal = <span class="patient-thal font-weight-bold">${arr[12]}</span>.
      The presence of heart disease is <span class="patient-target font-weight-bold">${arr[13]}</span>`+
    `</p>`

    return element;
}

// ############# Main ###########



document.addEventListener("DOMContentLoaded", () =>{
  let csvText = readTextFile("https://b2gdevs.github.io/MLIntro/dataFiles/heart.csv");
  let csvArray = parseCSV(csvText);
  let headers = popHeaders(csvArray);
  let dataContainer = document.getElementById("data-container");
  
  csvArray.shift();

  csvArray.forEach((row) => {
    dataContainer.appendChild(createPatientDescription(row));
    });

});

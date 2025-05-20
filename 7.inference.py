import requests
import json
import time
import logging
 
# Konfigurasi logging
logging.basicConfig(filename="api_model_logs.log", level=logging.INFO,
                    format="%(asctime)s - %(levelname)s - %(message)s")
 
# Endpoint API model
API_URL = "http://127.0.0.1:8000/predict"
 
# Contoh input untuk model (ubah sesuai dengan kebutuhan model)
input_data = {
  "dataframe_split": {
    "columns": [
      "gender",
      "SeniorCitizen",
      "Partner",
      "Dependents",
      "tenure",
      "PhoneService",
      "MultipleLines",
      "OnlineSecurity",
      "OnlineBackup",
      "DeviceProtection",
      "TechSupport",
      "StreamingTV",
      "StreamingMovies",
      "PaperlessBilling",
      "MonthlyCharges",
      "TotalCharges",
      "InternetService_DSL",
      "InternetService_Fiber optic",
      "InternetService_No",
      "Contract_Month-to-month",
      "Contract_One year",
      "Contract_Two year",
      "PaymentMethod_Bank transfer (automatic)",
      "PaymentMethod_Credit card (automatic)",
      "PaymentMethod_Electronic check",
      "PaymentMethod_Mailed check"
    ],
    "data": [
      [
        1,
        1,
        1,
        0,
        1.1643896396487294,
        1,
        1,
        0,
        0,
        0,
        0,
        0,
        0,
        0,
        -1.322910085587596,
        -0.3448102578430522,
        0,
        0,
        1,
        0,
        0,
        1,
        1,
        0,
        0,
        0
      ]
    ]
  }
}
 
# Konversi data ke JSON
headers = {"Content-Type": "application/json"}
payload = json.dumps(input_data)
 
# Mulai mencatat waktu eksekusi
start_time = time.time()
 
try:
    # Kirim request ke API
    response = requests.post(API_URL, headers=headers, data=payload)
   
    # Hitung response time
    response_time = time.time() - start_time
 
    if response.status_code == 200:
        prediction = response.json()  # Ambil hasil prediksi
 
        # Logging hasil request
        logging.info(f"Request: {input_data}, Response: {prediction}, Response Time: {response_time:.4f} sec")
 
        print(f"Prediction: {prediction}")
        print(f"Response Time: {response_time:.4f} sec")
    else:
        logging.error(f"Error {response.status_code}: {response.text}")
        print(f"Error {response.status_code}: {response.text}")
 
except Exception as e:
    logging.error(f"Exception: {str(e)}")
    print(f"Exception: {str(e)}")
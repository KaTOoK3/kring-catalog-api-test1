from flask import Flask, jsonify
import gspread
from oauth2client.service_account import ServiceAccountCredentials

app = Flask(__name__)

# Авторизация в Google Sheets
scope = ["https://spreadsheets.google.com/feeds", "https://www.googleapis.com/auth/drive"]
import os
import json

# Берём JSON из переменной окружения
google_creds_json = os.getenv("GOOGLE_CREDENTIALS_JSON")
google_creds_dict = json.loads(google_creds_json)

creds = ServiceAccountCredentials.from_json_keyfile_dict(google_creds_dict, scope)

client = gspread.authorize(creds)

# Открываем таблицу по названию
sheet = client.open("Catalog").sheet1

@app.route("/products")
def get_products():
    records = sheet.get_all_records()
    return jsonify(records)

if __name__ == "__main__":
    app.run()


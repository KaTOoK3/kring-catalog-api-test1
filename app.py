from flask import Flask, jsonify
import gspread
from oauth2client.service_account import ServiceAccountCredentials

app = Flask(__name__)

# Авторизация в Google Sheets
scope = ["https://spreadsheets.google.com/feeds", "https://www.googleapis.com/auth/drive"]
creds = ServiceAccountCredentials.from_json_keyfile_name("credentials.json", scope)
client = gspread.authorize(creds)

# Открываем таблицу по названию
sheet = client.open("Catalog").sheet1

@app.route("/products")
def get_products():
    records = sheet.get_all_records()
    return jsonify(records)

if __name__ == "__main__":
    app.run()

fole = "credentials.json"
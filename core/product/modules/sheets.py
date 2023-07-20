from pprint import pprint
import datetime
import httplib2
import apiclient.discovery
from oauth2client.service_account import ServiceAccountCredentials

from pathlib import Path


class Table:
    BASE_DIR = Path(__file__).resolve().parent.parent.parent

    # Файл, полученный в Google Developer Console
    CREDENTIALS_FILE = BASE_DIR / "files/cred2.json"
    # ID Google Sheets документа (можно взять из его URL)
    spreadsheet_id = "1SoXLSwe2RKi6h561y2GZEUTPW3GECgs7J00ywTxjDgs"

    # Авторизуемся и получаем service — экземпляр доступа к API
    credentials = ServiceAccountCredentials.from_json_keyfile_name(
        CREDENTIALS_FILE,
        [
            "https://www.googleapis.com/auth/spreadsheets",
            "https://www.googleapis.com/auth/drive",
        ],
    )
    httpAuth = credentials.authorize(httplib2.Http())
    service = apiclient.discovery.build("sheets", "v4", http=httpAuth)

    def table_write(self, val_list):
        resource = {"majorDimension": "COLUMNS", "values": val_list}

        table_range = "!B:B"
        self.service.spreadsheets().values().append(
            spreadsheetId=self.spreadsheet_id,
            range=table_range,
            body=resource,
            valueInputOption="USER_ENTERED",
        ).execute()

    def load_data(self, data):
        time = datetime.datetime.now().strftime("%m/%d/%Y %H:%M")
        self.table_write([
            [data["name"]],
            [data["phone"]],
            [data["email"]],
            [data["vendor_code"]],
            [data["code"]],
            [data["product_name"]],
            [time],
        ])


if __name__ == "__main__":
    vals = [
        ["valuea1"],
        ["valuea2"],
        ["valuea3"],
        ["4"],
        ["5"],
        ["6"],
        ["7"],
        ["weweg"],
    ]
    tb = Table()
    tb.table_write(vals)

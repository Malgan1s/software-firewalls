import requests
from ftplib import FTP

# 1. HTTP-запрос
def http_request():
    try:
        response = requests.get("https://www.virustotal.com/gui/home/upload")
        print(f"HTTP Status Code: {response.status_code}")
    except Exception as e:
        print(f"HTTP Error: {e}")

# 2. FTP-подключение
def ftp_connect():
    try:
        ftp = FTP("test.rebex.net")
        ftp.login("demo", "password")
        print("FTP Login Successful")
        ftp.quit()
    except Exception as e:
        print(f"FTP Error: {e}")

if __name__ == "__main__":
    http_request()
    ftp_connect()
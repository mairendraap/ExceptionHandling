# Coba test menggunakan kode dari Bu Lely dengan kernel Python 3.10, karena kode tersebut menggunakn kernel python 3.10 keatas. dan terdapat error dictionary

import re as r
accounts = {}

def load_data():
    with open("accounts.txt", "r") as f:
        accounts_data = f.read()

    pattern = r'(\d+)[|]([a-z ]+)[|](\d{6})[|](\d+)'
    result = r.findall(pattern, accounts_data, r.IGNORECASE)

    for id, name, pin, balance in result:
        accounts[id] = {
            "name": name,
            "pin": pin,
            "balance": int(balance)
        }

print("load completed")

try:
    load_data()
    while True:
        try:
            user_id = input("input account id: ")
            user_account = accounts(user_id)
            user_pin = input("enter pin: ")
            if not r.fullmatch(r'\d{6}', user_pin):
                print("Invalid PIN format. input 6 digits number.")
                raise Exception("Invalid PIN format")
            elif user_account["pin"] != user_pin:
                raise Exception("Incorrect PIN")

            print(f"Halo, {user_account['name']}!")
            print(f"sisa saldo: ${user_account['balance']}")
            repeat = input("ulangi? (y/n): ")
            if repeat.lower() != "y":
                break
        except KeyError:
            print("account id not found.")
        except Exception as e:
            print(e)
except FileNotFoundError:
    print("accounts.txt file not found.")
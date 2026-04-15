with open("accounts.txt", "r") as f:
    data = f.read()

def bank_system():
    accounts = {}
        
    for i in data.splitlines():
        if not i.strip():
            continue
            
        account_number, name, pin, balance = i.strip().split("|")
        
        accounts[int(account_number)] = {
            "name": name,
            "pin": int(pin),
            "balance": int(balance)
        }
        
    try:
        input_account = int(input("input account number: "))
        input_pin = int(input("enter pin: "))
        
        if input_account in accounts and accounts[input_account]["pin"] == input_pin:
            print(f"Halo, {accounts[input_account]['name']}!")
            print(f"Saldo kamu sisa: {accounts[input_account]['balance']}")

            menu = input("\nmau deposit, withdraw, atau tidak? (ketik 'deposit', 'withdraw', atau 'tidak'): ").lower()

            transaction_success = False 
            
            if menu == "deposit":
                try:
                    deposit_amount = int(input("berapa yg mau di deposit: "))
                    if deposit_amount > 0:
                        accounts[input_account]["balance"] += deposit_amount
                        print(f"deposit sukses, saldo kamu: {accounts[input_account]['balance']}")
                        transaction_success = True
                    else:
                        print("nominal deposit harus positif.")
                except ValueError:
                    print("invalid input. deposit harus input sebuah angka.")
                    
            elif menu == "withdraw":
                try:
                    withdraw_amount = int(input("berapa yg mau di tarik: "))
                    if withdraw_amount > 0:
                        if withdraw_amount <= accounts[input_account]["balance"]:
                            accounts[input_account]["balance"] -= withdraw_amount
                            print(f"tarik tunai berhasil, saldo kamu: {accounts[input_account]['balance']}")
                            transaction_success = True
                        else:
                            print("saldo kamu tidak cukup bro, jangan naif")
                    else:
                        print("nominal penarikan harus positif.")
                except ValueError:
                    print("invalid input. tarik tunai harus input sebuah angka")
            
            elif menu == "tidak":
                print("Oke, cek saldo selesai.")
                print("terima kasih sudah pakai bankherdan ya")
                return 
                
            else:
                print("invalid menu")

            if transaction_success:
                with open("accounts.txt", "w") as file:
                    for acc_num, info in accounts.items():
                        line = f"{acc_num}|{info['name']}|{info['pin']}|{info['balance']}\n"
                        file.write(line)
                print("terima kasih sudah pakai bankherdan ya")

        else:
            print("account number atau PIN salah.")
            
    except ValueError:
        print("\ninvalid input. Nomor akun dan PIN harus berupa angka.")

bank_system()
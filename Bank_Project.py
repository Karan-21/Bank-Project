# Bank Project by using dictionary data type
# {101:{"name":"sam","age":25,"amount":10000},102:{}}

data = {}  # empty data base
while True:
    print("1. Create a new account\n2. Existing Customer\n3. Exit")
    ch = int(input("Enter your choice:"))

    if ch == 1:
        acc = int(input("Enter your account number:"))

        list1 = ["Name","Age","Address","Phone","Amount"]
        list2 = []

        n = input("Enter name:")
        list2.append(n)

        a = input("Enter age:")
        list2.append(a)

        ad = input("Enter address:")
        list2.append(ad)

        phone = input("Enter phone number:")
        list2.append(phone)

        amt = int(input("Enter amount:"))
        list2.append(amt)

        data[acc] = dict(zip(list1,list2))
        print("------------ACCOUNT CREATED------------")

    elif ch == 2:
        ac = int(input("Enter your account number to fetch the data:"))
        if ac in data:
            print("----DATA FOUND----")
            while True:
                print("1. Check Balance\n2. Withdraw\n3. Deposite\n4. Main menu")
                ch = int(input("Enter your choice:"))
                if ch == 1:
                    print("Available Balance is:",data[ac]["Amount"])
                    print("-"*20)
                elif ch == 2:
                    amt = int(input("Enter amount to withdraw:"))
                    if data[ac]["Amount"] >= amt:
                        final_amt = data[ac]["Amount"] - amt
                        print("Withdraw Successfull!! Available balance is:",final_amt)
                        data[ac]["Amount"] = final_amt  # update new value
                        print("-"*20)
                    else:
                        print("----INSUFFICIENT BALANCE-----")
                elif ch == 3:
                    amt = int(input("Enter amount to deposite:"))
                    final_amt = data[ac]["Amount"] + amt
                    print("Deposite Successfull!! Available balance is:",final_amt)
                    data[ac]["Amount"] = final_amt  # update new value
                    print("-"*20)
                elif ch == 4:
                    break
        else:
            print("----DATA NOT FOUND-----")
        















        
        

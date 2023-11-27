print("welcome")
print("select your language")
language = int(input())
if language == 1:
    print("you choose HINDI")
else:
    print("you choose ENGLISH")

print("insert card")
print("enter pin")
ac = int(input())

accounts = {
    1234: {"acc_number": "11111111111", "name": "reddy", "balance": 1000},
    0: {"acc_number": "2222222222", "name": "karthik", "balance": 1100},
    2341: {"acc_number": "3333333333", "name": "deepak", "balance": 800},
    1: {"acc_number": "4444444444", "name": "vibhas", "balance": 1200},
    2000: {"acc_number": "5555555555", "name": "sankeerthan", "balance": 2000},
    2100: {"acc_number": "6666666666", "name": "yash", "balance": 6000},
    4444: {"acc_number": "7777777777", "name": "lohith", "balance": 5400},
    9999: {"acc_number": "8888888888", "name": "john", "balance": 3900},
    4789: {"acc_number": "9999999999", "name": "dinesh", "balance": 9000},
    101: {"acc_number": "0000000000", "name": "harsha", "balance": 10000},
}

print("savings or pin change or mini statement")
account = input()

if account == "savings":
    if ac in accounts:
        print("acc number " + accounts[ac]["acc_number"])
        print(accounts[ac]["name"])
        var_continue = "yes"

        while var_continue == "yes":
            print("enter withdrawal balance")
            b = int(input())
            withdrawl = b

            if withdrawl <= accounts[ac]["balance"]:
                print("collect your cash: " + str(withdrawl))
                accounts[ac]["balance"] -= b
                print("money left " + str(accounts[ac]["balance"]))
            else:
                print("insufficient balance")

            var_continue = input()
    else:
        print("your card is not associated with any account number")

elif account == "pin change":
    print("enter old pin ")
    ac = int(input())
    if ac == 1234:
        print("enter your new pin")
        ac = input()
        print("your new pin is: " + str(ac))
        print("do you want to withdraw")
        account = input()

        if account == "yes":
            b = int(input("b: "))
            withdrawl = b

            if withdrawl <= accounts[ac]["balance"]:
                print("collect your cash: " + str(withdrawl))
                accounts[ac]["balance"] -= b
                print("money left " + str(accounts[ac]["balance"]))

                var_continue = str(input("yes or no"))

                while var_continue == "yes":
                    b = int(input())
                    withdrawl = b

                    if withdrawl <= accounts[ac]["balance"]:
                        print("collect your cash: " + str(withdrawl))
                        accounts[ac]["balance"] -= b
                        print("money left " + str(accounts[ac]["balance"]))
                    else:
                        print("insufficient balance")

                    var_continue = input()
            else:
                print("insufficient balance")
        else:
            print("pin change is successful")
    else:
        print("your pin is wrong try again by inserting your card from the start.")




def bankFun(fnc):

    def helper(amt):
        print(f"Logging into the system......")
        fnc(amt)
        print(f"Logging out of the system......")
        print("-" * 40)

    return helper

@bankFun
def deposit(amt):
    print(f"{amt} credited into the account successfully....")

@bankFun
def withdraw(amt):
    print(f"{amt} debited from the account successfully....")


deposit(50000)
withdraw(15000)

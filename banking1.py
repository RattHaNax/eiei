def Show_Balance(balance):
         print("***********************************")
         print(f"Your Balance is: {balance}")
         print("***********************************")

def deposit(balance,deposit):
    balance += deposit
    print(f"Your deposit is: {deposit}")
    return balance

def withdraw(balance,withdraw):
    balance -= withdraw
    print(f"Your withdraw is: {withdraw}")
    return balance

if __name__ == '__main__':
    Show_Balance(1000)





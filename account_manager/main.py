class Person:
    def __init__(self, first_name, last_name):
        self.first_name = first_name
        self.last_name = last_name


class Client(Person):
    def __init__(self, first_name, last_name, account_number, balance=0):
        super().__init__(first_name, last_name)
        self.account_number = account_number
        self.balance = balance

    def __str__(self):
        return f'Client: {self.first_name} {self.last_name}\nAccount Balance {self.account_number}: ${self.balance}'

    def deposit(self, amount_deposit):
        self.balance += amount_deposit
        print("Deposit accepted")

    def withdraw(self, amount_withdraw):
        if self.balance >= amount_withdraw:
            self.balance -= amount_withdraw
            print('Withdrawal done')
        else:
            print('Insufficient funds')


def create_client():
    # Gather client information
    first_name = input("Enter your first name: ")
    last_name = input("Enter your last name: ")
    account_number = input("Enter your account number: ")

    # Create and return a new Client object
    client = Client(first_name, last_name, account_number)
    return client


def start():
    # Create a new client
    my_customer = create_client()
    print(my_customer)

    while True:
        print("Choose: Deposit (D), Withdraw (W), or Exit (E)")
        option = input().upper()

        if option == 'D':
            try:
                # Prompt for deposit amount
                dep_amount = float(input("Deposit amount: "))
                if dep_amount <= 0:
                    raise ValueError("Deposit amount must be a positive number.")

                # Deposit the amount and print updated account information
                my_customer.deposit(dep_amount)
                print(my_customer)
            except ValueError as e:
                print(f"Error: {str(e)}")
        elif option == 'W':
            try:
                # Prompt for withdrawal amount
                with_amount = float(input("Withdrawal amount: "))
                if with_amount <= 0:
                    raise ValueError("Withdrawal amount must be a positive number.")

                # Withdraw the amount and print updated account information
                my_customer.withdraw(with_amount)
                print(my_customer)
            except ValueError as e:
                print(f"Error: {str(e)}")
        elif option == 'E':
            break

    print("Thank you for using Python Bank")


start()

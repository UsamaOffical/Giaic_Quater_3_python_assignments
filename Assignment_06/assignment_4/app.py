class Bank:
    bank_name = "Default Bank"  # Class variable

    @classmethod
    def change_bank_name(cls, name):
        cls.bank_name = name

# Usage
b1 = Bank()
b2 = Bank()

print(b1.bank_name)  # Default Bank
Bank.change_bank_name("Global Bank")
print(b1.bank_name)  # Global Bank
print(b2.bank_name)  # Global Bank

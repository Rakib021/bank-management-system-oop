from Bank import BankAccount,Admin
def main():
    bank = BankAccount()

    bank.create_account("Sakib")
    bank.create_account("Mahfuz")
    bank.create_account("chinmoy")


    bank.deposit("Sakib", 1000)
    bank.withdraw("Sakib", 500)
    bank.transfer("Sakib", "Mahfuz", 200)
    bank.check_bal("Sakib")
    bank.transaction_history("Sakib")


    admin = Admin(bank)
    admin.create_account("chinmoy")
    admin.check_total_balance()
    admin.check_total_loan_amount()
    admin.enable_loan_feature()
    admin.disable_loan_feature()

if __name__ == "__main__":
    main()

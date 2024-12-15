import streamlit as st
st.title("Banking Application")
balance = 100000


# noinspection PyUnboundLocalVariable
class Bank:
    def deposit(self):
        amount = st.number_input("Enter the deposit amount:", min_value=0)
        if amount >= 100 and amount <= 50000:
            if amount % 100 == 0:
                st.write("Your deposit is valid")
                return amount
            else:
                st.write("Amount should be in multiples of 100")
        else:
            st.write("Your deposit is invalid. Deposit amount should be between 100 and 50,000.")
        return 0

    # noinspection PyUnboundLocalVariable
    def withdraw(self):
        withdrawl_amount = st.number_input("Enter the withdrawal amount:", min_value=0)
        if withdrawl_amount >= 100:
            if withdrawl_amount <= balance:
                if withdrawl_amount <= 20000:
                    balance -= withdrawl_amount
                    st.write("Transaction successful!")
                    st.write("Remaining balance:", balance)
                else:
                    st.write("Transaction failed! You cannot withdraw more than 20,000.")
            else:
                st.write("Insufficient funds!")
        else:
            st.write("Amount not valid! Withdrawal amount must be at least 100.")

    def viewOptions(self):
        st.subheader("1. Deposit")
        st.subheader("2. Withdraw")
        st.subheader("3. Balance Enquiry")
        st.subheader("0. Exit")

        option = st.text_input("Choose your option:")

        if st.button("Proceed"):
            if option == "1":
                deposit_amount = self.deposit()
                global balance
                balance += deposit_amount
            elif option == "2":
                self.withdraw()
            elif option == "3":
                st.write(f"Current Balance: {balance}")
            elif option == "0":
                st.write("Exiting...")
                return
            else:
                st.write("Invalid option. Please select a valid option.")

    def validation(self):
        st.subheader("Welcome to ABC Bank")
        pin = st.text_input("Enter the pin number:")
        if st.button("Confirm"):
            if pin == "1234":
                self.viewOptions()
            else:
                st.write("Incorrect PIN. Please try again.")

obj = Bank()
obj.validation()

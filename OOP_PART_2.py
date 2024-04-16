
#TODO PUBLIC CLASS
# class BankAccount:
#     def __init__(self,name,ballance,passport):
#         self.name = name
#         self.ballance = ballance
#         self.passport =passport
#
#     def print_data(self):
#         print("Name:",self.name,"\nBallance:",self.ballance,"\nPassport:",self.passport)
#
# bank_account1=BankAccount('Gabriel',980000,"8654636475654")
# bank_account1.print_data()


#TODO PROTECTED CLASS-noi oricum putem accesa datele dintr-o clasa protected dar nu este recomandat programatorilor sa se foloseasca de aceste date inafara clasei ,ESTE UN STANDART
#
# class BankAccount:
#     def __init__(self,name,ballance,passport):
#         self._name = name
#         self._ballance = ballance
#         self._passport =passport
#
#     def print_protected_data(self):
#         print("Name:",self._name,"\nBallance:",self._ballance,"\nPassport:",self._passport)
#
# bank_account1=BankAccount('Gabriel',980000,"8654636475654")
# bank_account1.print_protected_data()



#TODO PRIVATE CLASS

# class BankAccount:
#     def __init__(self,name,ballance,passport):
#         self.__name = name
#         self.__ballance = ballance
#         self.__passport =passport
#
#     def print_private_data(self):
#         print("Name:",self.__name,"\nBallance:",self.__ballance,"\nPassport:",self.__passport)
#
# bank_account1=BankAccount('Gabriel',980000,"8654636475654")
# bank_account1.print_private_data()
# #print(bank_account1.__name)

class BankAccount:
    def __init__(self, name, balance, passport):
        self.__name = name
        self.__balance = balance
        self.__passport = passport

    def get_balance(self):
        return self.__balance

    def set_balance(self, value):
        if not isinstance(value, (int, float)):
            raise ValueError("Balance must be a number")
        self.__balance = value

    balance = property(fget=get_balance, fset=set_balance)

c = BankAccount("Ivan", 200, "asfafafa")
c.set_balance(300)
print(c.balance)


#TODO PYTHON DECORATOR

def smart_divide(func):
    def inner(numbers):
        result = []
        for divisor in range(1, 11):
            result.append(func(numbers, divisor))
        return result
    return inner

@smart_divide
def divide(numbers, divisor):
    return sum(numbers) / divisor

numbers = [2, 3, 4, 5, 6, 7, 8, 9, 10]

print(divide(numbers))


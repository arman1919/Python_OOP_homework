class check_data():

    @classmethod
    def email_check(self,email:str):
        if email.count("@") != 1:
            return False
        if not email[0].isalpha():
            return False

        ls = email.split("@")
        ls[-1] = ls[-1].split(".")

        new_ls = []

        for i in range(len(ls) - 1):
            new_ls.append(ls[i])

        new_ls.append(ls[-1][0])
        new_ls.append(ls[-1][1])
        ls = new_ls

        if len(ls) != 3 or len(ls[0]) == 0 or len(ls[1]) == 0 or len(ls[2]) == 0:
            return False

        for i in ls[1]:
            if not i.isalpha():
                return False

        for i in ls[2]:
            if not i.isalpha():
                return False

        if " " in ls[0]:
            return False

        return True

    
    
    def _check_lower(self,s:str):
        for i in s:
            if not i.islower() and i.isalpha():
                return False
        return True
    
    @classmethod
    def url_check(self,url:str):
        if url.count(".") != 2:
            return False

        if " " in url:
            return False
        if url[0:11] !="http://www." and url[0:12] != "https://www.":
            return False

        ls = url.split(".")

        if not self._check_lower(ls[1]):
            return False

        path = ls[2]

        ls = path.split("/")

        for i in ls:
            if not self._check_lower(i):
                return False

        return True
    
    @classmethod
    def date_check(self,date):
        ls = date.split(".")
        if len(ls) != 3:
            return False
        if len(ls[0]) != 2 or len(ls[1]) != 2 or len(ls[2]) != 4:
            return False

        for i in ls:
            if not i.isdigit():
                return False

        if int(ls[0]) > 31 or int(ls[1]) > 12:
            return False

        return True

    @classmethod
    def number_check(self,number):
        roman_numerals = {
            'M': 1000,
            'D': 500,
            'C': 100,
            'L': 50,
            'X': 10,
            'V': 5,
            'I': 1
        }
        
        prev_value = 0
        total = 0
        
        for numeral in reversed(number):
            if numeral not in roman_numerals:
                return False
            
            value = roman_numerals[numeral]
            
            if value < prev_value:
                total -= value
            else:
                total += value
                prev_value = value
        
        return total <= 3999
    
    @classmethod
    def credit_cart_check(self,num:str):
        if num.count(" ") != 3:
            return False

        ls = num.split()
        for i in ls:
            if len(i) != 4 or not i.isdigit():
                return False

        return True
    
    @classmethod
    def mobile_phone_check(self,num):
        if len(num) != 9:
            return False
        if num[0] != "0":
            return False
        if not num.isdigit():
            return False
        return  True




def main():
    select = input("""select data type
    1. Email
    2. Website URL
    3. Date
    4. Number
    5. Credit Card Number
    6. Mobile Phone Number
    ---- """)

    

    if select == "1":

        mail = input("Enter email -")
        
        if check_data.email_check(mail):
            print("Correct email")
        else:
            print("Uncorrecr emali")

    elif select == "2":

        url = input("Enter url -")
        if check_data.url_check(url):
            print("Correct url")
        else:
            print("Uncorrecr url")

    if select == "3":

        date = input("Enter date -")
        if check_data.date_check(date):
            print("Correct date")
        else:
            print("Uncorrecr date")

    if select == "4":

        num = input("Enter number -")
        if check_data.number_check(num):
            print("Correct number")
        else:
            print("Uncorrecr number")

    if select == "5":

        card = input("Enter credit cart number -")
        if check_data.credit_cart_check(card):
            print("Correct credit cart number")
        else:
            print("Uncorrecr credit cart number")

    if select == "6":

        phone = input("Enter phone number -")
        if check_data.mobile_phone_check(phone):
            print("Correct phone number")
        else:
            print("Uncorrecr phone number")


main()
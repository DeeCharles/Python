# User Assignment

class User:
    def __init__(self,fname,lname,email,age):
        self.first_name=fname
        self.last_name=lname
        self.email=email
        self.age=age
        #Also include default attributes:
        self.is_rewards_member=False
        self.gold_card_points=0

    #Have this method print all of the users' details on separate lines.
    def display_info(self):
        print(f"{self.first_name}")
        print(f"{self.last_name}")
        print(f"{self.email}")
        print(f"{self.age}")
        print(f"{self.is_rewards_member}")
        print(f"{self.gold_card_points}")
        return self


    #Have this method change the user's member status to True and set their gold card points to 200.
    def enroll(self):
        if self.is_rewards_member==False:
            self.is_rewards_member=True
            self.gold_card_points=200
            #return True
        else:
            self.is_rewards_member==True
            print("User is already a member.")
            #return False
        return self

        


    #Have this method decrease the user's points by the amount specified.
    def spend_points(self, amount):
        if self.gold_card_points < amount:
            print("You do not have enough points")
        else:
            self.gold_card_points -= amount
            print(self.gold_card_points)
        return self

person_one=User("John","Doe","JD@email.com",25,)
person_two=User("Jane","Doe","JDoe@email.com",23)
person_three=User("Jill","Doe","JillD@email.com",16)

person_one.display_info().enroll().spend_points(50).enroll().display_info()
# person_two.enroll()
# person_two.spend_points(80)
# person_two.display_info()

# person_three.enroll()
# person_three.spend_points(40)
# person_three.display_info()






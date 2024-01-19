# inheritance has (Is-A) relation and aggregation has (Has-A) relation
# eg: car is a vehicle, car and vehicle follows inheritance relation where vehicle is base case and car is derived class
# eg: profile has an address, profile and address follows aggregation relation

class Profile:
    def __init__(self, name, gender, address):
        self.name = name
        self.gender = gender
        self.address = address

    def edit_profile(self, newname, newcity, newpincode, newstate):
        self.name = newname
        self.address = self.address.change_address(newcity, newpincode, newstate)

class Address:
    def __init__(self, city, pincode, state):
        self.city = city
        self.pincode = pincode
        self.state = state

    def change_address(self, newcity, newpincode, newstate):
        self.city = newcity
        self.pincode = newpincode
        self.state = newstate
        return self



myaddress = Address("Itahari", 56705, "Koshi")
myprofile = Profile("Niroj", "m", myaddress)

myprofile.edit_profile("Nisha", "Dharan", 56700, "Koshi")


print(myprofile.address.pincode, myprofile.address.state, myprofile.address.city)

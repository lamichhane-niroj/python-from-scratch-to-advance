# how can we make a private attribute in python we use double underscore __
# but then how can we access it -> we will make getter and setter for the private attributes
class Facebook():

    def __init__(self, name, gender):
        self.__name = name
        self.__gender = gender
        self.__post = 0
        self.__photo = ""

    def get_name(self):
        return self.__name

    def set_name(self, name):
        # now we can do safety check because it is passed through function. That's the whole point of encapsulation
        if type(name) == str:
            self.__name = name

    def upload_photo(self, photourl):
        self.__photo = photourl
        print("photo uploaded")

    def print_detail(self):
        print(f"User with name {self.__name} and gender {self.__gender}")

    def create_post(self):
        self.__post += 1


if __name__ == "__main__":
    niroj = Facebook("Niroj", "m")

    # niroj._Facebook__name = "hero"

    # niroj.__name = "Hero" # this will create a new variable of  __name but that doesn't affect the name variable
    niroj.print_detail()


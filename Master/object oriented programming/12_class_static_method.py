# static method are those method which doesn't belong to object, but it belongs to class. So, no object is required to access it
class Facebook:

    # now we wil create a counter that will keep record for number of user of our class
    # now how to access the static private attribute? -> we use static method

    """class variable - belongs to class"""

    __counter = 0

    def __init__(self, name, gender):
        """instance variable belongs to object"""
        self.__name = name
        self.__gender = gender
        self.__post = 0
        self.__photo = ""
        Facebook.__counter = Facebook.__counter + 1

    # static method it doesn't require object for calling
    @staticmethod
    def set_counter(val):
        if type(val) == int:
                Facebook.__counter = val

    @staticmethod
    def get_counter():
        return Facebook.__counter

    def upload_photo(self, photourl):
        self.__photo = photourl
        print("photo uploaded")

    def print_detail(self):
        print(f"User with name {self.__name} and gender {self.__gender}")

    def create_post(self):
        self.__post += 1


if __name__ == "__main__":
    niroj = Facebook("Niroj", "m")
    roshan = Facebook("Roshan", 'm')
    sreejana = Facebook("Sreejana", 'F')

    print(Facebook.get_counter())



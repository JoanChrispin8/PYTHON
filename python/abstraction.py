
# if use abstract method you should definetly use all @abstractmethod 
from abc import ABC, abstractmethod

class app(ABC):

    @abstractmethod
    def login(self):
        pass

    @abstractmethod
    def logout(self):
        pass

    def save(self):  # non abstract methos is compulsory to do but if you want you can do
        pass

class webapp(ABC):

    def login(self):
        print("App login successfull")

    def logout(self):
        print("Logout successsull ")        

WA  = webapp()
WA.login()
WA.logout()
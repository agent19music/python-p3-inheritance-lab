#!/usr/bin/env python

from user import User

class Student(User):
    
    def __init__(self, first_name, last_name):
        super().__init__(first_name, last_name)
        self.knowledge = []

    def learn(self,string):
        if isinstance (string,str):
            self.knowledge.append(string)
        else:
            print("Error: Learn method requires a string")
                
        pass
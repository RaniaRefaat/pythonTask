class Person:
    def __init__(self,name,money,mood,healthRate):
        self.name = name
        self.money = money
        self.mood = mood
        self.healthRate = healthRate

    def sleep(self,hours):
        if hours == 7:
            return mood = "happy"
        elif hours < 7:
            return mood = "tired"
        elif hours > 7:
            return mood = "lazy"

    def eat(self,meals):
        if meals == 3:
            return healthRate = 100%
        elif meals == 2:
            return healthRate = 75%
        elif meals == 1:
            return healthRate = 50% 


    @property
    def healthRate(self):
        return self.__healthRate
    @healthRate.setter
    def healthRate(self,healthRate):
        if healthRate < 100 and healthRate > 0:
            self.__healthRate = healthRate
       


class Employee(Person):
    moods=("happy","tired","lazy")
    def __init__(self,id,car,email,salary,distanceToWork):
        self.id = id
        self.car = car


    def work(hoursEmp):
        if hoursEmp == 8:
            return self.moods = "happy"
        elif hoursEmp > 8:
            return self.moods = "tired"
        elif hoursEmp < 8:
            return self.moods = "lazy"
    
    def drive(distance):


    def refuel(gasAmount = 100):
        return gasAmount + self.fuelRate


    def send_mail(to,subject,msg,reciever_name):

    @property
    def salary(self):
        return self.salary
    @salary.setter
    def salary(self,salary):
        if salary >= 1000:
            self.__salary = salary
    
    @property
    def email(self):
        return self.email
    @email.setter
    def email(self,email):
        if email == "valid":
            self.__email = email

    @property
    def healthRate(self):
        return self.healthRate
    @healthRate.setter
    def healthRate(self,healthRate):
        if healthRate > 0 and healthRate < 100:
            self.__healthRate = healthRate


class Car:
    def __init__(self,name,fuelRate,velocity):
        self.name = name
        self.fuelRate = fuelRate
        self.velocity = velocity

    def run(velocityCar,distanceCar):
        self.velocity = velocityCar
        #print("fuel rate decreases")
        #fuelRate--;
        if fuelRate == 0 :
            stop()

    def stop:
        self.velocity = 0
        print("distance remained:",)

    @property
    def velocity(self):
        return self.__velocity
    @velocity.setter
    def velocity(self,velocity):
        if velocity < 200 and velocity > 0:
            self.__velocity = velocity

    @property
    def fuelRate(self):
        return self.__fuelRate
    @fuelRate.setter
    def fuelRate(self,fuelRate):
        if fuelRate < 100 and fuelRate > 0:
            self.__fuelRate = fuelRate


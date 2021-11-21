from datetime import datetime
from Decorators.CompanyRewardDecorator import CompanyRewardDecorator
from datetime import datetime

class SumOfDigitsIsEqualToSumOfDayAndMonthMultipliedByThree(CompanyRewardDecorator):

    def sumOfDigitsIsEqualToSumOfDayAndMonthMultipliedByThree(self, word):
        sumOfDigits = 0 
        for char in word:
            sumOfDigits += int(char)

        sumOfDayAndMonthMultipliedByThree = (datetime.now().day + datetime.now().month) * 3

        return sumOfDigits == sumOfDayAndMonthMultipliedByThree


    def getReward(self):
        reward = 0
        for nip in self.getNip():
            if self.sumOfDigitsIsEqualToSumOfDayAndMonthMultipliedByThree(nip):
                reward += 550

        return reward

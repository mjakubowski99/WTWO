from Decorators.CompanyRewardDecorator import CompanyRewardDecorator
from datetime import datetime

class NipHasDigitsFromThisDay(CompanyRewardDecorator):

    def hasAllDigits(self, number, word):
        for digit in number:
            
            hasDigit = False 
            for char in word:
                if char == digit:
                    hasDigit = True 
            
            if not hasDigit:
                return False 
        return True 

    def nipHasDigitsFromThisDay(self, word):
        now = datetime.now()

        day = str(now.day)
        month = str(now.month)

        return self.hasAllDigits(day, word) and self.hasAllDigits(month, word)

    def getReward(self):
        reward = 0
        for nip in self.getNip():
            if self.nipHasDigitsFromThisDay(nip):
                reward += 15

        return reward
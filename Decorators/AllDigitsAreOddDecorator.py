
from Decorators.CompanyRewardDecorator import CompanyRewardDecorator

class AllDigitsAreOddDecorator(CompanyRewardDecorator):

    def allDigitsAreOdd(self, word):
        countOdd = 0
        for char in word:
            if int(char) % 2 != 0:
                countOdd+=1

        return countOdd == len(word)

    def getReward(self):
        reward = 0
        for nip in self.getNip():
            if self.allDigitsAreOdd(nip):
                reward+=50

        return reward 



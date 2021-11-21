from Decorators.CompanyRewardDecorator import CompanyRewardDecorator

class HalfOfDigitsIsDivisibleByThreeDecorator(CompanyRewardDecorator):

    def halfOfDigitsDivisibleByThree(self, word):
        countDivisibleByThree = 0
        for char in word:
            if int(char) % 3 == 0:
                countDivisibleByThree+=1

        return countDivisibleByThree >= len(word)//2 

    def getReward(self):
        reward = 0
        for nip in self.getNip():
            if self.halfOfDigitsDivisibleByThree(nip):
                reward += 100

        return reward 

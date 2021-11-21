from Decorators.CompanyRewardDecorator import CompanyRewardDecorator

class SumOfAbsDifferenceBetweenNeighbourDigitsIsMoreThanFiftyDecorator(CompanyRewardDecorator):

    def sumOfAbsDifferenceBetweenNeighbourDigitsIsMoreThanFifty(self, word):
        i = 0

        sumOfAbsDifferenceBetweenNeighbourDigits = 0
        while i < len(word)-1:
            sumOfAbsDifferenceBetweenNeighbourDigits += abs( int(word[i]) - int(word[i+1]) )
            i+=1

        return sumOfAbsDifferenceBetweenNeighbourDigits > 50

    def getReward(self):
        reward = 0
        for nip in self.getNip():
            if self.sumOfAbsDifferenceBetweenNeighbourDigitsIsMoreThanFifty(nip):
                reward += 200

        return reward

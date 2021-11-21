from Decorators.CompanyRewardDecorator import CompanyRewardDecorator
from Decorators.AllDigitsAreOddDecorator import AllDigitsAreOddDecorator
from Decorators.HalfOfDigitsIsDivisibleByThreeDecorator import HalfOfDigitsIsDivisibleByThreeDecorator
from Decorators.NipHasDigitsFromThisDay import NipHasDigitsFromThisDay
from Decorators.SumOfDigitsIsEqualToSumOfDayAndMonthMultipliedByThree import SumOfDigitsIsEqualToSumOfDayAndMonthMultipliedByThree
from Decorators.SumOfAbsDifferenceBetweenNeighbourDigitsIsMoreThanFiftyDecorator import SumOfAbsDifferenceBetweenNeighbourDigitsIsMoreThanFiftyDecorator
from Decorators.CompanyHasGoldCompanyStatusDecorator import CompanyHasGoldStatusDecorator

class FullRewardDecorator(CompanyRewardDecorator):

    def __init__(self, firm):
        self.firm = firm 
        self.decorators = [
            AllDigitsAreOddDecorator(self.firm),
            HalfOfDigitsIsDivisibleByThreeDecorator(self.firm),
            NipHasDigitsFromThisDay(self.firm),
            SumOfDigitsIsEqualToSumOfDayAndMonthMultipliedByThree(self.firm),
            SumOfAbsDifferenceBetweenNeighbourDigitsIsMoreThanFiftyDecorator(self.firm),
            CompanyHasGoldStatusDecorator(self.firm)
        ]

    def decorate(self, firm):
        self.firm = firm 
        for decorator in self.decorators:
            decorator.decorate(firm)

    def getReward(self):
        sum = 0
        for decorator in self.decorators:
            sum += decorator.getReward()

        return sum 

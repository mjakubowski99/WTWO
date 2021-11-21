
from Decorators.CompanyRewardDecorator import CompanyRewardDecorator

class CompanyHasGoldStatusDecorator(CompanyRewardDecorator):

    def firmHasGoldStatus(self):
        return self.firm.getIncome() > 100000

    def getReward(self):
        if self.firmHasGoldStatus():
            return 30
        return 0
                
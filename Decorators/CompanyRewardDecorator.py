from Composite.CompanyInterface import CompanyInterface

class CompanyRewardDecorator(CompanyInterface):

    def __init__(self, firm: CompanyInterface):
        self.firm = firm 

    def decorate(self, firm):
        self.firm = firm

    def getNip(self):
        return self.firm.getNip() 

    def getReward(self):
        pass 
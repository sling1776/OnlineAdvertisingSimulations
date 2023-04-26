import random
import matplotlib.pyplot as plt
import numpy as np

class Space:
    def __init__(self, rand=False):
        if rand:
            self.value = np.random.uniform(0, 5)
        else:
            self.value = 2
        self.companies = []
        

    def get_company(self):
        return self.companies
    
    def add_company(self, company):
        self.companies.append(company)

    def pay_companies(self):
        bidders = []
        standards = []
        for company in self.companies:
            if isinstance(company, Standard):
                standards.append(company)
            if isinstance(company, Bidder):
                bidders.append(company)
        
        # If there is a bidder then the bidder will pay an extra .5 to keep it to themselves. If there are more bidders, they will pay
        #       the extra .5 and then share the value between the bidders (if two bidders it is effectually a loss of .5 for both parties)
        if len(bidders) >= 1:
            for company in bidders:
                company.pay((self.value / len(bidders)) - (.5 * (len(bidders) > 1 or len(standards) > 0)))
        # Normal companies will share the space. More than 2 companies results in a loss.
        else:
            for company in standards:
                company.pay(self.value / len(standards))

    def __repr__(self):
        return str(self.value)
    
    def __gt__(self, other):
        return self.value > other.value
    
    def __lt__(self, other):
        return self.value < other.value
    
    def __eq__(self, other):
        return self.value == other.value
    
class Company:
    def __init__(self, name):
        self.name = name
        self.budget=1
        self.history = []
        self.history.append(self.budget)

    def pay(self, amount):
        self.budget += amount
    
    def buy(self):
        if self.budget >= 1:
            self.budget -=1
            return True
        return False
    
    def record(self):
        self.history.append(self.budget)
    
class Standard(Company):
    pass
    
class Bidder(Company):
    pass

class Hunter(Bidder):
    pass

    
class Simulation:
    def __init__(self, number_ad_spaces=100):
        self.number_ad_spaces = number_ad_spaces
        self.spaces = []
        self.companies = []

    def make_spaces(self, rand):
        self.spaces = []
        for _ in range(self.number_ad_spaces):
            self.spaces.append(Space(rand))
    
    def assign_companies_spaces(self):
        for company in self.companies:
            if isinstance(company, Hunter):
                l = []
                for space in self.spaces:
                    l.append(space)
                l.sort()
                while company.buy() and len(l) > 0:
                    s = l[-1]
                    l.remove(s)
                    s.add_company(company)
            else:
                available_spaces = [i for i in range(self.number_ad_spaces)]
                while company.buy() and len(available_spaces) > 0:
                    s = available_spaces[random.randint(0,len(available_spaces)-1)]
                    available_spaces.remove(s)
                    self.spaces[s].add_company(company)
            
            company.budget=0 # Cannot Save Unused Funds

    def simulate_day(self, rand):
        self.make_spaces(rand)
        self.assign_companies_spaces()
        
        for space in self.spaces:
            space.pay_companies()

        for company in self.companies:
            company.record()


    def simulate(self, numBidders=0, numStandard=0, numHunters=0, num_sim_days=100, title="", rand=False):
        self.companies = []
        self.spaces = []
        for i in range(numStandard):
            self.companies.append(Standard(f"Standard {i}"))
        for i in range(numBidders):
            self.companies.append(Bidder(f"Bidder {i}"))
        for i in range(numHunters):
            self.companies.append(Bidder(f"Hunter {i}"))

        for _ in range(num_sim_days):
            self.simulate_day(rand)
        
        plt.title(title)
        plt.xlabel("Days")
        plt.ylabel("Budget Amount")
        for company in self.companies:
            plt.plot(company.history, label=f"{company.name}")
        plt.legend()   
        plt.show()


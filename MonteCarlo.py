import numpy as np
import matplotlib.pyplot as plt
import math



class American_Call_Payoff:
    def __init__(self, pricePath, startSellPrice):
        self.pricePath = pricePath
        self.initPrice = pricePath[0]
        self.startSellPrice = startSellPrice


    def get_payoff(self):
        valueOfSellingEachMonth = [0 for _ in range(len(self.pricePath))]
        for month in range(len(self.pricePath)):
            if month == len(self.pricePath) - 1: # have to sell on last day?
                valueOfSellingEachMonth[month] = self.pricePath[month] - self.initPrice
            if self.pricePath[month] > self.startSellPrice:
                valueOfSellingEachMonth[month] = self.pricePath[month] - self.initPrice
        return valueOfSellingEachMonth
    

class NormalMotion:

    def simulate_paths(self):
        while(self.T - self.dt > 0):
            if self.changeVolitilityMonth > 0:
                if self.dt >= self.changeVolitilityMonth:
                    self.volatility = self.secondVolitility
                
            # New price = Current Price + Market Increase + Market Volatility

            # Market Increase = percent monthly drift * Current Price
            market_increase = self.drift * self.current_price
            # Market volitility = pull from standard normal distribution * monthly volitility * Current Price
            dWt = np.random.normal(0, 1)  # 68% of the time the volitility will be < 3%
            volatility_price_change = self.volatility * dWt * self.current_price
         
            self.current_price += volatility_price_change + market_increase  # Add the change to the current price
            self.prices.append(self.current_price)  # Append new price to series
            self.dt += 1   # Account for the step in time

    def __init__(self, initial_price, drift, volatility, dt, T, changeVolitilityMonth=-1, secondVolitility=0):
        self.current_price = initial_price
        self.initial_price = initial_price
        self.drift = drift
        self.volatility = volatility
        self.dt = dt
        self.T = T
        self.prices = []
        self.changeVolitilityMonth = changeVolitilityMonth
        self.secondVolitility = secondVolitility
        self.simulate_paths()


class BetaMotion:

    def simulate_paths(self):
        while(self.T - self.dt > 0):
            dWt = np.random.beta(14, 6) - .65  # Beta motion with shift to left of .65
            dYt = self.drift*self.dt + self.volatility*dWt  # Change in price
            # print("Change in price: {0}", dYt)
            self.current_price += dYt  # Add the change to the current price
            self.prices.append(self.current_price)  # Append new price to series
            self.T -= self.dt  # Accound for the step in time

    def __init__(self, initial_price, drift, volatility, dt, T):
        self.current_price = initial_price
        self.initial_price = initial_price
        self.drift = drift
        self.volatility = volatility
        self.dt = dt
        self.T = T
        self.prices = []
        self.simulate_paths()

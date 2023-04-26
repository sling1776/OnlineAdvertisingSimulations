from gameTheory import *

s = Simulation()
s.simulate(numStandard=1, title="Monopoly Standard Demo")
s.simulate(numStandard=2, title="Shared Standard")
s.simulate(numBidders=1, numStandard=1, title="Bidder vs Standard")
s.simulate(numBidders=2, title="Bidder vs Bidder")
s.simulate(numBidders=2, numStandard=1, title="Bidder vs Bidder vs Standard")
s.simulate(numHunters=1, numBidders=1, title="Hunter vs Bidder", rand=True)
s.simulate(numHunters=1, numBidders=2, title="Hunter vs Bidder vs Bidder", rand=True)

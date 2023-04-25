from MonteCarlo import *




# Do It of a compnay looking to buy an advertising space:
# How much is the space returning in revenue?
# How does the price change of space affect it?
# Advertising to Sales Ratio -> The amount of money spent on ads / revenue from product. (Hopefully around 10% - 25%)


# We use a basemark of 100,000 ad impressions. With this number we can determine the cost of a space and the revenue
# that we would generate. On average we can assume that ads will bring in buyers for a total of about .0004 of the total 
# impressions. For this we will use 400 buyers for every 100,000 impressions. 
# 
# Value_of_space = Revenue_generated - Cost_of_space
# Revenue_generated = (Num_impressions * .0004) * Product_price
# 

NUM_IMPRESSIONS = 100_000
IMPRESSION_TO_BUYER_RATIO = .0004
PRODUCT_PRICE = 51 # with 100,000 impressions, $50 will result in a $0 initial value.
COST_SPACE = 2000
NUMBER_MONTHS = 120
VALUE_GROWTH = .01
VOLITILITY = .20
NUMBER_PATHS = 5000


REVENUE_GENERATED = NUM_IMPRESSIONS * IMPRESSION_TO_BUYER_RATIO * PRODUCT_PRICE
INITAL_VALUE = REVENUE_GENERATED - COST_SPACE


# Initial price should not be $0.


price_paths_normal = []
for _ in range(NUMBER_PATHS):
    price_paths_normal.append(NormalMotion(INITAL_VALUE, VALUE_GROWTH/12, VOLITILITY/12, 1, 120).prices)


for path in price_paths_normal:
    plt.plot(path)
plt.show()

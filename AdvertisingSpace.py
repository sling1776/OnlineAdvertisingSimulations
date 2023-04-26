from MonteCarlo import *



class AdvertisingSpace:
    def __init__(self, num_clicks=100_000, product_price=50, excpected_annual_growth_value=.01, volatility=.1, click_to_buyer_ratio=.1, space_cost=None, cost_per_click=None, name="") -> None:
        assert space_cost is not None or cost_per_click is not None

        if cost_per_click is not None:
            self.space_cost = num_clicks*cost_per_click
        else:
            self.space_cost = space_cost
        self.num_clicks = num_clicks
        self.product_price = product_price
        self.expected_annual_growth_value = excpected_annual_growth_value
        self.volatility = volatility
        self.click_to_buyer_ratio= click_to_buyer_ratio
        
        # Value_of_space = Revenue_generated - Cost_of_space
        # Revenue_generated = (Num_impressions * impression_to_buyer_ratio) * Product_price
        self.revenue_generated = num_clicks * self.click_to_buyer_ratio * self.product_price
        self.inital_value = self.revenue_generated - self.space_cost

        if self.inital_value == 0: # initial value can't be zero for it to work.
            self.inital_value = 1

        self.name = name


    def simulateSpace(self, months_simulated=120, num_simulated_paths=1000, DISPLAY=True):
        plt.figure()
        price_paths_normal = []
        for _ in range(num_simulated_paths):
            price_paths_normal.append(NormalMotion(self.inital_value, self.expected_annual_growth_value/12, self.volatility/12, 1, months_simulated).prices)

        ends = []
        for path in price_paths_normal:
            ends.append(path[-1])
        ma = max(ends)
        average = np.average(ends)
        mi = min(ends)

        print(f"--------------------------------\n"+
                f"Report for {self.name} - ${self.product_price} item with approximately {self.num_clicks} clicks per month:\n" +
                f"\tAverage Return: ${round(average)}\n" +
                f"\tMax Return:     ${round(ma)}\n" +
                f"\tMin Return:     ${round(mi)}\n" +
                f"--------------------------------"
              )

        if DISPLAY:
            for path in price_paths_normal:
                plt.title(f"{self.name} - Start: \${self.inital_value} - Product: \${self.product_price}")
                plt.plot(path)
            plt.show()


if __name__ == '__main__':
    product_prices = [25, 50, 100]

    advertising_spaces = []
    for price in product_prices:

        # Youtube: has a higher click to buyer ratio because of google's ad targeting and not charging for skipped ads
        advertising_spaces.append(
            AdvertisingSpace(
                name="YouTube",
                cost_per_click=.02,
                click_to_buyer_ratio=.05, 
                num_clicks=1000,
                volatility=.1,
                product_price=price
            )
        )

        # Facebook: 
        advertising_spaces.append(
            AdvertisingSpace(
                name="FaceBook",
                cost_per_click=.37,
                click_to_buyer_ratio=.01,
                num_clicks=1000,
                volatility=.1,
                product_price=price
            )
        )

        # Instagram: higher volatility from younger users.
        advertising_spaces.append(
            AdvertisingSpace(
                name="Instagram",
                cost_per_click=.50,
                click_to_buyer_ratio=.01,
                num_clicks=1000,
                volatility=.15,
                product_price=price
            )
        )

        # TicToc: very high volatility from young users, tictok charges per view rather than click giving us a higher volatility
        views = 100_000
        advertising_spaces.append(
            AdvertisingSpace(
                name="TicToc",
                space_cost=10 * (views/1000), # $10 for 1000 views
                click_to_buyer_ratio=.01,
                volatility=.20,
                num_clicks=views * .01, # 1% of the views will click on our ad
                product_price=price
            )
        )

        # Google Search: Applies to search page only, Higher buy rate for each click because people who click are looking to buy
        advertising_spaces.append(
            AdvertisingSpace(
                name="Google Search",
                cost_per_click=1,
                click_to_buyer_ratio=.05,
                num_clicks=1000,
                volatility=.1,
                product_price=price
            )
        )

        # Google Display: Applies to google ad spaces on other websites. higher click to buyer ratio as people click the ad to buy it usually
        advertising_spaces.append(
            AdvertisingSpace(
                name="Google Display",
                cost_per_click=.44,
                click_to_buyer_ratio=.05,
                num_clicks=1000,
                volatility=.1,
                product_price=price
            )
        )


    for space in advertising_spaces:
        space.simulateSpace(DISPLAY=True)
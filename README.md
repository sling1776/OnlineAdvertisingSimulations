# Exploring Uncertainty Algorithms in the Context of Internet Advertisement

Our project will focus on three areas of internet advertisement: User response, advertisement space, and advertisement competition.

In our project we intend to use three algorithms: Explore and Exploit, Monte Carlo algorithms with advertising strategies similar to options, and Game Theory. 


## User Response

```UserResponse.py```

You don't always have the required information to make the best decision possible. In online advertising there are many different avenues one could take. This part of our project is dedicated to showing that the Epsilon-Greedy algorithm is a viable method of discovering the optimal advertising strategy. The strategies under consideration in our simulation are:

* Facebook
  * Native ads
  * Video ads
  * Carousel ads
  * Interactive ads
* Google
  * Search ads
  * Display ads
* Email
  * North/South America
  * UK
  * Europe
  * Asia/Pacific

Because we don't have access to much real-world data about internet advertising, this is likely due to the competitive nature of advertising, we created mock distributions of the click-through-rates for the different strategies. We created these distributions from an article found at https://agencyanalytics.com/blog/average-click-through-rate.

Click-through rate (CTR) is a metric used in online advertising to measure the ratio of users who click on a specific link to the number of total users who view a page, email, or advertisement.

### Requirements

To run ```UserResponse.py``` you will need the following:

* numpy
* matplotlib
* ``ExploreAndExploit.py``

### Output
Here is the reward function: ![](images/reward.png)

Here is the simulations graph: ![](images/simulations.png)

### Conclusion
From the rewards graph we can see that the Epsilon-Greedy algorithm does improve over time and from the simulations graph we can see that it does make a decision, more or less. In the real world, one could decide to go with the best performing option after they observe each option significantly diverging.

## Advertising Space

```AdvertisingSpace.py```

Choosing the most valuable advertising space for your company is the best way to increase revenue from your product. It is important that an advertising space brings in more revenue than it costs. By using a MonteCarlo algorithim we can predicit how an advertising space might improve for a product. Using this information we can determine which online advertising spaces are the best for a company. 

We believe that a monte carlo algorithm similar to stock options can be utilized to solve the problem of advertising space pricing. To help calculate what a space might be worth we will use the revenue generated from the space subtracted from the price of the space. The value of the space also depends on the product that the company would be selling and the click to buyer ratio that the product brings. 

Most of the simulation examples come from various popular advertising spaces. As not all the information needed is available since as researchers we are not selling products, we were able to esitmate averages for a fictitious company looking to buy an advertising space with various product prices and click to buyer ratios. 

### Requirements

To run ```AdvertisingSpace.py``` you will need the following:

* matplotlib
* ``MonteCarlo.py``

### Output

Interesting points to note are for TicToc which does not do well for advertising. Even with a product revenue of $100 it is an extremely expensive advertising space and only ends up with a return of around $1. The best return ended up being Google Display advertisements. An interesting point to notice is that for many configurations, if the product is not priced high enough, advertising ends up being more expensive than its worth.


## Advertisement Competition

```AdvertisementCompetitors.py```

Having different strategies for obtaining advertising spaces is important. What is interesting is 

Game theory algorithms will be implemented for simulation of this side of iternet advertisement.

To run ```AdvertisementCompetitors.py``` you will need the following:

* Insert required libraries here
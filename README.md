# EV-Charging-Simulation
Electric vehicles decide which charging station to go.
## Scope and data
In king county, there are a number of total 30,813 electric vehicles and 819 charging stations around 26 cities. By observing the data, we found that in the great Seattle area, there are more than 400 charging stations. In the city of Duvall, there are no charging stations existing. We grouped charging stations into a set of servers and cities into units. For example, in the great Seattle area, we grouped 400 charging stations into 3 servers and are located based on the charging station density on the map. In those areas without charging stations, they are incorporated into surrounding cities that have charging stations. In the end, we have 25 servers in 30 units and all 30,813 electric vehicles are considered in King county.
Based on the actual location of King county, we used latitude and longitude to set the unit boundary. Every charging station has its corresponding latitude and longitude coordinates. In addition, we generated random locations demonstrated by the coordinators of electric vehicles in each unit using the information of electric vehicle numbers. Once these coordinators are generated, the locations are fixed in each simulation process. After having the coordinates of both the charging stations and electric vehicles, the distance between electric vehicles and charging stations is calculated. The distance vector has totally of 924,390 elements.
## Simulation model
In the simulation model, the agent is an electric vehicle in any random places within the range of units. The server is a collection of charging stations in a particular area. To convert distances into decisions, the probability of electric vehicles to each server is calculated by the distance to the server. To be specific, we sort the distance data for an electric vehicle to all the servers in ascending order. The order list is divided into 5 intervals, corresponding to 5 sets of probabilities as shown in Figure 1. The electric vehicles have a probability of a uniform distribution between 0.75 to 0.95 to the server in the top 4 in the list. The probability of electric vehicles choosing the servers from the 5th to the 8th is between 0.65 to 0.85 in a uniform distribution. The probability of electric vehicles to the servers stations from the 9th to the 12th is between 0.55 to 0.75 in a uniform distribution. And The probability of electric vehicles to the servers stations from the 13th to the 16th is from 0.65 to 0.85 in a uniform distribution. The servers in the bottom 4 have 0 probability for any EV to choose for CS. There is an overlap between each interval that increases the randomness while EV chooses the charging station.

![image](https://user-images.githubusercontent.com/107434628/173617473-94b5c201-90b8-48e0-87e6-44eae16c8f17.png)

To convert the charging station numbers into decisions, we set up the probability of electric vehicles on any server based on the number of charging stations. The service rate probability is equal to 1 minus the fraction of 1 over the number of servers plus m in such area as shown in equation 1. The m is a fixed parameter equal to 1 that avoids computing with a 0 denominator.

𝑃_𝑆𝑗 = 1 − 1 / (𝑛𝑢𝑚𝑏𝑒𝑟 𝑜𝑓 𝑠𝑒𝑟𝑣𝑒𝑟𝑠 + 𝑚)

The selection of electric vehicle charging decisions is determined by the product of the probability of electric vehicles to each server based on the distance to the server and the service rate probability as shown below.

𝑃_𝑓 = 𝑃_𝑆𝑗 × 𝑃_𝐷𝑖𝑗

The probability of each electric vehicle reaching each server is calculated and stored in a list. At the end of the simulation process, the electric vehicles select a charging station based on the final probability list and the number of EVs in each server is counted. The ratio of the number of EVs and CS plus m, called “demand-supply ratio”, is used to determine if the system is idle or overloaded.
## Result
The model produces two results:
1. The number of electric vehicles going to each region.
2. The ratio of the number in 1 over the number of charging stations in that region.

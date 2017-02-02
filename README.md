# Scalable-Spatial-Analytics-Project
## Electricity price prediction and nodal price analysis on California ISO (Independent System Operator)

This repository provides the source code, images and report of a final project for the course CE263N Scalable Spatial Analytics taught at UC Berkeley.

In the United States, an independent system operator (ISO) controls and monitors the operation of the electrical power system within a given perimeter. In California, CAISO (California ISO) also acts as the electricity market operator. 
In this project we focused our attention on the **Day Ahead Market (DAM)** for electricity. This market takes place one day prior to the operating day and consists of scheduling the quantities and marginal electricity prices (wholesale) for each hour. 
The marginal clearing price corresponds to the intersection between the supply and demand curve: these curves are formed by CAISO who receive bids from all the market participants (essentially: electricity retailers, generators, and virtual bidders).

CAISO has the specificity of having different clearing prices based on location, this is done with the purpose of including externalities of electricity losses (around 6% on the transmission grid [6]), and electricity congestion in the final price [7]. All in all, the clearing price in the DAM is specific to a location (or node), and is referred to as **Local Marginal Price (LMP)**.

It is essential for a market participant to be able to predict the DAM price before submitting its bid to CAISO. That is why in a first step we decided to build a prediction model for the DAM price (average price in the system, not the LMP). It is also important for the market participant to understand the underlying risk when making a bid: that is why we studied the error between our prediction and the realized price.
In a second step, we examined and visualized the LMP behavior, which is particularly interesting if we want to understand the local market power an agent can have.

Final Project by Melanie Manguin, Emily Porter & Bertrand Travacca.

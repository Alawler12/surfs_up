# Surf Shop Weather Analysis

## Overview
The purpose of this analysis is to determine the sustainability of a surf and ice cream shop in Oahu.  To do this we analyzed the weather data for this location, specifically from June and December to see how the weather might look all year round. I used Python, Pandas methods, and SQLAlchemy to query the SQLite database and determine the weather outcomes for each month.

## Results
The three key differences between the weather in June and December are as follows:
  - The average temperature is about 3 degrees warmer in June
  - The maximum temperature is about 2 degrees warmer in June
  - The minimum temperature is 8 degrees warmer in June

![june_weatherPNG](https://github.com/Alawler12/surfs_up/blob/master/june_weather.PNG)
![December_weather.PNG](https://github.com/Alawler12/surfs_up/blob/master/december_weather.PNG)

## Summary
### Temperatures seem advantageous
Based on this analysis, an ice cream/surf shop seems sustainable year-round in Oahu, as temperatures are warm all year. The temperatures do not vary much between these two months.  While the minimum temperature in December is not exactly ice cream weather, the average temperature is only 3 degrees less than June, which suggests that cold days are not the norm.  

### More analysis needed
However, from our previous analysis of yearly weather, we know that precipitation varies monthly.  Some additional queries should be made before fully committing to the ice cream/surf shop model.  I would also like to perform an additional query on the monthly precipitation for June and December to compare those outcomes.  I would also perform a query to find the hottest, driest month of the year to give the shop a target opening date, so that it has the best chance of the best weather right from opening day.

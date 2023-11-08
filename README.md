# Calculate Mutual Fund Profit
This repository contains a Python function and a FastAPI app to calculate the profit for a mutual fund investment based on the given scheme code, start date, end date, and initial investment capital.
<br>
<br>
The calculate_profit function is implemented to perform the following steps:
<br>
Retrieve Net Asset Values (NAVs) from the API: https://api.mfapi.in/mf/<scheme_code> for the given start and end dates.
<br>
Calculate the number of units allotted on the purchase date, the value of the units on the redemption date, the net profit as the difference between the value on the redemption date and the initial investment.
<br>
<br>
he FastAPI app provides a single route /profit that accepts query string parameters scheme_code, start_date, end_date, and capital.
<br>
Run the FastAPI app using CMD:
<br>
  uvicorn mutualfund:app --reload
<br>
<br>
Access the API  locally by browsing the following URL:
<br>
http://localhost:8000/profit?scheme_code=101206&start_date=26-07-2023&end_date=18-10-2023&capital=1000000

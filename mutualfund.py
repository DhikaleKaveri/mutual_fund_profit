#!/usr/bin/env python
# coding: utf-8

import requests
from datetime import datetime, timedelta
from fastapi import FastAPI, Query


app = FastAPI()


def nav(data, date):
    for val in data:
        if val['date'] == date:
            return val['nav']
    return None


def calculate_profit(scheme_code, start_date, end_date, capital=1000000.0):
    
    url = f"https://api.mfapi.in/mf/{scheme_code}"
    response = requests.get(url)
    data = response.json()['data']
    nav_val1 = nav(data, start_date)
    nav_val2 = nav(data, end_date)
    
    start = datetime.strptime(start_date, '%d-%m-%Y')
    end = datetime.strptime(end_date, '%d-%m-%Y')
    while nav_val1 is None or nav_val2 is None:
        if nav_val1 is None:
            start += timedelta(days=1)
            nav_val1 = nav(data, start.strftime('%d-%m-%Y'))
        else:
            end -= timedelta(days=1)
            nav_val2 = nav(data, end.strftime('%d-%m-%Y'))    
    
    units_allotted = capital / float(nav_val1)
    value_redemption = units_allotted * float(nav_val2)
    net_profit = value_redemption - capital
    
    return net_profit



@app.get("/profit")
async def get_profit(scheme_code: str = Query(..., title="Scheme Code"),
               start_date: str = Query(..., title="Start Date (dd-mm-yyyy)"),
               end_date: str = Query(..., title="End Date (dd-mm-yyyy)"),
               capital: float = Query(1000000.0, title="Initial Investment")):
    try:
        profit = calculate_profit(scheme_code, start_date, end_date, capital)
        profit = round(profit,2)
        return {"net_profit": profit}
    except Exception as e:
        return {"error": str(e)}





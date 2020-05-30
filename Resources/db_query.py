# To add a new cell, type '# %%'
# To add a new markdown cell, type '# %% [markdown]'
# %%
# Dependencies
# ----------------------------------
# Imports the method used for connecting to DBs
from sqlalchemy import create_engine

# Imports the methods needed to abstract classes into tables
from sqlalchemy.ext.declarative import declarative_base

# Allow us to declare column types
from sqlalchemy import Column, Integer, String, Float, Date, VARCHAR, Time

from datetime import datetime

import os
import csv
import pandas as pd
 


# %%
# Create Stocks and Tweets Classes

# Sets an object to utilize the default declarative base in SQL Alchemy
Base = declarative_base()

class Stocks(Base):
    __tablename__ = 'stock'
    id = Column(Integer, primary_key=True)
    date = Column(Date)
    open = Column(Float)
    close = Column(Float)
    change =  Column(Float)


class Tweets(Base):
    __tablename__ = 'tweet'
    id = Column(Integer, primary_key=True)
    date = Column(Date)
    time = Column(Time)
    tweet = Column(String)


# %%
with open('TSLA_Cleaned.csv', newline='') as f:
    reader = csv.reader(f)
    data = list(reader)


# %%
# Create Database Connection
# ----------------------------------
# Creates a connection to our DB
engine = create_engine("sqlite:///ElonMusk.sqlite")
conn = engine.connect()
Base.metadata.create_all(engine)


# %%
# Create a Session Object to Connect to DB
# ----------------------------------
# Session is a temporary binding to our DB
from sqlalchemy.orm import Session
session = Session(bind=engine)


# %%
# Find the last row so the while loop knows when to end
end = len(data)
# Start where the data starts, avoiding the header
x = 1
# While there's data, convert each variable from a string to match the data type
while x < end:
    # Assign each value to a variable
    dt = datetime.strptime(data[x][1], '%Y-%m-%d').date()
    op = float(data[x][2])
    cl = float(data[x][3])
    ch = float(data[x][4])
    # Create a query, add it, and commit it
    stk = Stocks(date=dt, open=op, close=cl, change=ch)
    session.add(stk) 
    session.commit()
    # Next row!
    x += 1


# %%
stock_list = session.query(Stocks)
for x in stock_list:
    print(x.date, x.open, x.close, x.change)


# %%



# %%



# %%



# %%



# %%



# %%



# %%
# Query All Records in the the Database
data = engine.execute("SELECT * FROM ElonTweets_2010-2017.csv")
for row in data:
    print(row)


# %%



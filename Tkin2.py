from tkinter import *
import requests 
import json

pyc=Tk()
pyc.title("My Crypto")
pyc.iconbitmap("favicon.ico")



def font_color(amount):
    if amount>0:
        return "green"
    else:
        return "red"


def myPortfolio():

    api_request = requests.get("https://pro-api.coinmarketcap.com/v1/cryptocurrency/listings/latest?start=1&limit=20&convert=USD&CMC_PRO_API_KEY=66557877-3ca1-4aa0-802a-bbb9a1173d03")
    api = json.loads(api_request.content)

    coins = [
    {
        "symbol":"BTC",
        "amount_owned":92,
        "price_per_coin": 3200
    }, 
    {
        "symbol":"EOS",
        "amount_owned": 0.23,
        "price_per_coin": 2.05
    },
    {
        "symbol": "LTC",
        "amount_owned": 10,
        "price_per_coin": 55.03
    },
    {
        "symbol": "XMR",
        "amount_owned": 10,
        "price_per_coin": 135.05
    }
    ]



    total_pl = 0
    coin_row=1
    for i in range(0, 20):
        for coin in coins:
            
            if api["data"][i]["symbol"] == coin["symbol"]:

                total_paid = coin["amount_owned"] * coin["price_per_coin"]
                current_value = coin["amount_owned"] * api["data"][i]["quote"]["USD"]["price"]
                pl_percoin = api["data"][i]["quote"]["USD"]["price"] - coin["price_per_coin"]
                total_pl_coin = pl_percoin * coin["amount_owned"]

                name=Label(pyc,text=api["data"][i]["symbol"],bg="white",fg="pink",font="Lato 12 bold",padx="5",pady="5",borderwidth=2,relief="groove")
                name.grid(row=coin_row,column=0,sticky=N+S+E+W)

                price=Label(pyc,text="${0:.2f}".format(api["data"][i]["quote"]["USD"]["price"]),bg="white",fg="pink",font="Lato 12 bold",padx="5",pady="5",borderwidth=2,relief="groove")
                price.grid(row=coin_row,column=1,sticky=N+S+E+W)

                no_coins=Label(pyc,text=coin["amount_owned"],bg="white",fg="pink",font="Lato 12 bold",padx="5",pady="5",borderwidth=2,relief="groove")
                no_coins.grid(row=coin_row,column=2,sticky=N+S+E+W)

                amount_paid=Label(pyc,text="${0:.2f}".format(total_paid),bg="white",fg="pink",font="Lato 12 bold",padx="5",pady="5",borderwidth=2,relief="groove")
                amount_paid.grid(row=coin_row,column=3,sticky=N+S+E+W)

                current_valuee=Label(pyc,text="${0:.2f}".format(current_value),bg="white",fg="Pink",font="Lato 12 bold",padx="5",pady="5",borderwidth=2,relief="groove")
                current_valuee.grid(row=coin_row,column=4,sticky=N+S+E+W)

                pl_coin=Label(pyc,text="${0:.2f}".format(pl_percoin),bg="white",fg=font_color(pl_percoin),font="Lato 12 bold",padx="5",pady="5",borderwidth=2,relief="groove")
                pl_coin.grid(row=coin_row,column=5,sticky=N+S+E+W)

                Total_PL=Label(pyc,text="$%.2f"%(total_pl_coin),bg="white",fg=font_color(total_pl_coin),font="Lato 12 bold",padx="5",pady="5",borderwidth=2,relief="groove")
                Total_PL.grid(row=coin_row,column=6,sticky=N+S+E+W)

                coin_row=coin_row+1
      
            total_pl = total_pl + total_pl_coin

        # print(api["data"][i]["name"] + " - " + api["data"][i]["symbol"])
        # print("Price - ${0:.2f}".format(api["data"][i]["quote"]["USD"]["price"]))
        # print("Number Of Coin:", coin["amount_owned"])
        # print("Total Amount Paid:", "${0:.2f}".format(total_paid))
        # print("Current Value:", "${0:.2f}".format(current_value))
        # print("P/L Per Coin:", "${0:.2f}".format(pl_percoin))
        # print("Total P/L With Coin:", "$%.2f"%(total_pl_coin))
        # print("----------------")
    #print("Total P/L For Portfolio:","$%.2f"%(total_pl))
    #print(f"Total P/L For Portfolio:{total_pl: 0.2f}")#this is another way of printing by fstring

        
    Total_PL=Label(pyc,text="$%.2f"%(total_pl),bg="grey",fg=font_color(total_pl),font="Lato 12 bold",padx="5",pady="5",borderwidth=2,relief="groove")
    Total_PL.grid(row=coin_row,column=6,sticky=N+S+E+W)

    api=""
    update=Button(pyc,text="UPDATE",command=myPortfolio,bg="grey",fg="Blue",font="Lato 12 bold",padx="5",pady="5",borderwidth=2,relief="groove")
    update.grid(row=coin_row+1,column=6,sticky=N+S+E+W)
# pyc.mainloop() #it basically holds our GUI
# print("After closing Window")
name=Label(pyc,text="CoinName",bg="yellow",fg="black",font="Lato 12 bold",padx="5",pady="5",borderwidth=2,relief="groove")
name.grid(row=0,column=0,sticky=N+S+E+W)

price=Label(pyc,text="Price",bg="yellow",fg="black",font="Lato 12 bold",padx="5",pady="5",borderwidth=2,relief="groove")
price.grid(row=0,column=1,sticky=N+S+E+W)

no_coins=Label(pyc,text="coin Owned",bg="yellow",fg="black",font="Lato 12 bold",padx="5",pady="5",borderwidth=2,relief="groove")
no_coins.grid(row=0,column=2,sticky=N+S+E+W)

amount_paid=Label(pyc,text="Total Amount Paid",bg="yellow",fg="black",font="Lato 12 bold",padx="5",pady="5",borderwidth=2,relief="groove")
amount_paid.grid(row=0,column=3,sticky=N+S+E+W)

current_value=Label(pyc,text="Current_Value",bg="yellow",fg="black",font="Lato 12 bold",padx="5",pady="5",borderwidth=2,relief="groove")
current_value.grid(row=0,column=4,sticky=N+S+E+W)

pl_coin=Label(pyc,text="P/L Per Coin",bg="yellow",fg="black",font="Lato 12 bold",padx="5",pady="5",borderwidth=2,relief="groove")
pl_coin.grid(row=0,column=5,sticky=N+S+E+W)

Total_PL=Label(pyc,text="Total_P/L ",bg="yellow",fg="black",font="Lato 12 bold",padx="5",pady="5",borderwidth=2,relief="groove")
Total_PL.grid(row=0,column=6,sticky=N+S+E+W)
# name.pack()# not in ur control so better to use grid so as to do what we want
myPortfolio()
pyc.mainloop()
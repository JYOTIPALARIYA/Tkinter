from tkinter import *
from tkinter import messagebox,Menu
import requests 
import json
import sqlite3
import webbrowser
import threading

pyc=Tk()
pyc.title("My Crypto")
pyc.iconbitmap("favicon.ico")


con=sqlite3.connect('coin.db')
cursorOb=con.cursor()
cursorOb.execute("CREATE TABLE IF NOT EXISTS coin(id INTEGER PRIMARY KEY,symbol TEXT, amount INTEGER,price REAL)")
con.commit()


# print(coins)
# cursorOb.execute("INSERT INTO coin VALUES(1,'BTC',2,3520)")
# cursorOb.execute("INSERT INTO coin VALUES(2,'EOS',2,3520)")
# cursorOb.execute("INSERT INTO coin VALUES(3,'LTC',2,3520)")
# cursorOb.execute("INSERT 666INTO coin VALUES(4,'XMR',2,3520)")
# con.commit()
def enable_refresh(btn):
    btn.config(state='normal')

def refresh1():
    myPortfolio()

def reset():
    
    for cell in pyc.winfo_children():
        cell.destroy()
    nav_itm()
    app_head()
    myPortfolio()
    
    # re.update()
    # time.sleep(5)
    # re.config(state='normal')
    # re.update()

def nav_itm():
    def clear_all():
        cursorOb.execute("DELETE FROM coin")
        con.commit()
        timer.cancel()
        reset()
        messagebox.showinfo("Portfolio Notification","Portfolio cleared _ Add new Coins")
    
    def close_app():
        pyc.destroy()

    def help_url():
        r=messagebox.askokcancel("PortFolio","Do u really wanna open")
        if r:

            url="https://coinmarketcap.com/"
            webbrowser.open(url,new =1)
        
       
    menu=Menu(pyc)
    file_item=Menu(menu)
    file_item.add_command(label='Clear Portfolio',command=clear_all)
    file_item.add_command(label='Close Portfolio',command=close_app)
    menu.add_cascade(label='File',menu=file_item)
    #2nd item
    menu.add_cascade(label='Help',command=help_url)
    #3rd item
    link_menu=Menu(menu) 
    aurl="https://pro.coinmarketcap.com/account/"
    link_menu.add_command(label='API Account Page',command=lambda:webbrowser.open(aurl,new=1))
    durl=" https://coinmarketcap.com/api/documentation/v1/"
    link_menu.add_command(label='Documentation Page',command=lambda:webbrowser.open(durl,new=1))
    menu.add_cascade(label='View URL',menu=link_menu)
    pyc.config(menu=menu)

def myPortfolio():

    api_request = requests.get("https://pro-api.coinmarketcap.com/v1/cryptocurrency/listings/latest?start=1&limit=20&convert=USD&CMC_PRO_API_KEY=66557877-3ca1-4aa0-802a-bbb9a1173d03")
    api = json.loads(api_request.content)

    cursorOb.execute("SELECT * FROM coin")
    coins=cursorOb.fetchall()

    def font_color(amount):
        if amount>0:
            return "green"
        else:
            return "red"

    def insert_coin():
        cursorOb.execute("INSERT INTO coin(symbol,price,amount) Values(?,?,?)",(sym_txt1.get(),sym_txt2.get(),sym_txt3.get()))
        con.commit()
        timer.cancel()
        reset()
        messagebox.showinfo("Porfolio Application","Coin Added Successfully")
        
    def update():
        cursorOb.execute("UPDATE coin SET symbol=?,price=?,amount=? WHERE id=?",(sym_up.get(),price_up.get(),am_up.get(),id_update.get()))
        con.commit()
        timer.cancel()
        reset()
        messagebox.showinfo("Porfolio Application","Coin Updated Successfully")
        
    def delete():
        cursorOb.execute("DELETE FROM coin where id=?",ID_DEL.get(),)
        con.commit()
        timer.cancel()
        reset()
        messagebox.showinfo("Porfolio Application","Coin Deleted Successfully")
        

    # coins = [
    # {
    #     "symbol":"BTC",
    #     "amount_owned":92,
    #     "price_per_coin": 3200
    # }, 
    # {
    #     "symbol":"EOS",
    #     "amount_owned": 0.23,
    #     "price_per_coin": 2.05
    # },
    # {
    #     "symbol": "LTC",
    #     "amount_owned": 10,
    #     "price_per_coin": 55.03
    # },
    # {
    #     "symbol": "XMR",
    #     "amount_owned": 10,
    #     "price_per_coin": 135.05
    # }
    # ]



    total_pl = 0
    coin_row=1
    total_current_value=0
    total_amount_paid=0
    for i in range(0, 20):
        for coin in coins:
            
            if api["data"][i]["symbol"] == coin[1]:

                total_paid = coin[2] * coin[3]
                current_value = coin[2] * api["data"][i]["quote"]["USD"]["price"]
                pl_percoin = api["data"][i]["quote"]["USD"]["price"] - coin[3]
                total_pl_coin = pl_percoin * coin[2]


                name=Label(pyc,text=coin[0],bg="white",fg="pink",font="Lato 12 bold",padx="5",pady="5",borderwidth=2,relief="groove")
                name.grid(row=coin_row,column=0,sticky=N+S+E+W)

                name=Label(pyc,text=api["data"][i]["symbol"],bg="white",fg="pink",font="Lato 12 bold",padx="5",pady="5",borderwidth=2,relief="groove")
                name.grid(row=coin_row,column=1,sticky=N+S+E+W)

                price=Label(pyc,text="${0:.2f}".format(api["data"][i]["quote"]["USD"]["price"]),bg="white",fg="pink",font="Lato 12 bold",padx="5",pady="5",borderwidth=2,relief="groove")
                price.grid(row=coin_row,column=2,sticky=N+S+E+W)

                no_coins=Label(pyc,text=coin[2],bg="white",fg="pink",font="Lato 12 bold",padx="5",pady="5",borderwidth=2,relief="groove")
                no_coins.grid(row=coin_row,column=3,sticky=N+S+E+W)

                amount_paid=Label(pyc,text="${0:.2f}".format(total_paid),bg="white",fg="pink",font="Lato 12 bold",padx="5",pady="5",borderwidth=2,relief="groove")
                amount_paid.grid(row=coin_row,column=4,sticky=N+S+E+W)

                current_valuee=Label(pyc,text="${0:.2f}".format(current_value),bg="white",fg="Pink",font="Lato 12 bold",padx="5",pady="5",borderwidth=2,relief="groove")
                current_valuee.grid(row=coin_row,column=5,sticky=N+S+E+W)

                pl_coin=Label(pyc,text="${0:.2f}".format(pl_percoin),bg="white",fg=font_color(pl_percoin),font="Lato 12 bold",padx="5",pady="5",borderwidth=2,relief="groove")
                pl_coin.grid(row=coin_row,column=6,sticky=N+S+E+W)

                Total_PL=Label(pyc,text="$%.2f"%(total_pl_coin),bg="white",fg=font_color(total_pl_coin),font="Lato 12 bold",padx="5",pady="5",borderwidth=2,relief="groove")
                Total_PL.grid(row=coin_row,column=7,sticky=N+S+E+W)

                coin_row+=1
      
            total_pl+= total_pl_coin
            total_current_value+=current_value
            total_amount_paid+=total_paid

        # print(api["data"][i]["name"] + " - " + api["data"][i]["symbol"])
        # print("Price - ${0:.2f}".format(api["data"][i]["quote"]["USD"]["price"]))
        # print("Number Of Coin:", coin[2])
        # print("Total Amount Paid:", "${0:.2f}".format(total_paid))
        # print("Current Value:", "${0:.2f}".format(current_value))
        # print("P/L Per Coin:", "${0:.2f}".format(pl_percoin))
        # print("Total P/L With Coin:", "$%.2f"%(total_pl_coin))
        # print("----------------")
    #print("Total P/L For Portfolio:","$%.2f"%(total_pl))
    #print(f"Total P/L For Portfolio:{total_pl: 0.2f}")#this is another way of printing by fstring



    #INSERT------------
    sym_txt1=Entry(pyc,borderwidth=2,relief="groov")
    sym_txt1.grid(row=coin_row+1,column=1)
    sym_txt2=Entry(pyc,borderwidth=2,relief="groov")
    sym_txt2.grid(row=coin_row+1,column=2)
    sym_txt3=Entry(pyc,borderwidth=2,relief="groov")
    sym_txt3.grid(row=coin_row+1,column=3)
    addcoin=Button(pyc,text="Add_Coin",bg="grey",fg="black",command=insert_coin,font="Lato 12 bold",padx="5",pady="5",borderwidth=2,relief="groove")
    addcoin.grid(row=coin_row+1,column=4,sticky=N+S+E+W)

    #UPDATE------
    id_update=Entry(pyc,borderwidth=2,relief="groov")
    id_update.grid(row=coin_row+2,column=0)
    sym_up=Entry(pyc,borderwidth=2,relief="groov")
    sym_up.grid(row=coin_row+2,column=1)
    price_up=Entry(pyc,borderwidth=2,relief="groov")
    price_up.grid(row=coin_row+2,column=2)
    am_up=Entry(pyc,borderwidth=2,relief="groov")
    am_up.grid(row=coin_row+2,column=3)
    update_data=Button(pyc,text="Update_data",bg="grey",fg="black",command=update,font="Lato 12 bold",padx="5",pady="5",borderwidth=2,relief="groove")
    update_data.grid(row=coin_row+2,column=4,sticky=N+S+E+W)

    #DELETE

    ID_DEL=Entry(pyc,borderwidth=2,relief="groov")
    ID_DEL.grid(row=coin_row+3,column=1)
    del_data=Button(pyc,text="DELETE_DATA",bg="grey",fg="black",command=delete,font="Lato 12 bold",padx="5",pady="5",borderwidth=2,relief="groove")
    del_data.grid(row=coin_row+3,column=2,sticky=N+S+E+W)
    
    Total_cv=Label(pyc,text="$%.2f"%(total_current_value),bg="grey",fg=font_color(total_pl),font="Lato 12 bold",padx="5",pady="5",borderwidth=2,relief="groove")
    Total_cv.grid(row=coin_row,column=5,sticky=N+S+E+W)
    Total_ap=Label(pyc,text="$%.2f"%(total_amount_paid),bg="grey",fg=font_color(total_pl),font="Lato 12 bold",padx="5",pady="5",borderwidth=2,relief="groove")
    Total_ap.grid(row=coin_row,column=4,sticky=N+S+E+W) 
    Total_PL=Label(pyc,text="$%.2f"%(total_pl),bg="grey",fg=font_color(total_pl),font="Lato 12 bold",padx="5",pady="5",borderwidth=2,relief="groove")
    Total_PL.grid(row=coin_row,column=7,sticky=N+S+E+W)

    api=""
    refresh=Button(pyc,text="REFRESH",command=refresh1,bg="grey",fg="Blue",font="Lato 12 bold",padx="5",pady="5",borderwidth=2,relief="groove",state='disable')
    refresh.grid(row=coin_row+1,column=7,sticky=N+S+E+W,)
    global timer
    timer=threading.Timer(60,lambda btn=refresh:enable_refresh(btn))
    timer.start()


    # refresh.config(state='disable')
    # refresh.update()
    # time.sleep(10)
    # refresh.config(state = 'normal')
    # refresh.update()
# pyc.mainloop() #it basically holds our GUI
# print("After closing Window")

def app_head():
    PID=Label(pyc,text="ID",bg="yellow",fg="black",font="Lato 12 bold",padx="5",pady="5",borderwidth=2,relief="groove")
    PID.grid(row=0,column=0,sticky=N+S+E+W)
    name=Label(pyc,text="CoinName",bg="yellow",fg="black",font="Lato 12 bold",padx="5",pady="5",borderwidth=2,relief="groove")
    name.grid(row=0,column=1,sticky=N+S+E+W)


    price=Label(pyc,text="Price",bg="yellow",fg="black",font="Lato 12 bold",padx="5",pady="5",borderwidth=2,relief="groove")
    price.grid(row=0,column=2,sticky=N+S+E+W)

    no_coins=Label(pyc,text="coin Owned",bg="yellow",fg="black",font="Lato 12 bold",padx="5",pady="5",borderwidth=2,relief="groove")
    no_coins.grid(row=0,column=3,sticky=N+S+E+W)

    amount_paid=Label(pyc,text="Total Amount Paid",bg="yellow",fg="black",font="Lato 12 bold",padx="5",pady="5",borderwidth=2,relief="groove")
    amount_paid.grid(row=0,column=4,sticky=N+S+E+W)

    current_value=Label(pyc,text="Current_Value",bg="yellow",fg="black",font="Lato 12 bold",padx="5",pady="5",borderwidth=2,relief="groove")
    current_value.grid(row=0,column=5,sticky=N+S+E+W)

    pl_coin=Label(pyc,text="P/L Per Coin",bg="yellow",fg="black",font="Lato 12 bold",padx="5",pady="5",borderwidth=2,relief="groove")
    pl_coin.grid(row=0,column=6,sticky=N+S+E+W)

    Total_PL=Label(pyc,text="Total_P/L ",bg="yellow",fg="black",font="Lato 12 bold",padx="5",pady="5",borderwidth=2,relief="groove")
    Total_PL.grid(row=0,column=7,sticky=N+S+E+W)
    # name.pack()# not in ur control so better to use grid so as to do what we want



nav_itm()
app_head()    
myPortfolio()
def onclosing():
    timer.cancel()
    pyc.destroy()


pyc.protocol("WM_DELETE_WINDOW",onclosing)
pyc.mainloop()

cursorOb.close()
con.close()
import requests  # if not install by pip install requests
import json
#stores the data in api_request variable
api_request=requests.get("https://pro-api.coinmarketcap.com/v1/cryptocurrency/listings/latest?start=1&limit=5&convert=USD&CMC_PRO_API_KEY=66557877-3ca1-4aa0-802a-bbb9a1173d03")
#used json to get the parcable data
api=json.loads(api_request.content)#to deliver content of api req
# print(api)

# #Now I want to Fetch specific things only so:
# print(api["data"][0]["symbol"])
# print(api["data"][0]["quote"]["USD"]["price"])
# print(api["data"][1]["symbol"])
# # print(api["data"][1]["quote"]["USD"]["price"])
# print("{0:.2f}".format(api["data"][1]["quote"]["USD"]["price"]))#to print in 2 decimal points only


# #-------------------------------------now lets print in liio so that need not to write multiple lines
# for i in range(0,5):
#     print(api["data"][i]["symbol"])
#     print("{0:.2f}".format(api["data"][i]["quote"]["USD"]["price"]))
#     print("--------------------------------------------------------------------------------------------")


# #---------------------------------------------------now lets get info of those coins only whose info we need
# coins=["BTC","ETH","BCH"]
# for i in range(0,5):
#     for coin in coins:
#         if api["data"][i]["symbol"]==coin:
#          print(api["data"][i]["symbol"])
#          print("{0:.2f}".format(api["data"][i]["quote"]["USD"]["price"]))        #  print(".%2f"%api["data"][i]["quote"]["USD"]["price"])
#         print("--------------------------------------------------------------------------------------------")



#---------------------------------------------------now I want info like coin name ,price,num of coins etc so i need to make portfoio which is basically a dictionary
coins=[

    {
        "symbol":"BTC",
        "slug": "bitcoin",
        "num_market_pairs": 9195

    },
    {
        "symbol": "ETH",
        "slug": "ethereum",
        "num_market_pairs": 5310

    }
    
]
for i in range(0,5):
    for coin in coins:
        if api["data"][i]["symbol"]==coin["symbol"]:
         print(api["data"][i]["name"] + ", "+api["data"][i]["symbol"]+ " ,"+str(coin["num_market_pairs"]))
         #print(".%2f"%api["data"][i]["quote"]["USD"]["price"])
        print("*************")

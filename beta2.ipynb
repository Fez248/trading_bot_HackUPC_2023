from optibook.synchronous_client import Exchange
from math import trunc

import time
import logging
logger = logging.getLogger('client')
logger.setLevel('ERROR')

print("Setup was successful.")

FOSSIL = 'C1_FOSSIL_FUEL_ETF'
OIL = 'C1_OIL_CORP'
GAS = 'C1_GAS_INC'

GREEN = 'C2_GREEN_ENERGY_ETF'
WIND = 'C2_WIND_LTD'
SOLAR = 'C2_SOLAR_CO'

exchange = Exchange()
_ = exchange.connect()

instruments = exchange.get_instruments()
instruments

#Takes an ide either of the fossil market or the green market, calculates the estimated value of the basket and compares it to the real one
#then it trades based on that
def trade(ide):
    if ide == 'C1_FOSSIL_FUEL_ETF':
        tradeticks1 = exchange.get_trade_tick_history(ide)
        tradeticks2 = exchange.get_trade_tick_history(OIL)
        tradeticks3 = exchange.get_trade_tick_history(GAS)
        if (len(tradeticks1) > 0 and len(tradeticks2) > 0 and len(tradeticks3) > 0):
            expected_value = tradeticks2[-1].price * 0.5 + tradeticks3[-1].price * 0.5
            diff = tradeticks1[-1].price - expected_value
            if diff >= 0.01:
                make_trade(ide, diff, tradeticks1[-1].price)
                adjust_stocks(ide, tradeticks2[-1].price, tradeticks3[-1].price, diff)
        
        
    else:
        tradeticks1 = exchange.get_trade_tick_history(ide)
        tradeticks2 = exchange.get_trade_tick_history(WIND)
        tradeticks3 = exchange.get_trade_tick_history(SOLAR)
        if (len(tradeticks1) > 0 and len(tradeticks2) > 0 and len(tradeticks3) > 0):
            expected_value = tradeticks2[-1].price * 0.5 + tradeticks3[-1].price * 0.5
            diff = tradeticks1[-1].price - expected_value
            if diff >= 0.01:
                make_trade(ide, diff, tradeticks1[-1].price)
                adjust_stocks(ide, tradeticks2[-1].price, tradeticks3[-1].price, diff)

#it is supposed to check the margins of the limit 4 of the challence but I don't know why it keeps failing so I guess there is something I haven't been
#been able to fully understand.
def check_margins(ide):
    portofolio = exchange.get_positions_and_cash()
    tradeticks = exchange.get_trade_tick_history(ide)
    
    if ide == FOSSIL:
        tradeticks2 = exchange.get_trade_tick_history(OIL)
        tradeticks3 = exchange.get_trade_tick_history(GAS)
        return -50 <= tradeticks[-1].price * 0.5 + tradeticks2[-1].price <= 50 and -50 <= tradeticks[-1]-price * 0.5 + tradeticks3[-1].price <= 50
    else:
        tradeticks2 = exchange.get_trade_tick_history(WIND)
        tradeticks3 = exchange.get_trade_tick_history(SOLAR)
        return -50 <= tradeticks[-1].price * 0.5 + tradeticks2[-1].price <= 50 and -50 <= tradeticks[-1]-price * 0.5 + tradeticks3[-1].price <= 50

#this function comes with check_margins, it is supposed to correct this imbalances on my hedged position, selling or buying in order to be in between -50 and 50
def correct(ide, action):
    portofolio = exchange.get_positions_and_cash()
    
    if ide == FOSSIL:
        if portofolio[OIL]['volume'] > 0:
            exchange.insert_order(OIL, price = portofolio[OIL]['cash'], volume = portofolio[OIL]['volume'], side = action, order_type = 'ioc')
        if portofolio[GAS]['volume'] > 0:
            exchange.insert_order(GAS, price = portofolio[GAS]['cash'], volume = portofolio[GAS]['volume'], side = action, order_type = 'ioc')
        
    else:
        if portofolio[WIND]['volume'] > 0:
            exchange.insert_order(WIND, price = portofolio[WIND]['cash'], volume = portofolio[WIND]['volume'], side = action, order_type = 'ioc')
        if portofolio[SOLAR]['volume'] > 0:
            exchange.insert_order(SOLAR, price = portofolio[SOLAR]['cash'], volume = portofolio[SOLAR]['volume'], side = action, order_type = 'ioc')
        
    if check_margins(ide):
        correct(ide, ask)

#takes the id of one of the baskets, the difference between the real value and the estimated one, then it buys or sells depebding on the difference
#the volume is calculated using the function, (diff * 499) / 100, using trunc to delete the decimal part and adding 1 in case it is 0, this function
#to calculate the volume it's the result of a lot of tests and this is the one that performed the best
def make_trade(ide, diff, value):
    if diff >= 0:
        new_volume = (diff * 499) / 100        
        exchange.insert_order(ide, price = value, volume = trunc(new_volume) + 1, side = 'bid', order_type = 'limit')
        
        if not check_margins(ide):
            correct(ide, 'ask')
            
    else:
        new_volume = -(diff * 499) / 100
        exchange.insert_order(ide, price = value, volume = trunc(new_volume) + 1, side = 'ask', order_type = 'limit')
        
        if not check_margins(ide):
            correct(ide, 'ask')
#this function is called whenever we buy or sell a basket and it is supposed to also help with keeping the value between the margins, selling stocks
#if we buy the basket and viceversa, it works, but it keeps going out the limit
def adjust_stocks(ide, value1, value2, diff):
    if diff >= 0:
        new_volume = (diff * 500) / 100
        action = 'bid'
    else:
        new_volume = -(diff * 500) / 100
        action = 'ask'
        
    if ide == FOSSIL:
        exchange.insert_order(OIL, price = value1, volume = trunc(new_volume) + 1, side = action, order_type = 'limit')
        exchange.insert_order(GAS, price = value2, volume = trunc(new_volume) + 1, side = action, order_type = 'limit')
    else:
        exchange.insert_order(WIND, price = value1, volume = trunc(new_volume) + 1, side = action, order_type = 'limit')
        exchange.insert_order(SOLAR, price = value2, volume = trunc(new_volume) + 1, side = action, order_type = 'limit')
            
def main():
    time.sleep(0.5)
    while True:
        trade(GREEN)
        trade(FOSSIL)
        time.sleep(0.5)
        
main()

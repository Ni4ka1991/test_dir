#!/usr/bin/env python3


from boot import *
from models.OrderItem import *
from os import system
from services.TestDataService import *
from models.Money import *
from models.Product import *
from models.Currency import *
from ui.index import *



system ("clear")

oi = OrderItem( 12345, 4, 999 )

#oi2 = oirf.getOrderItem( 4, 999 )

print(oi)

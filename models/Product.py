from .Money import *



class Product:
    def __init__( self, _id, _name, _price ):
        self.setId( _id )
        self.setName( _name )        
        self.setPrice( _price )

    def setId( self, id ):
        if type( id ) != int:
            raise TypeError( "Id must be of type string" )
        self._id = id
 
    def getId( self ):
        return self._id

    def setName( self, name ):
        if type( name ) != str:
            raise TypeError( "Name must be of type string" )
        self._name = name

    def getName( self ):
        return self._name

    def setPrice( self, price ):
        if type( price ) != Money:
            raise TypeError( "Price must be of type Money!" )
            
        if price.amount < 0:
            raise ValueError("Product's price cannot be negative!")
        self._price = price

    def getPrice( self ):
        return self._price
       
    def __str__( self ):
        return f"\n " \
               f"Product ID: {self._id}\n " \
               f"Name:{self._name}\n" \
               f"Price:{self._price}\n"
                            
    def __repr__( self ):
        return str( self )

class ProductRepositoryFactory:
    def __init__(self):
        self._lastCreatedId = 0
        self._products=[]

    def getProduct( self, name, price):
        obj=Product( id, name, price )
        self._lastCreatedId += 1
        obj._id=self._lastCreatedId
        self.save(obj)
        return obj

    def save( self, product ):
        self._products.append( product )

    def saveAll(self,products):
        self._products = products

    def all(self):
        return tuple( self._products )

    def findById( self, id ):
        for p in self._products: 
            if p._id == id:
                return p

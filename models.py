# This is an auto-generated Django model module.
# You'll have to do the following manually to clean this up:
#   * Rearrange models' order
#   * Make sure each model has one field with primary_key=True
#   * Make sure each ForeignKey and OneToOneField has `on_delete` set to the desired behavior
#   * Remove `managed = False` lines if you wish to allow Django to create, modify, and delete the table
# Feel free to rename the models, but don't rename db_table values or field names.
from django.db import models


class Admin(models.Model):
    adminid = models.IntegerField(db_column='AdminID', primary_key=True)  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'Admin'


class Auction(models.Model):
    auctionid = models.AutoField(db_column='AuctionID', primary_key=True)  # Field name made lowercase.
    vin = models.ForeignKey('Car', models.DO_NOTHING, db_column='VIN')  # Field name made lowercase.
    status = models.CharField(db_column='Status', max_length=9)  # Field name made lowercase.
    startprice = models.DecimalField(db_column='StartPrice', max_digits=10, decimal_places=2)  # Field name made lowercase.
    highestprice = models.DecimalField(db_column='HighestPrice', max_digits=10, decimal_places=2, blank=True, null=True)  # Field name made lowercase.
    sellerid = models.ForeignKey('Seller', models.DO_NOTHING, db_column='SellerID')  # Field name made lowercase.
    buyerid = models.ForeignKey('Buyer', models.DO_NOTHING, db_column='BuyerID', blank=True, null=True)  # Field name made lowercase.
    startdate = models.DateTimeField(db_column='StartDate')  # Field name made lowercase.
    enddate = models.DateTimeField(db_column='EndDate', blank=True, null=True)  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'Auction'


class Bid(models.Model):
    bidid = models.AutoField(db_column='BidID', primary_key=True)  # Field name made lowercase.
    bidderid = models.ForeignKey('User', models.DO_NOTHING, db_column='BidderID')  # Field name made lowercase.
    auctionid = models.ForeignKey(Auction, models.DO_NOTHING, db_column='AuctionID')  # Field name made lowercase.
    amount = models.DecimalField(db_column='Amount', max_digits=10, decimal_places=2)  # Field name made lowercase.
    timestamps = models.DateTimeField(db_column='Timestamps')  # Field name made lowercase.
    iswin = models.IntegerField(db_column='IsWin')  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'Bid'


class Buyer(models.Model):
    buyerid = models.IntegerField(db_column='BuyerID', primary_key=True)  # Field name made lowercase.
    buycarnum = models.IntegerField(db_column='BuyCarNum', blank=True, null=True)  # Field name made lowercase.
    bidnum = models.CharField(db_column='BidNum', max_length=20, blank=True, null=True)  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'Buyer'


class Car(models.Model):
    vin = models.CharField(db_column='VIN', primary_key=True, max_length=17)  # Field name made lowercase.
    make = models.CharField(db_column='Make', max_length=50)  # Field name made lowercase.
    model = models.CharField(db_column='Model', max_length=50)  # Field name made lowercase.
    year = models.TextField(db_column='Year')  # Field name made lowercase. This field type is a guess.
    mileage = models.IntegerField(db_column='Mileage')  # Field name made lowercase.
    condition = models.CharField(db_column='Condition', max_length=19)  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'Car'


class Employee(models.Model):
    employee_id = models.IntegerField(blank=True, null=True)
    team_id = models.IntegerField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'Employee'


class Like(models.Model):
    buyerid = models.OneToOneField(Buyer, models.DO_NOTHING, db_column='BuyerID', primary_key=True)  # Field name made lowercase. The composite primary key (BuyerID, VIN) found, that is not supported. The first column is selected.
    vin = models.ForeignKey(Car, models.DO_NOTHING, db_column='VIN')  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'Like'
        unique_together = (('buyerid', 'vin'),)


class Order(models.Model):
    orderid = models.AutoField(db_column='OrderID', primary_key=True)  # Field name made lowercase.
    auctionid = models.ForeignKey(Auction, models.DO_NOTHING, db_column='AuctionID')  # Field name made lowercase.
    vin = models.ForeignKey(Car, models.DO_NOTHING, db_column='VIN')  # Field name made lowercase.
    status = models.CharField(db_column='Status', max_length=9)  # Field name made lowercase.
    amount = models.DecimalField(db_column='Amount', max_digits=10, decimal_places=2)  # Field name made lowercase.
    orderdate = models.DateTimeField(db_column='OrderDate')  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'Order'


class Payment(models.Model):
    paymentid = models.AutoField(db_column='PaymentID', primary_key=True)  # Field name made lowercase.
    method = models.CharField(db_column='Method', max_length=13)  # Field name made lowercase.
    amount = models.DecimalField(db_column='Amount', max_digits=10, decimal_places=2)  # Field name made lowercase.
    orderid = models.ForeignKey(Order, models.DO_NOTHING, db_column='OrderID')  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'Payment'


class Post(models.Model):
    vin = models.OneToOneField(Car, models.DO_NOTHING, db_column='VIN', primary_key=True)  # Field name made lowercase.
    sellerid = models.ForeignKey('Seller', models.DO_NOTHING, db_column='SellerID', blank=True, null=True)  # Field name made lowercase.
    startprice = models.DecimalField(db_column='StartPrice', max_digits=10, decimal_places=2)  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'Post'


class Report(models.Model):
    reporterid = models.OneToOneField('User', models.DO_NOTHING, db_column='reporterID', primary_key=True)  # Field name made lowercase. The composite primary key (reporterID, recipientID) found, that is not supported. The first column is selected.
    recipientid = models.ForeignKey('User', models.DO_NOTHING, db_column='recipientID', related_name='report_recipientid_set')  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'Report'
        unique_together = (('reporterid', 'recipientid'),)


class Review(models.Model):
    buyerid = models.OneToOneField(Buyer, models.DO_NOTHING, db_column='BuyerID', primary_key=True)  # Field name made lowercase. The composite primary key (BuyerID, OrderID) found, that is not supported. The first column is selected.
    orderid = models.ForeignKey(Order, models.DO_NOTHING, db_column='OrderID')  # Field name made lowercase.
    comment = models.CharField(db_column='Comment', max_length=255, blank=True, null=True)  # Field name made lowercase.
    rating = models.IntegerField(db_column='Rating', blank=True, null=True)  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'Review'
        unique_together = (('buyerid', 'orderid'),)


class Sales(models.Model):
    employee_id = models.IntegerField(blank=True, null=True)
    product_id = models.IntegerField(blank=True, null=True)
    sales = models.IntegerField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'Sales'


class Scores(models.Model):
    player_name = models.CharField(max_length=20, blank=True, null=True)
    gender = models.CharField(max_length=1, blank=True, null=True)
    day = models.DateField(blank=True, null=True)
    score_points = models.IntegerField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'Scores'


class Seller(models.Model):
    sellerid = models.IntegerField(db_column='SellerID', primary_key=True)  # Field name made lowercase.
    salecarnum = models.IntegerField(db_column='SaleCarNum', blank=True, null=True)  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'Seller'


class Shipment(models.Model):
    shipmentid = models.AutoField(db_column='ShipmentID', primary_key=True)  # Field name made lowercase.
    date = models.DateTimeField(db_column='Date')  # Field name made lowercase.
    status = models.CharField(db_column='Status', max_length=10)  # Field name made lowercase.
    cost = models.DecimalField(db_column='Cost', max_digits=10, decimal_places=2)  # Field name made lowercase.
    deliveryaddress = models.CharField(db_column='DeliveryAddress', max_length=255)  # Field name made lowercase.
    orderid = models.ForeignKey(Order, models.DO_NOTHING, db_column='OrderID')  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'Shipment'


class User(models.Model):
    userid = models.AutoField(db_column='UserID', primary_key=True)  # Field name made lowercase.
    firstname = models.CharField(db_column='FirstName', max_length=100)  # Field name made lowercase.
    lastname = models.CharField(db_column='LastName', max_length=100)  # Field name made lowercase.
    email = models.CharField(db_column='Email', unique=True, max_length=255)  # Field name made lowercase.
    phone = models.CharField(db_column='Phone', max_length=20, blank=True, null=True)  # Field name made lowercase.
    password = models.CharField(db_column='Password', max_length=255)  # Field name made lowercase.
    address = models.TextField(db_column='Address', blank=True, null=True)  # Field name made lowercase.
    usertype = models.CharField(db_column='UserType', max_length=6)  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'User'

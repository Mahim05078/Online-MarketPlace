from django.db import models


class Item(models.Model):
    item_id = models.IntegerField(primary_key=True)
    itemname = models.TextField(max_length=250, null=False, blank=False)
    itermtype = models.TextField(max_length=20, null=False, blank=False)

    def __str__(self):
        return self.itemname


class Shop(models.Model):
    shopid = models.IntegerField(primary_key=True)
    bookedStatus = models.IntegerField(null=False, blank=False)
    rentCost = models.FloatField(blank=False)

    def __str__(self):
        return self.shopid


class Customer(models.Model):
    cust_id = models.IntegerField(primary_key=True)
    cust_name = models.TextField(null=False, blank=False)
    cust_Adress = models.TextField(max_length=250, null=True, blank=True)
    cust_password = models.TextField(max_length=100, blank=False, null=False)
    cust_contact = models.TextField(max_length=15, null=False, blank=False)
    cust_email = models.TextField(max_length=100, blank=False, null=False)
    cust_creditno = models.TextField(max_length=20, blank=False, null=False)
    cust_dob = models.DateField()

    def __str__(self):
        return "%s %s" % (self.cust_name, self.cust_id)


class ShopItem(models.Model):
    item_id = models.ForeignKey(Item, on_delete=models.CASCADE)
    shop_id = models.ForeignKey(Shop, on_delete=models.CASCADE)
    itemamount = models.IntegerField(null=False, blank=False)
    itemprice = models.FloatField(null=False, blank=False)
    itembrand = models.CharField(max_length=20, null=False, blank=False)

    def __str__(self):
        return "%s %s" % (self.item_id, self.shop_id)


class Shopowner(models.Model):
    owner_id = models.IntegerField(primary_key=True)
    owner_name = models.TextField(null=False, blank=False)
    owner_Adress = models.TextField(max_length=250, null=True, blank=True)
    owner_password = models.TextField(max_length=100, blank=False, null=False)
    owner_contact = models.TextField(max_length=15, null=False, blank=False)
    owner_email = models.TextField(max_length=100, blank=True, null=True)
    owner_creditno = models.TextField(max_length=20, blank=False, null=False)
    owner_dob = models.TimeField()
    num_shop = models.IntegerField()
    owner_nid = models.TextField(max_length=100, blank=False, null=False)

    def __str__(self):
        return "%s %s" % (self.owner_name, self.owner_id)


class Shopassigned(models.Model):
    owner_id = models.ForeignKey(Shopowner, on_delete=models.CASCADE)
    shop_id = models.ForeignKey(Shop, on_delete=models.CASCADE)
    rent_Date = models.DateField(auto_now=True)
    expire_Date = models.DateField()
    remainPayment = models.FloatField(blank=False, null=False)

    def __str__(self):
        return "%s %s" % (self.owner_id, self.shop_id)



class RequestedRent(models.Model):
    NID = models.TextField(primary_key=True)
    shop_id = models.ForeignKey(Shop, on_delete=models.CASCADE)
    is_granted = models.IntegerField(blank=False,null=False)
    paid = models.IntegerField(blank=False,null=False)
    name = models.TextField(null=False, blank=False)
    email = models.TextField(null=False)
    mobile = models.TextField(null=False)
    address= models.TextField()

    def __str__(self):
        return "%s %s" % (self.name,self.shop_id)

























# class Employee(models.Model):
#     employee_id = models.IntegerField(primary_key=True)
#     name = models.TextField(max_length=50, null=False, blank= False)
#     address = models.TextField(max_length=250, null=False, blank= False)
#     mobileNo = models.TextField(max_length=250, null=False, blank= False)
#     emailId = models.EmailField(max_length=110, null=False, blank= False)
#     joiningDate = models.DateField(null=False, blank= False)
#     leavingDate = models.DateField(null=True, blank= True)
#     branch = models.ForeignKey(Branch, on_delete=models.CASCADE)

#     def __str__(self):
#         return self.name


# class Salesman(models.Model):
#     designation = "Salesman",
#     #branch_id = models.IntegerField(primary_key=True)
#     counterNo = models.IntegerField(null=False, blank= False)
#     employee = models.ForeignKey(Employee, on_delete=models.CASCADE,primary_key=True)

#     def __str__(self):
#         return "%s %s" % (self.designation, self.employee.name)


# class Backoffice(models.Model):
#     designation = models.TextField()
#     employee = models.ForeignKey(Employee, on_delete=models.CASCADE, primary_key=True)

#     def __str__(self):
#         return "%s %s" % (self.designation, self.employee.name)


# class Invoice(models.Model):
#     invoice_id = models.IntegerField(primary_key=True)
#     sellingTime = models.TimeField(auto_now_add=True)
#     employee = models.ForeignKey(Salesman, on_delete=models.CASCADE)

#     def __str__(self):
#         return "%s %s" % (self.sellingTime, self.employee)


# class Supply(models.Model):
#     supply_id = models.IntegerField(primary_key=True)
#     time = models.TimeField(auto_now_add=True)
#     brand = models.TextField(null=False, blank= False)
#     employee = models.ForeignKey(Backoffice, on_delete=models.CASCADE)

#     def __str__(self):
#         return "%s %s" % (self.time, self.brand)


# class Medicine(models.Model):
#     medicine_id = models.IntegerField(primary_key=True)
#     medicineName = models.TextField(null=False, blank= False)
#     #medicineTye = models.TextField(null=False, blank= False)
#     brand = models.TextField(null=False, blank= False)
#     amount = models.IntegerField(null=False, blank= False)
#     #description = models.TextField(null=False, blank= False)
#     medicineTye = models.ForeignKey(MedicineType, on_delete=models.CASCADE)

#     # def __str__(self):
#     #     return "%s %s %s" % (self.medicineName, self.medicineTye, self.brand)


# class MedicineInvoices(models.Model):
#     medicineinvoice_id = models.IntegerField(primary_key=True)
#     noOfUnit = models.IntegerField(null=False, blank= False)
#     invoice = models.ForeignKey(Invoice, on_delete=models.CASCADE)
#     medicine = models.ForeignKey(Medicine, on_delete=models.CASCADE)

#     def __str__(self):
#         return "%s %s %s" % (self.medicine, self.noOfUnit, self.invoice)


# class Price(models.Model):
#     price = models.FloatField(null=False, blank= False)
#     setOn = models.TimeField(primary_key=True,auto_now_add=True)
#     changedOn = models.TimeField(auto_now_add=True)
#     medicine = models.ForeignKey(Medicine, on_delete=models.CASCADE)

# class MedicineBatch(models.Model):
#     medicinebatch_id = models.IntegerField(primary_key=True)
#     supply = models.ForeignKey(Supply, on_delete=models.CASCADE)
#     medicine = models.ForeignKey(Medicine, on_delete=models.CASCADE)
#     dateOfManufacture = models.TimeField(null=False, blank= False)
#     dateOfExpire = models.TimeField(null=False, blank= False)
#     noOfUnit = models.IntegerField(null=False, blank= False)
#     buyingPrice = models.FloatField(null=False, blank= False)

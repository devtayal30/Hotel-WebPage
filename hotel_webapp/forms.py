from django import forms

class login(forms.Form):
    Staff_Name= forms.CharField
    Staff_Address=forms.CharField
    Staff_Pancard=forms.CharField
    Staff_Aadhaar= forms.CharField
    Staff_phoneno= forms.CharField

class onlinebooking(forms.Form):
    customer_name= forms.CharField
    Customer_Address=forms.CharField
    Customer_Pancard=forms.CharField
    Cutomer_Aadhaar_No= forms.CharField
    Customer_Phone_No= forms.CharField
    Deluxe_Room= forms.IntegerField
    Luxury_Room= forms.IntegerField
    Premier_Room= forms.IntegerField
    Premier_Plus_Room= forms.IntegerField
    The_Oberoi_Suites= forms.IntegerField
    Deluxe_Suites= forms.IntegerField
    Luxury_Suites= forms.IntegerField
    Kohinoor_Suites= forms.IntegerField
    AC_Room= forms.IntegerField
    Non_AC_Room= forms.IntegerField

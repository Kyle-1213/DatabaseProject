import random

from django.db import transaction
from django.core.management.base import BaseCommand

from forum.modeles import Customers, CustomerWishList, WishListPhone, WishListTV, Vender, Products, Service, InternetServices, PhoneServices, Phones, TVs
from forum.factories import (
        CustomersFactory,
        CustomerWishListFactory,
        WishListPhoneFactory,
        WishListTVFactory,
        VenderFactory,
        ProductsFactory,
        ServiceFactory,
        InternetServicesFactory,
        PhoneServicesFactory,
        PhonesFactory,
        TVsFactory
)

NUM_CUSTOMERS = 50
NUM_CUSTOMERS_WISH_LIST = 50
NUM_WISH_LIST_PHONE = 50
NUM_WISH_LIST_TV = 50
NUM_VENDER = 50
NUM_PRODUCTS = 50
NUM_SERVICE = 50
NUM_INTERNET_SERVICES = 50
NUM_PHONE_SERVICES = 50
NUM_PHONES = 50
NUM_TVS = 50

class Command(BaseCommand):
    help = "generates test data"

    @transaction.atomic
    def handle(self, *args, **kwargs):
        self.stdout.write("deleting old data...")
        models = [Customers, CustomerWishList, WishListPhone, WishListTV, Vender, Products, Service, InternetServices, PhoneServices, Phones, TVs]
        for m in models:
            m.objects.all().delete()

        self.stdout.write("Creating new data...")

        customers = []
        customerWishList = []
        wishListPhone = []
        wishListTV = []
        vender = []
        products = []
        service = []
        internetServices = []
        phoneServices = []
        phones = []
        tvs = []

        for _ in range(NUM_CUSTOMERS):
            person = CustomersFactory()
            customers.append(person)
        for _ in range(NUM_CUSTOMERS_WISH_LIST):
            person = CustomerWishListFactory()
            customerWishList.append(person)
        for _ in range(NUM_WISH_LIST_PHONE):
            person = WishListPhoneFactory()
            wishListPhone.append(person)
        for _ in range(NUM_WISH_LIST_TV):
            person = WishListTVFactory()
            wishListTV.append(person)
        for _ in range(NUM_VENDER):
            person = VenderFactory()
            vender.append(person)
        for _ in range(NUM_PRODUCTS):
            person = ProductsFactory()
            products.append(person)
        for _ in range(NUM_SERVICE):
            person = ServiceFactory()
            service.append(person)
        for _ in range(NUM_INTERNET_SERVICES):
            person = InternetServicesFactory()
            internetServices.append(person)
        for _ in range(NUM_PHONE_SERVICES):
            person = PhoneServicesFactory()
            phoneServices.append(person)
        for _ in range(NUM_PHONES):
            person = PhonesFactory()
            phones.append(person)
        for _ in range(NUM_TVS):
            person = TVsFactory()
            tvs.append(person)
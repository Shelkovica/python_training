import pytest
from model.contact import Contact
import random
import string


testdata = [
    Contact(firstname="firstname1", lastname="lastname1", address="address1",
            homephone="homephone1", mobilephone="mobilephone1", workphone="workphone1", email="email1", email2="email2", email3="email3",
            secondaryphone="secondaryphone1"),
    Contact(firstname="firstname2", lastname="lastname2", address="address2",
            homephone="homephone2", mobilephone="mobilephone2", workphone="workphone2", email="email21", email2="email22", email3="email23",
            secondaryphone="secondaryphone2")
]


#def random_string(prefix, maxlen):
 #   symbols = string.ascii_letters+string.digits
 #   return prefix + "".join([random.choice(symbols) for i in range(random.randrange(maxlen))])

#def random_email(maxlen):
 #   symbols = string.ascii_letters + string.digits
  #  email_address = "".join([random.choice(symbols) for i in range(random.randrange(maxlen))])
   # email_domain = "".join([random.choice(symbols) for i in range(random.randrange(maxlen))])
   # return email_address+"@"+email_domain+"."+"".join([random.choice(symbols) for i in range(random.randrange(maxlen))])


#testdata =  [Contact(firstname="", lastname="", address="",
#            homephone="", mobilephone="", workphone="", email="", email2="", email3="", secondaryphone="")]+ [
#    Contact(firstname=random_string("first",10), lastname=random_string("las",10),
#            address=random_string("addr",10), homephone=random_string("",10), mobilephone=random_string("",10),
#            workphone=random_string("",10), secondaryphone=random_string("",10), email=random_email(5), email2=random_email(6),
#            email3=random_email(5))
#for i in range (10)
#]
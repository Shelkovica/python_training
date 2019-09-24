import pytest
from model.contact import Contact
import random
import string
import os.path
import json
import getopt
import sys


try:
    opts, args = getopt.getopt(sys.argv[1:], "n:f:", ["number of contacts", "file"])
except getopt.GetoptError as err:
    getopt.usage()
    sys.exit(2)

n=5
f="data/contact.json"

for o, a in opts:
    if o == "-n":
        n=int(a)
    elif o == "-f":
        f = a


def random_string(prefix, maxlen):
    symbols = string.ascii_letters+string.digits
    return prefix + "".join([random.choice(symbols) for i in range(random.randrange(maxlen))])

def random_email(maxlen):
    symbols = string.ascii_letters + string.digits
    email_address = "".join([random.choice(symbols) for i in range(random.randrange(maxlen))])
    email_domain = "".join([random.choice(symbols) for i in range(random.randrange(maxlen))])
    return email_address+"@"+email_domain+"."+"".join([random.choice(symbols) for i in range(random.randrange(maxlen))])


testdata =  [Contact(firstname="", lastname="", address="",
            homephone="", mobilephone="", workphone="", email="", email2="", email3="", secondaryphone="")]+ [
    Contact(firstname=random_string("first",10), lastname=random_string("las",10),
            address=random_string("addr",10), homephone=random_string("",10), mobilephone=random_string("",10),
            workphone=random_string("",10), secondaryphone=random_string("",10), email=random_email(5), email2=random_email(6),
            email3=random_email(5))
for i in range (n)
]

file = os.path.join(os.path.dirname(os.path.abspath(__file__)), "..", f)

with open(file, "w") as f:
    f.write(json.dumps(testdata, default=lambda x: x.__dict__, indent=2))
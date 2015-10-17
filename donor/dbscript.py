import models

def populate_db():
    s1 = Store.object.create(name="Pathmark",address="123 25th Street",state="NY",zip="11111")
    s2 = Store.object.create(name="Walmart",address="234 56th Street",state="NY",zip="10000")
    s3 = Store.object.create(name="Costco",address="345 67th Street",state="NY",zip="11100")

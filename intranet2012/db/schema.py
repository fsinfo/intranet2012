from sqlalchemy import *

schema = MetaData()

addressbook = Table('addressbook', schema,
                    Column('address_id', Integer, primary_key = True),
                    Column('ldap_username', String(32), nullable = True),
                    Column('firstname', String(32), nullable = True),
                    Column('lastname', String(32), nullable = True),
                    Column('nickname', String(32), nullable = True),
                    Column('organization', String(32), nullable = True),
                    Column('street', String(64), nullable = True),
                    Column('zip', String(32), nullable = True),
                    Column('city', String(32), nullable = True),
                    Column('email', String(128), nullable = True),
                    Column('phone', String(32), nullable = True),
                    Column('birthday', Date(), nullable = True),
                    Column('comment', String(1000), nullable = True))


addressbook_additional_fields = Table('addressbook_additional_fields', schema,
                                      Column('id', Integer, primary_key = True),
                                      Column('address_id', Integer, ForeignKey('addressbook.address_id'), nullable = False),
                                      Column('type', String(32), nullable = False, index = True),
                                      Column('value', String(128), nullable = False))

addressbook_tags = Table('addressbook_tags', schema,
                         Column('tag_id', Integer, primary_key = True),
                         Column('tagname', String(64), nullable = False));

addressbook_tag_relation = Table('addressbook_tag_relation', schema,
                                 Column('address_id', Integer, ForeignKey('addressbook.address_id'), nullable = False),
                                 Column('tag_id', Integer, ForeignKey('addressbook_tags.tag_id'), nullable = False))

beverage_category = Table('beverage_category', schema,
                          Column('category_id', Integer, primary_key = True),
                          Column('name', String(32)))

beverage_item = Table('beverage_item', schema,
                      Column('item_id', Integer, primary_key = True),
                      Column('category_id', Integer, ForeignKey('beverage_category.category_id'), nullable = True))
                      Column('name', String(32), nullable = False),
                      Column('unit', String(32), nullable = True)) # Amount of said beverage to be sold per price… … penis

beverage_prices_list = Table('beverage_prices_list', schema,
                             Column('list_id', Integer, primary_key = True),
                             Column('from', Date(), nullable = False),
                             Column('to', Date(), nullable = False))

beverage_prices_item = Table('beverage_prices_item', schema,
                             Column('item_id', Integer, ForeignKey('beverage_item.item_id'), nullable = False),
                             Column('list_id', Integer, ForeignKey('beverage_prices_list.list_id'), nullable = False),
                             Column('internal_price', Decimal(6, 2), nullable=False),
                             Column('external_price', Decimal(6, 2), nullable=False))

beverage_tap = Table('beverage_tap', schema,
                     Column('tap_id', Integer, primary_key = True),
                     Column('list_id', Integer, ForeignKey('beverage_prices_list.list_id'), nullable = False),
                     Column('from', Date(), nullable = False),
                     Column('to', Date(), nullable = False))

beverage_customer = Table('beverage_customer', schema,
                          Column('customer_id', Integer, primary_key = True),
                          Column('ldap_username', String(32)))

beverage_customer_taps = Table('beverage_customer_taps', schema,
                               Column('customer_id', Integer, ForeignKey('beverage_customer.customer_id'), nullable = False),
                               Column('tap_id', Integer, ForeignKey('beverage_tap.tap_id'), nullable = False))




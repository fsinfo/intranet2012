from sqlalchemy import *

schema = MetaData()

addressbook = Table('addressbook', schema,
                    Column('address_id', Integer, primary_key = True),
                    Column('username', String(16), nullable = True),
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



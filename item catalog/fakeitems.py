from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker

from sqlalchemy_utils import database_exists, drop_database, create_database

from database_setup import Category, CategoryItem, User, Base

engine = create_engine('sqlite:///itemcatalog.db')

# Clear database
Base.metadata.drop_all(engine)
Base.metadata.create_all(engine)

# Bind the engine to the metadata of the Base class so that the
# declaratives can be accessed through a DBSession instance
Base.metadata.bind = engine

DBSession = sessionmaker(bind=engine)
# A DBSession() instance establishes all conversations with the database
# and represents a "staging zone" for all the objects loaded into the
# database session object. Any change made against the objects in the
# session won't be persisted into the database until you call
# session.commit(). If you're not happy about the changes, you can
# revert all of them back to the last commit by calling
# session.rollback()
session = DBSession()

# Create dummy user
user1 = User(name="pavan", email="16pa1a0563@vishnu.edu.in")
session.add(user1)
session.commit()

# Items for Strings
category1 = Category(name="horror", user_id=1)

session.add(category1)
session.commit()

item1 = CategoryItem(name="muni", user_id=1, description="cast:lawrence",
                     category=category1)

session.add(item1)
session.commit()

item2 = CategoryItem(name="ganga", user_id=1, description="cast:lawrence",
                     category=category1)

session.add(item2)
session.commit()

item3 = CategoryItem(name="shivalinga", user_id=1, description="cast:lawrence",
                     category=category1)

session.add(item3)
session.commit()

# Items for Woodwinds
category2 = Category(name="comedy", user_id=1)

session.add(category2)
session.commit()

item1 = CategoryItem(name="sudigadu", user_id=1,
                     description="cast:allarinaresh", category=category2)

session.add(item1)
session.commit()

item2 = CategoryItem(name="loukyam", user_id=1,
                     description="cast:gopichand", category=category2)

session.add(item2)
session.commit()

item3 = CategoryItem(name="marakathamani", user_id=1,
                     description="cast:aadhi", category=category2)

session.add(item3)
session.commit()

# Items for Percussion
category3 = Category(name="emotional", user_id=1)

session.add(category3)
session.commit()

item1 = CategoryItem(name="jailakusha", user_id=1,
                     description="cast:NTR", category=category3)

session.add(item1)
session.commit()

item2 = CategoryItem(name="nani", user_id=1,
                     description="cast:maheshbabu", category=category3)

session.add(item2)
session.commit()

item3 = CategoryItem(name="amacheppindhi", user_id=1,
                     description="cast:madhavan", category=category3)

session.add(item3)
session.commit()

# Items for Brass
category4 = Category(name="fighter emotional", user_id=1)

session.add(category4)
session.commit()


categories = session.query(Category).all()
for category in categories:
    print "Category: " + category.name

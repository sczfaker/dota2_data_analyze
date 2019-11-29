from sqlalchemy import create_engine
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy import Table, Column, Integer, Numeric, String
from sqlalchemy.orm import sessionmaker 
Base = declarative_base()

engine4 = create_engine('sqlite:///C:\\1cl\\cookies.db')

class Cookie(Base):
    __tablename__ = 'cookies'
    cookie_id = Column(Integer(), primary_key=True)
    cookie_name = Column(String(50), index=True)
    cookie_recipe_url = Column(String(255))
    cookie_sku = Column(String(55))
    quantity = Column(Integer())
    #unit_cost = Column(Numeric(12, 2))
    # def __repr__(self):
    #     return "<User(name='%s', fullname='%s', password='%s')>" % (
    #                self.cookie_id, self.cookie_name, self.cookie_recipe_url,self.cookie_sku,self.quantity)


if __name__ == '__main__':
    print(Cookie.__table__)
    Base.metadata.create_all(engine4) 
    Session = sessionmaker(bind=engine4)
    session_current=Session()
    first_Cookie=Cookie(cookie_id=112,cookie_name="苏诚招",cookie_recipe_url="scz.com",cookie_sku="djakhjq",quantity=14321)

    session_current.add(first_Cookie)
    session_current.commit()
# t=session_current.query(Cookie).all()#


#print (dir(engine4))
#print (dir(engine4))

#engine4.connect()
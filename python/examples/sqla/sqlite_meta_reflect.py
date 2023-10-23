from sqlalchemy import create_engine
import os
#from sqlalchemy import inspect
from sqlalchemy.engine import reflection

dbname = 'test.db'
if not os.path.exists(dbname):
    exit(f"Database file '{dbname}' could not be found")

engine = create_engine('sqlite:///test.db')
# inspector = inspect(engine)
# print(inspector)
# print(inspector.get_columns('address'))
# print(inspector.get_foreign_keys('address'))

insp = reflection.Inspector.from_engine(engine)
print(insp.get_table_names())

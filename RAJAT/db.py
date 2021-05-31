import sqlalchemy
from sqlalchemy import create_engine
DB_URL="mysql://root:root@localhost:3306/sqldb"
ENGINE=create_engine(DB_URL)
con=ENGINE.connect()
print(conn)

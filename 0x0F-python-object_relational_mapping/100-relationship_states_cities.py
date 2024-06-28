# 100-relationship_states_cities.py

import sys
from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker
from relationship_state import Base, State
from relationship_city import City

if __name__ == "__main__":
    # Get MySQL credentials and database name from command line arguments
    mysql_username = sys.argv[1]
    mysql_password = sys.argv[2]
    database_name = sys.argv[3]

    # Create the engine to connect to the MySQL server
    engine = create_engine(f'mysql+mysqldb://{mysql_username}:{mysql_password}@localhost/{database_name}', pool_pre_ping=True)

    # Bind the engine to the Base class (which includes both State and City)
    Base.metadata.create_all(engine)

    # Create a configured "Session" class
    Session = sessionmaker(bind=engine)

    # Create a session
    session = Session()

    # Create a new State object
    california = State(name="California")

    # Create a new City object
    san_francisco = City(name="San Francisco", state=california)

    # Add both objects to the session
    session.add(california)
    session.add(san_francisco)

    # Commit the transaction
    session.commit()

    # Print the id of the new State object
    print(california.id)

    # Close the session
    session.close()

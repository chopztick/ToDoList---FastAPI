from sqlmodel import SQLModel, create_engine
import os

# Get path to file, create path to the database
BASE_DIR = os.path.dirname(os.path.realpath(__file__))
db_path = 'sqlite:///' + os.path.join(BASE_DIR, 'tasks.db')
# To avoid issues with FastApi sessions
connect_args = {"check_same_thread": False}
# Create the engine
engine = create_engine(db_path, echo=True, connect_args=connect_args)


def create_db_and_tables():
    SQLModel.metadata.create_all(engine)


if __name__ == "__main__":
    create_db_and_tables()

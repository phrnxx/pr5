from sqlalchemy import create_engine, text
from datetime import datetime
import random
from db_config import get_database_url

def connect_db():
    return create_engine(get_database_url())

def generate_test_data(n):
    return [
        {
            'name': f'User{random.randint(1, 1000000)}',
            'email': f'user{random.randint(1, 1000000)}@example.com',
            'created_at': datetime.now()
        }
        for i in range(n)
    ]

def populate_db(size):
    engine = connect_db()
    data = generate_test_data(size)
    
    with engine.connect() as conn:
        for record in data:
            conn.execute(
                text("INSERT INTO users (name, email, created_at) VALUES (:name, :email, :created_at)"),
                record
            )
        conn.commit()

if __name__ == "__main__":
    sizes = [1000, 10000, 100000, 1000000]
    for size in sizes:
        print(f"Populating database with {size} records...")
        populate_db(size)
        print(f"Completed {size} records")

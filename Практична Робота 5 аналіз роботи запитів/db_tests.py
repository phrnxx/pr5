import psycopg2
import time
from db_config import db_config
from db_populate import insert_data

def connect_db():
    conn = psycopg2.connect(**db_config)
    return conn

def test_select(num_records):
    conn = connect_db()
    cursor = conn.cursor()
    
    start_time = time.time()
    cursor.execute("SELECT * FROM your_table LIMIT %s", (num_records,))
    rows = cursor.fetchall()
    end_time = time.time()
    
    cursor.close()
    conn.close()
    
    print(f"Select for {num_records} records took {end_time - start_time:.5f} seconds")

def test_update(num_records):
    conn = connect_db()
    cursor = conn.cursor()
    
    start_time = time.time()
    cursor.execute("UPDATE your_table SET age = age + 1 LIMIT %s", (num_records,))
    conn.commit()
    end_time = time.time()
    
    cursor.close()
    conn.close()
    
    print(f"Update for {num_records} records took {end_time - start_time:.5f} seconds")

def test_insert(num_records):
    start_time = time.time()
    insert_data(num_records)
    end_time = time.time()
    
    print(f"Insert for {num_records} records took {end_time - start_time:.5f} seconds")

def test_delete(num_records):
    conn = connect_db()
    cursor = conn.cursor()
    
    start_time = time.time()
    cursor.execute("DELETE FROM your_table WHERE age > 30 LIMIT %s", (num_records,))
    conn.commit()
    end_time = time.time()
    
    cursor.close()
    conn.close()
    
    print(f"Delete for {num_records} records took {end_time - start_time:.5f} seconds")

test_select(1000)
test_update(1000)
test_insert(1000)
test_delete(1000)

test_select(10000)
test_update(10000)
test_insert(10000)
test_delete(10000)

test_select(100000)
test_update(100000)
test_insert(100000)
test_delete(100000)

test_select(1000000)
test_update(1000000)
test_insert(1000000)
test_delete(1000000)

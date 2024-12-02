import time
from sqlalchemy import create_engine, text
import pandas as pd
from db_config import get_database_url

def benchmark_operation(engine, operation_func, data_size):
    start_time = time.time()
    operation_func(engine, data_size)
    end_time = time.time()
    return end_time - start_time

def benchmark_select(engine, size):
    with engine.connect() as conn:
        conn.execute(text("SELECT * FROM users LIMIT :size"), {"size": size})

def benchmark_update(engine, size):
    with engine.connect() as conn:
        conn.execute(
            text("UPDATE users SET name = name || '_updated' WHERE id IN (SELECT id FROM users LIMIT :size)"),
            {"size": size}
        )
        conn.commit()

def benchmark_delete(engine, size):
    with engine.connect() as conn:
        conn.execute(
            text("DELETE FROM users WHERE id IN (SELECT id FROM users LIMIT :size)"),
            {"size": size}
        )
        conn.commit()

def run_benchmarks():
    engine = create_engine(get_database_url())
    data_sizes = [1000, 10000, 100000, 1000000]
    results = []

    for size in data_sizes:
        print(f"\nBenchmarking {size} records...")
        
        select_time = benchmark_operation(engine, benchmark_select, size)
        update_time = benchmark_operation(engine, benchmark_update, size)
        delete_time = benchmark_operation(engine, benchmark_delete, size)
        
        results.append({
            'Data Size': size,
            'Select (s)': round(select_time, 4),
            'Update (s)': round(update_time, 4),
            'Delete (s)': round(delete_time, 4)
        })

    df = pd.DataFrame(results)
    print("\nBenchmark Results (seconds):")
    print(df.to_string(index=False))
    
    df.to_csv('benchmark_results.csv', index=False)
    with open('comparison_table.md', 'w') as f:
        f.write("# Порівняльна таблиця результатів\n\n")
        f.write(df.to_markdown(index=False))

if __name__ == "__main__":
    run_benchmarks()

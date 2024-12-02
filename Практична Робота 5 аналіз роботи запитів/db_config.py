db_config = {
    'host': 'your_db_host',
    'port': 'your_db_port',
    'dbname': 'your_db_name',
    'user': 'your_db_user',
    'password': 'your_db_password'
}

def get_database_url():
    return f"postgresql://{db_config['user']}:{db_config['password']}@{db_config['host']}:{db_config['port']}/{db_config['dbname']}"

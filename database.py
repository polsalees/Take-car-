import sqlite3

def create_connection():
    """Create a connection to the SQLite database."""
    conn = sqlite3.connect('car_tracker.db')
    return conn

def create_tables():
    """Create the necessary tables for the car tracking application."""
    conn = create_connection()
    cursor = conn.cursor()

    # Create the 'cars' table
    cursor.execute('''
        CREATE TABLE IF NOT EXISTS cars (
            id INTEGER PRIMARY KEY AUTOINCREMENT,
            model TEXT,
            year INTEGER,
            vin TEXT
        );
    ''')

    # Create the 'expenses' table
    cursor.execute('''
        CREATE TABLE IF NOT EXISTS expenses (
            id INTEGER PRIMARY KEY AUTOINCREMENT,
            car_id INTEGER,
            date TEXT,
            category TEXT,  -- e.g., Fuel, Insurance, Misc
            amount REAL,
            description TEXT,
            FOREIGN KEY(car_id) REFERENCES cars(id)
        );
    ''')

    # Create the 'maintenance' table
    cursor.execute('''
        CREATE TABLE IF NOT EXISTS maintenance (
            id INTEGER PRIMARY KEY AUTOINCREMENT,
            car_id INTEGER,
            date TEXT,
            service TEXT,  -- e.g., Oil Change, Tire Rotation
            mileage INTEGER,  -- Mileage at the time of maintenance
            cost REAL,
            description TEXT,
            FOREIGN KEY(car_id) REFERENCES cars(id)
        );
    ''')

    # Create the 'mileage_log' table
    cursor.execute('''
        CREATE TABLE IF NOT EXISTS mileage_log (
            id INTEGER PRIMARY KEY AUTOINCREMENT,
            car_id INTEGER,
            date TEXT,
            mileage INTEGER,  -- Odometer reading
            FOREIGN KEY(car_id) REFERENCES cars(id)
        );
    ''')

    # Create the 'fuel_log' table
    cursor.execute('''
        CREATE TABLE IF NOT EXISTS fuel_log (
            id INTEGER PRIMARY KEY AUTOINCREMENT,
            car_id INTEGER,
            date TEXT,
            mileage INTEGER,  -- Odometer reading at the time of fill-up
            liters REAL,  -- Amount of fuel filled
            price_per_liter REAL,
            total_cost REAL,
            FOREIGN KEY(car_id) REFERENCES cars(id)
        );
    ''')

    # Commit the changes and close the connection
    conn.commit()
    conn.close()

# Initialize the database and create tables
if __name__ == '__main__':
    create_tables()

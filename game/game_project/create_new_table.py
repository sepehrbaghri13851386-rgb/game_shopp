import psycopg2
import time

url = "postgresql://game_ahopp_ab_user:d03Vl0MfHqEKNiCmXggmDJe7NlbdmIqG@dpg-d9h202naqgkc73dm2n50-a.oregon-postgres.render.com/game_ahopp_ab"

for attempt in range(5):
    try:
        conn = psycopg2.connect(url, connect_timeout=15)
        cur = conn.cursor()
        cur.execute("""
            CREATE TABLE IF NOT EXISTS game_shop_products (
                id BIGSERIAL PRIMARY KEY,
                title VARCHAR(50) NOT NULL,
                image VARCHAR(100) NOT NULL,
                gheymat NUMERIC(12,0) NOT NULL,
                category VARCHAR(20) NOT NULL DEFAULT 'action'
            );
        """)
        conn.commit()
        cur.execute("SELECT column_name FROM information_schema.columns WHERE table_name = 'game_shop_products';")
        print("game_shop_products COLUMNS:", [row[0] for row in cur.fetchall()])
        conn.close()
        break
    except Exception as e:
        print(f"Attempt {attempt+1} failed: {e}")
        time.sleep(3)
import sqlite3

def init_db():
    conn = sqlite3.connect('market_analysis.db')
    c = conn.cursor()
    c.execute('''CREATE TABLE IF NOT EXISTS reports
                 (query text, date text, sentiment text)''')
    conn.commit()
    conn.close()

if __name__ == "__main__":
    init_db()

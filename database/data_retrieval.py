import sqlite3

def save_report(query, sentiment):
    conn = sqlite3.connect('market_analysis.db')
    c = conn.cursor()
    c.execute("INSERT INTO reports VALUES (?, datetime('now'), ?)", 
              (query, str(sentiment)))
    conn.commit()
    conn.close()

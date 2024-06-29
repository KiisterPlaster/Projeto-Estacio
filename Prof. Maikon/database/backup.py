from app import db
import os

def backup_db():
    backup_file = 'backup/backup.sql'
    with open(backup_file, 'w') as f:
        for line in db.engine.execute('SELECT * FROM message'):
            f.write(f"{line}\n")
    print("Backup created successfully")

if __name__ == "__main__":
    backup_db()

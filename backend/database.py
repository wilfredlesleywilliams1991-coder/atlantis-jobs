import sqlite3
DB = "backend.db"

def init_db():
    conn = sqlite3.connect(DB)
    c = conn.cursor()
    c.execute("""CREATE TABLE IF NOT EXISTS jobs (
                    id INTEGER PRIMARY KEY,
                    title TEXT,
                    description TEXT,
                    location TEXT,
                    active INTEGER
                )""")
    c.execute("""CREATE TABLE IF NOT EXISTS applications (
                    id INTEGER PRIMARY KEY,
                    name TEXT,
                    skills TEXT,
                    job_id INTEGER,
                    phone TEXT
                )""")
    conn.commit()
    preload_jobs_and_applicants()
    conn.close()

def preload_jobs_and_applicants():
    conn = sqlite3.connect(DB)
    c = conn.cursor()
    unskilled_jobs = [
        ("General Labour", ["hardworking","willing to learn"]),
        ("Cleaner", ["cleaning","attention to detail"]),
        ("Store Assistant", ["organization","teamwork"]),
        ("Packager", ["packing","timely"])
    ]
    for i, (title, skills) in enumerate(unskilled_jobs, start=1):
        c.execute("INSERT OR IGNORE INTO jobs (id,title,description,location,active) VALUES (?,?,?,?,1)",
                  (i,title,"Unskilled position for school leavers","Atlantis"))
        c.execute("INSERT OR IGNORE INTO applications (id,name,skills,job_id,phone) VALUES (?,?,?,?,?)",
                  (i,f"School Leaver {i}","%s"%(",".join(skills)),i,f"+2782123456{i}"))
    # Add Willy G
    c.execute("INSERT OR IGNORE INTO applications (id,name,skills,job_id,phone) VALUES (99,'WILLY G','forklift,driver',1,'+27821234567')")
    conn.commit()
    conn.close()

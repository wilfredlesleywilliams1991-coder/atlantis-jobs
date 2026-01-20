import schedule
import time
from backend.ai.matcher import match_applicant
from backend.ai.whatsapp_agent import send_job_alert
from backend.database import DB
from backend.marketing.autoposter import auto_post
import sqlite3

def run_scheduler():
    schedule.every(5).minutes.do(process_jobs)
    schedule.every(30).minutes.do(auto_post)
    while True:
        schedule.run_pending()
        time.sleep(1)

def process_jobs():
    conn = sqlite3.connect(DB)
    c = conn.cursor()
    c.execute("SELECT id, skills, phone, job_id FROM applications")
    applicants = c.fetchall()
    for app_id, skills, phone, job_id in applicants:
        c.execute("SELECT title, description FROM jobs WHERE id=?", (job_id,))
        job = c.fetchone()
        score = match_applicant(skills.split(","), ["hardworking","willing to learn"]) # Example for unskilled
        send_job_alert(phone, job[0], score)
    conn.close()

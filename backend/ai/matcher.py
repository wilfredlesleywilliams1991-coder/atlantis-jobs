def match_applicant(cv_skills, job_skills):
    cv_set = set([s.lower().strip() for s in cv_skills])
    job_set = set([s.lower().strip() for s in job_skills])
    return int(len(cv_set & job_set)/len(job_set)*100)

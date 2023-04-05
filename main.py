from flask import Flask, render_template, jsonify, request
from flask_hcaptcha import hCaptcha
from database import load_jobs_from_db, load_job_from_db, add_application_to_db

app = Flask(__name__)
hcaptcha = hCaptcha(app)

HCAPTCHA_ENABLED = True
HCAPTCHA_SITE_KEY = "b6ef0162-6942-4d72-84c1-27f9334db145"
HCAPTCHA_SECRET_KEY = "0x60D73F90a9B9a9D0F8075051F3eF8Ec70FAd9a84"

#Create a route
@app.route("/")
def hello_world():
  jobs = load_jobs_from_db()
  return render_template("home.html",
                        jobs=jobs,
                        company_name='Jovian')

@app.route("/api/jobs")
def list_jobs():
  jobs = load_jobs_from_db()
  return jsonify(jobs)

@app.route("/job/<id>")
def show_job(id):
  job = load_job_from_db(id)
  if not job:
    return "Not Found", 404
  else:
    return render_template("jobpage.html", job=job)

@app.route('/api/job/<id>')
def show_job_json(id):
  job = load_job_from_db(id)
  return jsonify(job)

@app.route('/job/<id>/apply', methods=['post'])
def apply_to_job(id):
  data = request.form
  job = load_job_from_db(id)
  add_application_to_db(id, data)
  return render_template('application_submitted.html',     application=data, job=job)

@app.route("/submit", methods=["POST"])
def submit():

    if hcaptcha.verify():
        # SUCCESS
        pass
    else:
        # FAILED
        pass

if __name__=="__main__":
  app.run(host="0.0.0.0", debug=True)
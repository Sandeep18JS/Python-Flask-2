from flask import Flask, render_template, jsonify, request

from database import load_jobs_from_db, load_job_from_db, add_application_to_db

app = Flask(__name__)

# JOBS = [{
#   'id': 1,
#   'title': 'Data analyst',
#   'location': 'Hyderabad,India',
#   'salary': 'Rs. 10,00,000'
# }, {
#   'id': 2,
#   'title': 'Data Scientist ',
#   'location': 'Delhi,India',
#   'salary': 'Rs. 15,00,000'
# }, {
#   'id': 3,
#   'title': 'Fronend engineer ',
#   'location': 'Bangalore,India',
#   'salary': 'Rs. 12,00,000'
# }, {
#   'id': 4,
#   'title': 'Backend engineer ',
#   'location': 'Chennai,India',
#   'salary': 'Rs. 14,00,000'
# }]


@app.route('/')
def hello_world():
  jobs = load_jobs_from_db()
  return render_template('home.html', jobs=jobs)


@app.route('/api/jobs')
def list_jobs():
  jobs = load_jobs_from_db()
  return jsonify(jobs)


@app.route('/job/<id>')
def show_jobs(id):
  job = load_job_from_db(id)
  if not job:
    return "NOt_Found", 404
  return render_template('jobpage.html', job=job)


@app.route("/api/job/<id>")
def show_job_json(id):
  job = load_job_from_db(id)
  return jsonify(job)


@app.route('/job/<id>/apply', methods=['post'])
def apply_to_job(id):
  data = request.form
  job = load_job_from_db(id)
  add_application_to_db(id, data)
  return render_template('application_submitted.html',
                         application=data,
                         job=job)


if __name__ == '__main__':
  app.run(host='0.0.0.0', debug=True)

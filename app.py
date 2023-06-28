from flask import Flask, render_template, jsonify

from database import load_jobs_from_db

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


if __name__ == '__main__':
  app.run(host='0.0.0.0', debug=True)

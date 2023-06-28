from sqlalchemy import create_engine, text
import os

# Create the database connection URL with SSL parameters
db_url = os.environ['DB_URL']

# Create the SQLAlchemy engine
engine = create_engine(db_url,
                       connect_args={"ssl": {
                         "ssl_ca": "/etc/ssl/cert.pem"
                       }})


def load_jobs_from_db():
  with engine.connect() as conn:
    result = conn.execute(text("select * from jobs"))
    jobs = []
    for row in result.all():
      jobs.append(row._asdict())
    return jobs


def load_job_from_db(id):
  with engine.connect() as conn:
    result = conn.execute(text(f"SELECT * FROM jobs WHERE id = :val"),
                          {"val": id})
    rows = result.mappings().all()
    if len(rows) == 0:
      return None
    else:
      return dict(rows[0])


# with engine.connect() as conn:
#     result = conn.execute(text("select * from jobs"))

#     result_dicts = []
#     for row in result:
#         result_dict = dict(row._asdict())
#         result_dicts.append(result_dict)

#     print(result_dicts)

# print("type(result):", type(result))
# result_all = result.fetchall()

# print("type(result_all):", type(result_all))
# first_result = result_all[0]

# print("type(first_result):", type(first_result))
# first_result_dict = first_result._asdict()

# print("type(first_result_dict):",
# type(first_result_dict))
# print(first_result_dict)

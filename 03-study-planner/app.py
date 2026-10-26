import math
from flask import Flask, render_template_string, request

app = Flask(__name__)

PAGE = """<!doctype html>
<html lang="en">
<head>
  <meta charset="utf-8">
  <meta name="viewport" content="width=device-width,initial-scale=1">
  <title>Study Sprint Planner</title>
  <style>
    *{box-sizing:border-box}body{margin:0;font-family:Arial,sans-serif;color:#17223b;background:#eef3f9}
    main{max-width:850px;margin:48px auto;padding:0 20px}header{padding:36px;border-radius:18px;background:#202f59;color:white}
    header h1{margin:0 0 12px;font-size:2.1rem}header p{margin:0;line-height:1.5;color:#dce4f7}
    section{background:white;border-radius:18px;padding:28px;margin-top:20px;box-shadow:0 4px 18px #1a2c5012}
    label{display:block;font-weight:bold;margin:18px 0 7px}input,textarea{width:100%;padding:12px;border:1px solid #b9c5d7;border-radius:9px;font:inherit}
    textarea{min-height:88px}button{margin-top:22px;padding:13px 20px;background:#2759df;color:white;border:0;border-radius:9px;font-weight:bold;cursor:pointer}
    .grid{display:grid;grid-template-columns:1fr 1fr;gap:18px}.error{color:#9f2020;font-weight:bold}
    .summary{font-size:1.1rem;background:#edf4ff;padding:16px;border-radius:10px}
    .day{border-top:1px solid #e7edf5;padding:15px 0}.day strong{color:#254bba}
    footer{text-align:center;color:#617089;padding:20px;font-size:.9rem}@media(max-width:600px){.grid{grid-template-columns:1fr}}
  </style>
</head>
<body><main>
  <header><h1>Study Sprint Planner</h1><p>Turn revision topics and available study hours into a daily study schedule.</p></header>
  <section>
    <h2>Create your schedule</h2>
    <form method="post">
      <label for="subjects">Topics (separated by commas)</label>
      <textarea id="subjects" name="subjects" required placeholder="Docker, Python, Cloud deployment">{{ form.subjects }}</textarea>
      <div class="grid">
        <div><label for="hours">Total study hours</label><input id="hours" name="hours" type="number" min="0.5" max="500" step="0.5" required value="{{ form.hours }}"></div>
        <div><label for="days">Number of days</label><input id="days" name="days" type="number" min="1" max="30" required value="{{ form.days }}"></div>
      </div>
      <button type="submit">Generate study plan</button>
    </form>
    {% if error %}<p class="error">{{ error }}</p>{% endif %}
  </section>
  {% if plan %}
  <section><h2>Your study plan</h2>
    <p class="summary"><strong>{{ plan.minutes_per_day }} minutes/day</strong> across {{ plan.days }} days · {{ plan.hours }} total hours</p>
    {% for day in plan.schedule %}
      <div class="day"><strong>Day {{ day.number }}</strong><p>
      {% for item in day.blocks %}{{ item.topic }}: {{ item.minutes }} min{% if not loop.last %} · {% endif %}{% endfor %}
      </p></div>
    {% endfor %}
  </section>
  {% endif %}
  <footer>Custom Flask web application • Docker Deployment Task 4.3</footer>
</main></body></html>"""

@app.route("/", methods=["GET", "POST"])
def home():
    form = {"subjects": "", "hours": "6", "days": "3"}
    error, plan = None, None
    if request.method == "POST":
        form = {k: request.form.get(k, "") for k in form}
        try:
            subjects = [item.strip() for item in form["subjects"].split(",") if item.strip()]
            hours = float(form["hours"])
            days = int(form["days"])
            if not subjects or not (0.5 <= hours <= 500) or not (1 <= days <= 30):
                raise ValueError
            minutes = math.ceil(hours * 60 / (days * len(subjects)))
            schedule = [
                {"number": d, "blocks": [{"topic": topic, "minutes": minutes} for topic in subjects]}
                for d in range(1, days + 1)
            ]
            plan = {"minutes_per_day": minutes * len(subjects), "hours": hours,
                    "days": days, "schedule": schedule}
        except ValueError:
            error = "Enter topics, study hours between 0.5 and 500, and 1–30 days."
    return render_template_string(PAGE, form=form, error=error, plan=plan)

@app.get("/health")
def health():
    return {"status": "ok", "application": "Study Sprint Planner"}

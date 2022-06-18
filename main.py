from flask import Flask, render_template

from utils import *

app = Flask(__name__)


@app.route("/")
def main_page():
    candidates = load_candidates_from_json()
    return render_template("list.html", candidates=candidates)


@app.route("/candidate/<int:idx>")
def candidate_page(idx):
    candidate = candidate_by_id(idx)
    if not candidate:
        return "Кандидат не найден"
    return render_template("card.html", candidate=candidate)


@app.route("/search/<candidate_name>")
def search_candidates_page(candidate_name):
    candidates = get_candidates_by_name(candidate_name)
    return render_template("search.html", candidates=candidates)


@app.route("/skill/<skill_name>")
def search_candidates_by_skill_page(skill_name):
    candidates = get_candidates_by_skill(skill_name)
    return render_template("skill.html", skill=skill_name, candidates=candidates)


if __name__ == "__main__":
    app.run()

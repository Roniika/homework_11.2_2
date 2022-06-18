import json


def load_candidates_from_json():
    with open("candidates.json", "r", encoding="utf-8") as file:
        return json.load(file)


def candidate_by_id(uid: int):
    for candidate in load_candidates_from_json():
        if candidate["id"] == uid:
            return candidate


def get_candidates_by_name(candidate_name):
    result = []
    for candidate in load_candidates_from_json():
        if candidate_name.lower() in candidate["name"].lower():
            result.append(candidate)
    return result


def get_candidates_by_skill(skill_name):
    result = []
    for candidate in load_candidates_from_json():
        if skill_name in candidate["skills"].lower().split(", "):
            result.append(candidate)
    return result











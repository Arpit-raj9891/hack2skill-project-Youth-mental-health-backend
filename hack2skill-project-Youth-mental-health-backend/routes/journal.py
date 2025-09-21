from flask import Blueprint, request, jsonify
import json
import os

journal_bp = Blueprint("journal", __name__)

# Local JSON file to store journal entries
JOURNAL_FILE = "journals.json"

# Ensure the file exists
if not os.path.exists(JOURNAL_FILE):
    with open(JOURNAL_FILE, "w") as f:
        json.dump({}, f, indent=4)

# Helper functions
def load_journals():
    with open(JOURNAL_FILE, "r") as f:
        return json.load(f)

def save_journals(data):
    with open(JOURNAL_FILE, "w") as f:
        json.dump(data, f, indent=4)

# ➝ Add a journal entry
@journal_bp.route("/", methods=["POST"])
def add_journal():
    data = request.json
    entry = data.get("entry")
    date = data.get("date")  # Expected format: "YYYY-MM-DD"

    if not entry or not date:
        return jsonify({"error": "entry and date are required"}), 400

    journals = load_journals()
    journals[date] = {"entry": entry, "date": date}
    save_journals(journals)

    return jsonify({"message": "Journal entry saved successfully"}), 201

# ➝ Fetch journal entry by date
@journal_bp.route("/<date>", methods=["GET"])
def get_journal(date):
    journals = load_journals()
    entry = journals.get(date)

    if not entry:
        return jsonify({"error": "No entry found for this date"}), 404

    return jsonify(entry), 200

from flask import Flask, request, jsonify
import sqlite3

app = Flask(__name__)

@app.route("/search", methods=["GET"])
def search():
    query = request.args.get("q")
    if not query:
        return jsonify({"error": "Query parameter 'q' is required."}), 400

    # Query the database
    conn = sqlite3.connect("oria.db")
    cursor = conn.cursor()
    cursor.execute("""
        SELECT id, title, content
        FROM Documents
        WHERE content LIKE ?
    """, (f"%{query}%",))

    results = [
        {"id": row[0], "title": row[1], "content": row[2][:200] + "..."}
        for row in cursor.fetchall()
    ]
    conn.close()

    # Return results as JSON
    return jsonify(results)

if __name__ == "__main__":
    app.run(debug=True)
from flask import Flask, render_template, request, jsonify

app = Flask(__name__)

books_data = [
    {"id": 1, "title": "رحلة إلى المريخ", "author": "أحمد علي", "genre": "خيال علمي", "year": 2022},
    {"id": 2, "title": "فنون البرمجة بالبايثون", "author": "سارة محمد", "genre": "تقنية", "year": 2023},
    {"id": 3, "title": "تاريخ الأندلس", "author": "خالد إبراهيم", "genre": "تاريخ", "year": 2018},
    {"id": 4, "title": "دليل الطبخ السريع", "author": "فاطمة ناصر", "genre": "طبخ", "year": 2024},
]

@app.route("/")
def home():
    return render_template("index.html", books=books_data)

@app.route("/book/<int:book_id>")
def book_details(book_id):
    book = next((b for b in books_data if b["id"] == book_id), None)
    return render_template("book_details.html", book=book)

@app.route("/search")
def search():
    query = request.args.get("query", "").lower()
    if query:
        results = [book for book in books_data if query in book["title"].lower() or query in book["author"].lower()]
    else:
        results = books_data
        
    return render_template("search_results.html", results=results, query=query)

@app.route("/api/search")
def api_search():
    query = request.args.get("q", "").lower()
    results = [book for book in books_data if query in book["title"].lower() or query in book["author"].lower()]
    return jsonify(results) # إرجاع البيانات بتنسيق JSON

if __name__ == "__main__":
    app.run(debug=True)

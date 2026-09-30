from flask import Flask, render_template, jsonify, request
from markupsafe import escape

app = Flask(__name__)

# 1. Danh sách BOOKS >= 4 cuốn
BOOKS = [
    {
        "id": 1,
        "title": "Lập trình Python Căn bản",
        "author": "Nguyễn Văn A",
        "year": 2021,
        "category": "Lập trình",
        "available": True
    },
    {
        "id": 2,
        "title": "Flask Web Development",
        "author": "Miguel Grinberg",
        "year": 2018,
        "category": "Lập trình",
        "available": True
    },
    {
        "id": 3,
        "title": "Cấu trúc Dữ liệu và Giải thuật",
        "author": "Trần Văn B",
        "year": 2020,
        "category": "Khoa học máy tính",
        "available": False
    },
    {
        "id": 4,
        "title": "Thiết kế Cơ sở Dữ liệu",
        "author": "Lê Thị C",
        "year": 2019,
        "category": "Cơ sở dữ liệu",
        "available": True
    }
]

# Hàm bổ trợ tìm sách theo ID
def find_book(book_id):
    return next((book for book in BOOKS if book["id"] == book_id), None)


# 2. Route Trang chủ: /
@app.route('/')
def home():
    total_books = len(BOOKS)
    available_books = sum(1 for book in BOOKS if book['available'])
    return render_template('index.html', total_books=total_books, available_books=available_books)


# 3. Route Danh sách & Lọc thể loại: /books
@app.route('/books')
def get_books():
    selected_category = request.args.get('category')
    
    # Lấy danh sách thể loại duy nhất để làm thanh lọc
    categories = sorted(list(set(book['category'] for book in BOOKS)))
    
    # Lọc sách nếu có query parameter category
    if selected_category:
        filtered_books = [book for book in BOOKS if book['category'] == selected_category]
    else:
        filtered_books = BOOKS
        
    return render_template(
        'books.html', 
        books=filtered_books, 
        categories=categories, 
        selected_category=selected_category
    )


# 4. Route Chi tiết sách: /books/<int:book_id>
@app.route('/books/<int:book_id>')
def get_book_detail(book_id):
    book = find_book(book_id)
    if not book:
        # Trả về trang 404 tùy biến kèm mã lỗi 404
        error_msg = f"Không có sách với ID = {escape(book_id)}"
        return render_template('404.html', message=error_msg), 404
    
    return render_template('detail.html', book=book)


# 5. API Route: /api/books (Lấy danh sách sách dạng JSON)
@app.route('/api/books')
def api_get_books():
    return jsonify(BOOKS), 200


# 5. API Route: /api/books/<int:book_id> (Lấy chi tiết dạng JSON)
@app.route('/api/books/<int:book_id>')
def api_get_book_detail(book_id):
    book = find_book(book_id)
    if not book:
        return jsonify({"error": f"Không có sách với ID = {book_id}"}), 404
    return jsonify(book), 200


# 6. Trang 404 tuỳ biến chung cho ứng dụng
@app.errorhandler(404)
def page_not_found(e):
    # Nếu đường dẫn bắt đầu bằng /api/, trả về JSON lỗi 404
    if request.path.startswith('/api/'):
        return jsonify({"error": "Resource not found"}), 404
    
    # Ngược lại trả về giao diện HTML có menu chung
    return render_template('404.html'), 404


if __name__ == '__main__':
    app.run(debug=True)
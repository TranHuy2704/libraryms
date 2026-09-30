# LibraryMS - Hệ thống Quản lý Thư viện (v0.1)

Ứng dụng Web Quản lý Thư viện đơn giản được xây dựng bằng Python và Flask Framework phục vụ cho bài tập môn Học phần Phần mềm Mã nguồn mở.

---

## 1. Cấu trúc thư mục dự án

```text
libraryms/
├── app.py                  # Mã nguồn chính chạy ứng dụng Flask
├── README.md               # File hướng dẫn và ghi chép test case
├── .gitignore              # Cấu hình bỏ qua thư mục ảo .venv/
└── templates/              # Thư mục chứa giao diện HTML
    ├── base.html           # Layout dùng chung
    ├── books.html          # Danh sách sách + bộ lọc Thể loại
    ├── book_detail.html    # Chi tiết cuốn sách
    └── 404.html            # Trang báo lỗi 404 tùy chỉnh (HTML)

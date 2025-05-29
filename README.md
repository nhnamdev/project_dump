

Phát hiện ngôn ngữ

Anh

Việt

Pháp

Việt

Anh

Trung (Giản thể)
# 🚀 ProjectDump

**ProjectDump** is a Python CLI tool that detects a project's technologies, filters out non-essential files, and compiles the source code and directory structure into a single readable file.

---

## 📦 Features

- 🔍 Auto-detects technologies (Python, JavaScript, Java, etc.)
- 🧹 Skips dependencies, binaries, media, and config clutter
- 🌲 Generates a clean directory tree
- 📄 Dumps readable source code with syntax highlighting
- ⚡ Handles large projects and ignores huge files (>100MB)

---

## 🧑‍💻 Supported Technologies (Partial List)

- **Languages**: Python, JS/TS, Java, Kotlin, PHP, Ruby, Go, Rust, C#, Dart, R, Scala, Elixir
- **Frameworks**: React, Vue, Svelte, Angular, Next.js, Nuxt, Flutter, Android, iOS
- **Infra**: Docker, Kubernetes, Terraform, Ansible
- **CI/CD**: GitHub Actions, GitLab CI, CircleCI

---

## 📂 Output Example
```
🚀 PROJECTDUMP
========================================
🌐 Select language (en/vi): en
📂 Enter the project folder path: /path/to/your/project
🔍 Analyzing project at: /path/to/your/project
🔍 Scanning directories...
🛠️  Detected technologies: python
📁 Extensions included: .py, .pyi, .pyx
📁 Generating directory tree...
📄 Processing files...
  📝 Processing: aggregator.py
  📝 Processing: constants.py
  📝 Processing: detector.py
  📝 Processing: filters.py
  📝 Processing: one_file_version.py
  📝 Processing: tree_generator.py
  📝 Processing: __main__.py

✅ Success! File created: /path/to/your/project/source_dump.txt

📊 Summary:
   - Files processed: 7
   - Output size: 30275 characters (~28 KB)
   - Total lines: 870

🎉 Done! The source_dump.txt file is ready.
```

Inside `source_dump.txt`demo:
```text
# ==================================================
# Path: /path/to/your/project
# Detected tech: python
# ==================================================

## DIRECTORY STRUCTURE

New folder/
├── __pycache__/
├── __main__.py
├── aggregator.py
├── constants.py
├── detector.py
├── filters.py
├── one_file_version.py
├── source_dump.txt
└── tree_generator.py

## FILE CONTENTS

### __main__.py

import os
...
```

## 🚀 Usage
Run from the command line:
```bash
  python main.py /path/to/your/project
```

## 📁 What It Ignores
- **Dependency folders**: node_modules, venv, etc.

- **Media & binaries**: .jpg, .exe, .log, etc.

- **Config/IDE**: .git, .vscode, .github, etc.

- **Large files over 100MB**

## ✅ Requirements
Python 3.x

## 🤝 Contributing
Feel free to fork and contribute to enhance tech detection, support new stacks, or improve output formatting!


2.563 / 5.000
# 🚀 ProjectDump

**ProjectDump** là một công cụ Python CLI phát hiện các công nghệ của dự án, lọc ra các tệp không cần thiết và biên dịch mã nguồn và cấu trúc thư mục thành một tệp duy nhất có thể đọc được.

---

## 📦 Tính năng

- 🔍 Tự động phát hiện các công nghệ (Python, JavaScript, Java, v.v.)
- 🧹 Bỏ qua các phụ thuộc, tệp nhị phân, phương tiện và cấu hình lộn xộn
- 🌲 Tạo cây thư mục sạch
- 📄 Đổ mã nguồn có thể đọc được với cú pháp tô sáng
- ⚡ Xử lý các dự án lớn và bỏ qua các tệp lớn (>100MB)

---

## 🧑‍💻 Các công nghệ được hỗ trợ (Danh sách một phần)

- **Ngôn ngữ**: Python, JS/TS, Java, Kotlin, PHP, Ruby, Go, Rust, C#, Dart, R, Scala, Elixir
- **Khung**: React, Vue, Svelte, Angular, Next.js, Nuxt, Flutter, Android, iOS
- **Cơ sở hạ tầng**: Docker, Kubernetes, Terraform, Ansible
- **CI/CD**: GitHub Hành động, GitLab CI, CircleCI

---
## 📂 Ví dụ đầu ra
```
🚀 PROJECTDUMP
=======================================
🌐 Chọn ngôn ngữ (en/vi): en
📂 Nhập đường dẫn thư mục dự án: /path/to/your/project
🔍 Phân tích dự án tại: /path/to/your/project
🔍 Quét thư mục...
🛠️ Các công nghệ được phát hiện: python
📁 Các phần mở rộng được bao gồm: .py, .pyi, .pyx
📁 Đang tạo cây thư mục...
📄 Đang xử lý tệp...
📝 Đang xử lý: aggregator.py
📝 Đang xử lý: constants.py
📝 Đang xử lý: detector.py
📝 Đang xử lý: filters.py
📝 Đang xử lý: one_file_version.py
📝 Đang xử lý: tree_generator.py
📝 Đang xử lý: __main__.py

✅ Thành công! Tệp đã tạo: /path/to/your/project/source_dump.txt

📊 Tóm tắt:
- Tệp đã xử lý: 7
- Kích thước đầu ra: 30275 ký tự (~28 KB)
- Tổng số dòng: 870

🎉 Hoàn tất! Tệp source_dump.txt đã sẵn sàng.
```

Bên trong `source_dump.txt`demo:
```text
# ===================================================
# Đường dẫn: /path/to/your/project
# Công nghệ được phát hiện: python
# ======================================================

## CẤU TRÚC THƯ MỤC

Thư mục mới/
├── __pycache__/
├── __main__.py
├── aggregator.py
├── constants.py
├── detector.py
├── filters.py
├── one_file_version.py
├── source_dump.txt
└── tree_generator.py

## NỘI DUNG TỆP

### __main__.py

import os
...
```

## 🚀 Cách sử dụng
Chạy từ dòng lệnh:
```bash
python main.py /path/to/your/project
```

## 📁 Những gì nó bỏ qua
- **Thư mục phụ thuộc**: node_modules, venv, v.v.

- **Phương tiện & tệp nhị phân**: .jpg, .exe, .log, v.v.

- **Cấu hình/IDE**: .git, .vscode, .github, v.v.

- **Tệp lớn trên 100MB**

## ✅ Yêu cầu
Python 3.x

## 🤝 Đóng góp
Hãy thoải mái phân nhánh và đóng góp để nâng cao khả năng phát hiện công nghệ, hỗ trợ các ngăn xếp mới hoặc cải thiện định dạng đầu ra!
Gửi ý kiến phản hồi
Có kết quả dịch

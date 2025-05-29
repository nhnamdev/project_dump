import tkinter as tk
from tkinter import filedialog, scrolledtext
from aggregator import aggregate_code
from constants import TEXT_VI
import os
import shutil

class ProjectDumpApp:
    def __init__(self, root):
        self.root = root
        self.root.title(TEXT_VI['app_title'])

        self.project_path = tk.StringVar()
        self.output_path = tk.StringVar()

        # --- Chọn thư mục dự án ---
        tk.Label(root, text="📂 Thư mục dự án cần tổng hợp:").pack(pady=3)
        tk.Entry(root, textvariable=self.project_path, width=60).pack(padx=10)
        tk.Button(root, text="🔍 Chọn thư mục dự án", command=self.select_project_folder).pack(pady=5)

        # --- Chọn thư mục xuất file ---
        tk.Label(root, text="💾 Thư mục lưu file `source_dump.txt`:").pack(pady=3)
        tk.Entry(root, textvariable=self.output_path, width=60).pack(padx=10)
        tk.Button(root, text="📁 Chọn thư mục lưu", command=self.select_output_folder).pack(pady=5)

        # --- Nút xử lý ---
        tk.Button(root, text="🚀 Tổng hợp mã nguồn", command=self.run_aggregation).pack(pady=10)

        # --- Khung hiển thị log ---
        self.output_box = scrolledtext.ScrolledText(root, wrap=tk.WORD, width=80, height=20)
        self.output_box.pack(padx=10, pady=10)

    def select_project_folder(self):
        folder = filedialog.askdirectory()
        if folder:
            self.project_path.set(folder)

    def select_output_folder(self):
        folder = filedialog.askdirectory()
        if folder:
            self.output_path.set(folder)

    def run_aggregation(self):
        project = self.project_path.get()
        output = self.output_path.get()

        if not os.path.isdir(project):
            self.output_box.insert(tk.END, "❌ Thư mục dự án không hợp lệ!\n")
            return

        if not os.path.isdir(output):
            self.output_box.insert(tk.END, "❌ Thư mục lưu file không hợp lệ!\n")
            return

        # Ghi đè file đầu ra tại thư mục output
        def custom_aggregate_code(project_path, text):
            success = aggregate_code(project_path, text)
            default_file = os.path.join(project_path, "source_dump.txt")
            if os.path.exists(default_file):
                try:
                    new_path = os.path.join(output, "source_dump.txt")
                    shutil.copy2(default_file, new_path)   # ✅ copy file
                    os.remove(default_file)                # ✅ xóa file gốc nếu cần
                    self.output_box.insert(tk.END, f"✅ File đã lưu tại: {new_path}\n")
                except Exception as e:
                    self.output_box.insert(tk.END, f"❌ Không thể sao chép file: {e}\n")
                    return False
            return success

        self.output_box.insert(tk.END, f"🔎 Đang xử lý dự án: {project}\n")
        if custom_aggregate_code(project, TEXT_VI):
            self.output_box.insert(tk.END, TEXT_VI['done'] + "\n")
        else:
            self.output_box.insert(tk.END, TEXT_VI['error'] + "\n")

if __name__ == "__main__":
    root = tk.Tk()
    app = ProjectDumpApp(root)
    root.mainloop()

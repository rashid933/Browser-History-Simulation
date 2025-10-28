import tkinter as tk
from tkinter import messagebox

# -----------------------------
# Browser History Logic
# -----------------------------
class BrowserHistory:
    def __init__(self):
        self.back_stack = []
        self.forward_stack = []
        self.current_page = None

    def visit(self, url):
        if self.current_page:
            self.back_stack.append(self.current_page)
        self.current_page = url
        self.forward_stack.clear()

    def back(self):
        if not self.back_stack:
            return None
        self.forward_stack.append(self.current_page)
        self.current_page = self.back_stack.pop()
        return self.current_page

    def forward(self):
        if not self.forward_stack:
            return None
        self.back_stack.append(self.current_page)
        self.current_page = self.forward_stack.pop()
        return self.current_page

# -----------------------------
# GUI Class
# -----------------------------
class BrowserApp:
    def __init__(self, root):
        self.browser = BrowserHistory()
        self.root = root
        self.root.title("Browser History Simulator")
        self.root.geometry("400x350")
        self.root.config(bg="#f5f5f5")

        # URL entry
        self.url_entry = tk.Entry(root, width=35, font=("Arial", 12))
        self.url_entry.pack(pady=10)

        # Buttons
        btn_frame = tk.Frame(root, bg="#f5f5f5")
        btn_frame.pack(pady=5)

        self.visit_btn = tk.Button(btn_frame, text="Visit", width=10, command=self.visit_page, bg="#4CAF50", fg="white")
        self.visit_btn.grid(row=0, column=0, padx=5)

        self.back_btn = tk.Button(btn_frame, text="Back", width=10, command=self.go_back, bg="#2196F3", fg="white")
        self.back_btn.grid(row=0, column=1, padx=5)

        self.forward_btn = tk.Button(btn_frame, text="Forward", width=10, command=self.go_forward, bg="#FF9800", fg="white")
        self.forward_btn.grid(row=0, column=2, padx=5)

        # Current page label
        self.current_label = tk.Label(root, text="Current Page: None", font=("Arial", 12, "bold"), bg="#f5f5f5")
        self.current_label.pack(pady=10)

        # History display
        self.history_text = tk.Text(root, height=8, width=45, font=("Consolas", 10))
        self.history_text.pack(pady=10)
        self.history_text.config(state="disabled")

        self.update_display()

    # --- Button functions ---
    def visit_page(self):
        url = self.url_entry.get().strip()
        if not url:
            messagebox.showwarning("Input Error", "Please enter a URL!")
            return
        self.browser.visit(url)
        self.url_entry.delete(0, tk.END)
        self.update_display()

    def go_back(self):
        page = self.browser.back()
        if not page:
            messagebox.showinfo("Info", "No pages in back history.")
        self.update_display()

    def go_forward(self):
        page = self.browser.forward()
        if not page:
            messagebox.showinfo("Info", "No pages in forward history.")
        self.update_display()

    def update_display(self):
        # Update current label
        current = self.browser.current_page if self.browser.current_page else "None"
        self.current_label.config(text=f"Current Page: {current}")

        # Update history text box
        self.history_text.config(state="normal")
        self.history_text.delete(1.0, tk.END)
        self.history_text.insert(tk.END, f"Back Stack:\n{self.browser.back_stack}\n\n")
        self.history_text.insert(tk.END, f"Forward Stack:\n{self.browser.forward_stack}\n")
        self.history_text.config(state="disabled")


# -----------------------------
# Run the App
# -----------------------------

if __name__ == "__main__":
    root = tk.Tk()
    app = BrowserApp(root)
    root.mainloop()

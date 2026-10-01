import math
import tkinter as tk
from tkinter import messagebox

# --- Authentication Logic ---
def check_login():
    username = entry_username.get().strip()
    password = entry_password.get()
    
    # Hardcoded credentials for quick testing
    if username == "admin" and password == "password123":
        login_window.destroy()  # Close the login screen
        open_calculator()       # Open the main calculator
    else:
        messagebox.showerror("Login Failed", "Invalid username or password.")

# --- Main Calculator Window ---
def open_calculator():
    def calculate():
        try:
            radius = float(entry_radius.get())
            area = math.pi * (radius ** 2)
            circumference = 2 * math.pi * radius
            
            label_radius_val.config(text=f"{radius}")
            label_area_val.config(text=f"{area:.2f}")
            label_circumference_val.config(text=f"{circumference:.2f}")
        except ValueError:
            messagebox.showerror("Invalid Input", "Please enter a valid numeric radius.")

    # --- Dark Theme Palette ---
    BG_MAIN = "#1e1e1e"
    BG_CARD = "#2d2d2d"
    TXT_MAIN = "#ffffff"
    TXT_MUTED = "#b3b3b3"
    ACCENT_BLUE = "#3b82f6"
    ACCENT_GREEN = "#10b981"
    BORDER_COLOR = "#404040"

    root = tk.Tk()
    root.title("Circle Calculator")
    root.geometry("400x320")
    root.configure(bg=BG_MAIN)
    root.resizable(False, False)

    heading = tk.Label(root, text="Circle Calculator", font=("Arial", 16, "bold"), bg=BG_MAIN, fg=TXT_MAIN)
    heading.pack(pady=(25, 15))

    input_frame = tk.Frame(root, bg=BG_MAIN)
    input_frame.pack(pady=5)

    lbl_prompt = tk.Label(input_frame, text="Enter Radius:", font=("Arial", 11), bg=BG_MAIN, fg=TXT_MUTED)
    lbl_prompt.pack(side=tk.LEFT, padx=8)

    global entry_radius
    entry_radius = tk.Entry(input_frame, font=("Arial", 11), width=12, justify="center",
                            bg=BG_CARD, fg=TXT_MAIN, insertbackground=TXT_MAIN, bd=1, relief="solid")
    entry_radius.pack(side=tk.LEFT, padx=5)
    entry_radius.focus()

    btn_calculate = tk.Button(root, text="Calculate", font=("Arial", 11, "bold"), 
                              bg=BG_CARD, fg=ACCENT_GREEN, 
                              activebackground="#3d3d3d", activeforeground="#14b8a6", 
                              width=12, bd=1, relief="solid", highlightbackground=BORDER_COLOR,
                              padx=10, pady=5, command=calculate, cursor="hand2")
    btn_calculate.pack(pady=15)

    results_frame = tk.LabelFrame(root, text=" Results ", font=("Arial", 10, "bold"), bg=BG_CARD, fg=TXT_MUTED, bd=1, relief="solid")
    results_frame.pack(padx=25, pady=10, fill="x")
    results_frame.columnconfigure(1, weight=1)

    tk.Label(results_frame, text="Radius:", font=("Arial", 11), bg=BG_CARD, fg=TXT_MUTED).grid(row=0, column=0, sticky="w", padx=15, pady=8)
    global label_radius_val
    label_radius_val = tk.Label(results_frame, text="--", font=("Arial", 11, "bold"), bg=BG_CARD, fg=TXT_MAIN)
    label_radius_val.grid(row=0, column=1, sticky="e", padx=15, pady=8)

    tk.Label(results_frame, text="Area:", font=("Arial", 11), bg=BG_CARD, fg=TXT_MUTED).grid(row=1, column=0, sticky="w", padx=15, pady=8)
    global label_area_val
    label_area_val = tk.Label(results_frame, text="--", font=("Arial", 11, "bold"), bg=BG_CARD, fg=ACCENT_BLUE)
    label_area_val.grid(row=1, column=1, sticky="e", padx=15, pady=8)

    tk.Label(results_frame, text="Circumference:", font=("Arial", 11), bg=BG_CARD, fg=TXT_MUTED).grid(row=2, column=0, sticky="w", padx=15, pady=8)
    global label_circumference_val
    label_circumference_val = tk.Label(results_frame, text="--", font=("Arial", 11, "bold"), bg=BG_CARD, fg=ACCENT_GREEN)
    label_circumference_val.grid(row=2, column=1, sticky="e", padx=15, pady=8)

    root.mainloop()

# --- Login UI Window ---
login_window = tk.Tk()
login_window.title("Login")
login_window.geometry("300x220")
login_window.configure(bg="#f8f9fa")
login_window.resizable(False, False)

# Title Label
tk.Label(login_window, text="System Login", font=("Arial", 14, "bold"), bg="#f8f9fa", fg="#212529").pack(pady=(20, 15))

# Username Fields
frame_user = tk.Frame(login_window, bg="#f8f9fa")
frame_user.pack(pady=5)
tk.Label(frame_user, text="Username:", font=("Arial", 10), bg="#f8f9fa", width=10, anchor="w").pack(side=tk.LEFT)
entry_username = tk.Entry(frame_user, font=("Arial", 10), width=18)
entry_username.pack(side=tk.LEFT)
entry_username.focus()

# Password Fields (Masked with show="*")
frame_pass = tk.Frame(login_window, bg="#f8f9fa")
frame_pass.pack(pady=5)
tk.Label(frame_pass, text="Password:", font=("Arial", 10), bg="#f8f9fa", width=10, anchor="w").pack(side=tk.LEFT)
entry_password = tk.Entry(frame_pass, font=("Arial", 10), width=18, show="*")
entry_password.pack(side=tk.LEFT)

# Login Button
btn_login = tk.Button(login_window, text="Login", font=("Arial", 10, "bold"), bg="#0d6efd", fg="white", 
                      width=12, command=check_login, cursor="hand2")
btn_login.pack(pady=20)

# Bind the Enter key to login automatically
login_window.bind('<Return>', lambda event: check_login())

login_window.mainloop()

# bridge_ui.py  — Corrected, simple, modern, error-free Bridge UI (Tkinter)

import tkinter as tk
from tkinter import ttk, messagebox, filedialog
import json, time

# --- Calculation (placeholder) ---
def calc_bridge(span, width, girders, live):
    deck_thickness = 0.2
    density_conc = 25
    area = span * width
    self_weight = density_conc * deck_thickness * area
    uniform_load = (self_weight / span) + live
    moment = uniform_load * span**2 / 8
    shear = uniform_load * span / 2
    return {
        "deck_self_weight_kN": round(self_weight, 2),
        "uniform_load_kN_per_m": round(uniform_load, 2),
        "total_moment_kN_m": round(moment, 2),
        "total_shear_kN": round(shear, 2),
        "per_girder_moment_kN_m": round(moment / girders, 2),
        "per_girder_shear_kN": round(shear / girders, 2)
    }

# --- App Window ---
class BridgeApp(tk.Tk):
    def __init__(self):
        super().__init__()
        self.title("Bridge Designer — Simple")
        self.geometry("820x460")
        self.configure(bg="#f3f4f6")
        self._style()
        self._ui()

    def _style(self):
        style = ttk.Style(self)
        try:
            style.theme_use("clam")
        except:
            pass

        style.configure("Card.TFrame", background="white", relief="flat")
        style.configure("Title.TLabel", font=("Segoe UI", 14, "bold"), background="white")
        style.configure("Small.TLabel", font=("Segoe UI", 9), foreground="#475569", background="white")
        style.configure("TLabel", background="white", foreground="#111827")

        style.configure("Accent.TButton",
                        background="#2563eb",
                        foreground="white",
                        padding=8,
                        font=("Segoe UI", 10, "bold"))
        style.map("Accent.TButton", background=[("active", "#1e40af")])

    def _ui(self):
        # Header
        header = ttk.Frame(self, style="Card.TFrame", padding=16)
        header.place(x=12, y=12, width=796, height=70)

        ttk.Label(header, text="Bridge Module — Designer", style="Title.TLabel").pack(anchor="w")
        ttk.Label(header, text="Simple · clean · fast · modern UI", style="Small.TLabel").pack(anchor="w", pady=(4,0))

        # Left card (Inputs)
        left = ttk.Frame(self, style="Card.TFrame", padding=12)
        left.place(x=12, y=94, width=360, height=340)

        ttk.Label(left, text="Input Parameters", style="Title.TLabel").grid(row=0, column=0, columnspan=2, sticky="w", pady=(0,10))

        # Span
        ttk.Label(left, text="Span (m):").grid(row=1, column=0, sticky="w", pady=6)
        self.ev_span = tk.StringVar(value="30")
        ttk.Entry(left, textvariable=self.ev_span, width=18).grid(row=1, column=1)

        # Width
        ttk.Label(left, text="Width (m):").grid(row=2, column=0, sticky="w", pady=6)
        self.ev_width = tk.StringVar(value="10")
        ttk.Entry(left, textvariable=self.ev_width, width=18).grid(row=2, column=1)

        # Girders
        ttk.Label(left, text="Girders:").grid(row=3, column=0, sticky="w", pady=6)
        self.ev_girders = tk.StringVar(value="4")
        ttk.Entry(left, textvariable=self.ev_girders, width=18).grid(row=3, column=1)

        # Live load
        ttk.Label(left, text="Live load (kN/m):").grid(row=4, column=0, sticky="w", pady=6)
        self.ev_live = tk.StringVar(value="5")
        ttk.Entry(left, textvariable=self.ev_live, width=18).grid(row=4, column=1)

        # Buttons
        btn_frame = ttk.Frame(left, style="Card.TFrame")
        btn_frame.grid(row=6, column=0, columnspan=2, pady=18)

        ttk.Button(btn_frame, text="Calculate", style="Accent.TButton",
                   command=self.on_calculate).pack(side="left", padx=6)
        ttk.Button(btn_frame, text="Clear", command=self.on_clear).pack(side="left", padx=6)
        ttk.Button(btn_frame, text="Save JSON", command=self.on_save).pack(side="left", padx=6)

        # Right card (Results)
        right = ttk.Frame(self, style="Card.TFrame", padding=12)
        right.place(x=384, y=94, width=424, height=340)

        ttk.Label(right, text="Results", style="Title.TLabel").pack(anchor="w")

        self.result_labels = {}
        frame_res = ttk.Frame(right, style="Card.TFrame")
        frame_res.pack(fill="x", pady=(8,10))

        for title in [
            "Deck Self-weight (kN):",
            "Uniform load (kN/m):",
            "Total moment (kN·m):",
            "Total shear (kN):",
            "Per-girder M / V:"
        ]:
            row = ttk.Frame(frame_res, style="Card.TFrame")
            row.pack(fill="x", pady=4)
            ttk.Label(row, text=title).pack(side="left")
            val = ttk.Label(row, text="—")
            val.pack(side="right")
            self.result_labels[title] = val

        ttk.Label(right, text="Schematic", style="Small.TLabel").pack(anchor="w")

        self.canvas = tk.Canvas(right, width=380, height=140,
                                bg="#f9fafb", highlightthickness=1, highlightbackground="#e5e7eb")
        self.canvas.pack(pady=8)

        # initial schematic + default results
        self.draw_schematic(30, 4)

    def on_calculate(self):
        try:
            s = float(self.ev_span.get())
            w = float(self.ev_width.get())
            g = int(float(self.ev_girders.get()))
            l = float(self.ev_live.get())
            if s <= 0 or w <= 0 or g <= 0:
                raise ValueError
        except Exception:
            messagebox.showerror("Invalid input", "Please enter valid positive numbers.")
            return

        out = calc_bridge(s, w, g, l)

        # put numbers as strings so UI shows properly
        self.result_labels["Deck Self-weight (kN):"].config(text=f"{out['deck_self_weight_kN']}")
        self.result_labels["Uniform load (kN/m):"].config(text=f"{out['uniform_load_kN_per_m']}")
        self.result_labels["Total moment (kN·m):"].config(text=f"{out['total_moment_kN_m']}")
        self.result_labels["Total shear (kN):"].config(text=f"{out['total_shear_kN']}")
        self.result_labels["Per-girder M / V:"].config(
            text=f"{out['per_girder_moment_kN_m']} / {out['per_girder_shear_kN']}")

        self.draw_schematic(s, g)

    def on_clear(self):
        self.ev_span.set("30")
        self.ev_width.set("10")
        self.ev_girders.set("4")
        self.ev_live.set("5")
        for v in self.result_labels.values():
            v.config(text="—")
        self.draw_schematic(30, 4)

    def on_save(self):
        try:
            data = {
                "inputs": {
                    "span": float(self.ev_span.get()),
                    "width": float(self.ev_width.get()),
                    "girders": int(float(self.ev_girders.get())),
                    "live": float(self.ev_live.get())
                },
                "timestamp": int(time.time())
            }
        except Exception:
            messagebox.showerror("Invalid input", "Enter valid values first.")
            return

        fn = filedialog.asksaveasfilename(defaultextension=".json",
                                          filetypes=[("JSON files","*.json")])
        if not fn:
            return

        with open(fn, "w") as f:
            json.dump(data, f, indent=2)

        messagebox.showinfo("Saved", "File saved successfully.")

    def draw_schematic(self, span, girders):
        c = self.canvas
        c.delete("all")

        W = 380; H = 140
        x0, x1 = 20, W - 20
        y_deck = 40
        deck_h = 22

        # Deck (no radius)
        c.create_rectangle(x0, y_deck, x1, y_deck + deck_h,
                           fill="#2563eb", outline="#1846b3", width=2)

        # Supports
        c.create_rectangle(x0 + 4, y_deck + deck_h, x0 + 14, y_deck + deck_h + 20,
                           fill="#334155", outline="")
        c.create_rectangle(x1 - 14, y_deck + deck_h, x1 - 4, y_deck + deck_h + 20,
                           fill="#334155", outline="")

        # Girders
        g = max(1, int(girders))
        usable = (x1 - x0 - 40)
        for i in range(g):
            xi = x0 + 20 + (usable / 2 if g == 1 else i * (usable / (g - 1)))
            c.create_line(xi, y_deck + deck_h, xi, y_deck + deck_h + 20,
                          fill="#0f172a", width=3)

        # Labels
        c.create_text(x0, y_deck - 10, anchor="w",
                      text=f"Span: {span} m", fill="#0f172a",
                      font=("Segoe UI", 9, "bold"))
        c.create_text(x1, y_deck - 10, anchor="e",
                      text=f"Girders: {g}", fill="#0f172a",
                      font=("Segoe UI", 9, "bold"))

if __name__ == "__main__":
    BridgeApp().mainloop()

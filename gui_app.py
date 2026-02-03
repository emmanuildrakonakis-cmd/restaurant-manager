import customtkinter as ctk
from models import Restaurant_manager 
from datetime import datetime

# Ρυθμίσεις: Dark Mode & Μπλε θέμα
ctk.set_appearance_mode("Dark")  
ctk.set_default_color_theme("blue")  

class RestaurantApp(ctk.CTk):
    def __init__(self):
        super().__init__()

        # 1. Σύνδεση με το Backend
        self.manager = Restaurant_manager()

        # 2. Ρύθμιση Παραθύρου
        self.title("Taverna Manager v4.0 (Pro UI)")
        self.geometry("1100x700")

        # Layout: 2 Στήλες
        self.grid_columnconfigure(1, weight=1)
        self.grid_rowconfigure(0, weight=1)

        # ==========================================
        # ΑΡΙΣΤΕΡΗ ΣΤΗΛΗ (INPUTS & ACTIONS)
        # ==========================================
        self.sidebar_frame = ctk.CTkFrame(self, width=300, corner_radius=0)
        self.sidebar_frame.grid(row=0, column=0, sticky="nsew")

        # --- ΤΙΤΛΟΣ: ΝΕΑ ΚΡΑΤΗΣΗ ---
        self.logo_label = ctk.CTkLabel(self.sidebar_frame, text="📝 ΝΕΑ ΚΡΑΤΗΣΗ", font=ctk.CTkFont(size=18, weight="bold"))
        self.logo_label.grid(row=0, column=0, padx=20, pady=(20, 10))

        self.entry_name = ctk.CTkEntry(self.sidebar_frame, placeholder_text="Όνομα Πελάτη")
        self.entry_name.grid(row=1, column=0, padx=20, pady=5)

        self.entry_people = ctk.CTkEntry(self.sidebar_frame, placeholder_text="Αριθμός Ατόμων")
        self.entry_people.grid(row=2, column=0, padx=20, pady=5)

        self.entry_date = ctk.CTkEntry(self.sidebar_frame, placeholder_text="Ημερομηνία")
        self.entry_date.grid(row=3, column=0, padx=20, pady=5)
        self.entry_date.insert(0, datetime.now().strftime("%Y-%m-%d"))

        self.entry_time = ctk.CTkEntry(self.sidebar_frame, placeholder_text="Ώρα (π.χ. 21:00)")
        self.entry_time.grid(row=4, column=0, padx=20, pady=5)

        self.entry_table = ctk.CTkEntry(self.sidebar_frame, placeholder_text="Τραπέζι (No)")
        self.entry_table.grid(row=5, column=0, padx=20, pady=5)

        self.btn_add = ctk.CTkButton(self.sidebar_frame, text="✅ Προσθήκη Κράτησης", fg_color="green", command=self.add_booking_gui)
        self.btn_add.grid(row=6, column=0, padx=20, pady=15)

        # --- ΔΙΑΧΩΡΙΣΤΙΚΗ ΓΡΑΜΜΗ ---
        self.separator = ctk.CTkLabel(self.sidebar_frame, text="-" * 40)
        self.separator.grid(row=7, column=0, pady=5)

        # --- ΤΙΤΛΟΣ: ΤΑΜΕΙΟ ---
        self.checkout_label = ctk.CTkLabel(self.sidebar_frame, text="💸 ΤΑΜΕΙΟ / CHECKOUT", font=ctk.CTkFont(size=18, weight="bold"))
        self.checkout_label.grid(row=8, column=0, padx=20, pady=(10, 5))

        self.entry_checkout_name = ctk.CTkEntry(self.sidebar_frame, placeholder_text="Όνομα για Κλείσιμο")
        self.entry_checkout_name.grid(row=9, column=0, padx=20, pady=5)

        self.entry_tips = ctk.CTkEntry(self.sidebar_frame, placeholder_text="Ποσό Tips (€)")
        self.entry_tips.grid(row=10, column=0, padx=20, pady=5)

        self.btn_pay = ctk.CTkButton(self.sidebar_frame, text="💰 Κλείσιμο Τραπεζιού", fg_color="#D35B58", hover_color="#C72C41", command=self.pay_booking_gui)
        self.btn_pay.grid(row=11, column=0, padx=20, pady=15)

        # --- EXTRAS ---
        self.btn_report = ctk.CTkButton(self.sidebar_frame, text="📅 Μηνιαία Αναφορά (.txt)", fg_color="#3B8ED0", command=self.generate_report_gui)
        self.btn_report.grid(row=12, column=0, padx=20, pady=10)

        self.status_label = ctk.CTkLabel(self.sidebar_frame, text="Έτοιμο.", text_color="gray")
        self.status_label.grid(row=13, column=0, padx=20, pady=20)


        # ==========================================
        # ΔΕΞΙΑ ΣΤΗΛΗ (ΛΙΣΤΑ & ΦΙΛΤΡΑ)
        # ==========================================
        self.main_frame = ctk.CTkFrame(self)
        self.main_frame.grid(row=0, column=1, padx=20, pady=20, sticky="nsew")

        # --- ΦΙΛΤΡΟ ΗΜΕΡΟΜΗΝΙΑΣ (ΝΕΟ!) ---
        self.filter_frame = ctk.CTkFrame(self.main_frame, fg_color="transparent")
        self.filter_frame.pack(pady=10, fill="x", padx=10)

        self.label_list = ctk.CTkLabel(self.filter_frame, text="📅 Πρόγραμμα Ημέρας:", font=ctk.CTkFont(size=14, weight="bold"))
        self.label_list.pack(side="left", padx=5)

        # Πεδίο αναζήτησης ημερομηνίας
        self.entry_filter_date = ctk.CTkEntry(self.filter_frame, width=120, placeholder_text="YYYY-MM-DD")
        self.entry_filter_date.pack(side="left", padx=5)
        self.entry_filter_date.insert(0, datetime.now().strftime("%Y-%m-%d")) # Default σήμερα

        # Κουμπιά Φίλτρου
        self.btn_search = ctk.CTkButton(self.filter_frame, text="🔍 Αναζήτηση", width=100, command=self.search_by_date)
        self.btn_search.pack(side="left", padx=5)

        self.btn_show_all = ctk.CTkButton(self.filter_frame, text="👁️ Όλα", width=80, fg_color="gray", command=self.show_all_bookings)
        self.btn_show_all.pack(side="left", padx=5)

        # --- ΛΙΣΤΑ (TEXTBOX) ---
        self.textbox = ctk.CTkTextbox(self.main_frame, width=600, height=500, font=("Courier", 14))
        self.textbox.pack(padx=20, pady=10, fill="both", expand=True)

        # Φόρτωση αρχικών δεδομένων (Όλων)
        self.refresh_list(filter_date=None)

    # ==========================================
    # LOGIC FUNCTIONS
    # ==========================================

    def add_booking_gui(self):
        name = self.entry_name.get()
        date = self.entry_date.get()
        time = self.entry_time.get()
        
        if not name or not date:
            self.status_label.configure(text="⚠️ Συμπλήρωσε τα στοιχεία!", text_color="orange")
            return

        try:
            people = int(self.entry_people.get())
            table = int(self.entry_table.get())
            self.manager.add_reservation(name, people, date, time, table)
            
            # Καθαρισμός
            self.entry_name.delete(0, "end")
            self.entry_people.delete(0, "end")
            self.status_label.configure(text=f"✅ Προστέθηκε: {name}", text_color="green")
            
            # Ανανέωση λίστας (δείχνουμε την ημερομηνία που μόλις έβαλε)
            self.refresh_list(filter_date=None) 
            
        except ValueError:
            self.status_label.configure(text="❌ Λάθος αριθμοί!", text_color="red")

    def pay_booking_gui(self):
        name_query = self.entry_checkout_name.get()
        tips_str = self.entry_tips.get()

        if not name_query or not tips_str:
            self.status_label.configure(text="⚠️ Βάλε όνομα και Tips!", text_color="orange")
            return

        res = self.manager.find_reservation_by_name(name_query)

        if res:
            try:
                tips = float(tips_str)
                res.add_tips(tips)
                self.manager.save_to_db()
                
                self.status_label.configure(text=f"💰 Πληρώθηκε: {res.customer_name}", text_color="green")
                self.entry_checkout_name.delete(0, "end")
                self.entry_tips.delete(0, "end")
                self.refresh_list(filter_date=None)
            except ValueError:
                self.status_label.configure(text="❌ Τα tips πρέπει να είναι αριθμός!", text_color="red")
        else:
            self.status_label.configure(text="❌ Δεν βρέθηκε πελάτης.", text_color="red")

    def generate_report_gui(self):
        self.manager.tips_process()
        self.status_label.configure(text="📄 Η αναφορά δημιουργήθηκε!", text_color="#3B8ED0")

    # --- ΝΕΕΣ ΣΥΝΑΡΤΗΣΕΙΣ ΦΙΛΤΡΟΥ ---
    def search_by_date(self):
        target_date = self.entry_filter_date.get()
        self.refresh_list(filter_date=target_date)

    def show_all_bookings(self):
        self.refresh_list(filter_date=None)

    # --- Η ΚΑΡΔΙΑ ΤΗΣ ΛΙΣΤΑΣ (ΤΩΡΑ ΜΕ ΦΙΛΤΡΟ) ---
    def refresh_list(self, filter_date=None):
        self.textbox.configure(state="normal")
        self.textbox.delete("0.0", "end")
        
        if not self.manager.reservations:
            self.textbox.insert("0.0", "📭 Δεν υπάρχουν κρατήσεις.")
            self.textbox.configure(state="disabled")
            return

        text_output = ""
        found_count = 0

        # Τίτλος Λίστας
        if filter_date:
            text_output += f"🔎 ΑΠΟΤΕΛΕΣΜΑΤΑ ΓΙΑ: {filter_date}\n\n"
        else:
            text_output += f"📋 ΟΛΕΣ ΟΙ ΚΡΑΤΗΣΕΙΣ\n\n"

        for res in self.manager.reservations:
            # ΑΝ υπάρχει φίλτρο ΚΑΙ η ημερομηνία δεν ταιριάζει -> Προσπέρασέ το
            if filter_date and res.res_date != filter_date:
                continue

            # Εικονίδια
            status_icon = "🔴 ΚΛΕΙΣΤΟ" if res.is_closed else "🟢 ΑΝΟΙΧΤΟ"
            
            # Δημιουργία γραμμής
            line = f"📅 {res.res_date} | 🕒 {res.time} | Τραπέζι {res.table_id}\n"
            line += f"👤 {res.customer_name} ({res.people_count} άτ.) | {status_icon} | Tips: {res.tips}€\n"
            line += "-" * 55 + "\n"
            text_output += line
            found_count += 1
            
        if found_count == 0:
            text_output += "❌ Κανένα αποτέλεσμα."

        self.textbox.insert("0.0", text_output)
        self.textbox.configure(state="disabled")

if __name__ == "__main__":
    app = RestaurantApp()
    app.mainloop()
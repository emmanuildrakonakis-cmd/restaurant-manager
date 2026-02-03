import json
import os
from datetime import datetime

class Reservation:
    def __init__(self, customer_name, people_count, res_date, time, table_id, notes="", tips=0.0, is_closed=False, date_closed=None): 
        self.customer_name = customer_name
        self.people_count = people_count
        self.res_date = res_date  # Ημερομηνία που θα έρθει ο πελάτης
        self.time = time
        self.table_id = table_id
        self.notes = notes
        
        self.tips = tips
        self.is_closed = is_closed
        self.date_closed = date_closed # Ημερομηνία που πλήρωσε (για το ταμείο)

    def add_tips(self, amount):
        if amount > 0:
            self.tips += amount
        self.is_closed = True
        
        # Καταγράφουμε πότε έγινε η πληρωμή (Σήμερα)
        self.date_closed = datetime.now().strftime("%Y-%m-%d")
        
        print(f"💰 Το τραπέζι έκλεισε. Tips: {self.tips}€ | Ημ. Πληρωμής: {self.date_closed}")

    def to_dict(self):
        return {
            "customer_name": self.customer_name,
            "people_count": self.people_count,
            "res_date": self.res_date,
            "time": self.time,
            "table_id": self.table_id,
            "notes": self.notes,
            "tips": self.tips,
            "is_closed": self.is_closed,
            "date_closed": self.date_closed
        }

class Restaurant_manager:
    def __init__(self):
        self.reservations = []
        self.db_file = "history.json"
        # Φόρτωση παλιών δεδομένων κατά την εκκίνηση
        self.load_from_db()

    def add_reservation(self, customer_name, people_count, res_date, time, table_id, notes=""):
        new_res = Reservation(customer_name, people_count, res_date, time, table_id, notes)
        self.reservations.append(new_res)
        print(f"✅ Κράτηση: {customer_name} στις {res_date} (Τραπέζι {table_id})")
        self.save_to_db()

    def find_reservation_by_name(self, name_query):
        for reservation in self.reservations:
            if name_query in reservation.customer_name:
                return reservation
        return None

    def save_to_db(self):
        data_to_save = [res.to_dict() for res in self.reservations]
        with open(self.db_file, "w", encoding="utf-8") as f:
            json.dump(data_to_save, f, ensure_ascii=False, indent=4)

    def load_from_db(self):
        if not os.path.exists(self.db_file): return
        try:
            with open(self.db_file, "r", encoding="utf-8") as f:
                data = json.load(f)
            self.reservations = []
            for item in data:
                # Χρησιμοποιούμε .get() για ασφάλεια αν λείπει κάποιο πεδίο
                res = Reservation(
                    item["customer_name"], item["people_count"], item.get("res_date", "Unknown"), 
                    item["time"], item["table_id"], item["notes"], item["tips"], 
                    item["is_closed"], item["date_closed"]
                )
                self.reservations.append(res)
            print(f"📂 Φορτώθηκαν {len(self.reservations)} κρατήσεις από το ιστορικό.")
        except Exception as e:
            print(f"⚠️ Πρόβλημα κατά τη φόρτωση αρχείου: {e}")

    def show_daily_schedule(self, target_date):
        print(f"\n=== 📅 ΠΡΟΓΡΑΜΜΑ ΓΙΑ: {target_date} ===")
        found = False
        for res in self.reservations:
            # Δείχνουμε μόνο όσους έχουν κράτηση για τη συγκεκριμένη μέρα
            if res.res_date == target_date:
                status = "🔴 Κλειστό" if res.is_closed else "🟢 Ανοιχτό"
                print(f"🕒 {res.time} | Τραπέζι {res.table_id} | {res.customer_name} | {status}")
                found = True
        
        if not found:
            print(f"📭 Καμία κράτηση για {target_date}.")

    def tips_process(self):
        # 1. Βρίσκουμε τον τρέχοντα μήνα (π.χ. "2026-02")
        current_month = datetime.now().strftime("%Y-%m")
        
        print(f"\n📊 --- ΜΗΝΙΑΙΑ ΑΝΑΦΟΡΑ ({current_month}) ---")
        
        monthly_tips = 0.0
        count = 0
        
        # 2. Αθροίζουμε ΜΟΝΟ τις κρατήσεις αυτού του μήνα που έχουν κλείσει
        for res in self.reservations:
            if res.is_closed and res.date_closed and res.date_closed.startswith(current_month):
                monthly_tips += res.tips
                count += 1
        
        if count == 0:
            print(f"❌ Δεν βρέθηκαν κλεισμένες κρατήσεις για τον μήνα {current_month}.")
            return

        # 3. Υπολογισμοί Ποσοστών
        waiterA = monthly_tips * 0.5
        waiterB = monthly_tips * 0.2
        kitchen = monthly_tips * 0.2
        lantza = monthly_tips * 0.1

        # 4. Εμφάνιση στην Οθόνη
        print(f"✅ Βρέθηκαν {count} κρατήσεις.")
        print(f"💵 ΣΥΝΟΛΟ ΜΗΝΑ: {monthly_tips}€")
        print("-" * 30)
        print(f"👤 Σερβιτόρος Α: {waiterA}€")
        print(f"👤 Σερβιτόρος Β: {waiterB}€")
        print(f"👨‍🍳 Κουζίνα:      {kitchen}€")
        print(f"🧼 Λάντζα:       {lantza}€")

        # 5. ΔΗΜΙΟΥΡΓΙΑ ΑΡΧΕΙΟΥ (REPORT)
        filename = f"report_{current_month}.txt"
        
        with open(filename, "w", encoding="utf-8") as f:
            f.write(f"=== ΜΗΝΙΑΙΑ ΑΝΑΦΟΡΑ: {current_month} ===\n")
            f.write(f"Σύνολο Κρατήσεων: {count}\n")
            f.write(f"ΣΥΝΟΛΙΚΑ TIPS:    {monthly_tips}€\n")
            f.write("-" * 30 + "\n")
            f.write(f"Σερβιτόρος Α:     {waiterA}€\n")
            f.write(f"Σερβιτόρος Β:     {waiterB}€\n")
            f.write(f"Κουζίνα:          {kitchen}€\n")
            f.write(f"Λάντζα:           {lantza}€\n")
            f.write("-" * 30 + "\n")
            f.write(f"Εκδόθηκε στις: {datetime.now().strftime('%Y-%m-%d %H:%M')}\n")

        print(f"\n✅ Το αρχείο '{filename}' δημιουργήθηκε επιτυχώς!")
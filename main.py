from models import Restaurant_manager
from datetime import datetime
import sys

manager = Restaurant_manager()

print("🍽️  TAVERNA MANAGER APP v2.0 (Dates Supported) 🍽️")

while True:
    print("\n-------------------------")
    print("1️⃣  Νέα Κράτηση")
    print("2️⃣  Προβολή Προγράμματος (ανά ημέρα)")
    print("3️⃣  Πληρωμή & Tips")
    print("4️⃣  Ταμείο Μήνα & Έξοδος")
    print("-------------------------")
    
    choice = input("👉 Επίλεξε (1-4): ")

    if choice == "1":
        print("\n📝 --- ΝΕΑ ΚΡΑΤΗΣΗ ---")
        name = input("Όνομα Πελάτη: ")
        
        # --- ΗΜΕΡΟΛΟΓΙΟ ---
        today_str = datetime.now().strftime("%Y-%m-%d")
        print(f"Ημερομηνία (Πάτα Enter για ΣΗΜΕΡΑ: {today_str})")
        date_input = input("ή γράψε άλλη (π.χ. 2026-02-15): ")
        
        # Αν πατήσει Enter (κενό), βάζουμε τη σημερινή
        if date_input.strip() == "":
            res_date = today_str
        else:
            res_date = date_input

        try:
            people = int(input("Αριθμός Ατόμων: "))
            table = int(input("Τραπέζι: "))
        except ValueError:
            print("❌ Λάθος! Πρέπει να δώσεις αριθμό.")
            continue
            
        time = input("Ώρα (π.χ. 21:00): ")
        notes = input("Σημειώσεις: ")
        
        # Περνάμε και την ημερομηνία πλέον!
        manager.add_reservation(name, people, res_date, time, table, notes)

    elif choice == "2":
        # Ζητάμε ημερομηνία για να δείξουμε το πρόγραμμα
        today_str = datetime.now().strftime("%Y-%m-%d")
        print(f"\nΓια ποια μέρα θες πρόγραμμα; (Enter για ΣΗΜΕΡΑ: {today_str})")
        target_date = input("Ημερομηνία: ")
        
        if target_date.strip() == "":
            target_date = today_str
            
        manager.show_daily_schedule(target_date)

    elif choice == "3":
        print("\n💸 --- ΠΛΗΡΩΜΗ ---")
        search = input("Δώσε όνομα πελάτη: ")
        res = manager.find_reservation_by_name(search)
        
        if res:
            print(f"✅ Βρέθηκε: {res.customer_name} ({res.res_date})")
            try:
                amount = float(input("Tips: "))
                res.add_tips(amount)
                manager.save_to_db() # Σώνουμε την αλλαγή
            except:
                print("❌ Λάθος ποσό.")
        else:
            print("❌ Δεν βρέθηκε.")

    elif choice == "4":
        manager.tips_process()
        print("👋 Bye!")
        break
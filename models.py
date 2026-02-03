class Reservation:
    def __init__(self,customer_name,people_count,time,table_id,notes="") : 
        self.customer_name = customer_name
        self.people_count = people_count
        self.time = time
        self.table_id = table_id
        self.notes = notes


        self.tips = 0.0
        self.is_closed = False

    def add_tips(self,amount):#Προσθέτει φιλοδώρημα στην κράτηση
        if amount > 0:
            self.tips += amount
        self.is_closed = True
        print(f"Το τραπέζι του/της {self.customer_name} έχει κλείσει με φιλοδώρημα: {self.tips}")


class Restaurant_manager:
    def __init__(self):
        self.reservations = []

    def add_reservation(self,customer_name,people_count,time,table_id,notes=""):
        reservation = Reservation(customer_name,people_count,time,table_id,notes)#Δημιουργει αντικειμενο τυπου Reservation
        self.reservations.append(reservation)#To prosθέτει στη λίστα κρατήσεων
        print(f"Προστέθηκε κράτηση για τον/την {customer_name} στο τραπέζι {table_id}.")

    def show_daily_schedule(self):
        print("== ΚΡΑΤΗΣΕΙΣ ΗΜΕΡΑΣ ==")
        if len(self.reservations) == 0:
            print("Δεν υπάρχουν κρατήσεις για σήμερα.")
        else:
            for reservation in self.reservations:
             print(f"Ωρα: {reservation.time}, Πελάτης: {reservation.customer_name}, Άτομα: {reservation.people_count}, Τραπέζι: {reservation.table_id}, Σημειώσεις: {reservation.notes}, Κλειστό: {reservation.is_closed}, Φιλοδώρημα: {reservation.tips}")

    def find_reservation_by_name(self,name_query):
        for reservation in self.reservations:
           if name_query in reservation.customer_name:
                return reservation
        return None
    
    def tips_process(self):
        # 1. Πρώτα κάνουμε τους υπολογισμούς
        total_tips = 0.0
        for reservation in self.reservations:
            total_tips += reservation.tips
            
        waiterA_share = total_tips * 0.5
        waiterB_share = total_tips * 0.2
        kitchen_share = total_tips * 0.2
        lantza_share = total_tips * 0.1

        # 2. Εμφάνιση στην Οθόνη (για να βλέπεις τι γίνεται τώρα)
        print("\n--- ΑΠΟΤΕΛΕΣΜΑΤΑ (ΟΘΟΝΗ) ---")
        print(f"Συνολικά: {total_tips}€")
        print(f"Σερβιτόρος Α: {waiterA_share}€")
        # ... κλπ (τυπώνει στην κονσόλα)

        # 3. Αποθήκευση στο Αρχείο (Disk)
        # Το 'w' σημαίνει ότι σβήνει τα παλιά και γράφει νέο αρχείο
        with open("tips_report.txt", "w", encoding="utf-8") as file:
            file.write("=== ΤΑΜΕΙΟ ΗΜΕΡΑΣ ===\n") # Το \n αλλάζει γραμμή
            file.write(f"Συνολικά φιλοδώρημα: {total_tips}€\n")
            file.write("-" * 20 + "\n")
            file.write(f"Μερίδιο σερβιτόρου Α: {waiterA_share}€\n")
            file.write(f"Μερίδιο σερβιτόρου Β: {waiterB_share}€\n")
            file.write(f"Μερίδιο κουζίνας:     {kitchen_share}€\n")
            file.write(f"Μερίδιο λάντζας:      {lantza_share}€\n")
            
        print("✅ Η αναφορά αποθηκεύτηκε επιτυχώς στο αρχείο 'tips_report.txt'")
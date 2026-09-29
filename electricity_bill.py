import csv 
from datetime import datetime 
 
 
# List to store previous bills 
bill_history = [] 
 
 
def get_positive_number(message): 
    while True: 
        try: 
            value = float(input(message)) 
 
            if value > 0: 
                return value 
            else: 
                print("Please enter a value greater than 0.") 
 
        except ValueError: 
            print("Invalid input! Please enter a number.") 
 
 
def get_positive_integer(message): 
    while True: 
        try: 
            value = int(input(message)) 
 
            if value > 0: 
                return value 
            else: 
                print("Please enter a number greater than 0.") 
 
        except ValueError: 
            print("Invalid input! Please enter a whole number.") 

def select_category():
    while True:
        print("\n") 
        print("╔════════════════════════════════════════════════════════════════╗") 
        print("║                      INDUSTRIAL CATEGORY                       ║") 
        print("╠════════════════════════════════════════════════════════════════╣") 
        print("║                                                                ║") 
        print("║  1. Small Industry                                             ║") 
        print("║  2. Medium Industry                                            ║") 
        print("║  3. Large Industry                                             ║") 
        print("║                                                                ║") 
        print("╚════════════════════════════════════════════════════════════════╝") 
 
 
        choice = input("Select industry category: ") 
 
        if choice == "1": 
            return "Small Industry", 6, 2000 
 
        elif choice == "2": 
            return "Medium Industry", 7, 5000 
 
        elif choice == "3": 
            return "Large Industry", 8, 10000 
 
        else: 
            print("Invalid choice! Please select 1, 2 or 3.") 
 
 
def calculate_energy_charge(units, rate): 
 
    if units <= 1000: 
        energy_charge = units * rate 
 
    elif units <= 5000: 
        energy_charge = (1000 * rate) + ((units - 1000) * (rate + 1)) 
 
    else: 
        energy_charge = (1000 * rate) + (4000 * (rate + 1)) + \
                        ((units - 5000) * (rate + 2)) 
        return energy_charge 
 
def save_bill_history(bill): 
    with open("bill_history.csv", "a", newline="", encoding="utf-8") as file:
        writer = csv.writer(file) 
 
        writer.writerow([ 
            bill["bill_number"], 
            bill["industry_name"], 
            bill["category"], 
            bill["units"], 
            bill["total_bill"], 
            bill["date"] 
        ]) 
def generate_bill_number(): 
    if len(bill_history) == 0: 
        return "IND0001" 
 
    return "IND" + str(len(bill_history) + 1).zfill(4)         
def calculate_bill(): 
    print("\n") 
    print("╔══════════════════════════════════════════════╗") 
    print("║           ELECTRICITY BILL CALCULATOR        ║") 
    print("╠══════════════════════════════════════════════╣") 
    print("║              ENTER INDUSTRY DETAILS          ║") 
    print("╚══════════════════════════════════════════════╝") 
     
 
    print("\n========== BILL CALCULATION ==========") 
 
    industry_name = input("Enter industry name: ") 
 
    category, rate, fixed_charges = select_category() 
 
    power = get_positive_number( 
        "Enter power consumption (kW): " 
    ) 
 
    hours = get_positive_number( 
        "Enter operating hours per day: " 
    ) 
 
    days = get_positive_integer( 
        "Enter number of operating days: " 
    ) 
 
    tax_rate = get_positive_number( 
        "Enter tax/surcharge (%): " 
    ) 
 
    # Calculate units 
    units = power * hours * days 
 
    # Calculate energy charges 
    energy_charges = calculate_energy_charge(units, rate) 
 
    # Calculate subtotal 
    subtotal = energy_charges + fixed_charges 
 
    # Calculate tax 
    tax = subtotal * tax_rate / 100 
 
    # Calculate final bill 
    total_bill = subtotal + tax 
 
    # Bill number 
    bill_number = generate_bill_number() 
    # Date and time 
    date_time = datetime.now().strftime("%d-%m-%Y %I:%M %p") 
 
    # Store bill in history 
    bill = { 
        "bill_number": bill_number, 
        "industry_name": industry_name, 
        "category": category, 
        "units": units, 
        "total_bill": total_bill, 
        "date": date_time 
    } 
 
    bill_history.append(bill) 
    save_bill_history(bill) 
    save_bill_receipt(bill) 
    # Display bill 
    print("\n") 
    print("=" * 60) 
    print("             INDUSTRIAL ELECTRICITY BILL") 
    print("=" * 60) 
    print("\n") 
    print("╔════════════════════════════════════════════════════════╗") 
    print("║                  ELECTRICITY BILL                      ║") 
    print("╠════════════════════════════════════════════════════════╣") 
    print("║                                                        ║") 
 
    print(f"║  Bill Number       : {bill_number:<34} ║") 
    print(f"║  Date & Time       : {date_time:<34} ║") 
    print(f"║  Industry Name     : {industry_name:<34} ║") 
    print(f"║  Industry Category : {category:<34} ║") 
 
    print("║                                                        ║") 
 
    print(f"║  Units Consumed    : {str(round(units, 2)) + ' kWh':<34} ║") 
    print(f"║  Energy Charges    : {'₹ ' + str(round(energy_charges, 2)):<34} ║") 
    print(f"║  Fixed Charges     : {'₹ ' + str(round(fixed_charges, 2)):<34} ║") 
    print(f"║  Tax / Surcharge   : {'₹ ' + str(round(tax, 2)):<34} ║") 
 
    print("║                                                        ║") 
 
    print(f"║  TOTAL BILL        : {'₹ ' + str(round(total_bill, 2)):<34} ║") 
 
    print("║                                                        ║") 
    print("╚════════════════════════════════════════════════════════╝") 
    print("-" * 60) 
    print("                 CONSUMPTION DETAILS") 
    print("-" * 60) 
 
    print("Power Consumption :", power, "kW") 
    print("Operating Hours   :", hours, "hours/day") 
    print("Operating Days    :", days, "days") 
    print("Total Units       :", units, "kWh") 
 
    print("-" * 60) 
    print("                    BILL DETAILS") 
    print("-" * 60) 
 
    print("Applicable Rate   : ₹", rate, "per unit") 
    print("Energy Charges    : ₹", round(energy_charges, 2)) 
    print("Fixed Charges     : ₹", round(fixed_charges, 2)) 
    print("Tax/Surcharge     : ₹", round(tax, 2)) 
 
    print("-" * 60) 
    print("TOTAL BILL        : ₹", round(total_bill, 2)) 
    print("=" * 60) 
 
def view_bill_history(): 
    print("\n") 
    print("╔══════════════════════════════════════════════╗") 
    print("║                 BILL HISTORY                 ║") 
    print("╚══════════════════════════════════════════════╝") 
 
    if len(bill_history) == 0: 
        print("No bills have been generated yet.") 
        return 
 
    industry_search = input("Enter Industry Name: ") 
 
    found = False 
 
    for bill in bill_history: 
        if bill["industry_name"].lower() == industry_search.lower(): 
 
            print("\n----------------------------------------") 
            print("Bill Number :", bill["bill_number"]) 
            print("Industry    :", bill["industry_name"]) 
            print("Category    :", bill["category"]) 
            print("Units       :", bill["units"], "kWh") 
            print("Total Bill  : ₹", round(bill["total_bill"], 2)) 
            print("Date        :", bill["date"]) 
            print("----------------------------------------") 
 
            found = True 
 
    if not found: 
        print("No bills found for this industry.") 
    
def consumption_analysis(): 
    print("\n") 
    print("╔══════════════════════════════════════════════╗") 
    print("║              CONSUMPTION ANALYSIS            ║") 
    print("╚══════════════════════════════════════════════╝") 
     
    
 
    if len(bill_history) == 0: 
        print("No bills available for analysis :(") 
        return 
 
    industry_search = input("Enter Industry Name: ") 
 
    total_units = 0 
    total_bill = 0 
    number_of_bills = 0 
    category = "" 
 
    for bill in bill_history: 
        if bill["industry_name"].lower() == industry_search.lower(): 
            total_units += bill["units"] 
            total_bill += bill["total_bill"] 
            number_of_bills += 1 
            category = bill["category"] 
 
    if number_of_bills == 0: 
        print("No bills found for this industry.") 
        return 
 
    average_units = total_units / number_of_bills 
    average_bill = total_bill / number_of_bills 
 
    print("\n----------------------------------------") 
    print("Industry        :", industry_search) 
    print("Category        :", category) 
    print("Number of Bills :", number_of_bills) 
    print("Total Units     :", round(total_units, 2), "kWh") 
    print("Average Units   :", round(average_units, 2), "kWh") 
    print("Total Billing   : ₹", round(total_bill, 2)) 
    print("Average Bill    : ₹", round(average_bill, 2)) 
    print("----------------------------------------") 
 
 
def search_bill(): 
    print("\n") 
    print("╔══════════════════════════════════════════════╗") 
    print("║                   SEARCH BILL                ║") 
    print("╚══════════════════════════════════════════════╝") 
     
     
 
    search_number = input("Enter Bill Number: ") 
 
    found = False 
 
    for bill in bill_history: 
        if  bill["bill_number"].upper() == search_number.upper(): 
            print("\n----------------------------------------") 
            print("Bill Number :", bill["bill_number"]) 
            print("Industry    :", bill["industry_name"]) 
            print("Category    :", bill["category"]) 
            print("Units       :", bill["units"], "kWh") 
            print("Total Bill  : ₹", round(bill["total_bill"], 2)) 
            print("Date        :", bill["date"]) 
            print("----------------------------------------") 
 
            found = True 
            break 
 
    if not found: 
        print("Bill not found!") 
def save_bill_receipt(bill): 
    filename = bill["bill_number"] + ".txt" 
 
    with open(filename, "w", encoding="utf-8") as file:
        file.write("========================================\n") 
        file.write("       INDUSTRIAL ELECTRICITY BILL\n") 
        file.write("========================================\n\n") 
 
        file.write("Bill Number : " + bill["bill_number"] + "\n") 
        file.write("Date        : " + bill["date"] + "\n") 
        file.write("Industry    : " + bill["industry_name"] + "\n") 
        file.write("Category    : " + bill["category"] + "\n") 
        file.write("Units       : " + str(bill["units"]) + " kWh\n") 
        file.write("Total Bill  : ₹" + str(round(bill["total_bill"], 2)) + "\n") 
 
        file.write("\n========================================\n") 
        file.write("             THANK YOU!\n") 
        file.write("========================================\n") 
 
    print("\nReceipt saved successfully!") 
    print("File Name:", filename)         
def load_bill_history(): 
    try: 
        with open("bill_history.csv", "r", encoding="utf-8") as file: 
            reader = csv.reader(file) 
 
            for row in reader: 
                if len(row) == 6: 
                    bill = { 
                        "bill_number": row[0], 
                        "industry_name": row[1], 
                        "category": row[2], 
                        "units": float(row[3]), 
                        "total_bill": float(row[4]), 
                        "date": row[5] 
                    } 
                    bill_history.append(bill) 
 
    except FileNotFoundError: 
        pass 
# MAIN MENU 
load_bill_history() 
 
while True: 
    print("\n") 
    print("╔══════════════════════════════════════════════╗") 
    print("║        INDUSTRIAL ELECTRICITY SYSTEM         ║") 
    print("╠══════════════════════════════════════════════╣") 
    print("║                                              ║") 
    print("║  1. Calculate Electricity Bill               ║") 
    print("║  2. View Bill History                        ║") 
    print("║  3. Search Bill                              ║") 
    print("║  4. Consumption Analysis                     ║") 
    print("║  5. Exit                                     ║") 
    print("║                                              ║") 
    print("╚══════════════════════════════════════════════╝") 
 
    choice = input("Enter your choice: ") 
 
    if choice == "1": 
        calculate_bill() 
 
    elif choice == "2": 
        view_bill_history() 
 
    elif choice == "3": 
        search_bill() 
 
    elif choice == "4": 
        consumption_analysis() 
 
    elif choice == "5": 
        print("\n") 
        print("╔══════════════════════════════════════════════╗") 
        print("║                                              ║") 
        print("║           SYSTEM CLOSED SUCCESSFULLY         ║") 
        print("║                                              ║") 
        print("║        Thank you for using the system:)      ║") 
        print("║                                              ║") 
        print("╚══════════════════════════════════════════════╝") 
        break 
 
    else: 
        print("Invalid choice!") 
 


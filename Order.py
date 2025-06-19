users = {}
selected_lang = "en"
global_cart = []
global_total = 0.0
delivery_fee = 30.0

# 🗣️ Messages
languages = {
    "en": {
        "welcome": "Welcome to Your Needs!",
        "login_signup": "Do you want to (1) Login or (2) Sign Up?",
        "enter_username": "Enter your username:",
        "enter_password": "Enter your password:",
        "signup_success": "Signup successful! Please login.",
        "login_success": "Login successful!",
        "invalid_credentials": "Invalid credentials. Try again.",
        "choose_language": "Choose language:\n1. English\n2. Arabic",
        "choose_category": "Choose category:\n1. Food\n2. Groceries\n3. Pharmacy",
        "invalid_choice": "Invalid choice. Please try again.",
        "choose_restaurant": "Choose a restaurant:",
        "menu_list": "Menu List:",
        "choose_item": "Choose item number to add to cart (or type 'done' to finish): ",
        "item_added": "Added to cart:",
        "groceries_list": "Groceries List:",
        "choose_disease": "Choose your disease:",
        "medicine_list": "Medicine List:",
        "receipt": "Receipt",
        "total_price": "Total Price (without delivery):",
        "delivery_fee": "Delivery Fee:",
        "final_total": "Final Total (including delivery):",
        "enter_address": "Enter your delivery address: ",
        "thank_you": "Thank you {username} for your order!",
        "estimated_time": "Estimated delivery time: 30-45 minutes",
        "another_order": "Do you want to make another order? (yes/no): "
    },
    "ar": {
        "welcome": "مرحبًا بك في احتياجاتك!",
        "login_signup": "هل تريد (1) تسجيل الدخول أم (2) إنشاء حساب؟",
        "enter_username": "ادخل اسم المستخدم:",
        "enter_password": "ادخل كلمة المرور:",
        "signup_success": "تم إنشاء الحساب بنجاح! يرجى تسجيل الدخول.",
        "login_success": "تم تسجيل الدخول بنجاح!",
        "invalid_credentials": "بيانات اعتماد غير صالحة. حاول مرة أخرى.",
        "choose_language": "اختر اللغة:\n1. الإنجليزية\n2. العربية",
        "choose_category": "اختر الفئة:\n1. طعام\n2. بقالة\n3. صيدلية",
        "invalid_choice": "خيار غير صالح. حاول مرة أخرى.",
        "choose_restaurant": "اختر مطعمًا:",
        "menu_list": "قائمة الطعام:",
        "choose_item": "اختر رقم العنصر للإضافة إلى السلة (أو اكتب 'تم' للإنهاء): ",
        "item_added": "تمت الإضافة إلى السلة:",
        "groceries_list": "قائمة البقالة:",
        "choose_disease": "اختر حالتك المرضية:",
        "medicine_list": "قائمة الأدوية:",
        "receipt": "الإيصال",
        "total_price": "السعر الإجمالي (بدون التوصيل):",
        "delivery_fee": "رسوم التوصيل:",
        "final_total": "السعر النهائي (بما في ذلك التوصيل):",
        "enter_address": "ادخل عنوان التوصيل: ",
        "thank_you": "شكرًا لك {username} على طلبك!",
        "estimated_time": "وقت التوصيل المتوقع: 30-45 دقيقة",
        "another_order": "هل تريد تقديم طلب آخر؟ (نعم/لا): "
    }
}

# 🏪 Translations
restaurant_names_ar = {
    "KFC": "كنتاكي",
    "McDonald's": "ماكدونالدز",
    "Pizza Hut": "بيتزا هت",
    "Burger King": "برجر كينج",
    "Hardee's": "هارديز",
    "Papa John's": "بابا جونز",
    "Subway": "صب واي",
    "Domino's": "دومينوز",
    "Cook Door": "كوك دور",
    "Buffalo Burger": "بافلو برجر"
}

grocery_names_ar = {
    "Dairy": "منتجات الألبان",
    "Fruits": "الفواكه",
    "Vegetables": "الخضروات"
}

pharmacy_names_ar = {
    "Headache": "صداع",
    "Cold": "برد",
    "Allergy": "حساسية",
    "Diabetes": "سكري"
}

def translate(key):
    return languages[selected_lang][key]

# 🧱 Data builder
def format_item(en, ar):
    return ar if selected_lang == "ar" else en

restaurant_data = {
    "KFC": [("Zinger", "زنجر", 70.0), ("Twister", "توستر", 60.0)],
    "McDonald's": [("Big Mac", "بيج ماك", 75.0), ("McChicken", "ماك تشيكن", 65.0)],
    "Pizza Hut": [("Margherita", "مارغريتا", 80.0), ("Pepperoni", "بيبروني", 90.0)],
    "Burger King": [("Whopper", "وابر", 85.0), ("Chicken Royale", "تشكن رويال", 70.0)],
    "Hardee's": [("Thickburger", "ثيك برجر", 95.0), ("Crispy Chicken", "تشكن مقرمش", 60.0)],
    "Papa John's": [("Cheese Pizza", "بيتزا جبنة", 80.0), ("Super Papa", "سوبر بابا", 95.0)],
    "Subway": [("Chicken Teriyaki", "ترياكي دجاج", 60.0), ("Tuna", "تونة", 55.0)],
    "Domino's": [("Veggie Pizza", "بيتزا خضار", 75.0), ("Pepperoni Pizza", "بيتزا بيبروني", 90.0)],
    "Cook Door": [("Fajita", "فاهيتا", 65.0), ("Chicken Ranch", "تشكن رانش", 70.0)],
    "Buffalo Burger": [("Buffalo Classic", "كلاسيك بافلو", 80.0), ("Firestorm", "فايرستورم", 85.0)],
}

grocery_data = {
    "Dairy": [("Milk", "لبن", 20.0), ("Cheese", "جبنة", 30.0), ("Yogurt", "زبادي", 10.0)],
    "Fruits": [("Apple", "تفاح", 10.0), ("Banana", "موز", 8.0), ("Orange", "برتقال", 9.0)],
    "Vegetables": [("Tomato", "طماطم", 6.0), ("Cucumber", "خيار", 5.0), ("Potato", "بطاطس", 7.0)],
}

pharmacy_data = {
    "Headache": [("Panadol", "بنادول", 15.0), ("Adol", "أدول", 12.0)],
    "Cold": [("Flurest", "فلورست", 20.0), ("Actifed", "أكتيفيد", 18.0)],
    "Allergy": [("Claritin", "كلاريتين", 25.0), ("Zyrtec", "زيرتك", 22.0)],
    "Diabetes": [("Insulin", "إنسولين", 100.0), ("Glucophage", "جلوكوفاج", 50.0)],
}

restaurants = {}
groceries = {}
pharmacy = {}

def build_data():
    global restaurants, groceries, pharmacy
    restaurants = {
        rest: {format_item(en, ar): price for en, ar, price in items}
        for rest, items in restaurant_data.items()
    }
    groceries = {
        cat: {format_item(en, ar): price for en, ar, price in items}
        for cat, items in grocery_data.items()
    }
    pharmacy = {
        dis: {format_item(en, ar): price for en, ar, price in items}
        for dis, items in pharmacy_data.items()
    }

# 📲 User interaction
def choose_language():
    global selected_lang
    print("Choose language:\n1. English\n2. Arabic")
    lang = input("Enter 1 or 2: ").strip()
    selected_lang = "ar" if lang == '2' else "en"
    build_data()

def login_signup():
    print(translate("login_signup"))
    choice = input("Enter 1 or 2: ")
    username = input(translate("enter_username"))
    password = input(translate("enter_password"))
    if choice == '1':
        if users.get(username) == password:
            print(translate("login_success"))
            return username
        else:
            print(translate("invalid_credentials"))
            return login_signup()
    elif choice == '2':
        users[username] = password
        print(translate("signup_success"))
        return login_signup()
    else:
        print(translate("invalid_choice"))
        return login_signup()

def choose_category(username):
    global global_cart, global_total
    while True:
        print("\n" + translate("choose_category"))
        choice = input("Enter 1, 2 or 3: ").strip()
        if choice == '1':
            show_restaurants()
        elif choice == '2':
            show_groceries()
        elif choice == '3':
            show_pharmacy()
        else:
            print(translate("invalid_choice"))
            continue
        again = input(translate("another_order")).strip().lower()
        if again not in ["yes", "y", "نعم", "ن"]:
            break
    show_receipt(username)

def show_restaurants():
    global global_cart, global_total
    print("\n" + translate("choose_restaurant"))
    keys = list(restaurants.keys())
    for i, r in enumerate(keys, 1):
        name = restaurant_names_ar[r] if selected_lang == "ar" else r
        print(f"{i}. {name}")
    choice = input("Choose restaurant number: ").strip()
    if not choice.isdigit() or not (1 <= int(choice) <= len(keys)):
        print(translate("invalid_choice"))
        return show_restaurants()
    selected = keys[int(choice)-1]
    menu = restaurants[selected]
    print(translate("menu_list"))
    items = list(menu.items())
    for i, (item, price) in enumerate(items, 1):
        print(f"{i}. {item} - {price} L.E.")
    while True:
        inp = input(translate("choose_item")).strip().lower()
        if inp in ["done", "تم"]:
            break
        if inp.isdigit() and 1 <= int(inp) <= len(items):
            item, price = items[int(inp)-1]
            global_cart.append(item)
            global_total += price
            print(translate("item_added"), item)
        else:
            print(translate("invalid_choice"))

def show_groceries():
    global global_cart, global_total
    print("\n" + translate("groceries_list"))
    cats = list(groceries.keys())
    for i, cat in enumerate(cats, 1):
        name = grocery_names_ar[cat] if selected_lang == "ar" else cat
        print(f"{i}. {name}")
    choice = input("Enter category number: ").strip()
    if not choice.isdigit() or not (1 <= int(choice) <= len(cats)):
        return show_groceries()
    cat = cats[int(choice)-1]
    items = list(groceries[cat].items())
    for i, (item, price) in enumerate(items, 1):
        print(f"{i}. {item} - {price} L.E.")
    while True:
        inp = input(translate("choose_item")).strip().lower()
        if inp in ["done", "تم"]:
            break
        if inp.isdigit() and 1 <= int(inp) <= len(items):
            item, price = items[int(inp)-1]
            global_cart.append(item)
            global_total += price
            print(translate("item_added"), item)
        else:
            print(translate("invalid_choice"))

def show_pharmacy():
    global global_cart, global_total
    print("\n" + translate("medicine_list"))
    keys = list(pharmacy.keys())
    for i, dis in enumerate(keys, 1):
        name = pharmacy_names_ar[dis] if selected_lang == "ar" else dis
        print(f"{i}. {name}")
    choice = input("Enter disease number: ")
    if not choice.isdigit() or not (1 <= int(choice) <= len(keys)):
        return show_pharmacy()
    dis = keys[int(choice)-1]
    items = list(pharmacy[dis].items())
    for i, (item, price) in enumerate(items, 1):
        print(f"{i}. {item} - {price} L.E.")
    while True:
        inp = input(translate("choose_item")).strip().lower()
        if inp in ["done", "تم"]:
            break
        if inp.isdigit() and 1 <= int(inp) <= len(items):
            item, price = items[int(inp)-1]
            global_cart.append(item)
            global_total += price
            print(translate("item_added"), item)
        else:
            print(translate("invalid_choice"))

def show_receipt(username):
    print("\n" + translate("receipt"))
    for item in global_cart:
        print(f"- {item}")
    print(f"{translate('total_price')}: {global_total} L.E.")
    print(f"{translate('delivery_fee')}: {delivery_fee} L.E.")
    final = global_total + delivery_fee
    print(f"{translate('final_total')}: {final} L.E.")
    print(translate("thank_you").format(username=username))
    print(translate("estimated_time"))

# 🚀 Start
choose_language()
user = login_signup()
choose_category(user)

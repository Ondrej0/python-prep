#Task 1
def get_grade(score):
    if score >= 70:
        return "First"
    elif score >= 60:
        return "2:1"
    elif score >= 50:
        return "2:2"
    elif score >= 40:
        return "Third"
    else:
        return "Fail"

scores = [83, 67, 52, 44, 32]

for score in scores:
    print(f"{score}: {get_grade(score)}")

#Task 2
transactions = [120, -50, 300, -20, -100, 75, -25]


def analyse_transactions(transactions):
    analysed_transactions = []
    for transaction in transactions:
        if transaction < 0:
            analysed_transactions.append(abs(transaction))
    return analysed_transactions

print(analyse_transactions(transactions))

#Task 3
words = [
    "python",
    "java",
    "python",
    "spring",
    "java",
    "python",
    "react"
]

def count_words(words):
    word_count = {}
    for word in words:
        word_count[word] = word_count.get(word, 0) + 1
    return word_count

print(count_words(words))

#Task 4
def most_common(word_count):
    common_word = None
    common_word_count = 0

    for word, count in word_count.items():
        if count > common_word_count:
            common_word_count = count
            common_word = word

    return common_word


print(most_common(count_words(words)))

#Task 5
user_ids = [
    "U101",
    "U102",
    "U103",
    "U101",
    "U104",
    "U102",
    "U105"
]

def find_duplicates(ids):
    seen = set()
    duplicates = set()

    for id in ids:
        if id not in seen:
            seen.add(id)
        else:
            duplicates.add(id)

    return duplicates

print(find_duplicates(user_ids))

#Task 6
required_permissions = {
    "READ_ACCOUNT",
    "MAKE_PAYMENT",
    "VIEW_TRANSACTIONS"
}

user_permissions = {
    "READ_ACCOUNT",
    "VIEW_TRANSACTIONS",
    "CHANGE_PASSWORD"
}

def missing_permissions(required_permissions, user_permissions):
    return required_permissions - user_permissions

print(missing_permissions(required_permissions, user_permissions))

#Task 7
transactions = [
    ("Tesco", 45),
    ("Amazon", 120),
    ("Netflix", 15),
    ("Apple", 999),
    ("Gym", 30)
]

def large_transactions(transactions, limit):
    result = []

    for merchant, amount in transactions:
        if amount > limit:
            result.append(merchant)

    return result
print(large_transactions(transactions, 100))

#Task 8
accounts = ["ACC100", "ACC200", "ACC300", "ACC400"]

def find_account(accounts, target):
    for index, name in enumerate(accounts):
        if name == target:
            return index

print(find_account(accounts, "ACC300"))
print(find_account(accounts, "ACC999"))

#Task 9
usernames = [
    "  Ondrej ",
    "JAMES",
    " sarah",
    "ONDREJ",
    "  james  ",
    "",
    "   "
]

def clean_usernames(usernames):
    return list({
        username.strip().lower()
        for username in usernames
        if username.strip()
    })

print(clean_usernames(usernames))

#Task 10 / Task 11
class BankAccount:
    def __init__(self, username, balance):
        self.username = username
        self.balance = balance

    def deposit(self, amount):
        if amount <= 0:
            raise ValueError("Deposit amount must be positive")
        self.balance += amount

    def withdraw(self, amount):
        if amount <= 0:
            raise ValueError("Withdraw amount must be positive")
        elif amount > self.balance:
            raise ValueError("Insufficient funds")
        self.balance -= amount

account = BankAccount("Ondrej", 100)

try:
    account.withdraw(150)
except ValueError as error:
    print(error)

print(account.balance)

#Final test
users = [
    {"id": 1, "name": "  Ondrej ", "active": True},
    {"id": 2, "name": "JAMES", "active": False},
    {"id": 3, "name": " sarah", "active": True},
    {"id": 4, "name": "ONDREJ", "active": True},
    {"id": 5, "name": "", "active": True},
    {"id": 6, "name": "Lewis", "active": False}
]

def process_users(users):

    unique_users = {}

    for user in users:
        if not user["active"]:
            continue
        name = user["name"].strip().lower()
        if name:
            unique_users[name] = unique_users.get(name, 0) + 1

    return unique_users

print(process_users(users))
from pathlib import Path



BASE_DIR = Path(__file__).resolve().parent.parent






DB_PATH = BASE_DIR / "data" / "finance.db"




CATEGORY_KEYWORDS = {
    "food": ["zomato", "swiggy", "food", "dominos"],
    "study": ["book", "tuition", "exam", "school", "coaching"],
    "fashion": ["myntra", "ajio", "clothing", "zara", "pants", "shirt"],
    "hostel": ["hostel", "room rent", "pg", "accommodation"],
    "college": ["college", "university", "fee", "semester"],
    "bank": ["modification charges", "atm fee", "sms charge"],
    "cash_withdrawal": ["aeps", "atm", "cash", "cw", "withdraw"],
    "transfer": ["p2p", "p2v", "upi", "to", "from", "@", "imps", "rtgs"],
    "unknown": []  # fallback
}

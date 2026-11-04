"""Check a vet clinic's gross-ups and month in this repo's layout.

1. Every gross-up row reads across: gross billed - fee = net in bank, so the
   full bill is revenue and the fee is an expense.
2. Every loan payment splits exactly: interest + principal = payment. Only
   the interest is a cost; the principal pays the loan down.
3. The month file: profit is every "In profit" line added up. Lines kept out
   of profit (loan principal) are listed by account.

Usage: python3 check_vet_month.py gross-ups.csv loan-payments.csv september-2026-month.csv
Python 3, standard library only.
"""
import csv
import sys
from collections import defaultdict
from decimal import Decimal


def d(cell):
    return Decimal(cell.strip()) if cell and cell.strip() else Decimal("0")


def check_gross_ups(path):
    ok = True
    with open(path, newline="", encoding="utf-8") as f:
        for r in csv.DictReader(f):
            gross, fee, net = d(r["Gross billed"]), d(r["Fee"]), d(r["Net in bank"])
            rate = fee / gross * 100 if gross else Decimal("0")
            if gross - fee != net:
                ok = False
                print(f"{r['Deposit']}: {gross:,.2f} - {fee:,.2f} is {gross - fee:,.2f}, file says {net:,.2f}")
            else:
                print(f"{r['Deposit']}: revenue {gross:,.2f}, fee {fee:,.2f} ({rate:.1f}%), deposited {net:,.2f}")
    return ok


def check_loans(path):
    ok = True
    with open(path, newline="", encoding="utf-8") as f:
        for r in csv.DictReader(f):
            pay, interest, principal = d(r["Payment from bank"]), d(r["Interest"]), d(r["Principal"])
            if interest + principal != pay:
                ok = False
                print(f"{r['Date']} {r['Loan']}: interest + principal is {interest + principal:,.2f}, payment is {pay:,.2f}")
            else:
                print(f"{r['Date']} {r['Loan']}: payment {pay:,.2f} = interest {interest:,.2f} (expense) + principal {principal:,.2f} (loan)")
    return ok


def check_month(path):
    income = expenses = Decimal("0")
    held = defaultdict(Decimal)
    with open(path, newline="", encoding="utf-8") as f:
        for r in csv.DictReader(f):
            amt = d(r["Amount"])
            if r["In profit"].strip().lower() == "yes":
                if amt >= 0:
                    income += amt
                else:
                    expenses -= amt
            else:
                held[r["Account"]] += amt
    print(f"Revenue {income:,.2f}, expenses {expenses:,.2f}, profit {income - expenses:,.2f}")
    for acct, bal in held.items():
        print(f"Kept out of profit: {acct} {bal:,.2f}")


if __name__ == "__main__":
    args = sys.argv[1:] + [None] * 3
    ok = check_gross_ups(args[0] or "gross-ups.csv")
    ok = check_loans(args[1] or "loan-payments.csv") and ok
    check_month(args[2] or "september-2026-month.csv")
    print("All checks pass." if ok else "Some checks failed; see above.")
    sys.exit(0 if ok else 1)

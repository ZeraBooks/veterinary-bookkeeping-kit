# Veterinary practice bookkeeping kit

Bookkeeping for a veterinary practice keeps exam and service revenue apart
from pharmacy and food sales, books drug and supply costs apart from outside
lab fees, grosses card and patient financing deposits back up before their
fees, and splits each equipment loan payment into interest and principal. This
kit has the chart of accounts, a checklist and a worked month.

## Files

| File | What it is |
|---|---|
| `chart-of-accounts.csv` | A starting chart of accounts for a general practice: services and pharmacy as separate income, drugs, labs and cremation as separate costs, client deposits and equipment loans. Columns: Number, Name, Type, Detail, Notes. |
| `month-end-checklist.md` | Nine steps for closing a clinic's month, from grossing up deposits to locking the period. |
| `gross-ups.csv` | A fictional card batch and patient financing payout, each grossed back up to the full bill with the fee on its own column. |
| `loan-payments.csv` | A fictional equipment loan payment split into interest and principal. |
| `september-2026-month.csv` | The same fictional clinic's September 2026 on cash basis: every line, its account, and whether it counts in profit. |
| `check_vet_month.py` | Checks the gross-ups and the loan split and prints revenue, expenses and profit for the month. Python 3, standard library only. |

## How to use it

1. Import `chart-of-accounts.csv` into your accounting software, or compare it
   with the accounts you have. Specialty and emergency hospitals usually split
   service revenue further.
2. Each month, fill in copies of `gross-ups.csv` from the processor statement
   and financing payout reports, and `loan-payments.csv` from the lender
   statements.
3. Run the check:

   ```
   python3 check_vet_month.py gross-ups.csv loan-payments.csv september-2026-month.csv
   ```

4. Work through `month-end-checklist.md` before you lock the month.

## The worked month

Cedar Hollow Animal Clinic is a fictional two-vet general practice. September
2026, cash basis:

| | Amount |
|---|---|
| Exams and services | 61,200.00 |
| Pharmacy and food sales | 14,800.00 |
| Services paid through patient financing | 3,500.00 |
| **Revenue** | **79,500.00** |
| Card processor fees, 2.6% of 76,000.00 | 1,976.00 |
| Financing provider fee, 7% of 3,500.00 | 245.00 |
| Drugs and medical supplies | 18,940.00 |
| Reference lab invoices | 4,310.00 |
| Payroll, gross wages | 32,600.00 |
| Employer payroll taxes | 2,493.90 |
| Ultrasound loan interest | 412.50 |
| Rent | 6,800.00 |
| Cremation provider | 1,150.00 |
| **Expenses** | **68,927.40** |
| **Profit** | **10,572.60** |

The ultrasound payment was 1,992.50, but 1,580.00 of it was principal and went
against the loan, so only 412.50 is a cost. The financing deposit was
3,255.00; the 245.00 fee is shown on its own line so the service is still
revenue at its full price.

All figures are fictional.

## FAQ

### Is a vet clinic's bookkeeping the same as a human medical clinic's?

Partly. Payroll and equipment loans work the same. The difference is who pays:
most pet insurance reimburses the pet owner after the visit, so the clinic is
paid in full at checkout and has few insurance deposits to chase. The work is
in the card and cash deposits and in running a pharmacy.

### How do I record a patient financing deposit?

Book the full bill as service revenue and the provider's fee as an expense.
The deposit is the bill less the fee, so booking only the deposit makes every
financed visit look cheaper than it was.

### Is the whole equipment loan payment an expense?

No. Only the interest is. The principal pays the loan down, so it goes against
the equipment loan balance, and the equipment itself is depreciated.

## Learn more

Full guide: [Bookkeeping for veterinary practices](https://www.zerabooks.com/bookkeeping-for-veterinary-practices). Related: [ZeraBooks bookkeeping services](https://www.zerabooks.com/bookkeeping-services).

## License

The content and data in this repository are licensed under
[CC BY 4.0](LICENSE). Free to use and adapt with credit to ZeraBooks.
The code (`*.py`) is licensed under [MIT](LICENSE-CODE).

Maintained by [ZeraBooks](https://www.zerabooks.com).

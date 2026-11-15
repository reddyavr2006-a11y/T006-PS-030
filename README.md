# PS-030 - NPS Accumulation, Asset Allocation and Annuity Engine

## Overview

This project implements a simplified National Pension System (NPS) processing engine for handling contributions, asset allocation, withdrawals, exits, annuity calculations and taxation.

---

## Input Files

| File | Purpose |
|--------|----------|
| subscribers.csv | Subscriber master data |
| navs.csv | Daily NAV values |
| holidays.csv | Business holidays |
| glidepath.csv | AUTO allocation rules |
| annuity_rates.csv | Annuity lookup rates |
| commands.txt | Transaction commands |

---

## How To Run

```bash
python src/main.py
```

---

## Output Files

| Output File | Description |
|------------|-------------|
| transactions.csv | Contribution transactions |
| holdings.csv | Current holdings |
| exits.csv | Exit calculations |
| tax_lines.csv | Tax records |
| rebalances.csv | Rebalancing records |

---

## Business Rules Implemented

| Rule | Description |
|--------|------------|
| BR-01 | Contribution Minimums |
| BR-02 | POP Charges |
| BR-03 | NAV & Unit Allocation |
| BR-04 | Active Allocation Validation |
| BR-05 | Auto Allocation Lookup |
| BR-06 | Rebalancing Tolerance |
| BR-07 | Partial Withdrawal Validation |
| BR-08 | Superannuation Exit |
| BR-09 | Premature Exit |
| BR-10 | Annuity Calculation |
| BR-11 | Tax Processing |
| BR-12 | Exit Precedence |

---

## Command Format

| Command | Arguments |
|----------|------------|
| `CONTRIBUTE` | txn_id, subscriber_id, tier, received_at, type, amount |
| `CHANGE_ALLOCATION` | subscriber_id, date, E, C, G, A |
| `PARTIAL_WITHDRAW` | subscriber_id, date, amount, purpose |
| `WITHDRAW_TIER2` | subscriber_id, date, amount |
| `UNFREEZE` | subscriber_id, date, amount |
| `EXIT` | subscriber_id, date, type, annuity_option, annuity_pct |
| `RUN_TO` | date |

---

## Test Suite

Run:

```bash
python -m pytest
```

Current Status:

```text
6 tests passing
```

---

## Project Structure

```text
src/
tests/
README.md
Decision_Log.md
```

---

## Original Project Brief


# PS-030 – NPS Accumulation, Asset Allocation and Annuity Engine — Sample Data Pack

Prepared by 10 SECONDS for Team T006.

## Files

| File | What it holds | Row count |
|---|---|---|
| `navs.csv` | Daily NAV per scheme (E, C, G, A) for every business day 2021-10-01 … 2026-10-31 | 5172 |
| `holidays.csv` | Market/business holidays (Saturday and Sunday are non-business days too) | 33 |
| `glide_paths.csv` | AUTO-choice glide path: target E/C/G % by completed age for LC75, LC50, LC25 (ages 18–75) | 174 |
| `annuity_rates.csv` | Annuity rate per Rs 1,000 of purchase price per year, by completed age at exit and option | 123 |
| `subscribers.csv` | 12 NPS subscribers with DOB, join date, tiers, allocation mode / lifecycle fund, nominee and monthly basic | 12 |
| `commands.txt` | Contributions (≈300), allocation changes, partial withdrawals, Tier II withdrawal, unfreeze, exits, RUN_TO and print commands | 311 |

Row count for `commands.txt` = command lines (comment lines starting with `#` and blank lines are not counted).

## Column reference

### subscribers.csv
| column | type | notes |
|---|---|---|
| subscriber_id | `SUB-001` … | |
| pran | 12 digits | fake PRAN |
| name, gender | string | |
| dob | date | completed age = full years on the date in question; birthday rebalances happen on the dob anniversary (29 Feb → 1 Mar in non-leap years) |
| join_date | date | account opening; partial-withdrawal and premature-exit clocks start here |
| tier_i, tier_ii | boolean | which tiers exist |
| allocation_mode | `ACTIVE` / `AUTO` | |
| lifecycle_fund | `LC75` / `LC50` / `LC25` / `NA` | AUTO only |
| active_e_pct … active_a_pct | number or `NA` | initial ACTIVE percentages (sum 100) |
| nominee_name, nominee_relation | string | |
| basic_salary_monthly | money | for the employer 10%-of-basic taxability test |
| mobile | 10 digits | |

### navs.csv — `date, scheme (E/C/G/A), nav (4 decimals)`, one row per scheme per business day. No rows on weekends/holidays.
### holidays.csv — `date, name`.
### glide_paths.csv — `fund, age, e_pct, c_pct, g_pct` (target by completed age; constant below 35 and above 55).
### annuity_rates.csv — `age, option (LIFE / LIFE_WITH_ROP / JOINT_LIFE), rate_per_1000_per_year` (annual annuity per Rs 1,000 purchase price).

### commands.txt — see below. Money in Rs (2 decimals), percentages plain numbers, timestamps IST.

## Command file format

One command per line, `COMMAND|arg1|...`, strictly in file order. `#` lines are comments. Automatic events (birthday rebalance, quarter-end custodian recovery, 1-April Tier-I minimum check, CRA unit redemption at the next NAV) are not commands: run all of them dated before a command's date before applying that command; `RUN_TO|date` flushes them to the given date.

| command | arguments | meaning |
|---|---|---|
| `CONTRIBUTE` | `txn_id`, `subscriber_id`, `tier` (I/II), `received_at`, `type` (EMPLOYEE/EMPLOYER/VOLUNTARY), `amount` | funds received; NAV date = received date if business day and before 09:30:00, else next business day |
| `CHANGE_ALLOCATION` | `subscriber_id`, `date`, `E`, `C`, `G`, `A` | ACTIVE allocation change (counts toward the 4 per financial year, Apr–Mar); invalid changes are rejected and do not count |
| `PARTIAL_WITHDRAW` | `subscriber_id`, `date`, `amount`, `purpose` | Tier I partial withdrawal; purpose must be one of CHILD_EDUCATION, CHILD_MARRIAGE, HOUSE_PURCHASE, MEDICAL, SKILL_DEVELOPMENT, STARTUP |
| `WITHDRAW_TIER2` | `subscriber_id`, `date`, `amount` | Tier II redemption, FIFO lots, capital-gains reporting |
| `UNFREEZE` | `subscriber_id`, `date`, `amount` | pays the Rs 100 charge plus arrears (shortfall to Rs 1,000) |
| `EXIT` | `subscriber_id`, `date`, `type` (SUPERANNUATION/PREMATURE/DEATH), `annuity_option`, `annuity_pct` | annuity_pct = % of corpus to annuity requested by the subscriber (engine enforces the minimum; 0 means 'all lump sum if allowed') |
| `RUN_TO` | `date` | process automatic events up to and including `date` |
| `PRINT_HOLDING` | `subscriber_id`, `date` | holding statement |
| `PRINT_TRANSACTIONS` | `subscriber_id`, `from_date`, `to_date` | transaction statement |

Conventions: units truncated to 4 decimals; CRA and custodian charges are redeemed pro-rata by value across schemes; rebalancing deviation compared after rounding to 2 decimals.

## Planted scenarios

Locators below are physical line numbers of the named file (a CSV header is line 1; comment lines in commands.txt count).

Edge cases from the brief (one bullet per edge case, in brief order):

- **Contribution received at 09:30:00 exactly** — SUB-001: CON at line 248 received 2026-04-15 09:29:59 → NAV of 2026-04-15; CON at line 249 received 2026-04-15 09:30:00 → not 'before 09:30' → NAV of the next business day 2026-04-16. Also line 250 (Saturday 2026-04-18 → NAV of Mon 2026-04-20) and line 284 (holiday 2026-10-02 → NAV of Mon 2026-10-05).
- **Tier I contributions summing to Rs 999 in a financial year** — SUB-005: FY 2024-25 has exactly two Tier I contributions, 500.00 (line 120, 2024-06-10) and 499.00 (line 156, 2025-01-20) = 999.00 → account frozen from 2025-04-01. CONTRIBUTE 2000.00 on 2025-05-12 (line 180) must be rejected while frozen; UNFREEZE on 2025-06-16 for 101.00 (line 185) = Rs 100 charge + Rs 1 arrears (shortfall to the Rs 1,000 minimum) lifts the freeze.
- **ACTIVE E at exactly 75% on the 50th birthday** — SUB-001 (DOB 1976-03-15): CHANGE_ALLOCATION 75/15/10/0 dated 2026-03-15, the 50th birthday (line 241) → allowed (max 75% 'up to age 50'). SUB-002 (DOB 1975-01-20, age 51) asks 75% on 2026-03-20 (line 244) → rejected (max 72.5 at 51); the corrected 72.5/15/7.5/5 on 2026-03-21 (line 245) → allowed.
- **Rebalancing where one scheme deviates by exactly 1.0 point** — SUB-004 (AUTO LC50, DOB 1990-06-10, age 35 at join): single contribution 100000.00 at line 188 received 2025-07-01 09:00 → POP 500.00, invested 99500.00 split 50/30/20 at the 2025-07-01 NAVs E 12.4375 / C 14.9250 / G 19.9000 (navs.csv lines 3814–3816) → units E 4000.0000, C 2000.0000, G 1000.0000. On the 36th birthday 2026-06-10 the NAVs are E 12.2500 / C 14.5000 / G 22.0000 (lines 4774–4776) → values 49000 / 29000 / 22000 = 49.00% / 29.00% / 22.00% against the age-36 LC50 target 48 / 29 / 23 → E deviates +1.0 point exactly (rebalance; not 'less than 1'), C 0.0 (skip), G −1.0 (rebalance). CRA and custodian redemptions are pro-rata by value, so they do not disturb the weights; compare deviations rounded to 2 decimals.
- **Partial withdrawal on the 3-year anniversary** — SUB-006 (joined 2023-08-14): PARTIAL_WITHDRAW 25000.00 on 2026-08-13 (line 275) → rejected (one day short); the same request on 2026-08-14 (line 276) → allowed if ≤ 25% of own contributions (employee contributions to date: check against the CONTRIBUTE lines for SUB-006).
- **Corpus of exactly Rs 5,00,000 at age 60** — SUB-007 (DOB 1966-09-21, ACTIVE 0/100/0/0): single VOLUNTARY contribution 490001.27 at line 264 (2026-07-01 09:05, business day) → POP 2450.01, invested 487551.26 at C NAV 14.6000 (navs.csv line 4835) → 33393.9219 units; CRA 3.75 redeemed at the next NAV 14.5781 (2026-07-02, line 4839) → 0.2572 units; EXIT SUPERANNUATION on the 60th birthday 2026-09-21 (line 283) at C NAV 14.9729 (line 5063) → corpus (33393.9219 − 0.2572) × 14.9729 = 500000.00 exactly → 100% lump sum allowed (corpus ≤ 5 lakh). Convention: the threshold corpus is units × NAV on the exit date before the quarter-end custodian recovery (the Sep-2026 quarter has not ended).
- **Fifth ACTIVE allocation change in a financial year** — SUB-003: CHANGE_ALLOCATION on 2025-05-10, 2025-07-10, 2025-10-10, 2026-01-12 (lines 178, 191, 208, 224) are the 4 allowed changes of FY 2025-26; the 5th on 2026-03-02 (line 236) must be rejected.
- **Exit on 60th birthday vs the day before** — SUB-008 (DOB 1966-10-05): EXIT SUPERANNUATION on 2026-10-04 (line 285) is one day before the 60th birthday → rejected (not eligible as superannuation; the command is not converted to a premature exit); EXIT on 2026-10-05 (line 286) → processed: LIFE_WITH_ROP with 40% annuity, 60% lump sum, GST 1.8% on the purchase price, rate for completed age 60 from annuity_rates.csv.

Extra traps:

- Duplicate CONTRIBUTE: line 112 repeats the previous line verbatim (same txn_id) → reject. Line 257: Tier I contribution of 499.00 (below the Rs 500 minimum) → reject. Line 163: ACTIVE change with A = 7% (> 5% cap) → reject. Line 204: PARTIAL_WITHDRAW with purpose VACATION (not in the allowed list) → reject.
- SUB-002 partial withdrawals on 2024-11-20, 2025-06-18, 2026-02-11 (lines 148, 186, 233) use up the 3 lifetime withdrawals; the 4th on 2026-09-16 (line 281) must be rejected.
- SUB-010: EMPLOYER contributions of 6000.00 per quarter-month against basic 50000.00 (12% > 10%) → 1000.00 of each employer contribution is taxable in that FY and must appear as a tax line. SUB-009 WITHDRAW_TIER2 40000.00 on 2026-03-10 (line 239) consumes Tier II lots FIFO: lots older than 36 months at LTCG 12.5%, younger lots at slab 30% — the lot bought 2023-04-18 is 35 months old on that date.
- SUB-011 EXIT DEATH on 2026-05-20 (line 260) → 100% to nominee, no annuity; SUB-012 EXIT PREMATURE on 2026-10-06 (line 288) after 5 years with a corpus below 2.5 lakh → 100% lump sum even though annuity_option LIFE was supplied. Quarter-end custodian recoveries fall on 31 Mar / 30 Jun / 30 Sep / 31 Dec (use the last business day's NAV when the date is a non-business day).


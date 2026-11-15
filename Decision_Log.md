Decision Log
PS-030 – NPS Accumulation, Asset Allocation and Annuity Engine
1
Chosen a modular architecture to separate contribution, allocation, withdrawal, exit, and tax processing.

2
Used dedicated loader functions for each master file to improve maintainability.

3
Selected CSV-based storage because all project inputs are provided as CSV files.

4
Implemented POP charge deduction before unit allocation to comply with BR-02.

5
Used NAV-based allocation calculations rather than fixed investment allocation values.

6
Implemented business-day validation to support NAV cut-off processing.

7
Separated ACTIVE and AUTO allocation logic due to different validation requirements.

8
Used glide-path lookup tables instead of hardcoding lifecycle fund allocations.

9
Implemented rebalancing tolerance as a separate function to simplify testing.

10
Created withdrawal validation functions independently for rule verification.

11
Separated superannuation and premature exit calculations because they have different annuity requirements.

12
Implemented annuity-rate lookup using annuity_rates.csv rather than fixed assumptions.

13
Created a shared utility module for reusable calculations.

14
Used command-driven processing because all transactions originate from commands.txt.

15
Stored transaction records before generating CSV outputs.

16
Implemented dedicated output managers for output-file generation.

17
Chose business-rule functions to improve clarity during viva demonstrations.

18
Implemented explicit validation for edge cases identified in the project brief.

19
Used evaluator-specified output column structures wherever possible.

20
Prioritized business-rule implementation before integration of final outputs.
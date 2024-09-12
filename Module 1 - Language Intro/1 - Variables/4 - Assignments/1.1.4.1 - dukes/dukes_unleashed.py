"""
For investments over $1M it can be typically assumed that they will return 5% forever.
Using the [2022 - 2023 JMU Cost of Attendance](https://www.jmu.edu/financialaid/learn/cost-of-attendance-undergrad.shtml),
calculate how much a rich alumnus would have to give to pay for one full year (all costs) for an in-state student
and an out-of-state student. Store your final answer in the variables: "in_state_gift" and "out_state_gift".

Note: this problem does not require the "compounding interest" formula from the previous problem.

"""

### Your code here ###
tuition_in = 30792
tuition_out = 47882
interest = .05

in_state_gift = tuition_in/interest

out_state_gift = tuition_out/interest

print ("The amount an alumni would need to invest to cover in state tuition for one student is",in_state_gift, "and", out_state_gift, "for out of state tuition")
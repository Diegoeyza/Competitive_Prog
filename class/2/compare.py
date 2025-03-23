output1 = '''Case 1: 4014
Case 2: 4908
Case 3: 1520597
Case 4: 766020
Case 5: 39967
Case 6: 9819207
Case 7: 753
Case 8: 40535
Case 9: 79043
Case 10: 1693
Case 11: 4242301
Case 12: 1536200
Case 13: 227423
Case 14: 24720
Case 15: 53409
Case 16: 971
Case 17: 2407249
Case 18: 13379892
Case 19: 15209
Case 20: 28151174
Case 21: 407817
Case 22: 3626
Case 23: 2137
Case 24: 654946971
Case 25: 53127
Case 26: 198485
Case 27: 10139
Case 28: 158841
Case 29: 6668
Case 30: 3560
Case 31: 14534
Case 32: 480383
Case 33: 265492
Case 34: 1129342
Case 35: 97659386
Case 36: 33077
Case 37: 54264
Case 38: 174023800
Case 39: 13886906
Case 40: 285766871
Case 41: 55766088
Case 42: 548813
Case 43: 354189
Case 44: 9140648
Case 45: 45751
Case 46: 109242505
Case 47: 6830
Case 48: 2084
Case 49: 84285
Case 50: 486592
'''
output2 = '''Case 1: 4014
Case 2: 4908
Case 3: 1520597
Case 4: 766020
Case 5: 39967
Case 6: 9819207
Case 7: 753
Case 8: 40535
Case 9: 79043
Case 10: 1693
Case 11: 4242301
Case 12: 1536200
Case 13: 227423
Case 14: 24720
Case 15: 53409
Case 16: 971
Case 17: 2407249
Case 18: 13379892
Case 19: 15209
Case 20: 28151174
Case 21: 407817
Case 22: 3626
Case 23: 2137
Case 24: 654946971
Case 25: 53127
Case 26: 198485
Case 27: 10139
Case 28: 158841
Case 29: 6668
Case 30: 3560
Case 31: 14534
Case 32: 480383
Case 33: 265492
Case 34: 1129342
Case 35: 97659386
Case 36: 33077
Case 37: 54264
Case 38: 174023800
Case 39: 13886906
Case 40: 285766871
Case 41: 55766088
Case 42: 548813
Case 43: 354189
Case 44: 9140648
Case 45: 45751
Case 46: 109242505
Case 47: 6830
Case 48: 2084
Case 49: 84285
Case 50: 486592
'''

# Convert both outputs into lists of tuples (case_number, value)
output1_lines = output1.strip().split('\n')
output2_lines = output2.strip().split('\n')

# Compare the values
comparison_results = []
for line1, line2 in zip(output1_lines, output2_lines):
    case1, value1 = line1.split(": ")
    case2, value2 = line2.split(": ")
    
    # Compare the case values
    if value1 == value2:
        comparison_results.append(f"Case {case1}: Equal")
    else:
        comparison_results.append(f"Case {case1}: Different ({value1} vs {value2})")

# Print results
for result in comparison_results:
    print(result)

import pandas as pd
from apyori import apriori


# Importing the dataset
store_data = pd.read_csv('store_data.csv', header=None)


# Data Preprocessing
# The Apriori library requires the dataset to be in the form of a list of lists.
records = []
for i in range(0, 7501):
    records.append([str(store_data.values[i,j]) for j in range(0, 20)])


# Applying Apriori
# Support = 35/7500 = 0.0045, min_confidence = 0.2 or 20%.
association_rules = apriori(records, min_support=0.0045, min_confidence=0.2, min_lift=3, min_length=2)
association_results = list(association_rules)  # Convert to a list since it is easier to view the results in this form.


# Viewing the Results
print("No. mined rules: ", len(association_results))  # total number of rules mined
print(f'{association_results[0]}\n')  # first rule (general complex form)


# Display the rule, support, confidence, and lift for each rule in a more clear way:
for item in association_results:

    # first index of the inner list
    # Contains base item and add item
    pair = item[0]
    items = [x for x in pair]
    print("Rule: " + items[0] + " --→ " + items[1])

    # second index of the inner list
    print("Support: " + str(item[1]))

    # third index of the list located at 0th
    # of the third index of the inner list

    print("Confidence: " + str(item[2][0][2]))
    print("Lift: " + str(item[2][0][3]))
    print("\n=====================================\n")

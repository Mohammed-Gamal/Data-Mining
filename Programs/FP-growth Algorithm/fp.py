import pandas as pd
from mlxtend.preprocessing import TransactionEncoder
from mlxtend.frequent_patterns import fpgrowth, association_rules

dataset = [['Milk', 'Onion', 'Nutmeg', 'Diapers', 'Eggs', 'Yogurt'],
           ['Dill', 'Onion', 'Nutmeg', 'Diapers', 'Eggs', 'Yogurt'],
           ['Milk', 'Apple', 'Diapers', 'Eggs'],
           ['Milk', 'Unicorn', 'Corn', 'Diapers', 'Yogurt'],
           ['Corn', 'Onion', 'Onion', 'Diapers', 'Ice cream', 'Eggs']]


# Initializing the transaction encoder
te = TransactionEncoder()
te_ary = te.fit(dataset).transform(dataset)
df = pd.DataFrame(te_ary, columns=te.columns_)
print(df)

# Apply FP-growth algorithm
fp = fpgrowth(df, min_support=0.6, use_colnames=True)  # 'use_colnames=True' to convert into the respective item names
print(fp, end='\n\n\n')


# Extracting association rules
res = association_rules(fp, min_threshold=1)
print(res)



import pandas as pd
from dateutil import parser
import matplotlib.pyplot as plt
import numpy as np
import seaborn as sn

dataset = pd.read_csv('Dataset/appdata10.csv')



# Exploratory Data Analysis (EDA)
# Here I am starting with some basic exploration of the dataset.  
# I’ll check the first few rows, get a statistical summary, and also extract the hour information from the timestamp.

dataset.head(10) 
dataset.describe() 
dataset["hour"] = dataset.hour.str.slice(1, 3).astype(int)


dataset2 = dataset.copy().drop(columns = ['user', 'screen_list', 'enrolled_date',
                                           'first_open', 'enrolled'])
print(dataset2.head())



# Plotting Distributions and Correlations
# Now I want to visually understand the data.  
# First, I’ll make histograms for each numerical column.  
# Then, I’ll check correlation of features with the target (enrolled) and also create a heatmap for overall correlation.

plt.suptitle('Histograms of Numerical Columns', fontsize=20)
for i in range(1, dataset2.shape[1] + 1):
    plt.subplot(3, 3, i)
    f = plt.gca()
    f.set_title(dataset2.columns.values[i - 1])
    vals = np.size(dataset2.iloc[:, i - 1].unique())
    plt.hist(dataset2.iloc[:, i - 1], bins=vals, color='#3F5D7D')
plt.tight_layout(rect=[0, 0.03, 1, 0.95])
plt.show() 


dataset2.corrwith(dataset.enrolled).plot.bar(figsize=(20,10),
                  title = 'Correlation with Response variable',
                  fontsize = 15, rot = 45,
                  grid = True)


sn.set(style="white", font_scale=2)
corr = dataset2.corr()
mask = np.zeros_like(corr, dtype=bool)
mask[np.triu_indices_from(mask)] = True
f, ax = plt.subplots(figsize=(18, 15))
f.suptitle("Correlation Matrix", fontsize=40)
cmap = sn.diverging_palette(220, 10, as_cmap=True)
sn.heatmap(corr, mask=mask, cmap=cmap, vmax=.3, center=0,
           square=True, linewidths=.5, cbar_kws={"shrink": .5})

plt.show()



# Feature Engineering (Dates and Time Differences)
# Next, I’ll work with the date and time columns.  
# I’ll convert them into proper datetime format, then calculate the time difference between first_open and enrollment.  
# If this difference is more than 48 hours, I’ll assume the user is not enrolled.

dataset.dtypes
dataset["first_open"] = [parser.parse(row_date) for row_date in dataset["first_open"]]
dataset["enrolled_date"] = [parser.parse(row_date) if isinstance(row_date, str) else row_date for row_date in dataset["enrolled_date"]]
dataset.dtypes

dataset["difference"] = (dataset.enrolled_date - dataset.first_open) / pd.Timedelta(hours=1)

response_hist = plt.hist(dataset["difference"].dropna(), color='#3F5D7D')
plt.title('Distribution of Time-Since-Screen-Reached')
plt.show()
plt.hist(dataset["difference"].dropna(), color='#3F5D7D', range = [0, 100])
plt.title('Distribution of Time-Since-Screen-Reached')
plt.show()
dataset.loc[dataset.difference > 48, 'enrolled'] = 0
dataset = dataset.drop(columns=['enrolled_date', 'difference', 'first_open'])



# Feature Engineering (Screens and Aggregation)
# Here I want to transform the screen_list column.  
# I’ll use the list of top screens and create new binary columns for each.  
# Whatever is left over, I’ll keep track of it with an "Other" feature.

top_screens = pd.read_csv('Dataset/top_screens.csv').top_screens.values
top_screens

dataset["screen_list"] = dataset.screen_list.astype(str) + ','
for sc in top_screens:
    dataset[sc] = dataset.screen_list.str.contains(sc).astype(int)
    dataset['screen_list'] = dataset.screen_list.str.replace(sc+",", "")
dataset['Other'] = dataset.screen_list.str.count(",")
dataset = dataset.drop(columns=['screen_list'])



# Funnel Features (Grouped Screen Categories)
# To make analysis easier, I’m grouping related screens into funnels.  
# For example: Savings screens will be combined into "SavingCount".  
# I do the same for Credit, CC, and Loan related screens and then drop the originals.

savings_screens = ["Saving1",
                    "Saving2",
                    "Saving2Amount",
                    "Saving4",
                    "Saving5",
                    "Saving6",
                    "Saving7",
                    "Saving8",
                    "Saving9",
                    "Saving10"]
dataset["SavingCount"] = dataset[savings_screens].sum(axis=1)
dataset = dataset.drop(columns=savings_screens)

cm_screens = ["Credit1",
               "Credit2",
               "Credit3",
               "Credit3Container",
               "Credit3Dashboard"]
dataset["CMCount"] = dataset[cm_screens].sum(axis=1)
dataset = dataset.drop(columns=cm_screens)

cc_screens = ["CC1",
                "CC1Category",
                "CC3"]
dataset["CCCount"] = dataset[cc_screens].sum(axis=1)
dataset = dataset.drop(columns=cc_screens)

loan_screens = ["Loan",
               "Loan2",
               "Loan3",
               "Loan4"]
dataset["LoansCount"] = dataset[loan_screens].sum(axis=1)
dataset = dataset.drop(columns=loan_screens)

dataset.head()
dataset.describe()
dataset.columns

# Saving Processed Dataset
# Finally, after cleaning and feature engineering, I’ll save the processed dataset into a new CSV file.

dataset.to_csv('new_appdata10.csv', index = False)


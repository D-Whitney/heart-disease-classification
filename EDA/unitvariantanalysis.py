#%%
import pandas as pd 
import seaborn as sns

#%%
df = pd.read_csv('../heart.csv')
feature_dict = {
    'age': 'numerical',
    'sex': 'categorical', 
    'cp': 'categorical', 
    'trestbps': 'numerical', 
    'chol': 'numerical', 
    'fbs': 'categorical', 
    'restecg': 'categorical', 
    'thalach': 'numerical',
    'exang': 'categorical', 
    'oldpeak': 'numerical', 
    'slope': 'categorical', 
    'ca': 'categorical', 
    'thal': 'categorical', 
    'target': 'categorical'
}
feature_df = pd.DataFrame(feature_dict, index=['feature_type']).T

df.describe()
sns.boxplot(data=df, y="trestbps", x="target")
# filtering out trestbps values over 182 (3 standard deviations above mean)
# %%

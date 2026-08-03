import pandas as pd
import numpy as np
from sklearn.preprocessing import (
    LabelEncoder,
    OneHotEncoder,
    StandardScaler,
    MinMaxScaler,
    RobustScaler
)


#HANDLE MISSING VALUES 
def fill_mising(df,column,method="mean",value = None):
    """"fill missing values in a column
        * method
        * mean
        * meadian
        * mode
        * constant
    """
    df=df.copy()
    if column not in df.columns:
        return df
    if method=="mean":
        if pd.api.types.is_numeric_dtype(df[column]):
            df[column] = df[column].fillna(df[column].mean())
    elif method == "meadian":
        if pd.api.types.is_numeric_dtype(df[column]):
            df[column] = df[column].fillna(df[column].median())
    elif method == "mode":
         mode = df[column].mode()
         if len(mode) > 0:
              df[column]==df[column].fillna(mode[0])
    elif method == "constant":
        df[column]== df[column].fillna(value)
    return df    

# REMOVE ROWS
def remove_missing_rows(df):
    df = df.copy()
    return df.dropna()

#REMOVE COLUMNS
def remove_missing_column(df):
    df = df.copy()
    return df.dropna(axis = 1) 

#REMOVE SELECTED COLUMN
def drop_columns(df,columns):
    df = df.copy()
    return df.drop(columns=columns)

#REMOVE DUPLICATE 
def remove_duplicates(df):
    df = df.copy()
    return df.drop_duplicates()

# RENAME COLUMN
def rename_column(df,old_name,new_name):
    df = df.copy()
    if old_name not in df.columns:
        return df
    return df.rename(
        columns = {
            old_name == new_name
        }
    )

#CHANGE DATATYPE
def convert_datatype(df,column,datatype):
    df = df.copy()
    try:
        if datatype == "int":
            df[column] = df[column].astype(int)
        elif datatype == "float":
            df[column] = df[column].astype(float)
        elif datatype == "str":
            df[column] = df[column].astype(str)
        elif datatype == "bool":
            df[column] = df[column].astype(bool)
        elif datatype == "datetime":
            df[column] = pd.to_datetime(df[column])
    except Exception:
        pass
    return df

#REPLACE VALUE
def replace_values(df,column,old_value,new_value):
    df[column] = df[column].replace(old_value,new_value)
    return df

#REMOVE NEGATIVE FUNCTION 
def remove_negative_values(df,column):
    df = df.copy()
    if pd.api.types.is_numeric_dtype(df[column]):
        df= df[df[column]>=0]
        return df 
    
# REMOVE EMPTY STRINGS
def remove_empty_string(df):
    df = df.copy()
    df.replace("",np.nan ,inplace = True) 
    return df   

#trim spaces
def trim_spaces(df):
    df = df.copy()
    for col in df.select_dtypes(include = "objects"):
        df[col] = df[col].str.strip()
    return df

#LOWER TEXT
def lowercase_columns(df):
    df = df.copy()
    object_cols = df.select_dtypes(include="object").columns
    for col in object_cols:
        df[col] = df[col].str.lower()
    return df

#UPPERCASE TEXT
def uppercase_columns(df):
    df = df.copy()
    object_cols = df.select_dtypes(include="object").columns
    for col in object_cols:
        df[col] = df[col].str.upper()
    return df

#TITLECASE FUNCTION
def titlecase_columns(df):
    df = df.copy()
    object_cols = df.select_dtypes(include="object").columns
    for col in object_cols:
        df[col] = df[col].str.title()
    return df

#RESET INDEX
def reset_index(df):
    return  df.reset_index(drop = True)

#SHORT VALUES    (by default asc short karta hai )
def short_dataframe(df,columns,ascending = True):
    return df.short_values(
        by = columns,
        ascending = ascending
    )

# FILTER ROWS
def filter_rows(df,column,value):
    return df[df[column]== value]

#label encoder  (only for string)
def lable_encoder(df,columns):
    df =df.copy()
    encoder =  LabelEncoder()
    for col in columns:
        if col in df.columns:
            df[col]=encoder.fit_transform(
                df[col].astype(str)
            )
    return df

#One Hot Encoder
def OneHotEncoder(df,columns):
    df = df.copy()
    df = pd.get_dummies(
        df,
        columns = columns,
        drop_first = False
    )
    return df

#standard scaler
def standard_scale(df,columns):
    scaler = StandardScaler()
    df[columns]= scaler.fit_transform(df[columns])
    return df

#minmax sacler
def standard_scale(df,columns):
    scaler = MinMaxScaler()
    df[columns]= scaler.fit_transform(df[columns])
    return df

#robust sacler
def standard_scale(df,columns):
    scaler = RobustScaler()
    df[columns]= scaler.fit_transform(df[columns])
    return df

#fill all numeric
def fill_all_numerical():
    df=df.copy()
    numeric =df.select_dtypes(include = np.number).columns
    for col in numeric:
        df[col]=df[col].fillna(df[col].mean())
    return df

#fill all categoric
def fill_all_categorical(df):
    categorical = df.select_dtypes(include=["object","category"]).columns
    for col in categorical:
            mode = df[col].mode()
            if len(mode)>0:
                df[col]=df[col].fillna(mode[0])
    return df

#PIPELINE
def preprocess_dataset(df):
    df=remove_duplicates(df)
    df=remove_empty_string(df)
    df = fill_all_numerical(df)
    df = fill_all_categorical(df)
    df = reset_index(df)

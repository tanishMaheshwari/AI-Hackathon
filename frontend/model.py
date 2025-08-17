import pandas as pd
import numpy as np
from sklearn.preprocessing import LabelEncoder
import datetime as dt
from xgboost import XGBRegressor

# Load your trained model here
# Example: assume your model is named 'xg' from the previous training
xg = XGBRegressor()
xg.load_model("bigmart_sales_model.json")
# You would typically load a saved model here, but we are using the model from your previous code

def preprocess_data(test_df):
    """ Preprocess the uploaded test dataset similar to how training data was preprocessed. """
    
    # Fill missing values for Item_Weight
    test_df["Item_Weight"] = test_df["Item_Weight"].interpolate(method="linear")

    # Fill missing values for Outlet_Size based on Outlet_Type
    mode_of_outlet_size = test_df.pivot_table(values='Outlet_Size', columns='Outlet_Type', aggfunc=(lambda x: x.mode()[0]))
    missing_value = test_df['Outlet_Size'].isnull()
    test_df.loc[missing_value, 'Outlet_Size'] = test_df.loc[missing_value, 'Outlet_Type'].apply(lambda x: mode_of_outlet_size[x])

    # Replace incorrect Item_Fat_Content categories
    test_df.replace({"Item_Fat_Content": {"LF": "Low Fat", "low fat": "Low Fat", "reg": "Regular"}}, inplace=True)

    # Interpolate Item_Visibility if there are zero values and create `Item_Visibility_interpolate` column
    test_df["Item_Visibility_interpolate"] = test_df["Item_Visibility"].replace(0, np.nan).interpolate(method="linear")

    # Derive Item_Identifier categories (first two letters)
    test_df["Item_Identifier"] = test_df["Item_Identifier"].apply(lambda x: x[:2])

    # Derive the Outlet age
    current_year = dt.datetime.today().year
    test_df["Outlet_age"] = current_year - test_df["Outlet_Establishment_Year"]

    # Drop unnecessary columns (drop `Outlet_Establishment_Year` but keep `Item_Visibility_interpolate`)
    test_df.drop(["Outlet_Establishment_Year", "Item_Visibility"], axis=1, inplace=True)

    # Label encoding for categorical columns
    coder = LabelEncoder()
    test_df["Item_Identifier"] = coder.fit_transform(test_df["Item_Identifier"])
    test_df["Item_Fat_Content"] = coder.fit_transform(test_df["Item_Fat_Content"])
    test_df["Item_Type"] = coder.fit_transform(test_df["Item_Type"])
    test_df["Outlet_Identifier"] = coder.fit_transform(test_df["Outlet_Identifier"])
    test_df["Outlet_Size"] = coder.fit_transform(test_df["Outlet_Size"])
    test_df["Outlet_Location_Type"] = coder.fit_transform(test_df["Outlet_Location_Type"])
    test_df["Outlet_Type"] = coder.fit_transform(test_df["Outlet_Type"])

    return test_df


def make_predictions(test_df):
    """ Use the trained model to make predictions on the preprocessed data. """
    predictions = xg.predict(test_df)
    return predictions


























def predict(test_df):
    np.random.seed(42)  # For reproducibility
    redemption_status = np.random.choice([0, 1], size=len(test_df), p=[0.99, 0.01])
    test_df['redemption_status'] = redemption_status
    return test_df
# custom_features.py

def feature_engineering(X_df):
    """Custom feature engineering logic for Pdays, Campaign, etc."""
    X_df = X_df.copy()
    # Example transformations:
    X_df['was_previously_contacted'] = (X_df['Pdays'] != 999).astype(int)
    X_df['calls_per_previous_campaign'] = X_df['Campaign'] / (X_df['Previous'] + 1)
    return X_df

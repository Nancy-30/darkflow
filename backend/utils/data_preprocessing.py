import pandas as pd
from sklearn.preprocessing import MinMaxScaler, StandardScaler
from sklearn.decomposition import PCA

def data_preprocessing(df, exclude_columns=None):
    if exclude_columns is None:
        exclude_columns = []

    def min_max_normalization(df, exclude_columns):
        numeric_cols = df.select_dtypes(include=["number"]).columns.difference(
            exclude_columns
        )
        scaler = MinMaxScaler()
        df[numeric_cols] = scaler.fit_transform(df[numeric_cols])
        return df

    def standardize(df, exclude_columns):
        if exclude_columns is None:
            exclude_columns = []

        numeric_cols = df.select_dtypes(include=["number"]).columns.difference(
            exclude_columns
        )
        scaler = StandardScaler()
        df[numeric_cols] = scaler.fit_transform(df[numeric_cols])
        return df

    def manage_null_values(df):
        numeric_cols = df.select_dtypes(include=["number"]).columns
        for col in numeric_cols:
            df[col].fillna(df[col].mean(), inplace=True)

        non_numeric_cols = df.select_dtypes(exclude=["number"]).columns
        for col in non_numeric_cols:
            df[col].fillna("Unknown", inplace=True)

        return df

    def pca_feature_reduction(df, variance_threshold=0.95):
        numeric_cols = df.select_dtypes(include=["number"]).columns
        x = df[numeric_cols].values

        # Standardize the data
        scaler = StandardScaler()
        X_scaled = scaler.fit_transform(x)

        # Apply PCA
        pca = PCA()
        pca.fit(X_scaled)
        explained_variance_ratio = pca.explained_variance_ratio_
        cumulative_explained_variance = explained_variance_ratio.cumsum()

        # Determine number of components
        n_components = (cumulative_explained_variance <= variance_threshold).sum() + 1
        pca = PCA(n_components=n_components)
        X_pca = pca.fit_transform(X_scaled)
        pca_df = pd.DataFrame(X_pca, columns=[f"PC{i+1}" for i in range(n_components)])

        return pca_df

    # Apply preprocessing steps
    df = manage_null_values(df)
    df = min_max_normalization(df, exclude_columns)
    df = pca_feature_reduction(df)

    return df

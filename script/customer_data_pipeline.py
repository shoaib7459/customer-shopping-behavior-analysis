# -----------------------------
# 1. Import Required Libraries
# -----------------------------

import os
import logging
import pandas as pd
import numpy as np
from sqlalchemy import create_engine


# -----------------------------
# 2. Configuration Variables
# -----------------------------

LOG_DIR = "../logs"
LOG_FILE_PATH = os.path.join(LOG_DIR, "pipeline.log")

DATA_FILE_PATH = "../data/customer_shopping_behavior.csv"

DATABASE_URL = "mysql+mysqlconnector://root@localhost:3306/project"
TABLE_NAME = "clean_customer_data"


# -----------------------------
# 3. Logger Configuration
# -----------------------------

os.makedirs(LOG_DIR, exist_ok=True)

logging.basicConfig(
    filename=LOG_FILE_PATH,
    level=logging.INFO,
    format="%(asctime)s | %(levelname)s | %(message)s"
)

logger = logging.getLogger(__name__)
logger.info("=" * 40)
logger.info("DATA PIPELINE STARTED")
logger.info("=" * 40)


# -----------------------------
# 4. Load Data
# -----------------------------

def load_data(file_path: str) -> pd.DataFrame:
    """
    Load raw customer data from CSV file.

    Parameters
    ----------
    file_path : str
        Path to the CSV file.

    Returns
    -------
    pd.DataFrame
        Loaded dataset.
    """
    logger.info('Loading Raw Data')
    try:
        df = pd.read_csv(file_path)
        logger.info(f"Data loaded successfully | Shape: {df.shape}")
        logger.info("=" * 40)
        logger.info("Initial Data Preview")
        logger.info("=" * 40)
        logger.info(f"Initial Preview: {df.head(10)}")
        return df

    except Exception as exc:
        logger.error(f"Failed to load data: {exc}")
        raise


# -----------------------------
# 5. Clean Column Names
# -----------------------------

def clean_data(df: pd.DataFrame, rename_columns: dict[str, str] | None = None) -> pd.DataFrame:
    """
    Standardize and clean column names.

    - Removes leading/trailing spaces
    - Converts to lowercase
    - Replaces spaces with underscores
    - Optionally renames specific columns

    Parameters
    ----------
    df : pd.DataFrame
        Input DataFrame.
    rename_columns : dict, optional
        Mapping of old column names to new ones.

    Returns
    -------
    pd.DataFrame
        Cleaned DataFrame.
    """
    logger.info('Data Cleaning Started')
    try:
        original_columns = df.columns.tolist()

        df.columns = (
            df.columns
            .str.strip()
            .str.lower()
            .str.replace(" ", "_")
        )

        if rename_columns:
            df.rename(columns=rename_columns, inplace=True)

        logger.info("Column cleaning completed")
        logger.info(f"Before: {original_columns}")
        logger.info(f"After : {df.columns.tolist()}")

        return df

    except Exception as exc:
        logger.error(f"Error during column cleaning: {exc}")
        raise


# -----------------------------
# 6. Handle Missing Values
# -----------------------------

def handle_missing_values(df: pd.DataFrame) -> pd.DataFrame:
    """
    Handle missing values using appropriate strategies.

    Strategy:
    ---------
    - review_rating: median imputation by category
    - numeric columns: median imputation
    - categorical columns: mode imputation

    Parameters
    ----------
    df : pd.DataFrame
        Input DataFrame with potential missing values.

    Returns
    -------
    pd.DataFrame
        DataFrame with missing values handled.
    """
    try:
        # ---- review_rating: category-wise median ----
        before = df["review_rating"].isna().sum()

        df["review_rating"] = (
            df.groupby("category")["review_rating"]
            .transform(lambda x: x.fillna(x.median()))
        )

        after = df["review_rating"].isna().sum()
        logger.info(
            f"review_rating nulls - Before: {before}, After: {after}"
        )

        # ---- Numeric columns: median imputation ----
        numeric_cols = df.select_dtypes(include=["int64", "float64"]).columns
        numeric_cols = numeric_cols.drop("review_rating", errors="ignore")

        if df[numeric_cols].isnull().any().any():
            df[numeric_cols] = df[numeric_cols].fillna(
                df[numeric_cols].median()
            )
            logger.info(
                f"Filled missing values in numeric columns: {list(numeric_cols)}"
            )

        # ---- Categorical columns: mode imputation ----
        categorical_cols = df.select_dtypes(include=["object"]).columns

        for col in categorical_cols:
            if df[col].isnull().any():
                mode_value = df[col].mode()
                if not mode_value.empty:
                    df[col] = df[col].fillna(mode_value[0])
                    logger.info(
                        f"Filled missing values in categorical column: {col}"
                    )

        logger.info("Missing values handled successfully")
        return df

    except Exception as exc:
        logger.error(f"Missing value handling failed: {exc}")
        raise


# -----------------------------
# 7. Feature Engineering
# -----------------------------

def create_age_group(df: pd.DataFrame) -> pd.DataFrame:
    """
    Create age_group feature based on age column.

    Age Groups:
    ----------
    0–25   : Young Adult
    26–40  : Young
    41–60  : Middle Aged
    61–100 : Senior
    """
    try:
        if "age" not in df.columns:
            raise ValueError("Column 'age' not found")
            
        df["age_group"] = pd.cut(
            df["age"],
            bins=[0, 25, 40, 60, 100],
            labels=["Young Adult", "Young", "Middle Aged", "Senior"]
        )

        logger.info("Age group feature created successfully")
        return df

    except Exception as exc:
        logger.error(f"Age group creation failed: {exc}")
        raise


def create_customer_segmentation(df: pd.DataFrame) -> pd.DataFrame:
    """
    Create a customer_segmentation feature based on purchase frequency.

    Business Logic
    --------------
    Customers are segmented according to the number of previous purchases:

    - New        : Exactly 1 previous purchase
    - Returning  : Between 2 and 5 previous purchases
    - Loyal      : More than 5 previous purchases
    - Unknown    : If none of the conditions match (default category)

    This segmentation helps in:
    - Understanding customer loyalty behavior
    - Identifying high-value customers
    - Supporting targeted marketing strategies
    - Analyzing revenue contribution by segment

    Parameters
    ----------
    df : pd.DataFrame
        Input DataFrame containing a 'previous_purchases' column.

    Returns
    -------
    pd.DataFrame
        The original DataFrame with an additional column:
        'customer_segmentation'.
    """
    try:
        if "previous_purchases" not in df.columns:
            raise ValueError("Column 'previous_purchases' not found")
        conditions = [
            df['previous_purchases'] == 1,
            df['previous_purchases'].between(2, 10),
            df['previous_purchases'] > 10
        ]

        choices = ['New', 'Returning', 'Loyal']

        df['customer_segmentation'] = np.select(
            conditions,
            choices,
            default='Unknown'
        )

        logger.info("Customer Segmentation feature created successfully")
        logger.info(f"\n{df[['previous_purchases','customer_segmentation']].head()}")

        return df

    except Exception as exc:
        logger.error(f'Customer Segmentation creation failed: {exc}')
        raise

# -----------------------------
# 8. Save Clean Data
# -----------------------------

def save_data(df: pd.DataFrame, database_url: str, table_name: str) -> None:
    """
    Save cleaned data to MySQL database.
    """
    try:
        engine = create_engine(database_url)
        df.to_sql(table_name, engine, if_exists="replace", index=False)
        logger.info(f"Data saved to database table: {table_name}")

    except Exception as exc:
        logger.error(f"Failed to save data: {exc}")
        raise


# -----------------------------
# 9. Main Pipeline
# -----------------------------

def main() -> None:
    """
    Execute the full data cleaning and EDA pipeline.
    """
    try:
        df = load_data(DATA_FILE_PATH)
        df = clean_data(df, rename_columns={"purchase_amount_(usd)": "purchase_amount"})
        df = handle_missing_values(df)
        df = create_age_group(df)
        df = create_customer_segmentation(df)
        save_data(df, DATABASE_URL, TABLE_NAME)

        logger.info("Pipeline executed successfully")

    except Exception as exc:
        logger.error(f"Pipeline failed: {exc}")
        raise


# -----------------------------
# 10. Entry Point
# -----------------------------

if __name__ == "__main__":
    main()

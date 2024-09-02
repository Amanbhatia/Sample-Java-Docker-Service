import pandas as pd
import numpy as np
import random
import string
import ast

def read_categories_from_file(filename):
    """Reads categories from a text file and returns them as a list.
    Args:
        filename: The name of the text file containing the categories.
    Returns:
        A list of categories.
    """
    with open(filename, 'r') as f:
        categories_str = f.read()

    # Use ast.literal_eval to safely evaluate the string as a Python list
    categories = ast.literal_eval(categories_str)
    print('Total categories: ', len(categories))
    return categories

# Function to generate random Product IDs
def generate_product_id():
    return 'T0101-P' + ''.join(random.choices(string.ascii_uppercase + string.digits, k=11))

def generate_data(seed, num_records, filename):
    # Set random seed for reproducibility
    np.random.seed(42)
    # Parameters
    categories = read_categories_from_file('SalesPrediction\data-generation-code\categories.txt')
    years = [2021, 2022, 2023]
    months = list(range(1, 13))
    weeks = list(range(1, 53))

    # Generate random data
    data = {
        'Category_Type': [],
        'Product_ID': [],
        'Year': [],
        'Month': [],
        'Week': [],
        'Total_Sales_Count': []
    }

    for _ in range(num_records):
        category = np.random.choice(categories)
        year = np.random.choice(years)
        month = np.random.choice(months)
        week = np.random.choice(weeks)

        # Randomize products per group
        products_per_group = random.randint(1, 50)

        for _ in range(products_per_group):
            product_id = generate_product_id()
            total_sales_count = np.random.randint(10, 50000)
            data['Category_Type'].append(category)
            data['Product_ID'].append(product_id)
            data['Year'].append(year)
            data['Month'].append(month)
            data['Week'].append(week)
            data['Total_Sales_Count'].append(total_sales_count)

    # Convert to DataFrame
    df = pd.DataFrame(data)

    # Calculate Category_Sales by aggregating Total_Sales per Category_Type, Year, Month, and Week
    df['Category_Sales_Count'] = df.groupby(['Category_Type', 'Year', 'Month', 'Week'])['Total_Sales_Count'].transform('sum')

    # Save to CSV
    df.to_csv(filename + '.csv', index=False)
    print("Sample Data:")
    print(df.head())


generate_data(44, 10000, 'my-train-data')
# src/data_import_export.py

import pandas as pd
import json
import xml.etree.ElementTree as ET
from sqlalchemy import create_engine

#================================================================================================
# IMPORT CODE
#================================================================================================
def import_csv(file_path):
    return pd.read_csv(file_path)

def import_excel(file_path, sheet_name=0):
    return pd.read_excel(file_path, sheet_name=sheet_name)

def import_text(file_path, delimiter='\t'):
    return pd.read_csv(file_path, delimiter=delimiter)

def import_json(file_path):
    with open(file_path, 'r') as file:
        return pd.DataFrame(json.load(file))

def import_xml(file_path, row_tag):
    tree = ET.parse(file_path)
    root = tree.getroot()
    rows = []
    for row in root.findall(row_tag):
        rows.append({child.tag: child.text for child in row})
    return pd.DataFrame(rows)

def import_sql(query, connection_string):
    engine = create_engine(connection_string)
    return pd.read_sql(query, engine)

# Example function to import data from an API
def import_api(url):
    response = requests.get(url)
    data = response.json()
    return pd.DataFrame(data)


#================================================================================================
# EXPORT CODE
#================================================================================================

def export_csv(df, file_path):
    df.to_csv(file_path, index=False)

def export_excel(df, file_path, sheet_name='Sheet1'):
    df.to_excel(file_path, sheet_name=sheet_name, index=False)

def export_pdf(df, file_path):
    import matplotlib.pyplot as plt
    from matplotlib.backends.backend_pdf import PdfPages
    
    fig, ax = plt.subplots(figsize=(12, 4))
    ax.axis('tight')
    ax.axis('off')
    table = ax.table(cellText=df.values, colLabels=df.columns, cellLoc='center', loc='center')
    pp = PdfPages(file_path)
    pp.savefig(fig, bbox_inches='tight')
    pp.close()

def export_html(df, file_path):
    df.to_html(file_path, index=False)

def export_sql(df, table_name, connection_string):
    engine = create_engine(connection_string)
    df.to_sql(table_name, engine, if_exists='replace', index=False)

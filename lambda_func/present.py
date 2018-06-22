import pandas as pd
import strings

def transform(data):
    return (dataframe_to_str(data) if isinstance(data, pd.DataFrame) else str(data))

def dataframe_to_str(dataframe):
    print(dataframe)
    columns = list(dataframe.columns.values)
    result = strings.general_strings['found_upon_request'] + ' ' + column_to_str(columns[0], 1) + ': ' + strings.general_strings['in_total'] + str(len(dataframe.index)) + '\n'
    for index, row in dataframe.iterrows():
        for column in columns:
            result = result + column_to_str(column, 0) + ': ' + row[column] + '/n'
        result = result + '/n'
    return result
        
def column_to_str(column, index=0):
    if column in strings.tables_columns:
        result = strings.tables_columns[column][index]
    else:
        result = column
    return result
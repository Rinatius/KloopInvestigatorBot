# def transform(data):
#     return (dataframe_to_str(data) if isinstance(data, pd.DataFrame) else str(data))
#
# def dataframe_to_str(dataframe):
#     print(dataframe)
#     columns = list(dataframe.columns.values)
#     result = strings.general_strings['found_upon_request'] + ' ' + column_to_str(columns[0], 1) + ': ' + strings.general_strings['in_total'] + str(len(dataframe.index)) + '\n'
#     for index, row in dataframe.iterrows():
#         for column in columns:
#             result = result + column_to_str(column, 0) + ': ' + check_none(row[column]) + '/n'
#         result = result + '/n'
#     return result
#
# def column_to_str(column, index=0):
#     if column in strings.tables_columns:
#         result = strings.tables_columns[column][index]
#     else:
#         result = column
#     return result
#
# def check_none(name):
#     if name is None:
#         return ''
#     else: return name


def df_to_text(df, diction=None, filt=None):
    result = ''
    if diction is None:
        diction = {}
    if df is None:
        result = None
    else:
        for index, row in df.iterrows():
            for ind, c in enumerate(row):
                if ind < len(row) - 1:
                    result += (diction.get(df.columns[ind], df.columns[ind]) +
                               ': ' + df.loc[index][df.columns[ind]] + '\n')
                else:
                    result += (diction.get(df.columns[ind], df.columns[ind]) +
                               ': ' + df.loc[index][df.columns[ind]] + '\n' + '\n')
    return result

__author__ = 'aschwartz - Avi@AviSchwartzCoding.com'
import xlrd


def open_file(path, tab, rows):
    """
    Open and read an Excel file
    """
    content = []
    book = xlrd.open_workbook(path)
    if type(tab) == int:
        tab = book.sheet_by_index(tab)
    else:
        tab = book.sheet_by_name(tab)
    for i in range(rows):
        try:
            content.append(tab.row_values(i))  # read a row
        except:
            break
    return content

def format_date(date):
    '''
    Converts Excel dates into a more useful format
    '''
    if len(str(date)) == 0:
        return None
    elif len(str(date)) == 8 or len(str(date)) == 10:
        return date
    else:
        year, month, day, hour, minute, second = xlrd.xldate_as_tuple(date, 0)
        day = str(day)
        month = str(month)
        if len(day) == 1: day = '0' + day
        if len(month) == 1: month = '0' + month
        formatted_date = month + '/' + day + '/' + str(year)[2:]
        return formatted_date

def screen_out_empty_rows(list):
    '''
    Screens out rows with nothing in the Column A
    '''
    output_list = []
    for row in list:
        try:
            string = str(row[0])
            if len(string) > 0:
                output_list.append(row)
        except:
            continue
    return output_list

def screen_out_columns(list, first_col, last_col):
    '''
    Screens out columns that are not within specified range
    '''
    output_list = []
    for row in list:
        output_list.append(row[first_col:last_col])
    return output_list

def keep_these_columns(data, *columns):
    '''
    Only keeps specified columns
    '''
    columns = list(columns)
    output_list = []
    for record in data:
        smaller_record = []
        for column in columns:
            smaller_record.append(record[column])
        output_list.append(smaller_record)
    return output_list


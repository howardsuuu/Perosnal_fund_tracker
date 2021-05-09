import datetime, time
import pandas as pd
import requests
import json
import csv
from dateutil.relativedelta import relativedelta
day = datetime.date.today()

def get_all_data():
    # day = datetime.date.today()
    one_yrs_ago = str(datetime.date.today() - relativedelta(years=1))
    initial_date = '2015-04-26'
    today = time.strftime("%Y-%m-%d")
    today_url = 'https://www.moneydj.com/funddj/bcd/tBCDNavList.djbcd?a=ACFH50&B='+initial_date + '&C=' + today
    raw_data = requests.get(today_url)


    first_handle_list = raw_data.text.replace(' ', ',')
    after_handle_list = first_handle_list.split(',')

    
    length = len(after_handle_list)
    middle_index = length//2
    first_half_date = after_handle_list[:middle_index]
    second_half_value = after_handle_list[middle_index:]
    after_handle_dict = dict(zip(first_half_date, second_half_value))
    
    dict_1 = {
        'Date' : first_half_date,
        'Value' : second_half_value,
    }
    print(dict_1)
    df = pd.DataFrame(dict_1)
    return df.to_csv('test.csv')


    
get_all_data()


# def fund_data_csv():
#     file_path = '/Users/howardsu666/Desktop/Github/howard_fund/test_1.csv'
#     file_exists = os.path.isfile(file_path)

#     try:
#         with open ('test_1.csv', 'a') as csvfile:
#             headers = ['Date', 'Value']
#             writer = csv.writer(csvfile, fieldnames=headers)

#             if not file_exists:
#                 writer.writeheader()  # file doesn't exist yet, write a header
#             for 
#     except IOError:
#         print("I/O error")
# fund_data_csv()
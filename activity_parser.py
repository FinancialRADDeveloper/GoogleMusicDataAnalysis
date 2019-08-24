import pandas as pd


def load_json_to_dataframe():

    return pd.read_json('takeout_data/My Activity/Google Play Music/My Activity.json')


def get_unique_vals_for_each_column(dataframe):

    headers = list(dataframe.columns)

    unique_vals_for_each_column = dict()

    a = (dataframe.applymap(type) == list).all()

    for column in headers:

        col_type = dataframe[column].dtype

        if bool(a[column]) is True:
            print('Data in column {} is a list'.format(column))

            # we need to do something special to make this into a tuple
            unique_data = dataframe[column].transform(tuple).unique()
            unique_vals_for_each_column[str(column)] = unique_data.tolist()
        else:
            print('Data in column {} is NOT a list'.format(column))
            try:
                unique_data = dataframe[column].unique()
                unique_vals_for_each_column[str(column)] = unique_data.tolist()
            except Exception as ie:
                pass

        # unique_vals_for_each_column[str(column)] = unique_data.tolist()


    return unique_vals_for_each_column


def calculate_hourly_activity(activity_data_frame):
    from dateutil import parser
    from datetime import datetime

    dt = parser.parse("2019-08-20T16:49:54.510Z")
    # datetime_object = datetime.strptime('', '%b %d %Y %I:%M%p')

    # this is going to be really slow but gets me to move on a come back to later

    string_activity_dates = activity_data_frame['time'].tolist()

    converted_dates = []

    # for i, elem in enumerate(string_activity_dates):
    #     converted_dates.append(parser.parse(elem))
    #     # elem = parser.parse(elem)
    #
    # activity_data_frame['datetime_time'] = converted_dates

    activity_data_frame['activity_datetime'] = pd.to_datetime(activity_data_frame['time'])

    activity_data_frame['hour'] = activity_data_frame['activity_datetime'].dt.hour

    listening_freq_by_hour = activity_data_frame['hour'].value_counts()

    xx = list(zip(listening_freq_by_hour.index.tolist(),listening_freq_by_hour.tolist()))

    listening_freq_by_hour = sorted(xx)

    # xx = sorted(xx, 0)
    # first we need to convert the column into a date time
    # activity_data_frame['ActivityDateTime'] = pd.to_datetime(activity_data_frame['time'],
    #                                                        format='%Y-%m-%d %H:%M:%S-%Z',
    #                                                        errors='coerce')
    # then extract the hour from the date time
    # activity_data_frame['activity_hour'] = activity_data_frame['datetime_time']


    # then get the frequency of each hour

    # then I guess we want to feed this into some sort of Jupyter notebook

    pass


def main():

    try:
        print("Attempting to load JSON to DataFrame")
        gmusic_activity_df = load_json_to_dataframe()

        calculate_hourly_activity(gmusic_activity_df)

        unique_vals = get_unique_vals_for_each_column(gmusic_activity_df)
        print("Finished load JSON to DataFrame")

    except Exception as e:

        print(e)

if __name__ == "__main__":
    main()


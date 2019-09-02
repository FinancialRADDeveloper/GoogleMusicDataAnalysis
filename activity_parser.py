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


def filter_out_skipped(activity_data_frame):

    listened_to_dataframe = activity_data_frame[activity_data_frame['title'].str.contains("Listened to")]

    skipped_tracks_dataframe = activity_data_frame[activity_data_frame['title'].str.contains("Skipped")]

    searched_activity_dataframe = activity_data_frame[activity_data_frame['title'].str.contains("Searched")]

    other_activity_dataframe = activity_data_frame[~activity_data_frame['title'].str.contains("Listened to")]
    other_activity_dataframe = other_activity_dataframe[~other_activity_dataframe['title'].str.contains("Skipped")]

    return listened_to_dataframe

def calculate_hourly_activity(activity_data_frame):

    string_activity_dates = activity_data_frame['time'].tolist()

    # converted_dates = []

    # for i, elem in enumerate(string_activity_dates):
    #     converted_dates.append(parser.parse(elem))
    #     # elem = parser.parse(elem)
    #
    # activity_data_frame['datetime_time'] = converted_dates

    activity_data_frame['activity_datetime'] = pd.to_datetime(activity_data_frame['time'])

    activity_data_frame['hour'] = activity_data_frame['activity_datetime'].dt.hour

    listened_to_dataframe = activity_data_frame[activity_data_frame['title'].str.contains("Listened to")]
    skipped_tracks_dataframe = activity_data_frame[activity_data_frame['title'].str.contains("Skipped")]
    searched_activity_dataframe = activity_data_frame[activity_data_frame['title'].str.contains("Searched")]

    listening_freq_by_hour = listened_to_dataframe['hour'].value_counts()
    skipped_freq_by_hour = skipped_tracks_dataframe['hour'].value_counts()
    search_freq_by_hour = searched_activity_dataframe['hour'].value_counts()

    daily_listening_stats = sorted(list(zip(listening_freq_by_hour.index.tolist(),listening_freq_by_hour.tolist())))
    skipped_stats = sorted(list(zip(skipped_freq_by_hour.index.tolist(), skipped_freq_by_hour.tolist())))
    search_stats = sorted(list(zip(search_freq_by_hour.index.tolist(), search_freq_by_hour.tolist())))

    import matplotlib.pyplot as plt


    plt.ion()

    # plt.style.use('ggplot')

    plt.bar([i[0] for i in daily_listening_stats], [j[1] for j in daily_listening_stats], color = 'blue')
    plt.bar([i[0] for i in skipped_stats], [j[1] for j in skipped_stats], color='red')
    plt.bar([i[0] for i in search_stats], [j[1] for j in search_stats], color='purple')
    plt.xlabel('Hour of the Day')
    plt.ylabel('Total tracks listened')

    plt.show()
#     plt.close()


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

        new_df = filter_out_skipped(gmusic_activity_df)

        calculate_hourly_activity(gmusic_activity_df)

        unique_vals = get_unique_vals_for_each_column(gmusic_activity_df)
        print("Finished load JSON to DataFrame")

    except Exception as e:

        print(e)


if __name__ == "__main__":
    main()


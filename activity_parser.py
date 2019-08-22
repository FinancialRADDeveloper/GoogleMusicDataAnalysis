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

    # first we need to convert the column into a date time

    # then extract the hour from the date time

    # then get the frequency of each hour

    # then I guess we want to feed this into some sort of Jupyter notebook

    pass


def main():

    try:
        print("Attempting to load JSON to DataFrame")
        gmusic_activity_df = load_json_to_dataframe()

        unique_vals = get_unique_vals_for_each_column(gmusic_activity_df)
        print("Finished load JSON to DataFrame")

    except Exception as e:

        print(e)

if __name__ == "__main__":
    main()


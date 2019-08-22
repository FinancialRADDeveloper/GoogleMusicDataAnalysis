import pandas as pd



def load_json_to_dataframe():

    return pd.read_json('takeout_data/My Activity/Google Play Music/My Activity.json')


def get_unique_vals_for_each_column(dataframe):

    headers = list(dataframe.columns)

    unique_vals_for_each_column = dict

    for column in headers:
        unique_data = dataframe[column_name].transform(tuple).unique()
        unique_vals_for_each_column.add(str(column), unique_data.to_list())


    return unique_vals_for_each_column

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


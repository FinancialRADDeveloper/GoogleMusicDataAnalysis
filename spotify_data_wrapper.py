
def get_genre_from_artist(artist_name):

    try:

        import spotipy
        import pandas as pd
        from spotipy.oauth2 import SpotifyClientCredentials  # To access authorised Spotify data

        client_id = '0c0cc89bfa1a42189a9bf8959c4cc4d1'
        client_secret = 'eff96e3fef8349daa8cf8a04bfb22efe'

        client_credentials_manager = SpotifyClientCredentials(client_id=client_id, client_secret=client_secret)

        sp = spotipy.Spotify(client_credentials_manager=client_credentials_manager)  # spotify object to access API
        name = artist_name  # chosen artist

        result = sp.search(name)  # search query

        # artist_df = pd.read_json(result)
        import pickle

        # Store data (serialize)
        with open('filename.pickle', 'wb') as handle:
            pickle.dump(result, handle, protocol=pickle.HIGHEST_PROTOCOL)

        # Load data (deserialize)
        with open('filename.pickle', 'rb') as handle:
            unserialized_data = pickle.load(handle)

        print(result == unserialized_data)



        keys_returned = result.keys()

        for elem in keys_returned:
            print(elem)

        result['tracks']['items'][0]['artists']

        return 'dddd'

    except Exception as e:
        print(e)





def test_examine_spotify_artist_data(artist_data):
    """
        Allow testing and development from previously pickled data.   No need for an internet connection and also
        prevnt the Spotify usgae stats from needlessly increasing before I know what I am doing with the retyurned data
        and how this can be combined into
    """

    # Load data (deserialize)
    with open('filename.pickle', 'rb') as handle:
        unserialized_data = pickle.load(handle)



def main():

    try:
        print("")

        genre = get_genre_from_artist('Sebastian Ingrosso')

        print("")

    except Exception as e:

        print(e)


if __name__ == "__main__":
    main()


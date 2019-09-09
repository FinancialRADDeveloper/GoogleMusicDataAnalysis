
def get_genre_from_artist(artist_name):

    try:


        import pandas as pd

        hit_the_internet = True
        if hit_the_internet:

            import spotipy
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


        else:

            result = read_artist_data_from_pickle(artist_name)

        keys_returned = result.keys()

        for elem in keys_returned:
            print(elem)

        x = result['tracks']['items'][0]['artists']

        return x

    except Exception as e:
        print(e)


def read_artist_data_from_pickle(artist_name):

    import pickle
    
    # Load data (deserialize)
    with open('{}.pickle'.format(artist_name), 'rb') as handle:
        return pickle.load(handle)


def main():

    try:
        print("")



        genre = get_genre_from_artist('Sebastian Ingrosso')

        print(genre)

    except Exception as e:

        print(e)


if __name__ == "__main__":
    main()


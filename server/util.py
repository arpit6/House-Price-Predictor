import pickle
import json
import numpy as np

__locations = None
__data_columns = None
__model = None


# Pass form data to prediction model
def get_estimated_price(city, POSTED_BY, UNDER_CONSTRUCTION, RERA, BHK_NO, SQUARE_FT):
    try:
        loc_index = __data_columns.index(city)
    except:
        loc_index = -1
    x = np.zeros(len(__data_columns))
    x[0] = POSTED_BY
    x[1] = UNDER_CONSTRUCTION
    x[2] = RERA
    x[3] = BHK_NO
    x[4] = SQUARE_FT
    if loc_index >= 0:
        x[loc_index] = 1

    return round(__model.predict([x])[0], 2)

def load_saved_artifacts():  # Load the pickle and json file
    print("Loading saved artifacts...start")
    global __data_columns
    global __locations

    with open("./artifacts/columns.json", "r") as f:
        __data_columns = json.load(f)['data_columns']
        __locations = __data_columns[5:]  # locations start from 5 column

    global __model
    if __model is None:
        with open('./artifacts/House_Price_Prediction.pickle', 'rb') as f:
            __model = pickle.load(f)
    print("Loading saved artifacts...done")

def get_location_names():
    return __locations

def get_data_columns():
    return __data_columns


if __name__ == '__main__':
    load_saved_artifacts()
    print(get_location_names())
    print(get_data_columns())
    print(get_estimated_price('Anantpur', 1, 1, 1, 5, 500))
    print(get_estimated_price('Ajmer', 1, 1, 1, 2, 100))
    print(get_estimated_price('Kalhalli', 0, 1, 0, 2, 100))  # other location
    print(get_estimated_price('Kalhalli', 1, 1, 1, 3, 100))  # other location
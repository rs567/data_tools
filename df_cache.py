import pandas as pd

# TODO make a function that pulls in data and then saves dataframe in a folder
    # Preserve data types
    # Options for different file types, csv, pickles, xlxs
def df_saver(df):
    # Check if the object is a pandas dataframe
    a = isinstance(df,pd.DataFrame)

    
    print(a)
    pass


if __name__ == "__main__":

    tb1 = [[ 0.4691, -0.2829, -1.5091, -1.1356],
           [ 1.2121, -0.1732,  0.1192, -1.0442],
           [-0.8618, -2.1046, -0.4949,  1.0718],
           [ 0.7216, -0.7068, -1.0396,  0.2719],
           [-0.425 ,  0.567 ,  0.2762, -1.0874],
           [-0.6737,  0.1136, -1.4784,  0.525 ]]
    df = pd.DataFrame(tb1)
    
    df_saver(df)


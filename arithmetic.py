import pandas as pd
import sys
import json
import prince


def set_data(data):
    pd.set_option('display.float_format', lambda x: '{:.6f}'.format(x))
    X = pd.DataFrame(
        data=data
    )
    return X


def set_ca(X):
    ca = prince.CA(
        n_components=2,
        n_iter=3,
        copy=True,
        check_input=True,
        engine='auto',
        random_state=42
    )
    ca = ca.fit(X)
    return ca


if __name__ == '__main__':
    data = json.loads(sys.argv[1])
    X = set_data(data)
    ca = set_ca(X)
    col = ca.column_coordinates(X).values
    pow = ca.row_coordinates(X).values
    print(col.tolist() + pow.tolist())

import pkg_resources
import pandas as pd


# def sp500():
#     # This is a stream-like object. If you want the actual info, call
#     # stream.read()
#     stream = pkg_resources.resource_stream(__name__, 'data/sp500.csv')
#     return pd.read_csv(stream, encoding='utf-8')


def nasdaq_dotcom():
    # This is a stream-like object. If you want the actual info, call
    # stream.read()
    stream = pkg_resources.resource_stream(__name__, "data/nasdaq_dotcom.csv")
    return pd.read_csv(stream, encoding="utf-8")


def choice_data(fp):
    stream = pkg_resources.resource_stream(__name__, fp)
    return pd.read_excel(stream)


def tohourordinal(ts):
    if not hasattr(tohourordinal, "no1900"):
        tohourordinal.no1900 = pd.Timestamp("1900-01-01").toordinal()
    return (pd.Timestamp.toordinal(ts) - tohourordinal.no1900) * 24 + ts.hour


def fromhourordinal(ho):
    if not hasattr(fromhourordinal, "no1900"):
        fromhourordinal.no1900 = pd.Timestamp("1900-01-01").toordinal()
    return pd.Timestamp.fromordinal(fromhourordinal.no1900 + ho // 24).replace(
        hour=ho % 24
    )

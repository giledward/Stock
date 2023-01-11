import yfinance as yf


def stock(ticket):  # default Stock
    ticker = yf.Ticker(ticket).info
    market_price = ticker['regularMarketPrice']
    previous_close_price = ticker['regularMarketPreviousClose']
    change = market_price - previous_close_price
    print(f'symbol: {ticker["symbol"]} || Change: {change}') if change < 0 else print(f'symbol: {ticker["symbol"]} || '
                                                                                      f'Change: +{change}')
    print('Market Price:', market_price)
    print('Previous Close Price:', previous_close_price)
    print(f'volume: {ticker["volume"]}')
    print(f'average Volume 10 days: {ticker["averageVolume10days"]}')
    print(f'targetLowPrice: {ticker["targetLowPrice"]}')
    print(f'targetMedianPrice: {ticker["targetMedianPrice"]}')
    print(f'targetHighPrice: {ticker["targetHighPrice"]}')
    print(f'Name: {ticker["shortName"]}')
    print(f'sharesShort: {ticker["sharesShort"]}')


def stock_v(ticket):
    ticker = yf.Ticker(ticket).info
    market_price = ticker['regularMarketPrice']
    previous_close_price = ticker['regularMarketPreviousClose']
    change = market_price - previous_close_price
    print(f'symbol: {ticker["symbol"]} || Change: {change}') if change < 0 else print(f'symbol: {ticker["symbol"]} || '
                                                                                      f'Change: +{change}')
    print('Market Price:', market_price)
    print(f'volume: {ticker["volume"]}')


def getName(ticket):
    ticker = yf.Ticker(ticket).info
    return f'{ticker["shortName"]}'


def getPrice(ticket):
    ticker = yf.Ticker(ticket).info
    return ticker["regularMarketPrice"]


def getVolume(ticket):
    ticker = yf.Ticker(ticket).info
    return ticker["volume"]


def getChange(ticket, percentage):
    ticker = yf.Ticker(ticket).info
    market_price = ticker['regularMarketPrice']
    previous_close_price = ticker['regularMarketPreviousClose']
    if not percentage:
        change = market_price - previous_close_price
        change = round(change, 3)
        return change
    else:
        change = ((market_price - previous_close_price) / market_price) * 100
        change = round(change, 2)
        return change


def getTargetLowPrice(ticket):
    ticker = yf.Ticker(ticket).info
    return ticker["targetLowPrice"]


def getTargetMedianPrice(ticket):
    ticker = yf.Ticker(ticket).info
    return ticker["targetMedianPrice"]


def getTargetHighPrice(ticket):
    ticker = yf.Ticker(ticket).info
    return ticker["targetHighPrice"]

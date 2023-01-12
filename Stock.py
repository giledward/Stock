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


def getVolume10days(ticket):
    ticker = yf.Ticker(ticket).info
    return ticker["averageVolume10days"]


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


def getZip(ticket):
    ticker = yf.Ticker(ticket).info
    return ticker["zip"]


def getSector(ticket):
    ticker = yf.Ticker(ticket).info
    return ticker["sector"]


def getEmployees(ticket):
    ticker = yf.Ticker(ticket).info
    return ticker["fullTimeEmployees"]


def getSummary(ticket):
    ticker = yf.Ticker(ticket).info
    return ticker["longBusinessSummary"]


def getCity(ticket):
    ticker = yf.Ticker(ticket).info
    return ticker["city"]


def getPhone(ticket):
    ticker = yf.Ticker(ticket).info
    return ticker["phone"]


def getState(ticket):
    ticker = yf.Ticker(ticket).info
    return ticker["state"]


def getCountry(ticket):
    ticker = yf.Ticker(ticket).info
    return ticker["country"]


def getCompanyOfficers(ticket):
    ticker = yf.Ticker(ticket).info
    return ticker["companyOfficers"]


def getWebsite(ticket):
    ticker = yf.Ticker(ticket).info
    return ticker["website"]


def getMaxAge(ticket):
    ticker = yf.Ticker(ticket).info
    return ticker["maxAge"]


def getAddress(ticket):
    ticker = yf.Ticker(ticket).info
    return ticker["address1"]


def getIndustry(ticket):
    ticker = yf.Ticker(ticket).info
    return ticker["industry"]


def getEbitdaMargins(ticket):
    ticker = yf.Ticker(ticket).info
    return ticker["ebitdaMargins"]


def getProfitMargins(ticket):
    ticker = yf.Ticker(ticket).info
    return ticker["profitMargins"]


def getGrossMargins(ticket):
    ticker = yf.Ticker(ticket).info
    return ticker["grossMargins"]


def getOperatingCashflow(ticket):
    ticker = yf.Ticker(ticket).info
    return ticker["operatingCashflow"]


def getRevenueGrowth(ticket):
    ticker = yf.Ticker(ticket).info
    return ticker["revenueGrowth"]


def getOperatingMargins(ticket):
    ticker = yf.Ticker(ticket).info
    return ticker["operatingMargins"]


def getEbitda(ticket):
    ticker = yf.Ticker(ticket).info
    return ticker["ebitda"]


def getRecommendationKey(ticket):
    ticker = yf.Ticker(ticket).info
    return ticker["recommendationKey"]


def getGrossProfits(ticket):
    ticker = yf.Ticker(ticket).info
    return ticker["grossProfits"]


def getFreeCashflow(ticket):
    ticker = yf.Ticker(ticket).info
    return ticker["freeCashflow"]


def getCurrentPrice(ticket):
    ticker = yf.Ticker(ticket).info
    return ticker["currentPrice"]


def getEarningsGrowth(ticket):
    ticker = yf.Ticker(ticket).info
    return ticker["earningsGrowth"]


def getCurrentRatio(ticket):
    ticker = yf.Ticker(ticket).info
    return ticker["currentRatio"]


def getCash(ticket):
    ticker = yf.Ticker(ticket).info
    return ticker["totalCash"]


def getDebt(ticket):
    ticker = yf.Ticker(ticket).info
    return ticker["totalDebt"]


def getRevenue(ticket):
    ticker = yf.Ticker(ticket).info
    return ticker["totalRevenue"]


def getCashPerShare(ticket):
    ticker = yf.Ticker(ticket).info
    return ticker["totalCashPerShare"]


def getRevenuePerShare(ticket):
    ticker = yf.Ticker(ticket).info
    return ticker["revenuePerShare"]


def getQuickRatio(ticket):
    ticker = yf.Ticker(ticket).info
    return ticker["quickRatio"]


def getTimezoneName(ticket):
    ticker = yf.Ticker(ticket).info
    return ticker["exchangeTimezoneName"]


def getTimezoneShortName(ticket):
    ticker = yf.Ticker(ticket).info
    return ticker["exchangeTimezoneShortName"]


def get52WeekChange(ticket):
    ticker = yf.Ticker(ticket).info
    return ticker["52WeekChange"]

def getForwardEps(ticket):
    ticker = yf.Ticker(ticket).info
    return ticker["forwardEps"]

def getSector(ticket):
    ticker = yf.Ticker(ticket).info
    return ticker["sector"]


print(getinfo("tsla"))

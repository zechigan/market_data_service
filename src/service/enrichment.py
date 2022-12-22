import datetime
import src.dataaccess.external.yahoo_finance as yahoo_finance
from src.models.asset import Stock


class YahooFinanceStockEnricher:
    @staticmethod
    def enrich(symbol: str):
        historical_data = yahoo_finance.get_stock_historical_data(symbol)
        historical_adjusted_close, historical_volume = {}, {}
        for price_data in historical_data["prices"]:
            if 'type' in price_data and price_data['type'] == 'DIVIDEND':
                continue
            date = datetime.datetime.fromtimestamp(price_data["date"])
            historical_adjusted_close[date] = price_data["adjclose"]
            historical_volume[date] = price_data["volume"]

        summary = yahoo_finance.get_stock_summary(symbol)
        summary_price = summary["price"]
        summary_profile = summary["summaryProfile"]
        summary_detail = summary["summaryDetail"]

        return Stock(
            average_daily_volume_10_day=summary_price["averageDailyVolume10Day"]["raw"],
            average_daily_volume_3_month=summary_price["averageDailyVolume3Month"]["raw"],
            country=summary_profile["country"],
            currency=summary_price["currency"],
            exchange=summary_price["exchange"],
            exchange_name=summary_price["exchangeName"],
            historical_adjusted_close=historical_adjusted_close,
            historical_volume=historical_volume,
            industry=summary_profile["industry"],
            long_name=summary_price["longName"],
            market_cap=summary_price["marketCap"]["raw"],
            monthly_beta_5_year=summary_detail["beta"]["raw"],
            sector=summary_profile["sector"],
            short_name=summary_price["shortName"],
            symbol=symbol,
        )
from dataclasses import dataclass


@dataclass
class Stock:
    average_daily_volume_10_day: float
    average_daily_volume_3_month: float
    country: str
    currency: str
    exchange: str
    exchange_name: str
    historical_adjusted_close: dict
    historical_volume: dict
    industry: str
    long_name: str
    market_cap: float
    monthly_beta_5_year: float
    sector: str
    short_name: str
    symbol: str
DROP TABLE IF EXISTS financialData;

CREATE TABLE financialData (
    year_month DATE,
    s_and_p_comp DECIMAL,
    dividend DECIMAL,
    earnings DECIMAL,
    CPI DECIMAL,
    fraction_date DATE,
    long_interest_rate DECIMAL,
    real_price DECIMAL,
    real_dividend DECIMAL,
    real_total_return_price DECIMAL,
    real_earnings DECIMAL,
    real_scaled_earnings DECIMAL,
    CAPE DECIMAL,
    TR_CAPE DECIMAL,
    excess_CAPE DECIMAL,
    monthly_bond_return DECIMAL,
    real_bond_return DECIMAL,
    ten_year_stock_return DECIMAL,
    ten_year_bond_return DECIMAL,
    ten_year_excess_return DECIMAL
);
import stock_request as sr

url = "https://finance.yahoo.com/quote/"
t = "SNDL"
new_stock = sr.Stock_request(t, url)

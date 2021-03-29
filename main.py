import stock_request as sr
import find_stock as fs

url = "https://finance.yahoo.com/quote/"
t = "SNDL"
new_stock = sr.Stock_request(t, url)
temp = fs.Find_stock()

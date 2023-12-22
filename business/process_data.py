from dal import get_data

"""
Will get data that looks like this:
90%/10% Ground Beef Chub, Case (priced per pound)
By Member's Mark | Item # 314945 | Model # PLU 12047
CURRENT PRICE: $3.88/LB
$3.88/lb
$329.06

first 2 lines are item name
    it *might* be safe to split the item name on a comma, to get a shortened name for reference purposes?
    definitely want to grab the whole second line: vendor name | item# | model# split on the pipe, easy...
second 2 are current_price
    might only need to grab the second line? but will have to do some testing...
last is inline_price
    inline price is sometimes the total price (for meats), but it is also sometimes the per-unit price (plastic forks)
    When I model the data in a class, I can use the presence of a '/' to determine which line is the per-unit/per-pound
"""

def process_data(url):
    item_name, current_price, inline_price = get_data(url)
    
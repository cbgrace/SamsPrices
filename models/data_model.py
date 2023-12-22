class PriceData:
    def __init__(self, product_name, vendor_name, item_number, model_number, current_price, per_unit_price):
        self._product_name = product_name
        self._vendor_name = vendor_name
        self._item_number = item_number
        self._model_number = model_number
        self._current_price = current_price
        self._per_unit_price = per_unit_price

    def __str__(self):
        return f"{self._product_name}, current price: {self._current_price} ({self._per_unit_price})"

    def __repr__(self):
        return f"{self._product_name}, current price: {self._current_price} ({self._per_unit_price})"
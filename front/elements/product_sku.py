from selene import have

from front.elements import wrapper


def check_for_value(value: str):
    wrapper.focus('product-sku').element('.occ-sku').should(have.text(f'SKU: {value}'))
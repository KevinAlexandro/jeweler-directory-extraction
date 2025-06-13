class Store:
    def __init__(self, store_id: str, business_name: str, scraped_at: str, town: str = None, phone_number: str = None):
        self.store_id = store_id
        self.business_name = business_name
        self.town = town
        self.phone_number = phone_number
        self.scraped_at = scraped_at

    def get_metadata(self):
        return {
            'store_id': self.store_id,
            'business_name': self.business_name,
            'town': self.town,
            'phone_number': self.phone_number,
            'scraped_at': self.scraped_at
        }

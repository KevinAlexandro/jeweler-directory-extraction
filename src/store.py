class Store:
    def __init__(self, business_name:str, town:str, phone_number:str, store_id:str):
        self.business_name = business_name
        self.town = town
        self.phone_number = phone_number
        self.store_id = store_id

    def get_metadata(self):
        return {
            'business_name': self.business_name,
            'town': self.town,
            'phone_number': self.phone_number,
            'store_id': self.store_id
        }

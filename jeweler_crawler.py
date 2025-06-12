from jeweler_api import JewelerAPI

class JewelerCrawler:
    def __init__(self):
        self.__api = JewelerAPI()
        self.__run()

    def __get_all_stores(self):
        response = self.__api.get_stores()

        if not response:
            raise Exception('No response from webpage.')

        # parse response
        for store in response:
            print(store.get('Title'))

    def __run(self):
        self.__get_all_stores()

if __name__ == '__main__':
    JewelerCrawler()
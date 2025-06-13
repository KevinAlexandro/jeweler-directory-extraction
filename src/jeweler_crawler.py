from jeweler_api import JewelerAPI
from crawled_data import CrawledData
from jeweler_api_utils import JewelerAPIUtils
from writer import Writer


class JewelerCrawler:
    def __init__(self):
        self.__crawled_data = CrawledData()
        self.__api = JewelerAPI()
        self.__api_utils = JewelerAPIUtils()
        self.__run()
        self.__writer = Writer(self.__crawled_data)

    def __get_all_stores(self):
        response = self.__api.get_stores()

        if not response:
            raise Exception('No response from webpage.')

        # parse response
        for store in response:
            self.__crawled_data.add_store(self.__api_utils.get_store_data(store))

    def __run(self):
        self.__get_all_stores()


if __name__ == '__main__':
    JewelerCrawler()

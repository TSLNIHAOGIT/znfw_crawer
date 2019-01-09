from scrapy.exceptions import DropItem
import json


class PricePipeline(object):
    # print('*********************/1')
    #
    # vat_factor = 1.15
    # #
    def process_item(self, item, spider):
        print('*********************\n1',item)
        # if item['price']:
        #     if item['price_excludes_vat']:
        #         item['price'] = item['price'] * self.vat_factor
        #     return item
        # else:
        #     raise DropItem("Missing price in %s" % item)
#
#
#
#
# class JsonWriterPipeline(object):
#
#     # def __init__(self):
#     #     self.file = open('items.jl', 'wb')
#
#     def process_item(self, item, spider):
#         # line = json.dumps(dict(item)) + "\n"
#         # self.file.write(line)
#         # return item
#         print('*********************\n2', item)
#
#
#
# class DuplicatesPipeline(object):
#
#     # def __init__(self):
#     #     self.ids_seen = set()
#
#     def process_item(self, item, spider):
#         # if item['id'] in self.ids_seen:
#         #     raise DropItem("Duplicate item found: %s" % item)
#         # else:
#         #     self.ids_seen.add(item['id'])
#         #     return item
#         print('*********************\n3', item)

class MongoDBPipeline(object):
    def process_item(self,item,spider):
        # print('item',item)
        return
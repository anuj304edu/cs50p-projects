
fruit_name = input('item: ').lower().strip()

fruits_list = {
             'apple':'130', 'avocado':'50', 'banana':'110', 'cantaloupe':'50',
             'grapefriut':'60', 'grapes':'90', 'honeydew melon':'50', 'kiwifruit':'90',
             'lemon':'15', 'lime':'20', 'nectarine':'60', 'orange':'80', 'peach':'60',
             'pear':'100', 'pineapple':'70', 'plums':'70', 'strawberries':'50',
             'sweet cherries':'100', 'tangerine':'50', 'watermelon':'80'
}
if fruit_name in fruits_list:
    print('calories: ', fruits_list[fruit_name])
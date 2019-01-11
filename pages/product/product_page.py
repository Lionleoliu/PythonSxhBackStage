from base.basepage import BasePage


class ProductPage(BasePage):

    def __init__(self, driver):
        super().__init__(driver)
        self.driver = driver

        # locators

    _productManagement_link = "//aside[@id = 'nav']//a[@class='auto']//span[text()='产品管理']"
    _selfProductManagement_link = "//aside[@id = 'nav']//a[@class='auto menu-li']//span[text()='自营产品管理']"
    _addProduct_button = "新增"
    _productName_field = "prod_name"
    _productCategory_dropDownBox = "catId"  # 产品类目
    _productTag_fakeDropDownBox = "tagator_inputTagator"  # 产品标签
    _productTag_hotSelling_li = "//div[@id = 'tagator_inputTagator']//li[text()='热卖']"
    _stockingUnit_dropDown = "unit"  # 入库单位
    _sellByPortion_field = "salesModelValue1"  # 按份数卖
    _productType_DropDownBox = "supplyType"  # 产品类型
    _productRegion_fakeDropDownBox = "select2-productPlaceId-container"
    _productRegionWuhan = "//ul[@id='select2-productPlaceId-results']//li[text()='武汉市/湖北省/中国']"
    _productClass_fakeDropDownBox = "select2-categoryId-container"
from base.basepage import BasePage


class ProductPage(BasePage):

    def __init__(self, driver):
        super().__init__(driver)
        self.driver = driver

        # locators

    _productManagement_link = "//aside[@id = 'nav']//a[@class='auto']//span[text()='��Ʒ����']"
    _selfProductManagement_link = "//aside[@id = 'nav']//a[@class='auto menu-li']//span[text()='��Ӫ��Ʒ����']"
    _addProduct_button = "����"
    _productName_field = "prod_name"
    _productCategory_dropDownBox = "catId"  # ��Ʒ��Ŀ
    _productTag_fakeDropDownBox = "tagator_inputTagator"  # ��Ʒ��ǩ
    _productTag_hotSelling_li = "//div[@id = 'tagator_inputTagator']//li[text()='����']"
    _stockingUnit_dropDown = "unit"  # ��ⵥλ
    _sellByPortion_field = "salesModelValue1"  # ��������
    _productType_DropDownBox = "supplyType"  # ��Ʒ����
    _productRegion_fakeDropDownBox = "select2-productPlaceId-container"
    _productRegionWuhan = "//ul[@id='select2-productPlaceId-results']//li[text()='�人��/����ʡ/�й�']"
    _productClass_fakeDropDownBox = "select2-categoryId-container"
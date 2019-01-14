from base.basepage import BasePage


class ProductPage(BasePage):

    def __init__(self, driver):
        super().__init__(driver)
        self.driver = driver

        ######## locators  ##########
        #############################

    _addProduct_button = "����"
    _productName_field = "prod_name"
    _productCategory_dropDownBox = "catId"  # ��Ʒ��Ŀ
    _productTag_fakeDropDownBox = "tagator_inputTagator"  # ��Ʒ��ǩ
    _productTagValue_hotSelling_li = "//div[@id = 'tagator_inputTagator']//li[text()='����']"
    _stockingUnit_dropDown = "unit"  # ��ⵥλ
    _sellByPortion_field = "salesModelValue1"  # ��������
    _productType_DropDownBox = "supplyType"  # ��Ʒ����
    _productRegion_fakeDropDownBox = "select2-productPlaceId-container"
    _productRegion_ValueWuhan = "//ul[@id='select2-productPlaceId-results']//li[text()='�人��/����ʡ/�й�']"
    _productClass_fakeDropDownBox = "select2-categoryId-container"
    _productClass_ValueFish = "//ul[@id='select2-categoryId-results']//li[contains(text(),'����������')]"
    _productBrand_fakeDropDownBox = "select2-brandId-container"
    _productBrand_ValueRedFuji = "//ul[@id='select2-brandId-results']//li[text()='�츻ʿ']"

    _productSpecification1 = "select2-specId1-container"
    _productSpecification1_ValueColor = "//ul[@id='select2-specId1-results']//li[text()='��ɫ����']"
    _productSpecificationValue1 = "//div[@class='col-sm-3']//li[@class='select2-search select2-search--inline']"
    _productSpecificationValue1_ValueRedColor = "//ul[@id='select2-specValueId1-results']//li[text()='��ɫ����']"

    _productSpecification2 = "select2-specId2-container"
    _productSpecification2_ValueColor = "//ul[@id='select2-specId2-results']//li[text()='����������']"
    _productSpecificationValue2 = "//div[@class='col-sm-3']//span[@class='select2-selection select2-selection--multiple']//input[@placeholder='��ѡ��']"
    _productSpecificationValue2_ValueRedColor = "//ul[@id='select2-specValueId2-results']//li[text()='�ܶ໨������']"

    _productSpecification3 = "select2-specId3-container"
    _productSpecification3_ValueColor = "//ul[@id='select2-specId3-results']//li[text()='��']"
    _productSpecificationValue3 = "specValueId3"
    _productSpecificationValue3_ValueRedColor = "//ul[@id='select2-specValueId3-results']//li[text()='����']"

    _buildSpecification_link = "���ɹ��"
    _productCreated_CheckBox = "//input[@id='specValueStr']//following-sibling::i"
    _productSpecificationInventory_field = "//div[@class='form-group']//input[contains(@class,'form-control') and contains(@onchange,'specValueInventoryStr(this)')]"
    _mainSpecification = "�����"
    _saveAndUploadPic = "btnsubmit1"

    def inputProductname(self, username):
        self.sendKeys(username, self._productName_field)

    def selectProductType(self, visibleValue):
        self.getDropdownByVisibleValue(locator=self._productType_DropDownBox, visibleValue=visibleValue)

    def clickProductTag(self):
        self.elementClick(self._productTag_fakeDropDownBox)

    def clickHotSellingTag(self):
        self.elementClick(self._productTagValue_hotSelling_li)

    def selectStockUnit(self, visibleValue):
        self.getDropdownByVisibleValue(locator=self._stockingUnit_dropDown, visibleValue=visibleValue)

    def inputStockUnit(self, unit):
        self.sendKeys(unit, self._stockingUnit_dropDown)

from base.basepage import BasePage


class ProductPage(BasePage):

    def __init__(self, driver):
        super().__init__(driver)
        self.driver = driver

        ######## locators  ##########
        #############################

    _addProduct_button = "新增"
    _productName_field = "prod_name"
    _productCategory_dropDownBox = "catId"  # 产品类目
    _productTag_fakeDropDownBox = "tagator_inputTagator"  # 产品标签
    _productTagValue_hotSelling_li = "//div[@id = 'tagator_inputTagator']//li[text()='热卖']"
    _stockingUnit_dropDown = "unit"  # 入库单位
    _sellByPortion_field = "salesModelValue1"  # 按份数卖
    _productType_DropDownBox = "supplyType"  # 产品类型
    _productRegion_fakeDropDownBox = "select2-productPlaceId-container"
    _productRegion_ValueWuhan = "//ul[@id='select2-productPlaceId-results']//li[text()='武汉市/湖北省/中国']"
    _productClass_fakeDropDownBox = "select2-categoryId-container"
    _productClass_ValueFish = "//ul[@id='select2-categoryId-results']//li[contains(text(),'三级：鲢鱼')]"
    _productBrand_fakeDropDownBox = "select2-brandId-container"
    _productBrand_ValueRedFuji = "//ul[@id='select2-brandId-results']//li[text()='红富士']"

    _productSpecification1 = "select2-specId1-container"
    _productSpecification1_ValueColor = "//ul[@id='select2-specId1-results']//li[text()='颜色子类']"
    _productSpecificationValue1 = "//div[@class='col-sm-3']//li[@class='select2-search select2-search--inline']"
    _productSpecificationValue1_ValueRedColor = "//ul[@id='select2-specValueId1-results']//li[text()='红色子类']"

    _productSpecification2 = "select2-specId2-container"
    _productSpecification2_ValueColor = "//ul[@id='select2-specId2-results']//li[text()='花粉量子类']"
    _productSpecificationValue2 = "//div[@class='col-sm-3']//span[@class='select2-selection select2-selection--multiple']//input[@placeholder='请选择']"
    _productSpecificationValue2_ValueRedColor = "//ul[@id='select2-specValueId2-results']//li[text()='很多花粉子类']"

    _productSpecification3 = "select2-specId3-container"
    _productSpecification3_ValueColor = "//ul[@id='select2-specId3-results']//li[text()='香']"
    _productSpecificationValue3 = "specValueId3"
    _productSpecificationValue3_ValueRedColor = "//ul[@id='select2-specValueId3-results']//li[text()='很香']"

    _buildSpecification_link = "生成规格"
    _productCreated_CheckBox = "//input[@id='specValueStr']//following-sibling::i"
    _productSpecificationInventory_field = "//div[@class='form-group']//input[contains(@class,'form-control') and contains(@onchange,'specValueInventoryStr(this)')]"
    _mainSpecification = "主规格"
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

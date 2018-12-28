class Config:

	SCHEME = "https"
	HOST = SCHEME + "://mobile-api-gateway.truemoney.com"

	DEVICE_OS = "android"
	DEVICE_ID = "574e0139a8e4460dac351feac6157871"
	DEVICE_TYPE = "Zenfone Max"
	DEVICE_VERSION = "7.1.2"
	APP_NAME = "wallet"
	APP_VERSION = "4.18.0"

	HEADERS = {
		"User-Agent": "okhttp/3.9.0",
		"Connection": "close",
		"Accept-Encoding": "gzip, deflate"
	}

	PARAMS = {
		"device_os": DEVICE_OS,
		"device_id": DEVICE_ID,
		"device_type": DEVICE_TYPE,
		"device_version": DEVICE_VERSION,
		"app_name": APP_NAME,
		"app_version": APP_VERSION
	}

	BANKS = [
		{
			"name": "ธนาคารไทยพาณิชย์",
			"code": "SCB"
		},
		{
			"name": "ธนาคารกรุงเทพ",
			"code": "BBL"
		},
		{
			"name": "ธนาคารกสิกรไทย",
			"code": "KBANK"
		},
		{
			"name": "ธนาคารกรุงไทย",
			"code": "KTB"
		},
		{
			"name": "ธนาคารทหารไทย",
			"code": "TMB"
		},
		{
			"name": "ธนาคารกรุงศรีอยุธยา",
			"code": "BAY"
		},
		{
			"name": "ธนาคารธนชาต",
			"code": "TBANK"
		},
		{
			"name": "ธนาคารซีไอเอ็มบี ไทย",
			"code": "CIMB"
		},
		{
			"name": "ธนาคารอิสลามแห่งประเทศไทย",
			"code": "ISBT"
		},
		{
			"name": "ธนาคารแลนด์ แอนด์ เฮาส์",
			"code": "LHBANK"
		},
		{
			"name": "ธนาคารยูโอบี",
			"code": "UOB"
		},
		{
			"name": "ธนาคารไทยเครดิตเพื่อรายย่อย",
			"code": "TCRB"
		},
		{
			"name": "ธนาคารซิตี้แบงก์",
			"code": "CITI"
		},
		{
			"name": "ธนาคารสแตนดาร์ดชาร์เตอร์ด",
			"code": "SCBT"
		},
		{
			"name": "ธนาคารไอซีบีซี ไทย",
			"code": "ICBCT"
		},
		{
			"name": "ธนาคารแห่งประเทศจีน",
			"code": "BOC"
		}
	]

	SIGNIN_PATH = "/mobile-api-gateway/api/v1/signin"
	SIGNIN_URL = HOST + SIGNIN_PATH
	PROFILE_PATH = "/mobile-api-gateway/api/v1/profile"
	PROFILE_URL = HOST + PROFILE_PATH
	DRAFT_TRANSACTION_PATH = "/mobile-api-gateway/api/v1/withdraw/draft-transaction/{}"
	DRAFT_TRANSACTION_URL = HOST + DRAFT_TRANSACTION_PATH
	WITHDRAW_PATH = "/mobile-api-gateway/api/v1/withdraw/transaction/{}/{}"
	WITHDRAW_URL = HOST + WITHDRAW_PATH
	WITHDRAW_OTP_PATH = "/mobile-api-gateway/api/v1/withdraw/draft-transaction/{}/send-otp/{}"
	WITHDRAW_OTP_URL = HOST + WITHDRAW_OTP_PATH
	WITHDRAW_STATUS_PATH = "/mobile-api-gateway/api/v1/withdraw/transaction/{}/status/{}"
	WITHDRAW_STATUS_URL = HOST + WITHDRAW_STATUS_PATH

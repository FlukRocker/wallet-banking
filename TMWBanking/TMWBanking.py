from .Config import Config
from urllib.parse import urlencode
import hashlib
import requests

class Wallet:

	isLogged = False

	fullname = None
	name = None
	mobileNumber = None
	email = None
	tmnId = None
	thaiId = None
	ewalletId = None

	def __init__(self, email, password):
		password = hashlib.sha1(("%s%s" % (email, password)).encode("utf-8")).hexdigest()

		jsonData = {
			"username": email,
			"password": password,
			"type": "email"
		}
		jsonResp = requests.post(Config.SIGNIN_URL, headers=Config.HEADERS, params=Config.PARAMS, json=jsonData).json()

		if jsonResp["code"] == "20000":
			self.accessToken = jsonResp["data"]["accessToken"]
			self.fullname = jsonResp["data"]["fullname"]
			self.name = jsonResp["data"]["title"] + " " + jsonResp["data"]["fullname"]
			self.mobileNumber = jsonResp["data"]["mobileNumber"]
			self.email = jsonResp["data"]["email"]
			self.currentBalance = jsonResp["data"]["currentBalance"]
			self.tmnId = jsonResp["data"]["tmnId"]
			self.thaiId = jsonResp["data"]["thaiId"]
		else:
			raise Exception("Cannot signin")

	def updateCurrentBalance(self):
		self.currentBalance = requests.get(Config.PROFILE_URL + "/" + self.accessToken, headers=Config.HEADERS, params=Config.PARAMS).json()["data"]["currentBalance"]
		return self.currentBalance

	def draftTransaction(self, bankName, bankAccount, amount):
		jsonData = {
			"amount": amount,
			"bankAccount": bankAccount,
			"bankName": bankName
		}
		return requests.post(Config.DRAFT_TRANSACTION_URL.format(self.accessToken), headers=Config.HEADERS, params=Config.PARAMS, json=jsonData).json()["data"]

	def withdrawOtp(self, draftTransactionId):
		return requests.put(Config.WITHDRAW_OTP_URL.format(draftTransactionId, self.accessToken), headers=Config.HEADERS, params=Config.PARAMS).json()["data"]

	def withdraw(self, draftTransactionId, otpString, otpRefCode, password):
		jsonData = {
			"mobileNumber": self.mobileNumber,
			"otpRefCode": otpRefCode,
			"otpString": otpString,
			"password": password
		}
		return requests.post(Config.WITHDRAW_URL.format(draftTransactionId, self.accessToken), headers=Config.HEADERS, params=Config.PARAMS, json=jsonData).json()["data"]

	def withdrawStatus(self, draftTransactionId):
		return requests.get(Config.WITHDRAW_STATUS_URL.format(draftTransactionId, self.accessToken), headers=headers, params=Config.PARAMS).json()["data"]

	def withdrawInfo(self, draftTransactionId):
		return requests.get(Config.WITHDRAW_PATH.format(draftTransactionId, self.accessToken), headers=Config.HEADERS, params=Config.PARAMS).json()["data"]

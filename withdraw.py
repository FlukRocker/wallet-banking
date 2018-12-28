from TMWBanking import TMWBanking
from getpass import getpass
import hashlib
import os
import time

print()
print("""----------------------------------
TRUEMONEY WALLET TO BANK
by Noxturnix
https://github.com/Noxturnix
----------------------------------""")

try:
	while True:
		# Get an identification from a user
		print()
		print("[TrueMoney Wallet signin]")
		email = input("Email: ")
		password = getpass("Password: ")

		# Signin to TrueMoney Wallet
		try:
			wallet = TMWBanking.Wallet(email, password)
			break
		except Exception as e:
			print("ERROR <%s>" % (e))

	while True:
		# Prompt for withdrawal
		print()
		print("""----------------------------------
Name => %s
Current Balance => %s baht
*โอนได้ครั้งละไม่ต่ำกว่า 500 บาท
----------------------------------""" % (wallet.name, float(wallet.currentBalance)))
		print("[Withdraw to Bank]")
		print("BANK LIST")
		for i in range(len(TMWBanking.Config.BANKS)):
			print("%s. %s (%s)" % (i + 1, TMWBanking.Config.BANKS[i]["name"], TMWBanking.Config.BANKS[i]["code"]))
		while True:
			select = input("Select a bank [1-%s]: " % (len(TMWBanking.Config.BANKS)))
			if select.isdigit() and int(select) > 0 and int(select) <= len(TMWBanking.Config.BANKS):
				bankName = TMWBanking.Config.BANKS[int(select) - 1]["code"]
				break
		bankAccount = input("Account number: ")
		while True:
			amount = input("Amount: ")
			try:
				if float(amount) < 500.0:
					continue
				else:
					break
			except:
				continue

		# Print transaction info
		draftTransactionInfo = wallet.draftTransaction(bankName, bankAccount, amount)
		print()
		print("""----------------------------------
Bank name => %s
Bank account => %s
Amount => %s
Fee => %s
----------------------------------""" % (draftTransaction["bankNameTh"], draftTransaction["bankAccount"], draftTransaction["amount"], draftTransaction["fee"]))

		# Ask user to confirm the transaction
		print("[Confirmation]")
		while True:
			confirm = input("Confirm? [Y/n]: ").lower() or "y"
			if confirm in ["y", "n"]:
				break

		if confirm == "n":
			wallet.updateCurrentBalance()
			continue
		break

	# Request an OTP
	otpInfo = wallet.withdrawOtp(draftTransaction["draftTransactionID"])

	# Print the OTP Information
	print()
	print("""----------------------------------
OTP has been sent to => ******%s
Ref. => %s
----------------------------------""" % (otpInfo["mobileNumber"][-4:], otpInfo["otpRefCode"]))

	# Get an OTP from a user
	print("[OTP Confirmation]")
	otpString = input("OTP: ")
	otpPassword = getpass("Password or PIN: ")

	# Confirm the OTP and complete the transaction
	withdrawalInfo = wallet.withdraw(draftTransaction["draftTransactionID"], otpString, otpRefCode, otpPassword)
	while True:
		withdrawalStatus = wallet.withdrawStatus(draftTransaction["draftTransactionID"])
		if withdrawalStatus["withdrawStatus"] == "SUCCESS":
			break
		time.sleep(3)
	withdrawalInfo = wallet.withdrawInfo(draftTransaction["draftTransactionID"])
	print()
	print("""----------------------------------
Bank name: %s
Amount => %s
Fee => %s

Balance => %s""" % (withdrawalInfo["bankNameTh"], withdrawalInfo["amount"], withdrawalInfo["fee"], withdrawalInfo["currentEwalletBalance"]))

	if "transactionDate" in withdrawalInfo and "transactionID" in withdrawalInfo:
		print("""
Transaction date => %s
Transaction ID => %s""" % (withdrawalInfo["transactionDate"], withdrawalInfo["transactionID"]))
	print()
	print("*ใช้เวลาประมาณ 2 วันเพื่อดำเนินการ")
	print("----------------------------------")
	print("[Withdrawal success]")
	print()

except (EOFError, KeyboardInterrupt):
	print()
	os._exit(0)

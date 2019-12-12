from zeep import Client

client = Client(wsdl='http://3.122.134.94:9095/sample-tafc/services?wsdl')

req_data = {
    'WebRequestCommon': {
        'company': 'NG0010001',
        'password': 'QWERTY',
        'userName': 'JMIG02',
    },
    'OfsFunction': {
        'activityName': '',
        'assignReason': '',
        'dueDate': '',
        'extProcess': '',
        'extProcessID': '',
        'gtsControl': '',
        'messageId': '',
        'noOfAuth': '',
        'owner': '',
        'replace': '',
        'startDate': '',
        'user': ''
    },
    'FUNDSTRANSFERACTRType': {
        'DebitAccount': '1000843713',
        'DebitCurrency': 'NGN',
        'DebitAmount': '6000',
        'DebitValueDate': '20180126',
        'DebitNarrative': 'IB FT Testing',
        'CreditNarrative': 'IB FT Testing',
        'CreditAccount': '1000843705',
        'CreditCurrency': 'NGN',
        'CreditAmount': '',
        'CreditValueDate': '20180126',
        'TreasuryRate': ''}
}

# def send_request(client, data):
#     r = client.service.WebRequestCommon(document=data)
#     return r
#
# r = send_request(client, req_data)
# print(r['data'])

response = client.service.WSFT(**req_data)
print(response.FUNDSTRANSFERType.DEBITAMOUNT)
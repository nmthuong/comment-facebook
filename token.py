mport requests, json, time, random
def gettoken(): #an trom cua Khoa hjhj
    id=input("id: ")
    pw=input("password: ")
    pl={'u': id, 'p': pw}
    get_token=requests.get('http://gymtranhuynh-winazure.rhcloud.com/token.php', params=pl).json()
    while True:
        try:
            token=get_token['access_token']
            return token
        except KeyError:
            print("sai password/id")
            break

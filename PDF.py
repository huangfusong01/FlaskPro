import requests

path = r'E:\pyCharm\FlaskPro\order'
def request_pdf():
    url = 'http://sales.17feia.com/sales/v1/labelHandle/syncGeneratePdf?orderId={}&importerAddress='
    cookies = {"JSESSIONID":"89160d7f-13a3-4fc2-b54e-a643674bd03a"}
    with open(path) as file:
        order_id = file.readlines()
        for id in order_id:
            new_url = url.format(id.rstrip())
            #print(new_url)
            result = requests.get(new_url,cookies=cookies)
            print(result.json())

if __name__ == '__main__':
    request_pdf()
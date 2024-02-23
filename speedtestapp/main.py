from speedtest import *

test = Speedtest()
test.get_closest_servers()
download_result = test.download()
upload_result = test.upload()
ping_result = test.results.ping

def main():
    return download_result, upload_result



# print(f'{download_result / 1024 /1024:.2f}')
# print(f'{upload_result / 1024 /1024:.2f}')
# print(f'{ping_result / 1024 /1024:.2f}')
# print(best)
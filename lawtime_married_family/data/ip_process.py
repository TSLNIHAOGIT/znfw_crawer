# path=r'/Users/ozintel/Tsl_exercise/znfw_crawer/lihun/data/ip.txt'
# paht2=r'/Users/ozintel/Tsl_exercise/znfw_crawer/lihun/data/ip2.txt'
# fo = open(paht2, "w")
# very_code=input('请处理验证码:\n')
# print(very_code)
# with open(path) as file:
#     ip=''
#     for each in file:
#
#         each=each.strip()
#         # print(each)
#         ip_format='{"ipaddr":"'+each+'"},\n'
#         ip_format=ip_format
#         # print(ip)
#         ip=ip+ip_format
#
#     fo.write(ip)
    # print(ip)



formdata = {
    'captcha': 1234,
    'power_key': 'adaad13dd1929ba50d1cd2710cb98c34',
    'servertype': 10,
    'requestmode': 'async'
}

formdata['captcha']=453

print(formdata)


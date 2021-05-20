from urllib import request

if __name__ == '__main__':
    url = 'https://i.taobao.com/my_taobao.htm?spm=a21bo.2017.1997525045.1.473411d9bvdqbD'
    headers = {
        'Cookie':'thw=cn; t=9d5947f271e20655000f64a8f7898b71; enc=T%2FF1xCd5rAIkophLEDRvhXgQ1RBHIfW0FRsKV7W6pRH5p%2FCv0g13bw26fdH8wziEqGs5j%2Bl%2F4726HsYfdIb%2BCQ%3D%3D; hng=CN%7Czh-CN%7CCNY%7C156; x=e%3D1%26p%3D*%26s%3D0%26c%3D0%26f%3D0%26g%3D0%26t%3D0%26__ll%3D-1%26_ato%3D0; _m_h5_tk=b28dd2cf0306ba31a6abbc62e165f0ad_1565103178192; _m_h5_tk_enc=7f8486cb3ed20994b7f1a64d43491057; cookie2=79b8a987eb5d1f703ac4946e0b05b454; _tb_token_=e9e6ee9fb4555; cna=u3C3FUt0XmECAXruCOt9fnkl; v=0; unb=2285810214; uc3=nk2=B0euR33feNix&vt3=F8dBy32gi4xxTUYFRkY%3D&id2=UUpprax0mH9cug%3D%3D&lg2=VFC%2FuZ9ayeYq2g%3D%3D; csg=1eb51d8d; lgc=demon%5Cu7405%5Cu740A; cookie17=UUpprax0mH9cug%3D%3D; dnk=demon%5Cu7405%5Cu740A; skt=02881005a3a7350c; existShop=MTU2NTA5NTMxMA%3D%3D; uc4=id4=0%40U2gjE%2B8nnLxwbsjoyTC8PIqRFvYD&nk4=0%40BQRDlHOSK6q5QC3jAz3b%2FOtyiR0%3D; tracknick=demon%5Cu7405%5Cu740A; _cc_=URm48syIZQ%3D%3D; tg=0; _l_g_=Ug%3D%3D; sg=%E7%90%8A4f; _nk_=demon%5Cu7405%5Cu740A; cookie1=Bqr4lbbLSepknTuYhYoQ31Bi95npQ0039aNgyfffgSU%3D; mt=ci=56_1; uc1=cookie16=URm48syIJ1yk0MX2J7mAAEhTuw%3D%3D&cookie21=VFC%2FuZ9aiKCaj7AzMHh1&cookie15=V32FPkk%2Fw0dUvg%3D%3D&existShop=false&pas=0&cookie14=UoTaHY749rjayA%3D%3D&tag=8&lng=zh_CN; _mw_us_time_=1565095313408; l=cBSP0RlHq_5GuWhDBOCZiuI-bobOMIRYhuPRwoLXi_5p56L6Uk_Ok5gKDFp6cjWd9ILB4k6UXwp9-etks3lD1kd8E5vP.; isg=BJeXuw7whqdATQJRyAXGfQNXJgshdBBaVUOoKenEzWbNGLda8a_jjtgyfviji0O2'
    }

    req = request.Request(url, headers=headers)
    rsp = request.urlopen(req)
    html = rsp.read().decode()
    with open('taobao.html','w',encoding='utf-8') as f:
        f.write(html)
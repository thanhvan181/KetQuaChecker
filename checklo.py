from requests_html import HTMLSession
import argparse

session = HTMLSession()
r = session.get('http://ketqua.net')

if r.status_code == 200:
    ids = {'Đặc Biệt': '#rs_0_0', 'Giải Nhất': '#rs_1_0',
           'Giải Nhì': ['#rs_2_0', '#rs_2_1'],
           'Giải Ba': ['#rs_3_0', '#rs_3_1', '#rs_3_2', '#rs_3_3', '#rs_3_4',
                       '#rs_3_5'],
           'Giải Tư': ['#rs_4_0', '#rs_4_1', '#rs_4_2', '#rs_4_3'],
           'Giải Năm': ['#rs_5_0', '#rs_5_1', '#rs_5_2', '#rs_5_3', '#rs_5_4',
                        '#rs_5_5'],
           'Giải Sáu': ['#rs_6_0', '#rs_6_1', '#rs_6_2'],
           'Giải Bảy': ['#rs_7_0', '#rs_7_1', '#rs_7_2', '#rs_7_3']}
    kq = {}
    for name, _id in ids.items():
        if isinstance(_id, list):
            kq[name] = [r.html.find(_)[0].text for _ in _id]
        else:
            kq[name] = r.html.find(_id)[0].text

    parser = argparse.ArgumentParser()
    parser.add_argument("num", help="list search numbers", type=int, nargs="+",)
    args = parser.parse_args()
    numbers = args.num

    def check_lo(args, kwargs):
        result = []
        # import pdb;pdb.set_trace()
        fmt = 'Số {} đã trúng lô trong giải {} là: {}'
        for num in args:
            for k, v in kwargs.items():
                if isinstance(v, list):
                    for _num in v:
                        if num == int(str(_num)[-2:]):
                            result.append(fmt.format(num, k, _num))
                elif num == int(str(v)[-2:]):
                    result.append(fmt.format(num, k, v))
        return result

    if check_lo(numbers, kq):
        for _ in check_lo(numbers, kq):
            print(_)
    else:
        # import pdb;pdb.set_trace()
        for k, v in kq.items():
            if isinstance(v, list):
                print('Kết quả {} là: '.format(k), *v)
            else:
                print('Kết quả {} là: {}'.format(k, v))
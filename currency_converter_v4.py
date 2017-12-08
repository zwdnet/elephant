# -*- coding:utf-8 -*-
"""小象学院python教程
汇率兑换4.0版，识别币种，让程序不停运行，将兑换功能封装到函数里"""

# 带单位的货币输入
currency_str_value = input("请输入带单位的货币金额（退出程序输入Q):")
# rmb_value = eval(rmb_str_value)
usd_vs_rmb = 6.77


def convert_currency(im, er):
    """
    :param im: 待兑换货币金额
    :param er: 汇率
    :return:  兑换的货币金额
    """
    return im / er


while currency_str_value != 'Q':
    unit = currency_str_value[-3:]

    if unit == "CNY":
        # 输入为人民币
        rmb_value = eval(currency_str_value[:-3])
        exchange_rate = usd_vs_rmb
        usd_value = convert_currency(rmb_value, exchange_rate)
        print("可兑换美元为", usd_value)
    elif unit == "USD":
        # 输入为美元
        usd_value = eval(currency_str_value[:-3])
        exchange_rate = 1.0 / usd_vs_rmb
        rmb_value = convert_currency(usd_value, exchange_rate)
        print("可兑换人民币为", rmb_value)
    else:
        # 其它情况
        print("输入错误")
    currency_str_value = input("请输入带单位的货币金额（退出程序输入Q):")
print("程序已退出")

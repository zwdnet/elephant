# -*- coding:utf-8 -*-
"""小象学院python教程
汇率兑换3.0版，识别币种，让程序不停运行"""

# 带单位的货币输入
currency_str_value = input("请输入带单位的货币金额（退出程序输入Q):")
# rmb_value = eval(rmb_str_value)
while currency_str_value != 'Q':
    usd_vs_rmb = 6.77
    unit = currency_str_value[-3:]

    if unit == "CNY":
        # 输入为人民币
        rmb_value = eval(currency_str_value[:-3])
        usd_value =  rmb_value / usd_vs_rmb
        print("可兑换美元为", usd_value)
    elif unit == "USD":
        # 输入为美元
        usd_value = eval(currency_str_value[:-3])
        rmb_value = usd_value * usd_vs_rmb
        print("可兑换人民币为", rmb_value)
    else:
        # 其它情况
        print("输入错误")
    currency_str_value = input("请输入带单位的货币金额（退出程序输入Q):")
print("程序已退出")
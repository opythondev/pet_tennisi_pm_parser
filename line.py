import re


# 'basketball', 'baseball', 'e-basketball'
def line_type_1(part, period, sport):
    markets = []
    o = part.split('\n<TD')
    if len(o) != 10:
        pass
    else:
        market_1 = re.findall('id="p">(.*)<.a>', o[1])
        if len(market_1) > 0:
            p1 = market_1[0]
            markets.append({'param': '', 'period': period, 'type': 'ML-ML1', 'value': p1})

        market_2 = re.findall('id="p">(.*)<.a>', o[2])
        if len(market_2) > 0:
            p2 = market_2[0]
            markets.append({'param': '', 'period': period, 'type': 'ML-ML2', 'value': p2})

        market_f1_p = re.findall('id="p">(.*)<.a>', o[3])
        if len(market_f1_p) > 0:
            market_f1_p = market_f1_p[0]
            market_f1 = re.findall('id="p">(.*)<.a>', o[4])
            if len(market_f1) > 0:
                pf1 = market_f1[0]
                markets.append({'param': float(market_f1_p), 'period': period, 'type': 'F-F1', 'value': pf1})

        market_f2_p = re.findall('id="p">(.*)<.a>', o[5])
        if len(market_f2_p) > 0:
            market_f2_p = market_f2_p[0]
            market_f2 = re.findall('id="p">(.*)<.a>', o[6])
            if len(market_f2) > 0:
                pf2 = market_f2[0]
                markets.append({'param': float(market_f2_p), 'period': period, 'type': 'F-F2', 'value': pf2})

        market_ou_u_p = re.findall('b>(.*)<.b>', o[8])
        if market_ou_u_p != '':
            market_ou_u_p = market_ou_u_p[0]
            market_ou_u = re.findall('id="p">(.*)<.a>', o[7])
            if len(market_ou_u) > 0:
                pou_u = market_ou_u[0]
                markets.append({'param': float(market_ou_u_p), 'period': period, 'type': 'OU-TU', 'value': pou_u})

            market_ou_o = re.findall('id="p">(.*)<.a>', o[9])
            if len(market_ou_o) > 0:
                pou_o = market_ou_o[0]
                markets.append({'param': float(market_ou_u_p), 'period': period, 'type': 'OU-TO', 'value': pou_o})

    return markets


# 'soccer', 'e-soccer', 'hockey', 'handball', 'e-hockey'
def line_type_2(part, period, sport):
    markets = []
    o = part.split('\n<TD')
    if len(o) != 14:
        pass
    else:
        market_1 = re.findall('id="p">(.*)<.a>', o[1])
        if len(market_1) > 0:
            p1 = market_1[0]
            markets.append({'param': '', 'period': period, 'type': '1X2-1', 'value': p1})

        market_x = re.findall('id="p">(.*)<.a>', o[2])
        if len(market_x) > 0:
            px = market_x[0]
            markets.append({'param': '', 'period': period, 'type': '1X2-x', 'value': px})

        market_2 = re.findall('id="p">(.*)<.a>', o[3])
        if len(market_2) > 0:
            p2 = market_2[0]
            markets.append({'param': '', 'period': period, 'type': '1X2-2', 'value': p2})

        market_1x = re.findall('id="p">(.*)<.a>', o[4])
        if len(market_1x) > 0:
            p1x = market_1x[0]
            markets.append({'param': '', 'period': period, 'type': 'DC-1X', 'value': p1x})

        market_12 = re.findall('id="p">(.*)<.a>', o[5])
        if len(market_12) > 0:
            p12 = market_12[0]
            markets.append({'param': '', 'period': period, 'type': 'DC-12', 'value': p12})

        market_x2 = re.findall('id="p">(.*)<.a>', o[6])
        if len(market_x2) > 0:
            px2 = market_x2[0]
            markets.append({'param': '', 'period': period, 'type': 'DC-X2', 'value': px2})

        market_f1_p = re.findall('id="p">(.*)<.a>', o[7])
        if len(market_f1_p) > 0:
            market_f1_p = market_f1_p[0]
            market_f1 = re.findall('id="p">(.*)<.a>', o[8])
            if len(market_f1) > 0:
                pf1 = market_f1[0]
                markets.append({'param': float(market_f1_p), 'period': period, 'type': 'F-F1', 'value': pf1})

        market_f2_p = re.findall('id="p">(.*)<.a>', o[9])
        if len(market_f2_p) > 0:
            market_f2_p = market_f2_p[0]
            market_f2 = re.findall('id="p">(.*)<.a>', o[10])
            if len(market_f2) > 0:
                pf2 = market_f2[0]
                markets.append({'param': float(market_f2_p), 'period': period, 'type': 'F-F2', 'value': pf2})

        market_ou_u_p = re.findall('b>(.*)<.b>', o[12])
        if market_ou_u_p != '':
            market_ou_u_p = market_ou_u_p[0]
            market_ou_u = re.findall('id="p">(.*)<.a>', o[11])
            if len(market_ou_u) > 0:
                pou_u = market_ou_u[0]
                markets.append({'param': float(market_ou_u_p), 'period': period, 'type': 'OU-TU', 'value': pou_u})

            market_ou_o = re.findall('id="p">(.*)<.a>', o[13])
            if len(market_ou_o) > 0:
                pou_o = market_ou_o[0]
                markets.append({'param': float(market_ou_u_p), 'period': period, 'type': 'OU-TO', 'value': pou_o})

    return markets


# 'tennis', 'e-tennis'
def line_type_3(part, period, sport):
    markets = []
    o = part.split('\n<TD')
    if len(o) != 14:
        pass
    else:
        market_1 = re.findall('id="p">(.*)<.a>', o[1])
        if len(market_1) > 0:
            p1 = market_1[0]
            markets.append({'param': '', 'period': period, 'type': 'ML-ML1', 'value': p1})

        market_2 = re.findall('id="p">(.*)<.a>', o[2])
        if len(market_2) > 0:
            p2 = market_2[0]
            markets.append({'param': '', 'period': period, 'type': 'ML-ML2', 'value': p2})

        market_2_0 = re.findall('id="p">(.*)<.a>', o[3])
        if len(market_2_0) > 0:
            p2_0 = market_2_0[0]
            markets.append({'param': '2:0', 'period': period, 'type': 'CS-CS', 'value': p2_0})

        market_2_1 = re.findall('id="p">(.*)<.a>', o[4])
        if len(market_2_1) > 0:
            p2_1 = market_2_1[0]
            markets.append({'param': '2:1', 'period': period, 'type': 'CS-CS', 'value': p2_1})

        market_1_2 = re.findall('id="p">(.*)<.a>', o[5])
        if len(market_1_2) > 0:
            p1_2 = market_1_2[0]
            markets.append({'param': '0:2', 'period': period, 'type': 'CS-CS', 'value': p1_2})

        market_0_2 = re.findall('id="p">(.*)<.a>', o[6])
        if len(market_0_2) > 0:
            p0_2 = market_0_2[0]
            markets.append({'param': '0:2', 'period': period, 'type': 'CS-CS', 'value': p0_2})

        market_f1_p = re.findall('id="p">(.*)<.a>', o[7])
        if len(market_f1_p) > 0:
            market_f1_p = market_f1_p[0]
            market_f1 = re.findall('id="p">(.*)<.a>', o[8])
            if len(market_f1) > 0:
                pf1 = market_f1[0]
                markets.append({'param': float(market_f1_p), 'period': period, 'type': 'F-F1', 'value': pf1})

        market_f2_p = re.findall('id="p">(.*)<.a>', o[9])
        if len(market_f2_p) > 0:
            market_f2_p = market_f2_p[0]
            market_f2 = re.findall('id="p">(.*)<.a>', o[10])
            if len(market_f2) > 0:
                pf2 = market_f2[0]
                markets.append({'param': float(market_f2_p), 'period': period, 'type': 'F-F2', 'value': pf2})

        market_ou_u_p = re.findall('b>(.*)<.b>', o[12])
        if market_ou_u_p != '':
            market_ou_u_p = market_ou_u_p[0]
            market_ou_u = re.findall('id="p">(.*)<.a>', o[11])
            if len(market_ou_u) > 0:
                pou_u = market_ou_u[0]
                markets.append({'param': float(market_ou_u_p), 'period': period, 'type': 'OU-TU', 'value': pou_u})

            market_ou_o = re.findall('id="p">(.*)<.a>', o[13])
            if len(market_ou_o) > 0:
                pou_o = market_ou_o[0]
                markets.append({'param': float(market_ou_u_p), 'period': period, 'type': 'OU-TO', 'value': pou_o})

    return markets


# 'volleyball', 'e-volleyball'
def line_type_4(part, period, sport):
    markets = []
    o = part.split('\n<TD')
    if len(o) != 16:
        pass
    else:
        market_1 = re.findall('id="p">(.*)<.a>', o[1])
        if len(market_1) > 0:
            p1 = market_1[0]
            markets.append({'param': '', 'period': period, 'type': 'ML-ML1', 'value': p1})

        market_2 = re.findall('id="p">(.*)<.a>', o[2])
        if len(market_2) > 0:
            p2 = market_2[0]
            markets.append({'param': '', 'period': period, 'type': 'ML-ML2', 'value': p2})

        market_f1_p = re.findall('id="p">(.*)<.a>', o[3])
        if len(market_f1_p) > 0:
            market_f1_p = market_f1_p[0]
            market_f1 = re.findall('id="p">(.*)<.a>', o[4])
            if len(market_f1) > 0:
                pf1 = market_f1[0]
                markets.append({'param': float(market_f1_p), 'period': period, 'type': 'F-F1', 'value': pf1})

        market_f2_p = re.findall('id="p">(.*)<.a>', o[5])
        if len(market_f2_p) > 0:
            market_f2_p = market_f2_p[0]
            market_f2 = re.findall('id="p">(.*)<.a>', o[6])
            if len(market_f2) > 0:
                pf2 = market_f2[0]
                markets.append({'param': float(market_f2_p), 'period': period, 'type': 'F-F2', 'value': pf2})

        market_ou_u_p = re.findall('b>(.*)<.b>', o[8])
        if market_ou_u_p != '':
            market_ou_u_p = market_ou_u_p[0]
            market_ou_u = re.findall('id="p">(.*)<.a>', o[7])
            if len(market_ou_u) > 0:
                pou_u = market_ou_u[0]
                markets.append({'param': float(market_ou_u_p), 'period': period, 'type': 'OU-TU', 'value': pou_u})

            market_ou_o = re.findall('id="p">(.*)<.a>', o[9])
            if len(market_ou_o) > 0:
                pou_o = market_ou_o[0]
                markets.append({'param': float(market_ou_u_p), 'period': period, 'type': 'OU-TO', 'value': pou_o})

        market_3_0 = re.findall('id="p">(.*)<.a>', o[10])
        if len(market_3_0) > 0:
            p3_0 = market_3_0[0]
            markets.append({'param': '3:0', 'period': period, 'type': 'CS-CS', 'value': p3_0})

        market_3_1 = re.findall('id="p">(.*)<.a>', o[11])
        if len(market_3_1) > 0:
            p3_1 = market_3_1[0]
            markets.append({'param': '3:1', 'period': period, 'type': 'CS-CS', 'value': p3_1})

        market_3_2 = re.findall('id="p">(.*)<.a>', o[12])
        if len(market_3_2) > 0:
            p3_2 = market_3_2[0]
            markets.append({'param': '3:2', 'period': period, 'type': 'CS-CS', 'value': p3_2})

        market_0_3 = re.findall('id="p">(.*)<.a>', o[13])
        if len(market_0_3) > 0:
            p0_3 = market_0_3[0]
            markets.append({'param': '0:3', 'period': period, 'type': 'CS-CS', 'value': p0_3})

        market_1_3 = re.findall('id="p">(.*)<.a>', o[14])
        if len(market_1_3) > 0:
            p1_3 = market_1_3[0]
            markets.append({'param': '1:3', 'period': period, 'type': 'CS-CS', 'value': p1_3})

        market_2_3 = re.findall('id="p">(.*)<.a>', o[15])
        if len(market_2_3) > 0:
            p2_3 = market_2_3[0]
            markets.append({'param': '2:3', 'period': period, 'type': 'CS-CS', 'value': p2_3})

    return markets


# 'e-other'
def line_type_5(part, period, sport):
    markets = []
    o = part.split('\n<TD')
    if len(o) == 14:
        market_1 = re.findall('id="p">(.*)<.a>', o[1])
        if len(market_1) > 0:
            p1 = market_1[0]
            markets.append({'param': '', 'period': period, 'type': 'ML-ML1', 'value': p1})

        market_2 = re.findall('id="p">(.*)<.a>', o[2])
        if len(market_2) > 0:
            p2 = market_2[0]
            markets.append({'param': '', 'period': period, 'type': 'ML-ML2', 'value': p2})

        market_2_0 = re.findall('id="p">(.*)<.a>', o[3])
        if len(market_2_0) > 0:
            p2_0 = market_2_0[0]
            markets.append({'param': '2:0', 'period': period, 'type': 'CS-CS', 'value': p2_0})

        market_2_1 = re.findall('id="p">(.*)<.a>', o[4])
        if len(market_2_1) > 0:
            p2_1 = market_2_1[0]
            markets.append({'param': '2:1', 'period': period, 'type': 'CS-CS', 'value': p2_1})

        market_1_2 = re.findall('id="p">(.*)<.a>', o[5])
        if len(market_1_2) > 0:
            p1_2 = market_1_2[0]
            markets.append({'param': '0:2', 'period': period, 'type': 'CS-CS', 'value': p1_2})

        market_0_2 = re.findall('id="p">(.*)<.a>', o[6])
        if len(market_0_2) > 0:
            p0_2 = market_0_2[0]
            markets.append({'param': '0:2', 'period': period, 'type': 'CS-CS', 'value': p0_2})

        market_f1_p = re.findall('id="p">(.*)<.a>', o[7])
        if len(market_f1_p) > 0:
            market_f1_p = market_f1_p[0]
            market_f1 = re.findall('id="p">(.*)<.a>', o[8])
            if len(market_f1) > 0:
                pf1 = market_f1[0]
                markets.append({'param': float(market_f1_p), 'period': period, 'type': 'F-F1', 'value': pf1})

        market_f2_p = re.findall('id="p">(.*)<.a>', o[9])
        if len(market_f2_p) > 0:
            market_f2_p = market_f2_p[0]
            market_f2 = re.findall('id="p">(.*)<.a>', o[10])
            if len(market_f2) > 0:
                pf2 = market_f2[0]
                markets.append({'param': float(market_f2_p), 'period': period, 'type': 'F-F2', 'value': pf2})

        market_ou_u_p = re.findall('b>(.*)<.b>', o[12])
        if len(market_ou_u_p) > 0:
            market_ou_u_p = market_ou_u_p[0]
            market_ou_u = re.findall('id="p">(.*)<.a>', o[11])
            if len(market_ou_u) > 0:
                pou_u = market_ou_u[0]
                markets.append({'param': float(market_ou_u_p), 'period': period, 'type': 'OU-TU', 'value': pou_u})

            market_ou_o = re.findall('id="p">(.*)<.a>', o[13])
            if len(market_ou_o) > 0:
                pou_o = market_ou_o[0]
                markets.append({'param': float(market_ou_u_p), 'period': period, 'type': 'OU-TO', 'value': pou_o})
    elif len(o) == 3:
        market_1 = re.findall('id="p">(.*)<.a>', o[1])
        if len(market_1) > 0:
            p1 = market_1[0]
            markets.append({'param': '', 'period': period, 'type': 'ML-ML1', 'value': p1})

        market_2 = re.findall('id="p">(.*)<.a>', o[2])
        if len(market_2) > 0:
            p2 = market_2[0]
            markets.append({'param': '', 'period': period, 'type': 'ML-ML2', 'value': p2})
    else:
        pass

    return markets

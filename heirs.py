from pprint import pprint


def init(heirs):
    result = {}
    if heirs['son'] > 0:
        son = Son(heirs)
        result['son'] = son.his_portion()
    if heirs['son-of-son'] > 0:
        son_of_son = Son_Of_Son(heirs)
        result['son-of-son'] = son_of_son.his_portion()
    if heirs['father'] == 1:
        father = Father(heirs)
        result['father'] = father.his_portion()
    if heirs['grand-father'] > 0:
        grand_father = Grand_Father(heirs)
        result['grand-father'] = grand_father.his_portion()
    if heirs['husband'] > 0:
        husband = Husband(heirs)
        result['husband'] = husband.his_portion()
    if heirs['brother'] > 0:
        brother = Brother(heirs)
        result['brother'] = brother.his_portion()
    if heirs['daughter'] > 0:
        daughter = Daughter(heirs)
        result['daughter'] = daughter.her_portion()
    if heirs['daughter-of-son'] > 0:
        daughter_of_son = Daughter_Of_Son(heirs)
        result['daughter-of-son'] = daughter_of_son.her_portion()
    if heirs['mother'] == 1:
        mother = Mother(heirs)
        result['mother'] = mother.her_portion()
    if heirs['grand-mother'] > 0:
        grand_mother = Grand_Mother(heirs)
        result['grand-mother'] = grand_mother.her_portion()
    if heirs['wife'] > 0:
        wife = Wife(heirs)
        result['wife'] = wife.her_portion()
    if heirs['fbrother'] > 0:
        fbrother = Fbrother(heirs)
        result['fbrother'] = fbrother.his_portion()
    if heirs['son-of-brother'] > 0:
        son_of_brother = Son_Of_Brother(heirs)
        result['son-of-brother'] = son_of_brother.his_portion()
    if heirs['son-of-fbrother'] > 0:
        son_of_fbrother = Son_Of_Fbrother(heirs)
        result['son-of-fbrother'] = son_of_fbrother.his_portion()
    if heirs['uncle'] > 0:
        uncle = Uncle(heirs)
        result['uncle'] = uncle.his_portion()
    if heirs['funcle'] > 0:
        funcle = Funcle(heirs)
        result['funcle'] = funcle.his_portion()
    if heirs['cousin'] > 0:
        cousin = Cousin(heirs)
        result['cousin'] = cousin.his_portion()
    if heirs['fcousin'] > 0:
        fcousin = Fcousin(heirs)
        result['fcousin'] = fcousin.his_portion()
    if heirs['sister'] > 0:
        sister = Sister(heirs)
        result['sister'] = sister.her_portion()
    if heirs['fsister'] > 0:
        fsister = Fsister(heirs)
        result['fsister'] = fsister.her_portion()
    if heirs['msiblings'] > 0:
        msiblings = Msiblings(heirs)
        result['msiblings'] = msiblings.their_portion()

    return result


class Inheritance:
    def __init__(self, heirs):
        self.heirs = heirs


########################################################
# SECTION ONE
########################################################


class Son(Inheritance):
    def is_forbidden(self):
        return False

    def his_portion(self):
        heirs = self.heirs
        if self.is_forbidden():
            return 'F'
        elif sum([x for x in heirs.values()]) == 1:
            return 'A'
        elif heirs['daughter'] > 0:
            return 'DOF'
        else:
            return 'R'


class Son_Of_Son(Inheritance):
    def is_forbidden(self):
        heirs = self.heirs
        if heirs['son'] > 0:
            return True
        else:
            return False

    def his_portion(self):
        heirs = self.heirs
        if self.is_forbidden():
            return 'F'
        elif sum([x for x in heirs.values()]) == 1:
            return 'A'
        elif heirs['daughter-of-son'] > 0:
            return 'DOF'
        elif heirs['son-of-son'] > 1:
            return 'R'


class Father(Inheritance):
    def is_forbidden(self):
        return False

    def his_portion(self):
        heirs = self.heirs
        if self.is_forbidden():
            return 'F'
        elif sum([x for x in heirs.values()]) == 1:
            return 'A'
        elif heirs['son'] > 0 or heirs['son-of-son'] > 0:
            return '1/6'
        elif heirs['daughter'] > 0 or heirs['daughter-of-son'] > 0:
            return '1/6,R'
        else:
            return 'R'


class Grand_Father(Inheritance):
    def is_forbidden(self):
        heirs = self.heirs
        if heirs['father'] > 0:
            return True
        else:
            return False

    def his_portion(self):
        heirs = self.heirs
        if self.is_forbidden():
            return 'F'
        elif sum([x for x in heirs.values()]) == 1:
            return 'A'
        elif heirs['son'] > 0 or heirs['son-of-son'] > 0:
            return '1/6'
        elif heirs['daughter'] > 0 or heirs['daughter-of-son'] > 0:
            return '1/6,R'
        else:
            return 'R'


class Husband(Inheritance):
    def is_forbidden(self):
        return False

    def his_portion(self):
        heirs = self.heirs
        if self.is_forbidden():
            return 'F'
        if heirs['son'] > 0 or heirs['daughter'] > 0 or heirs['son-of-son'] > 0 or heirs['daughter-of-son'] > 0:
            return '1/4'
        else:
            return '1/2'


class Brother(Inheritance):
    def is_forbidden(self):
        heirs = self.heirs
        if heirs['son'] > 0 or heirs['son-of-son'] > 0 or heirs['father'] > 0 or heirs['grand-father'] > 0:
            return True
        else:
            return False

    def his_portion(self):
        heirs = self.heirs
        if self.is_forbidden():
            return 'F'
        elif sum([x for x in heirs.values()]) == 1:
            return 'A'
        elif heirs['sister'] > 0:
            return 'DOF'
        else:
            return 'R'


########################################################
# SECTION TWO
########################################################


class Daughter(Inheritance):
    def is_fobidden(self):
        return False

    def her_portion(self):
        heirs = self.heirs
        if self.is_fobidden():
            return 'F'
        elif heirs['son'] > 0:
            return 'HOM'
        elif heirs['daughter'] == 1:
            return '1/2'
        elif heirs['daughter'] > 1:
            return '2/3'


class Daughter_Of_Son(Inheritance):
    def is_forbidden(self):
        heirs = self.heirs
        if heirs['son'] > 0:
            return True
        elif heirs['daughter'] > 1 and heirs['son-of-son'] == 0:
            return True
        else:
            return False

    def her_portion(self):
        heirs = self.heirs
        if self.is_forbidden():
            return 'F'
        elif heirs['son-of-son'] > 0:
            return 'HOM'
        elif heirs['daughter'] == 1:
            return '1/6'
        elif heirs['daughter-of-son'] == 1:
            return '1/2'
        else:
            return '2/3'


class Mother(Inheritance):
    def is_forbidden(self):
        return False

    def her_portion(self):
        heirs = self.heirs
        if self.is_forbidden():
            return 'F'
        if heirs['son'] > 0 or heirs['daughter'] > 0 or heirs['son-of-son'] > 0 or heirs['daughter-of-son'] > 0 or (
                heirs['brother'] + heirs['fbrother'] + heirs['sister'] + heirs['fsister'] + heirs['msiblings']) > 1:
            return '1/6'
        else:
            return '1/3'


class Grand_Mother(Inheritance):
    def is_forbidden(self):
        heirs = self.heirs
        if heirs['mother'] == 1:
            return True
        else:
            return False

    def her_portion(self):
        heirs = self.heirs
        if self.is_forbidden():
            return 'F'
        else:
            return '1/6'


class Wife(Inheritance):
    def is_forbidden(self):
        return False

    def her_portion(self):
        heirs = self.heirs
        if heirs['son'] > 0 or heirs['daughter'] > 0 or heirs['son-of-son'] > 0 or heirs['daughter-of-son'] > 0:
            return '1/8'
        else:
            return '1/4'


########################################################
# SECTION THREE
########################################################


class Fbrother(Inheritance):
    def is_forbidden(self):
        heirs = self.heirs
        if heirs['son'] > 0 or heirs['son-of-son'] > 0 or heirs['father'] == 1 or heirs['grand-father'] == 1:
            return True
        elif heirs['brother'] > 0 or (heirs['sister'] > 0 and (heirs['daughter'] > 0 or heirs['daughter-of-son'] > 0)):
            return True
        else:
            return False

    def his_portion(self):
        heirs = self.heirs
        if self.is_forbidden():
            return 'F'
        elif sum([x for x in heirs.values()]) == 1:
            return 'A'
        elif heirs['fsister'] > 0:
            return 'DOF'
        else:
            return 'R'


class Son_Of_Brother(Inheritance):
    def is_forbidden(self):
        heirs = self.heirs
        if heirs['son'] > 0 or heirs['son-of-son'] > 0 or heirs['father'] > 0 or heirs['grand-father'] > 0:
            return True
        elif heirs['brother'] > 0 or heirs['fbrother'] > 0:
            return True
        elif (heirs['sister'] > 0 or heirs['fsister'] > 0) and (heirs['daughter'] > 0 or heirs['daughter-of-son'] > 0):
            return True
        else:
            False

    def his_portion(self):
        heirs = self.heirs
        if self.is_forbidden():
            return 'F'
        elif sum([x for x in heirs.values()]) == 1:
            return 'A'
        else:
            return 'R'


class Son_Of_Fbrother(Inheritance):
    def is_forbidden(self):
        heirs = self.heirs
        if heirs['son'] > 0 or heirs['son-of-son'] > 0 or heirs['father'] > 0 or heirs['grand-father'] > 0:
            return True
        elif heirs['brother'] > 0 or heirs['fbrother'] > 0:
            return True
        elif (heirs['sister'] > 0 or heirs['fsister'] > 0) and (heirs['daughter'] > 0 or heirs['daughter-of-son'] > 0):
            return True
        elif heirs['son-of-brother'] > 0:
            return True
        else:
            False

    def his_portion(self):
        heirs = self.heirs
        if self.is_forbidden():
            return 'F'
        elif sum([x for x in heirs.values()]) == 1:
            return 'A'
        else:
            return 'R'


class Uncle(Inheritance):
    def is_forbidden(self):
        heirs = self.heirs
        if heirs['son'] > 0 or heirs['son-of-son'] > 0 or heirs['father'] > 0 or heirs['grand-father'] > 0:
            return True
        elif heirs['brother'] > 0 or heirs['fbrother'] > 0:
            return True
        elif (heirs['sister'] > 0 or heirs['fsister'] > 0) and (heirs['daughter'] > 0 or heirs['daughter-of-son'] > 0):
            return True
        elif heirs['son-of-brother'] > 0:
            return True
        elif heirs['son-of-fbrother'] > 0:
            return True
        else:
            False

    def his_portion(self):
        heirs = self.heirs
        if self.is_forbidden():
            return 'F'
        elif sum([x for x in heirs.values()]) == 1:
            return 'A'
        else:
            return 'R'


class Funcle(Inheritance):
    def is_forbidden(self):
        heirs = self.heirs
        if heirs['son'] > 0 or heirs['son-of-son'] > 0 or heirs['father'] > 0 or heirs['grand-father'] > 0:
            return True
        elif heirs['brother'] > 0 or heirs['fbrother'] > 0:
            return True
        elif (heirs['sister'] > 0 or heirs['fsister'] > 0) and (heirs['daughter'] > 0 or heirs['daughter-of-son'] > 0):
            return True
        elif heirs['son-of-brother'] > 0:
            return True
        elif heirs['son-of-fbrother'] > 0:
            return True
        elif heirs['uncle'] > 0:
            return True
        else:
            False

    def his_portion(self):
        heirs = self.heirs
        if self.is_forbidden():
            return 'F'
        elif sum([x for x in heirs.values()]) == 1:
            return 'A'
        else:
            return 'R'


class Cousin(Inheritance):
    def is_forbidden(self):
        heirs = self.heirs
        if heirs['son'] > 0 or heirs['son-of-son'] > 0 or heirs['father'] > 0 or heirs['grand-father'] > 0:
            return True
        elif heirs['brother'] > 0 or heirs['fbrother'] > 0:
            return True
        elif (heirs['sister'] > 0 or heirs['fsister'] > 0) and (heirs['daughter'] > 0 or heirs['daughter-of-son'] > 0):
            return True
        elif heirs['son-of-brother'] > 0:
            return True
        elif heirs['son-of-fbrother'] > 0:
            return True
        elif heirs['uncle'] > 0:
            return True
        elif heirs['funcle'] > 0:
            return True
        else:
            False

    def his_portion(self):
        heirs = self.heirs
        if self.is_forbidden():
            return 'F'
        elif sum([x for x in heirs.values()]) == 1:
            return 'A'
        else:
            return 'R'


class Fcousin(Inheritance):
    def is_forbidden(self):
        heirs = self.heirs
        if heirs['son'] > 0 or heirs['son-of-son'] > 0 or heirs['father'] > 0 or heirs['grand-father'] > 0:
            return True
        elif heirs['brother'] > 0 or heirs['fbrother'] > 0:
            return True
        elif (heirs['sister'] > 0 or heirs['fsister'] > 0) and (heirs['daughter'] > 0 or heirs['daughter-of-son'] > 0):
            return True
        elif heirs['son-of-brother'] > 0:
            return True
        elif heirs['son-of-fbrother'] > 0:
            return True
        elif heirs['uncle'] > 0:
            return True
        elif heirs['funcle'] > 0:
            return True
        elif heirs['cousin'] > 0:
            return True
        else:
            False

    def his_portion(self):
        heirs = self.heirs
        if self.is_forbidden():
            return 'F'
        elif sum([x for x in heirs.values()]) == 1:
            return 'A'
        else:
            return 'R'


########################################################
# SECTION FOUR
########################################################


class Sister(Inheritance):
    def is_forbidden(self):
        heirs = self.heirs
        if heirs['son'] > 0 or heirs['son-of-son'] > 0 or heirs['father'] > 0 or heirs['grand-father'] > 0:
            return True
        else:
            return False

    def her_portion(self):
        heirs = self.heirs
        if self.is_forbidden():
            return 'F'
        elif heirs['brother'] > 0:
            return 'HOM'
        elif heirs['daughter'] > 0 or heirs['daughter-of-son'] > 0:
            return 'R'
        elif heirs['sister'] > 1:
            return '2/3'
        else:
            return '1/2'


class Fsister(Inheritance):
    def is_forbidden(self):
        heirs = self.heirs
        if heirs['son'] > 0 or heirs['son-of-son'] > 0 or heirs['father'] > 0 or heirs['grand-father'] > 0:
            return True
        elif heirs['brother'] > 0:
            return True
        elif heirs['sister'] > 0 and (heirs['daughter'] > 0 or heirs['daughter-of-son'] > 0):
            return True
        elif heirs['sister'] > 1:
            return True
        else:
            return False

    def her_portion(self):
        heirs = self.heirs
        if self.is_forbidden():
            return 'F'
        elif heirs['fbrother'] > 0:
            return 'HOM'
        elif heirs['daughter'] > 0 or heirs['daughter-of-son'] > 0:
            return 'R'
        elif heirs['sister'] == 1:
            return '1/6'
        elif heirs['fsister'] == 1:
            return '1/2'
        else:
            return '2/3'


class Msiblings(Inheritance):
    def is_forbidden(self):
        heirs = self.heirs
        if heirs['son'] > 0 or heirs['son-of-son'] > 0 or heirs['daughter'] > 0 or heirs['daughter-of-son'] > 0 or \
                heirs['father'] == 1 or heirs['grand-father'] == 1:
            return True
        else:
            return False

    def their_portion(self):
        heirs = self.heirs
        if self.is_forbidden():
            return 'F'
        elif heirs['msiblings'] == 1:
            return '1/6'
        else:
            return '1/3'


########################################################
# SECTION FIVE ==> CALCULATION
########################################################


results = {}


def calc(heirs_data_, inheritance):
    global results
    heirs_data = init(heirs_data_)
    bands = {}
    required = {}
    outs = {}
    for heir_data in heirs_data:
        temp = heirs_data[heir_data]
        if temp != 'A' and temp != 'F' and temp != 'DOF' and temp != 'HOM' and 'R' not in temp:
            required[heir_data] = temp
            if temp == '1/8':
                outs[heir_data] = 8
            elif temp == '1/6':
                outs[heir_data] = 6
            elif temp == '1/4':
                outs[heir_data] = 4
            elif temp == '1/3':
                outs[heir_data] = 3
            elif temp == '1/2':
                outs[heir_data] = 2
            else:
                outs[heir_data] = 3
        elif temp == 'F':
            results[heir_data] = 'محجوب'
        else:
            bands[heir_data] = temp

    # Calculate the origin of the problem
    print(outs)
    if len(outs) != 0:
        origin_of_problem = max(list(outs.values()))
        flag = 1
        temp = origin_of_problem
        while (flag):
            temp_outs = outs.copy()
            for temp_out in temp_outs:
                temp_outs[temp_out] = origin_of_problem % temp_outs[temp_out]
            if sum(list(temp_outs.values())) == 0:
                flag = 0
            else:
                origin_of_problem += temp
        # Calculate the share of each person or heir
        shares = {}
        for required_ in required:
            if required[required_] == '1/8':
                shares[required_] = origin_of_problem / 8
            elif required[required_] == '1/6':
                shares[required_] = origin_of_problem / 6
            elif required[required_] == '1/4':
                shares[required_] = origin_of_problem / 4
            elif required[required_] == '1/3':
                shares[required_] = origin_of_problem / 3
            elif required[required_] == '1/2':
                shares[required_] = origin_of_problem / 2
            else:
                shares[required_] = (origin_of_problem * 2) / 3

        flag = 0
        for band in bands:
            temp = bands[band]
            if temp == 'A' or temp == 'DOF' or temp == 'HOM' or 'R' in temp:
                flag = 1

        print(shares)
        print(origin_of_problem)
        sum_of_shares = sum(list(shares.values()))
        print(sum_of_shares)
        if sum_of_shares > origin_of_problem:
            value_of_share = inheritance / sum_of_shares
            print(value_of_share)
            for share in shares:
                results[share] = round(shares[share] * value_of_share, 2)
            calcBands(bands, heirs_data_, 0)
        elif sum_of_shares < origin_of_problem:
            if flag:
                value_of_share = inheritance / origin_of_problem
                print(value_of_share)
                for share in shares:
                    results[share] = round(value_of_share * shares[share], 2)
                    inheritance -= round(value_of_share * shares[share], 2)
                calcBands(bands, heirs_data_, inheritance)
            else:
                if 'husband' in outs:
                    results['husband'] = inheritance / outs['husband']
                    inheritance = inheritance - inheritance / outs['husband']
                    del shares['husband']
                elif 'wife' in outs:
                    results['wife'] = inheritance / outs['wife']
                    inheritance = inheritance - inheritance / outs['wife']
                    del shares['wife']
                sum_of_shares = sum(list(shares.values()))
                value_of_share = inheritance / sum_of_shares
                for share in shares:
                    results[share] = round(shares[share] * value_of_share, 2)
    else:
        calcBands(bands, heirs_data_, inheritance)

    return results


def calcBands(bands, heirs_data_, remainder):
    global results
    no_of_siblings = 0
    if 'DOF' in list(bands.values()):
        temp = {}
        for band in bands:
            if bands[band] == 'DOF':
                no_of_siblings += heirs_data_[band] * 2
                temp[band] = heirs_data_[band] * 2
            elif bands[band] == 'HOM':
                no_of_siblings += heirs_data_[band]
                temp[band] = heirs_data_[band]
        value_of_share = remainder / no_of_siblings
        for temp_ in temp:
            results[temp_] = value_of_share * temp[temp_]
    else:
        for band in bands:
            if 'R' in bands[band]:
                results[band] = round(remainder, 2)
            elif bands[band] == 'A':
                results[band] = round(remainder, 2)


########################################################
# SECTION FIVE ==> TESTING
########################################################


# heirs = {'brother': 0,
#          'cousin': 0,
#          'daughter-of-son': 0,
#          'daughter': 0,
#          'father': 0,
#          'fbrother': 0,
#          'fcousin': 1,
#          'fsister': 0,
#          'funcle': 0,
#          'grand-father': 0,
#          'grand-mother': 0,
#          'husband': 0,
#          'mother': 0,
#          'msiblings': 0,
#          'sister': 0,
#          'son': 0,
#          'son-of-brother': 0,
#          'son-of-fbrother': 0,
#          'son-of-son': 0,
#          'uncle': 1,
#          'wife': 0}
#
# result = calc(heirs, 3000)
#
# pprint(result)
# pprint(init(heirs))

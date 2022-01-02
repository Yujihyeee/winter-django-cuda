import csv
import pandas as pd
from django.db.models import Count
from common.models import ValueObject, Reader, Printer
from user.models import User


class Processing:
    def __init__(self):
        vo = ValueObject()
        reader = Reader()
        self.printer = Printer()
        vo.context = 'user/data/'
        vo.fname = 'user2.csv'
        self.csvfile = reader.new_file(vo)

    def insert_data(self):
        self.insert_users()

    def insert_users(self):
        with open('user/data/user2.csv', newline='', encoding='utf8') as f:
            data_reader = csv.DictReader(f)
            for row in data_reader:
                # if not FinReports.objects.filter(category=row['항목명']).exists():
                users = User.objects.create(user_id=row['user_id'],
                                            address=row['address'],
                                            birth=row['birth'],
                                            card_company=row['card_company'],
                                            card_number=row['card_number'],
                                            email=row['email'],
                                            first_name=row['first_name'],
                                            gender=row['gender'],
                                            last_name=row['last_name'],
                                            mbti=row['mbti'],
                                            mbti_list=row['mbti_list'],
                                            name=row['name'],
                                            passport=row['passport'],
                                            password=row['password'],
                                            phone_number=row['phone_number'],
                                            reg_date=row['reg_date'],
                                            username=row['username'])
                print(f'1 >>>> {users}')
        print('USER DATA UPLOADED SUCCESSFULLY!')

    # def count_mbti(self):
    #     mbti = User.objects.raw("select user_id, mbti, count(gender) as mbti_count from tripn_mariadb.users group by mbti order by mbti_count desc")
    #     mbti = {row.mbti: row.mbti_count for row in mbti}
    #     print(type(mbti))
        # df = pd.DataFrame(mbti, index=['여', '남'])
        # print(df)

        # gender = User.objects.raw("select user_id, mbti, gender, count(mbti), count(gender) as gender_count from tripn_mariadb.users group by gender order by gender_count, gender desc")

        # gender = {row.gender: row.gender_count for row in gender}
        # print(mbti)
        # print(gender)
        # return mbti
        # ls = [{"istj":0}, {"istp":0}, {"isfj":0}, {"isfp":0}, {"intj":0}, {"intp":0}, {"infj":0}, {"infp":0}, {"estj":0},
        #       {"estp":0}, {"esfj":0}, {"esfp":0}, {"entj":0}, {"entp":0}, {"enfj":0}, {"enfp":0}]
        # test = []
        # mbti = User.objects.all()
        # for i in mbti:
        #     for j in ls:
        #         if i.mbti == list(j.keys())[0]:
        #             j[i.mbti] = j[i.mbti] + 1
        # for i in ls:
        #     test.append(list(i.values())[0])
        # print(test)
        # ls.sort(reverse=True)
        # print(test)
        # [print(i.mbti) for i in mbti]
        # ls = ['istj','istp','isfj','isfp','intj','intp','infj','infp','estj','estp','esfj','esfp','entj','entp','enfj','enfp']
        # g = ['여', '남']
        # mbti_sum = User.objects.filter(mbti__in=ls, gender__in=g)
        # sum = mbti_sum.filter(gender='여').values()[0].aggregate(Count(ls))
        # print(sum)
        # return mbti_sum

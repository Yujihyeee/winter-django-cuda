from django.test import TestCase

# Create your tests here.

# def pre_process(self):
#     arr = []
#     for i in range(5, 9):
#         pr = JejuSchedule.objects.get(id=i)
#         print(pr)
#         plane = Plane.objects.filter(id__in=pr.plane).values('economyCharge')
#         pl_df = pd.DataFrame(plane, columns=['economyCharge'])
#         plane_pr = pl_df['economyCharge'].sum()
#         acc_pr = Accommodation.objects.get(id=pr.acc_id)
#         activity = Activity.objects.filter(id__in=pr.activity).values('price')
#         act_df = pd.DataFrame(activity, columns=['price'])
#         act_pr = act_df['price'].sum()
#         people = pr.people
#         day = pr.day
#         unit = acc_pr.standard_number
#         print(people/unit)
#         acc_price = math.ceil(people/unit) * acc_pr.price * day
#         print(acc_price)
#         reg_date = pr.reg_date.date()
#         price = (plane_pr * people) + acc_price + act_pr
#         tax = price * 0.1
#         subtotal = price + tax
#         fee = subtotal * 0.2
#         total_price = subtotal + fee
#         jeju_schedule_id = i
#         arr.append(reg_date)
#         arr.append(people)
#         arr.append(day)
#         arr.append(plane_pr)
#         arr.append(acc_pr.price)
#         arr.append(act_pr)
#         arr.append(price)
#         arr.append(int(tax))
#         arr.append(int(subtotal))
#         arr.append(int(fee))
#         arr.append(int(total_price))
#         arr.append(jeju_schedule_id)
#     n = 12
#     result = [arr[i * n:(i + 1) * n] for i in range((len(arr) + n - 1) // n)]
#     df = pd.DataFrame(result, columns=['reg_date', 'people', 'day', 'plane_pr', 'acc_pr', 'act_pr', 'price', 'tax',
#                                        'subtotal', 'fees', 'total_price', 'jeju_schedule_id'])
#     df.to_csv(self.csvfile)

# def process(self, p):
#     arr = []
#     pr = JejuSchedule.objects.get(pk=p)
#     print(pr)
#     plane = Plane.objects.filter(id__in=pr.plane).values('economyCharge')
#     pl_df = pd.DataFrame(plane, columns=['economyCharge'])
#     plane_pr = pl_df['economyCharge'].sum()
#     acc_pr = Accommodation.objects.get(id=pr.acc_id)
#     activity = Activity.objects.filter(id__in=pr.activity).values('price')
#     act_df = pd.DataFrame(activity, columns=['price'])
#     act_pr = act_df['price'].sum()
#     people = pr.people
#     day = pr.day
#     unit = acc_pr.standard_number
#     print(people/unit)
#     acc_price = math.ceil(people/unit) * acc_pr.price * day
#     print(acc_price)
#     reg_date = pr.reg_date.date()
#     price = (plane_pr * people) + acc_price + act_pr
#     tax = price * 0.1
#     subtotal = price + tax
#     fee = subtotal * 0.2
#     total_price = subtotal + fee
#     jeju_schedule_id = p
#     arr.append(reg_date)
#     arr.append(people)
#     arr.append(day)
#     arr.append(plane_pr)
#     arr.append(acc_pr.price)
#     arr.append(act_pr)
#     arr.append(price)
#     arr.append(int(tax))
#     arr.append(int(subtotal))
#     arr.append(int(fee))
#     arr.append(int(total_price))
#     arr.append(jeju_schedule_id)
#     n = 12
#     result = [arr[i * n:(i + 1) * n] for i in range((len(arr) + n - 1) // n)]
#     df = pd.DataFrame(result, columns=['reg_date', 'people', 'day', 'plane_pr', 'acc_pr', 'act_pr', 'price', 'tax',
#                                        'subtotal', 'fees', 'total_price', 'jeju_schedule_id'])
#     df.to_csv('reservation/data/get_price.csv')

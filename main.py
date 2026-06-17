class MemberCard:
    def __init__(self, customer_name, points = 0):
        self.customer_name = customer_name
        self.points = points
        self.__points = 0

    @property
    def points(self):
        return self.__points

    @points.setter
    def points(self, value):
        if isinstance(value, int) and value >= 0:
            self.__points = value
        else:
            print("Dữ liệu không hợp lệ")


    def add_points(self, amount):
        if isinstance(amount, int) and amount > 0:
            self.__points += amount
        else:
            print("Số điểm cộng không hợp lệ")

    @staticmethod
    def is_eligible_for_voucher(bill_amount):
        return bill_amount >= 200000


card1 = MemberCard("Le Van C", 100)

print("Điểm ban đầu:", card1.points)

print("\nThử gán điểm âm:")
card1.points = -50

print("Điểm hiện tại:", card1.points)

print("\nThử gán chuỗi:")
card1.points = "một trăm"

print("Điểm hiện tại:", card1.points)

print("\nCộng thêm 50 điểm:")
card1.add_points(50)

print("Điểm hiện tại:", card1.points)

print("\nKiểm tra Voucher:")

result = MemberCard.is_eligible_for_voucher(250000)

print("Hóa đơn 250000 VNĐ đủ điều kiện:", result)

print("\nThông tin khách hàng:")
print(f"Tên: {card1.customer_name}")
print(f"Điểm: {card1.points}")
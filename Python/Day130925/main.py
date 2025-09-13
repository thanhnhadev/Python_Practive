# Viết một chương trình Python để:
#
# Định nghĩa một mẫu regex để tìm và trích xuất tất cả các thông tin quan trọng (thời gian, mức độ, ID giao dịch, tên người dùng, số tiền, trạng thái) từ mỗi dòng nhật ký.
#
# Sử dụng re.findall() để tìm tất cả các giao dịch trong tệp nhật ký mẫu.
#
# In ra kết quả dưới dạng một danh sách các dictionary, mỗi dictionary chứa thông tin của một giao dịch, có dạng như sau:
#
# {
#   "time": "2023-10-27 14:30:05",
#   "level": "INFO",
#   "id": "1a2b3c4d",
#   "user": "Alice",
#   "amount": "150",
#   "status": "SUCCESS"
# }
#
# [2023-10-27 14:30:05] INFO - Transaction ID: 1a2b3c4d, User: Alice, Amount: 150, Status: SUCCESS
# [2023-10-27 14:30:05] INFO - Transaction ID: 1a2b3c4e, User: Bob, Amount: 50, Status: FAIL
import re

log_text = """
[2023-10-27 14:30:05] INFO - Transaction ID: 1a2b3c4d, User: Alice, Amount: 150, Status: SUCCESS
[2023-10-27 14:30:05] INFO - Transaction ID: 1a2b3c4e, User: Bob, Amount: 50, Status: FAIL
"""

pattern = re.compile(
    r"\[(?P<time>[\d\-:\s]+)\]\s+"
    r"(?P<level>\w+)\s+-\s+"
    r"Transaction ID:\s(?P<id>[a-z0-9]+),\s"
    r"User:\s(?P<user>\w+),\s"
    r"Amount:\s(?P<amount>\d+),\s"
    r"Status:\s(?P<status>\w+)"
)

matches = pattern.findall(log_text)

result = []
for m in matches:
    transaction = {
        "time": m[0],
        "level": m[1],
        "id": m[2],
        "user": m[3],
        "amount": m[4],
        "status": m[5]
    }
    result.append(transaction)

print(result)

from datetime import datetime


format_ = "%d-%m-%Y"
timestamp = datetime.timestamp(datetime.strptime("12-07-2022", format_))
print(timestamp)
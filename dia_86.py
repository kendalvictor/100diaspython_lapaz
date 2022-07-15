from datetime import datetime


format_ = "%d/%m/%Y"
diff_ = datetime.now().date() - datetime.strptime("20/04/2022", format_).date()
print(diff_.total_seconds())
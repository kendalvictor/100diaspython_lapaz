from datetime import datetime


init ='%b %d %Y %H:%M%p'
new = '%Y-%m-%d %H:%M:%S'
format_ = datetime.strptime("Jul 11 2022 1:30AM", init).strftime(new)
                                                                               
print(format_)
    
    
   
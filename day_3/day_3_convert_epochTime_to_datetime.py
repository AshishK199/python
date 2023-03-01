import datetime

epoch_time = 80246891
print("epoch time time is : {}".format(epoch_time))
dt_modification = datetime.datetime.fromtimestamp(epoch_time)
print("Modification time is : {}".format(dt_modification))
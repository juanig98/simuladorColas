from mm1 import MM1
from mms import MMS

# mm1 = MM1(service_rate=2,arrival_rate=1)
# mm1.graf()
# mm1 = MM1(service_rate=6,arrival_rate=4)
# mm1.graf()

# mms = MMS(service_rate=3, arrival_rate=8, num_servers=3)
# mms = MMS(service_rate=10, arrival_rate=20, num_servers=3)
# mms = MMS(service_rate=5, arrival_rate=8, num_servers=2)
mms = MMS(service_rate=5, arrival_rate=16, num_servers=4)
mms.graf()
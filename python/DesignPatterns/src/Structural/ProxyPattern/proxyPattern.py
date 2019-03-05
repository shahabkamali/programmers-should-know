import time

class Producer:
    """Define the 'resource-intensive' objects to instantiate! """
    def produce(self):
        print("Producer is working hard!")

    def meet(self):
        print("Producer has time to meet you now!")


class Proxy():
    """Define the 'relativley less resource-intensive' proxy to instantiate as a middleman"""
    def __init__(self):
        self.occupied = 'No'
        self.producer = None

    def produce(self):
        """ check if producer is available"""
        print ("Artist checking if Producer is availbale")

        if self.occupied == 'No':
            # If the producer is available, create a producer object!
            self.producer = Producer()
            time.sleep(2)

            #make the produver meet the guest!
            self.producer.meet()

        else:
            # otherwise, dont instantiate a producer

            time.sleep(2)
            print("Producer is busy!")
 
# instantiate a Proxy
p = Proxy()

#Make the proxy: artist produce until Producer is available

p.produce()

#Change the state to 'occupied'
p.occupied = 'Yes'

#Make the Producer produce

p.produce()

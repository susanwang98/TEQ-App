from abc import ABC

class Observable(ABC):
    '''
    Abstract object that will notify observers
    '''
    
    def __init__(self):
        ''' (Observable) -> None
        
        Initialize an Observable object
        '''
        self.observers = []

    def raise_event(self):
        ''' (Observable) -> None
        
        Notifys all Observers
        '''
        for obs in self.observers:
            obs.notify(self)

    def add_observer(self, observer):
        ''' (Observable, Observer) -> None
        
        Adds an Observer from the Observables list
        of Observers to be notified
        '''
        self.observers.append(observer)

    def remove_observer(self, observer):
        ''' (Observable, Observer) -> None
        
        Removes an Observer from the Observables list
        of Observers to be notified
        '''
        self.observers.remove(observer)

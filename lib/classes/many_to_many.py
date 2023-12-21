class NationalPark:

    def __init__(self, name):
        self._name = name
    @property
    def name(self):
        return self._name
    @name.getter
    def name(self):
        return self._name
    @name.setter
    def name(self,name):
        if not hasattr(self,'name') and isinstance(name,str) and len(name)>=3:
            self._name = name
    
        
    def trips(self):
        trips_li = []
        for trip in Trip.all:
            if trip.national_park == self:
                trips_li.append(trip)
        return trips_li


    def visitors(self):
        unique_visitors = set()
        for trip in self.trips():
            unique_visitors.add(trip.visitor)
        return list(unique_visitors)
    # def visitors(self):
    #     visitors_li = []
    #     for trip in Trip.all:
    #         if trip.national_park == self:
    #             visitors_li.append(trip.visitor)
    #     return visitors_li
                
                
    
    def total_visits(self):
        return len(self.trips())
    
    def best_visitor(self):
        visitors_dict = {}
        for trip in self.trips():
            visitor = trip.visitor
            if visitor in visitors_dict:
                visitors_dict[visitor] += 1
            else:
                visitors_dict[visitor] = 1

        if visitors_dict:
            best_visitor = max(visitors_dict, key=visitors_dict.get)
            return best_visitor
        else:
            return None


class Trip:
    all = []
    def __init__(self, visitor, national_park, start_date, end_date):
        self.visitor = visitor
        self.national_park = national_park
        self.start_date = start_date
        self.end_date = end_date
        Trip.all.append(self)
    @property
    def start_date(self):
        return self._start_date
    @start_date.getter
    def start_date(self):
        return self._start_date
    @start_date.setter
    def start_date(self,val):
        if isinstance(val,str) and len(val) >= 7:
            self._start_date = val
    @property
    def end_date(self):
        return self._end_date
    @end_date.getter
    def end_date(self):
        return self._end_date
    @end_date.setter
    def end_date(self,val):
        if isinstance(val,str) and len(val) >= 7:
            self._end_date = val

class Visitor:
    def __init__(self, name):
        self._name = name
    @property
    def name(self):
        return self._name
    @name.getter
    def name(self):
        return self._name
    @name.setter
    def name(self,name):
        if isinstance(name,str) and 1 <=len(name)<=15:
            self._name = name
        
       
    
        
    def trips(self):
        trips_li = []
        for trip in Trip.all:
            if trip.visitor == self:
                trips_li.append(trip)
        return trips_li
    
    # def national_parks(self):
    #     national_parks = set()
    #     for trip in Trip.all:
    #         national_parks.add(trip.national_park)
    #     return list(national_parks)
    def national_parks(self):
        national_parks = set()
        for trip in self.trips():
            national_parks.add(trip.national_park)
        return list(national_parks)
    
    def total_visits_at_park(self, park):
        total_visits = 0
        for trip in self.trips():
            if trip.national_park == park:
                total_visits += 1
        return total_visits
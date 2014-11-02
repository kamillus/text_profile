import json

#user profile class used to store the datapoints of the user
class ProfileData(object):
    data_points = []
    name = ""
    
    def __init__(self):
        pass
        
    def set_name(self, name):
        self.name = name
        
    def append_point(self, point):
        self.data_points.append(point)
        
    def load_data(self):
        pass
        
    def flush(self):
        f = open('data', 'w')
        output = {self.name:[]}
        
        for point in self.data_points:
            output[self.name].append({"time": point.time, 
                "error_count": point.error_count, 
                "distance": point.distance,
            })
        
        f.write(json.dumps(output))
        
class DataPoint(object):
    def __init__(self, time=0, error_count=0, distance=0):
        self.time = time
        self.error_count = error_count
        self.distance = distance
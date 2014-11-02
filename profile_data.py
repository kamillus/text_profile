import json

class Profiles(object):
    def __init__(self):
        self.profiles = {}
        self.load_data()

    
    def load_data(self):
        try:
            data = json.loads(open('data', 'r').read())
            for key, datum in data.iteritems():
                self.profiles[key] = ProfileData()
                self.profiles[key].set_name(key)
                for point in datum:
                    self.profiles[key].append_point(DataPoint(point["time"], point["error_count"], point["distance"]))
        except Exception as e:
             print e
    
    def append_profile(self, profile):
        self.profiles[profile.name] = profile
                
    def flush(self):
        f = open('data', 'w')
        output = {}
        
        for key, profile in self.profiles.iteritems():
            output[profile.name] = []
            for point in profile.get_points():
                output[profile.name].append({"time": point.time, 
                    "error_count": point.error_count, 
                    "distance": point.distance,
                })
        
        f.write(json.dumps(output))
        
    def get_classifier_data(self):
        points = []
        targets = []
        
        for key, profile in self.profiles.iteritems():
            for point in profile.data_points:
                points.append([point.time, point.error_count, point.distance])
                targets.append(profile.name)
                
        return (points, targets)
            


#user profile class used to store the datapoints of the user
class ProfileData(object):
    def __init__(self):
        self.data_points = []

    def set_name(self, name):
        self.name = name
        
    def append_point(self, point):
        self.data_points.append(point)

    def get_points(self):
        return self.data_points

        
class DataPoint(object):
    def __init__(self, time=0, error_count=0, distance=0):
        self.time = time
        self.error_count = error_count
        self.distance = distance
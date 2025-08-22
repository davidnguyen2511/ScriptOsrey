import csv
from datetime import datetime
import glob
import os
import time
import random

def himmelblau(x, y):
    """Calculate the Himmelblau function value for a given (x, y) pair."""
    x = 6*x/1000 - 6
    y = 6*y/1000 -6
    return (x**2 + y - 11)**2 + (x + y**2 - 7)**2

def generate_random_point():
    """Generate a random point (x, y) within the range [-5, 5]."""
    x = random.randint(0,2000)
    y = random.randint(0,2000)
    return x, y

def getPoint():
    # Generate two random points
    point1 = generate_random_point()
    point2 = generate_random_point()
    
    # Calculate the Himmelblau function values for both points
    value1 = himmelblau(*point1)
    value2 = himmelblau(*point2)
    return point1 if value1 < value2 else point2

def getErrorPoint():
    if random.random() > 0.3:
        return ""
    # Generate a random number of points (between 1 and 10)
    num_points = 1
    while random.random() > 0.5:
        num_points += 1
    
    points = []
    
    for _ in range(num_points):
        point = getPoint()
        
        # Add point to the list in the format "x,y"
        points.append(f"{point[0]}:{point[1]}")
    
    # Join all points with ";" separator and return the result
    return ";".join(points)

class CSVManager:
    def __init__(self, filename):
        self.filename = filename
        self.rows = []

    def write_data(self, row, col, data):

        max_cols = max(len(r) for r in self.rows) if self.rows else 0
        while len(self.rows) <= row:
            self.rows.append([""] * max_cols)

        for r in self.rows:
            while len(r) <= col:
                r.append("")

        self.rows[row][col] = data

        

    def saveFile(self):
        with open(self.filename, mode='w', newline='') as file:
            writer = csv.writer(file)
            writer.writerows(self.rows)

class FakeDataManager():
    def __init__(self):
        path_file = r"D:/AppRelease/OspreyInspectFolder8"
        self.csv_manager = CSVManager(path_file + "/Generated_Lot_" + datetime.now().strftime("%Y%m%d%H%M%S") + ".csv")

        # Writing data to specific row and column based on the uploaded CSV structure
        self.csv_manager.write_data(0, 0, "Name")
        self.csv_manager.write_data(0, 1, "Value")
        self.csv_manager.write_data(1, 0, "Lot ID")
        self.csv_manager.write_data(1, 1, "A1B2C3dF")
        self.csv_manager.write_data(2, 0, "Operator ID")
        self.csv_manager.write_data(2, 1, "a")
        self.csv_manager.write_data(3, 0, "Recipe Name")
        self.csv_manager.write_data(3, 1, "2_S_Spherical_ver1.3_1D")
        self.csv_manager.write_data(4, 0, "System ID")
        self.csv_manager.write_data(4, 1, "machine 9")
        self.csv_manager.write_data(5, 0, "Image Directory")
        self.csv_manager.write_data(5, 1, "D:\\Projects\\ED\\C#\\SEED\\App Config\\Images")
        self.csv_manager.write_data(6, 0, "Start Lot")
        self.csv_manager.write_data(6, 1, datetime.now().strftime("%Y:%m:%d:%H:%M:%S"))

        self.csv_manager.write_data(9, 0, "Statictis")
        self.csv_manager.write_data(9, 1, "Value")

        self.csv_manager.write_data(10, 0, "Inspected")
        self.csv_manager.write_data(11, 0, "Passed")
        self.csv_manager.write_data(12, 0, "ML Passed")
        self.csv_manager.write_data(13, 0, "Yield %")
        self.csv_manager.write_data(14, 0, "Failed")
        self.csv_manager.write_data(15, 0, "Lot ID")

        self.csv_manager.write_data(10, 1, "1000")
        self.csv_manager.write_data(11, 1, "990")
        self.csv_manager.write_data(12, 1, "95")
        self.csv_manager.write_data(13, 1, "0.672216")
        self.csv_manager.write_data(14, 1, "81")

        self.defectList = ["Lens Location Defect","Diameter Defect","Non Circular Defect","Multiple Lens Defect","Edge Chip-off","Edge Tear","Flash Edge Defect","Edge Thickness","Surface Scratch Defect","Fiber Defect","Polymer Bubble","Dark Spot Defect","Whitening Defect","Incorrect Marking","Light Intensity","Foreign Material on Shell","Broken Edge DF", "Pass", "Pass"]

        for idx, eachDefect in enumerate(self.defectList):
            self.csv_manager.write_data(15+idx, 0, eachDefect)
            self.csv_manager.write_data(15+idx, 1, random.randint(1000,100000))

        columns = [
            "No", "Image Name", "Vision Result", "ML Result", "Final Result", "Result Inspected",
            "Lens Location Defect", "Diameter Defect", "Non Circular Defect", "Multiple Lens Defect", 
            "Edge Chip-off", "Edge Tear", "Flash Edge Defect", "Edge Thickness", "Surface Scratch Defect", 
            "Fiber Defect", "Polymer Bubble", "Dark Spot Defect", "Whitening Defect", "Incorrect Marking", 
            "Light Intensity", "Foreign Material on Shell", "Broken Edge DF", "Inspection time(ms)", 
            "Lens Center", "Lens Radius"
        ]

        # Write column names first
        for index, column in enumerate(columns):
            self.csv_manager.write_data(35, index, column)
        self.counter = 36

    

    def fakeInspect(self):
        for idx, eachDefect in enumerate(self.defectList): # change the conter in the statistict
            self.csv_manager.write_data(15+idx, 0, eachDefect)
            self.csv_manager.write_data(15+idx, 1, random.randint(1000,100000))
    
        self.csv_manager.write_data(self.counter,0,self.counter-36)
        self.csv_manager.write_data(self.counter,1,"Image_"+str(self.counter-36))
        self.csv_manager.write_data(self.counter,2,"True" if random.random()>0.5 else "False")
        self.csv_manager.write_data(self.counter,3,"True" if random.random()>0.5 else "False")
        self.csv_manager.write_data(self.counter,4,"True" if random.random()>0.5 else "False")
        self.csv_manager.write_data(self.counter,5,self.defectList[random.randint(0,len(self.defectList)-1)]) # Result inspect

        self.csv_manager.write_data(self.counter,6,"" if random.random()>0.1 else "False")
        self.csv_manager.write_data(self.counter,7,"" if random.random()>0.1 else "False")
        self.csv_manager.write_data(self.counter,8,"" if random.random()>0.1 else "False")
        self.csv_manager.write_data(self.counter,9,"" if random.random()>0.1 else "False")
        self.csv_manager.write_data(self.counter,19,"" if random.random()>0.1 else "False")
        self.csv_manager.write_data(self.counter,20,"" if random.random()>0.1 else "False")

        
        for i in range(13):
            if i+10 == 19 or i+10 == 20:
                continue
            self.csv_manager.write_data(self.counter,10 + i,getErrorPoint())

        self.csv_manager.write_data(self.counter,23,random.randint(200,500))
        self.csv_manager.write_data(self.counter,24,str(random.randint(900,1100))+":"+str(random.randint(900,1100)))
        self.csv_manager.write_data(self.counter,25,random.randint(800,900))
        self.counter += 1
        self.csv_manager.saveFile()

    def closeLot(self):
        self.csv_manager.write_data(7, 0, "End Lot")
        self.csv_manager.write_data(7, 1, datetime.now().strftime("%Y:%m:%d:%H:%M:%S"))
        self.csv_manager.saveFile()

def delete_oldest_csv(folder_path):
    # Get all CSV files in the folder
    csv_files = glob.glob(os.path.join(folder_path, "*.csv"))
    
    # Check if the number of CSV files is greater than 10
    if len(csv_files) > 5:
        # Sort the files by modified time (oldest first)
        csv_files.sort(key=lambda x: os.path.getmtime(x))
        
        # Delete the oldest CSV file
        oldest_file = csv_files[0]
        os.remove(oldest_file)
        return True
    else:
        return False



if __name__ == "__main__":
    initFile = 0
    for i in range(initFile):
        data = FakeDataManager()
        for _ in range(random.randint(1000,2000)):
            data.fakeInspect()
        data.closeLot()

    while True:
        data = FakeDataManager()
        for _ in range(random.randint(2000,3000)):
            data.fakeInspect()
            time.sleep(0.3)
        data.closeLot()
        while delete_oldest_csv("./"):
            pass
        print("Lot closed at " + datetime.now().strftime("%Y:%m:%d - %H:%M:%S"))
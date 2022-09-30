import csv
from pathlib import Path

def ReadSensorReadings( file ):
    if CheckPathAndFileExists(file):        
        with open(file, mode='r') as csv_file:
            SensorReadings = csv.reader(csv_file, delimiter=',')
            return   SeperateParameterFromCsvFile(SensorReadings)                    
    else :
        return False

def SeperateParameterFromCsvFile(SensorReadings):
    BatteryTemperatureValues = []
    BatterySoCValues = [] 
    SensorReadingCount = 0
    for Value in SensorReadings:
        SensorReadingCount +=1
        PrintOnConsole(f'{Value[0]},{Value[1]}')
        BatteryTemperatureValues.append(Value[0])
        BatterySoCValues.append(Value[1])
    PrintOnConsole(f'Sensor Reading Count is {SensorReadingCount-1}')
    return BatteryTemperatureValues,BatterySoCValues

def PrintOnConsole(PrintData):
    print(PrintData)

def CheckPathAndFileExists(CSVfilename):
    path = Path(Path.cwd()/CSVfilename)
    
    if(path.exists()):
        if path.is_file():
            return True    
    return False
 

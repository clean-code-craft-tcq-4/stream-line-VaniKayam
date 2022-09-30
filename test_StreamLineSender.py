import unittest
import StreamLine_Sender 

Invalid_CSVfile = 'InvalidCSVfile.csv'
Valid_CSVfile = 'SensorParameterReadings.csv'
Valid_CSVTestFilePath = 'Test_CSVfilePath/test.csv'
InValid_CSVTestFilePath = 'Test_CSVfilePaths/test.csv'

class StreamLine_Sender_TestCase(unittest.TestCase):
    def test_FileExistance_CSVfile(self):
        self.assertFalse(StreamLine_Sender.CheckPathAndFileExists(Invalid_CSVfile))
        self.assertTrue(StreamLine_Sender.CheckPathAndFileExists(Valid_CSVfile))   
        self.assertTrue(StreamLine_Sender.CheckPathAndFileExists(Valid_CSVTestFilePath))
        self.assertFalse(StreamLine_Sender.CheckPathAndFileExists(InValid_CSVTestFilePath))
        
    def test_ReadSensorReadings(self):
        
        Test_file_data = StreamLine_Sender.ReadSensorReadings(Valid_CSVfile)
        self.assertTrue(Test_file_data[0][0] == ("Temperature"))
        self.assertTrue(Test_file_data[1][0] == ("SOC"))
        self.assertTrue(Test_file_data[0][1] == ("56"))
        self.assertTrue(Test_file_data[0][2] == ("24"))
        self.assertTrue(Test_file_data[1][1] == ("59"))
        self.assertTrue(Test_file_data[1][2] == ("55"))
        self.assertFalse(Test_file_data[0][0] == ("SOC"))
        self.assertFalse(Test_file_data[1][2] == ("57"))

if __name__ == "__main__": 
    unittest.main()

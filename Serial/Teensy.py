import serial
import time

class Teensy():
    def __init__(self):
        self.board = '/dev/ttyACM0'
        self.baud = 9600
        self.commands = []
        print("=====================Teensy Init===================================")
        print(f"Teensy board {self.board} has been initiated. See /dev/ttyACM0 on arduino IDE for board details")
        print(f"Baud Rate: {self.baud} bits per second")
        print("===================================================================")
    
    def aggregateCommands(self, input):
        '''Collect a list of commands to pass to the Teensy'''
        self.commands.append(input)

    def sendCommands(self):
        '''Send Commands to the Teensy using Serial Communication'''
        ser = serial.Serial('/dev/ttyACM0', self.baud, timeout=1)
        ser.reset_input_buffer()

        for i in range(len(self.commands)):
            specificCommand = self.commands[i]
            ser.write(specificCommand)
            line = ser.readline().decode('utf-8').rstrip()
            print(line)
            time.sleep(1)

    def teensyStatus():
        '''Gather state of teensy from GPIO pins (ready to run, running, idle, or error)'''
        pass

        


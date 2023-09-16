import serial
import time

class Teensy():
    def __init__(self):
        self.board = '/dev/ttyACM0'
        self.baud = 9600
        self.commands = []
        print("=====================Teensy Init===================================")
        print(f"Teensy board {self.board} has been initiated. See {self.board} on arduino IDE for board details")
        print(f"Baud Rate: {self.baud} bits per second")
        print("===================================================================")
    
    def aggregateCommands(self, input):
        '''Collect a list of commands to pass to the Teensy'''
        self.commands.append(input)

    def sendCommands(self):
        '''Send Commands to the Teensy using Serial Communication'''
        print(self.commands)
        ser = serial.Serial(self.board, self.baud, timeout=1)

        for i in range(len(self.commands)):
            ser.reset_input_buffer()
            specificCommand = self.commands[i]
            print(specificCommand)
            ser.write(bytes(str(specificCommand),'utf-8'))
            line = ser.readline().decode('utf-8').rstrip()
            print("Teensy received command")
            time.sleep(0.5)

    def teensyStatus():
        '''Gather state of teensy from GPIO pins (ready to run, running, idle, or error)'''
        pass

        


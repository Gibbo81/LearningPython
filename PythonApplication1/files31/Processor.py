class Processor():
    def __init__(self, reader, writer):
        self.reader = reader
        self.writer = writer

    def process(self):
        while True:
            data=self.reader.readline()#.read()
            if not data: 
                break
            data= self.Converter(data)
            self.writer.write(data)
    
    def Converter(self, data):
        assert false, 'converter must be defined'





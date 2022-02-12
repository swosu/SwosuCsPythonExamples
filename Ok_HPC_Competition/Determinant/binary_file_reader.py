class binary_file_reader:


    def __init__(self):
        self.sum_ = 0
        self.file_name = ''

    def get_sum(self,num1,num2):
        self.sum_ = num1+num2
        return self.sum_

    def load_matrix(self,matrix_side_length):
        import os.path

        self.file_name = self.get_file_name(matrix_side_length)
        print(self.file_name)
        if os.path.isfile(self.file_name):
            print ("File exist")
        else:
            print ("File not exist")
            self.download_file(self.file_name)

    def get_file_name(self, matrix_side_length):
        #m0016x0016.bin
        short_nugget = str(matrix_side_length).zfill(4)
        self.file_name = "m" + short_nugget + 'x' + short_nugget + '.bin'
        return self.file_name

    def download_file(self, file_name):
        #https://www.tutorialspoint.com/downloading-files-from-web-using-python
        import requests

        url = 'http://morpheus.mcs.utulsa.edu/~papama/hpc/' + file_name
        r = requests.get(url, allow_redirects=True)
        open(file_name, 'wb').write(r.content)

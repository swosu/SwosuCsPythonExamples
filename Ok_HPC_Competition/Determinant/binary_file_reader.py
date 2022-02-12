class binary_file_reader:


    def __init__(self):
        self.sum_ = 0
        self.file_name = ''
        self.matrix = []

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
            print ("File not exist, attempting download")
            self.download_file(self.file_name)
            self.load_matrix(matrix_side_length)
        self.matrix = self.read_matrix(matrix_side_length, self.file_name)
        #print(self.matrix)
        return self.matrix

    def read_matrix(self, matrix_side_length, file_name):
        print(f'loading matrix: {file_name}')
        import numpy as np
        import os.path
        if os.path.isfile(file_name):
            print (f'File exists: {file_name}.')
            self.matrix = np.fromfile(file_name,  dtype=np.float64, count = -1)
            #print(self.matrix)
            self.matrix = np.reshape(self.matrix, (matrix_side_length, matrix_side_length))
            #print(self.matrix)
            return self.matrix
        else:
            print('\n\n\n SOMETHING IS WRONG, FILE IS MISSING!!! RETRY !!!\n\n\n')
            self.load_matrix(matrix_side_length)


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

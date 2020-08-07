import json, os, subprocess, sys
from PyPDF2 import PdfFileReader, PdfFileWriter

"""
    USAGE 
    1. Ensure You have only the pdf file you want to extract in the folder
    2. 

"""


class CheckPackages:
    packages = [
        'PyPDF2'
    ]
    def __init__(self):

        try:
            import pip
        except ModuleNotFoundError:
            os.system('python mypip.py')

        for package in self.packages:
            try:
                import package
            except ModuleNotFoundError as e:
                self.intall_libry(package)

    def intall_libry(self, tool_name):
        subprocess.check_call([sys.executable, "-m", "pip", "install", tool_name])

    # make inport for the next class
    from PyPDF2 import PdfFileReader, PdfFileWriter


class PDFExtract:

    # packages = [
    #     'PyPDF2'
    # ]
    file_ext=''
    pdf_files = []
    readers = []

    def __init__(self, file_ext):

        packa = CheckPackages()

        self.file_ext = file_ext
        self.pdf_files = self.get_files_by_ext()

        for pdf_file in self.pdf_files:
                self.readers.append(PdfFileReader(pdf_file, 'r'))

        # Check wether pip is installed else install mypip.py
        # try:
        #     import pip
        # except ModuleNotFoundError:
        #     os.system('python mypip.py')

        # iterate through the packages and install the ones not installed
        # reqs = subprocess.check_output([sys.executable, '-m', 'pip', 'freeze'])
        # installed_packages = [r.decode().split('==')[0] for r in reqs.split()]

        # for package in self.packages:
        #     try:
        #         import package
        #     except ModuleNotFoundError as e:
        #         self.intall_libry(package)
                


    # Call the below method only once   
    # def intall_libry(self, tool_name):
    #     subprocess.check_call([sys.executable, "-m", "pip", "install", tool_name])

    def get_files_by_ext(self):
        extracted_files= []
        dir_files = os.listdir(os.path.dirname(os.path.realpath(__file__)))
        for file in dir_files:
            for y in range(1, 6):
                if file[-y:]==self.file_ext:
                    extracted_files.append(file)    
        return extracted_files

    def load_pages(self, start_page, end_page):
        if len(self.pdf_files)==1:
            for i in range(start_page, end_page):
                pageText = self.readers[0].getPage(i).extractText().split()
                print(pageText)
        else:
            print('Provide One PDF file at a time')
        #return self.readers

pdf = PDFExtract('pdf')
print(pdf.load_pages(2,3))
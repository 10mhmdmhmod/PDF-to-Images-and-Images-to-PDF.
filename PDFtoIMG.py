from pdf2image import convert_from_path
from tkinter import Tk
from tkinter.filedialog import askopenfilename
from tkinter.filedialog import askdirectory


print=("HI,This is PDF to IMAGE "
       "BY Mohamed Mahmod"+"\n"+
         "Please Choose file")
Tk().withdraw()
user_pdf_path = askopenfilename()

print=("Now Please Choose output location ")
Tk().withdraw()
user_outpot_path = askdirectory()

# pdf 2 image functions
convert_from_path(
    pdf_path=user_pdf_path,
    dpi=200,
    output_folder=user_outpot_path,
    first_page=None,
    last_page=None,
    fmt="png",
    jpegopt=None,
    thread_count=1,
    userpw=None,
    use_cropbox=False,
    strict=False,
    transparent=False,
    single_file=False,
    #output_file=uuid_generator(),
    poppler_path=None,
    grayscale=False,
    size=None,
    paths_only=False,)
# Basic sys.argv -> OOP

# argv is a util of the sys lib
import sys
import os

# Local_
from File_Man import File_Man

# Create a class object too keep code clean
class ShowArgv():
    def __init__(self):
        self.FM = File_Man()
        self.header_ = f"<!DOCTYPE html>\
        <html lang='en'>\
        <head>\
        <meta charset='UTF-8'>\
        </head><body>"
        self.footer_ = "</body></html>"




        # STYLE PER LINE
    def set_tags_(self, line_, style_):
        try:
            style_tag = "style='border-radius: 35px; background: #5dff00 ; padding: 20px; ' "
            ret_ = ""
            if "&" in str(line_):
                r_ = line_.replace("& ", "")
                ret_ = f"<img src='{r_}' {style_tag} ><br>"
                print("[IMG]:",str(ret_))


            if "%" in str(line_):
                r_ = str(line_[2:])
                ret_ = f"<pre>{r_}</pre><br>"
                print("[CODE]:",str(ret_))


            elif "#" in str(line_):
                rt_ = line_.replace("#", "")
                ret_ = f"<h1 {style_tag} >{rt_}</h1><br>"
                print("[HEAD]:",str(ret_))


            elif "-" in str(line_):
                rt_ = f"<h3 {style_tag} >{line_}</h3><br>"
                ret_ = rt_.replace("-", "")
                print("[LST]:",str(ret_))


            elif "@" in str(line_):
                pre_ = str(str(line_[1:]).split(" ")[0])
                post_ = str(str(line_).replace(f"{pre_}", ""))
                rt_ = f"<p {style_tag} ><a href='http://{pre_}' >{post_}</a></p><br>"
                ret_ = rt_.replace("@", "")
                print("[FTR]:",str(ret_))

            if ret_ != None:
                return ret_
        except Exception as e:
            print(f"[E]:[SET_STYLE]:[{str(e)}]")




    # open given file name
    def read_that_file(self, f_name, out_f, to_pdf):
        try:
            ret_ = ""
            build_html = []
            # Add header
            build_html.append(str(self.header_))
            f_data = self.FM.read_file(f_name, "\n")
            for i, val_ in enumerate(f_data):
                # Add fontified Line
                cVal = val_.translate( { ord(i): None for i in "\n"} )
                if len(cVal) > 2:
                    try:
                        ret_ = self.set_tags_(str(cVal), "")
                    except Exception as e:
                        print(f"[E]:[set_tags]:[{str(e)}]")
                    if ret_:
                        get_line_ = str(ret_)+"\n"
                        build_html.append(get_line_)

            # Add Footer
            build_html.append(str(self.footer_))

            # TURN INTO STR
            fine_ = ""
            for j, vai_ in enumerate(build_html):
                print(">>",str(vai_))
                fine_ += str(vai_)

            # Write to the new file
            self.FM.write_file(out_f, fine_, "", "w")


            # pandoc reports/7/report.html -o reports/7/report.pdf
            #to_doc = f"weasyprint -e utf-8  {out_f}  {to_pdf}"
            to_doc = f"pisa {out_f}  {to_pdf}"
            os.system(to_doc)


        except Exception as e:
            print(f"[E]:[READ_THAT]:[{str(e)}]")





    # create a function to enumerate the arguments
    '''
    argv[1] = file_in.txt
    argv[2] = file_out.html
    argv[3] = file.pdf
    '''
    def get_args(self, args_):
        for i, ar_ in enumerate(args_):
            print(f"[{str(i)}]:[{str(ar_)}]")
        #print(f"[number of args]:[{str(len(sys.argv))}]")
        file_in  = str(args_[1])



        if len(args_) > 2:
            file_out = str(args_[2])
        else:
            file_out = str(args_[1]).replace(".txt", ".html")
        if len(args_) > 3:
            to_pdf   = str(args_[3])
        else:
            to_pdf = str(args_[1]).replace(".txt", ".pdf")


        print("File_To_read : ", file_in)
        self.read_that_file(file_in, file_out, to_pdf)



# To use an Object Callback (function)
if __name__=="__main__":
    # - You must first Initialize the Object
    SA = ShowArgv()
    if sys.argv:
        # run the callback
        SA.get_args(sys.argv)



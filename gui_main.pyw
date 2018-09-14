import os, sys

from tkinter import *
from tkinter import filedialog, ttk
from tkinter.scrolledtext import ScrolledText

from huffman_encoder import (
    encode_bin,
    decode_bin
)

class CompressFrame(Frame):
    def __init__(self):
        super().__init__()
        self.render_select_file_section()

    def render_select_file_section(self):
        self.title_label = Label(self, bg='#ffffff', text='COMPRESSION', anchor=CENTER, relief=FLAT)
        self.title_label.grid(row=0, column=0, columnspan=2, padx=12, pady=10, sticky=W+E+N+S)


        self.input_file_entry = Entry(self, width=50, relief=FLAT, bg='#eee', fg='#333',
                                      selectbackground='#ffffff', selectforeground='#333',
                                      validate='key', exportselection=False)
        self.input_file_entry.grid(row=1, column=0, padx=(12, 6), pady=6, ipadx=12, ipady=6)
        self.input_file_entry.delete(0, END)
        self.input_file_entry.insert(0, ' Select File for Compression')
        vcmd = (self.register(self.validate_input_path), '%P')
        self.input_file_entry.config(validatecommand=vcmd)


        self.select_file_btn = Button(self, text='Select File', command=self.select_btn_callback,
                                      relief=FLAT, bg='#3267ef', fg='#fff', width=11)
        self.select_file_btn.grid(row=1, column=1, padx=(6, 12), pady=6, ipadx=12, ipady=3)


        self.compress_file_btn = Button(self, text='Compress File', command=self.compress_btn_callback,
                                        relief=FLAT, bg='#ddd', fg='#fff', disabled='#666', 
                                        state=DISABLED)
        self.compress_file_btn.grid(row=2, column=0, columnspan=2, padx=12, pady=6, ipadx=12, ipady=3, sticky=W+E+N+S)

        
        self.status_label = Label(self, bg='#ffffff', text='---', anchor=W, relief=FLAT)
        self.status_label.grid(row=3, column=0, columnspan=2, padx=12, pady=6, ipadx=12, ipady=0, sticky=W+E+N+S)
        

        self.config(bg='#ffffff')
        # self.pack(ipadx=12, ipady=12)
        self.pack()

    def select_btn_callback(self):
        input_file_path = filedialog.askopenfilename()
        self.input_file_entry.delete(0, END)
        self.input_file_entry.insert(0, input_file_path)

    def validate_input_path(self, P):
        if os.path.isfile(P):
            self.compress_file_btn.config(state=NORMAL, relief=FLAT, bg='#1fc186')
        else:
            self.compress_file_btn.config(state=DISABLED, relief=GROOVE, bg='#ffffff')
        return True
    
    def compress_btn_callback(self):
        uncompressed_data = None
        with open(self.input_file_entry.get(), 'rb') as input_file:
            uncompressed_data = input_file.read()
        
        if uncompressed_data is None:
            self.status_label.config(text='ERROR: Could Not Open File!')

        compressed_data = encode_bin(uncompressed_data, True)
        
        if compressed_data is None:
            self.status_label.config(text='ERROR: Compression Failed!')

        dir_name = os.path.split(self.input_file_entry.get())[0]
        file_name = os.path.split(self.input_file_entry.get())[1]
        ext = file_name.split('.')[-1] if '.' in file_name else ''

        output_filepath = filedialog \
                          .asksaveasfilename(initialdir=dir_name,
                                             title="Save Compressed File",
                                             filetypes=(("Compressed File","*.hc1"),("all files","*.*")))

        output_filepath = output_filepath if output_filepath.split('.')[-1] == ext else output_filepath + '.' + ext
        output_filepath = output_filepath if output_filepath.split('.')[-1] == 'hc1' else output_filepath + '.hc1'
        
        with open(output_filepath, 'wb') as output_file:
            output_file.write(compressed_data)

        self.status_label.config(text='SUCCESS: File Compressed Successfully!')


class DecompressFrame(Frame):
    def __init__(self):
        super().__init__()
        self.render_select_file_section()

    def render_select_file_section(self):
        self.title_label = Label(self, bg='#ffffff', text='DECOMPRESSION', anchor=CENTER, relief=FLAT)
        self.title_label.grid(row=0, column=0, columnspan=2, padx=12, pady=10, sticky=W+E+N+S)

        
        self.input_file_entry = Entry(self, width=50, relief=FLAT, bg='#eee', fg='#333',
                                      selectbackground='#ffffff', selectforeground='#333',
                                      validate='key', exportselection=False)
        self.input_file_entry.grid(row=1, column=0, padx=(12, 6), pady=6, ipadx=12, ipady=6)
        self.input_file_entry.delete(0, END)
        self.input_file_entry.insert(0, ' Select File for Decompression')
        vcmd = (self.register(self.validate_input_path), '%P')
        self.input_file_entry.config(validatecommand=vcmd)


        self.select_file_btn = Button(self, text='Select File', command=self.select_btn_callback,
                                      relief=FLAT, bg='#3267ef', fg='#fff', width=11)
        self.select_file_btn.grid(row=1, column=1, padx=(6, 12), pady=6, ipadx=12, ipady=3)


        self.decompress_file_btn = Button(self, text='Decompress File', command=self.decompress_btn_callback,
                                        relief=FLAT, bg='#ddd', fg='#fff', disabled='#666', 
                                        state=DISABLED)
        self.decompress_file_btn.grid(row=2, column=0, columnspan=2, padx=12, pady=6, ipadx=12, ipady=3, sticky=W+E+N+S)

        
        self.status_label = Label(self, bg='#ffffff', text='---', anchor=W, relief=FLAT)
        self.status_label.grid(row=3, column=0, columnspan=2, padx=12, pady=6, ipadx=12, ipady=0, sticky=W+E+N+S)
        

        self.config(bg='#ffffff')
        # self.pack(ipadx=12, ipady=12)
        self.pack()

    def select_btn_callback(self):
        input_file_path = filedialog.askopenfilename()
        self.input_file_entry.delete(0, END)
        self.input_file_entry.insert(0, input_file_path)

    def validate_input_path(self, P):
        if os.path.isfile(P):
            self.decompress_file_btn.config(state=NORMAL, relief=FLAT, bg='#1fc186')
        else:
            self.decompress_file_btn.config(state=DISABLED, relief=GROOVE, bg='#ffffff')
        return True
    
    def decompress_btn_callback(self):
        compressed_data = None
        with open(self.input_file_entry.get(), 'rb') as input_file:
            compressed_data = input_file.read()
        
        if compressed_data is None:
            self.status_label.config(text='ERROR: Could Not Open File!')

        decompressed_data = decode_bin(compressed_data, True)
        
        if decompressed_data is None:
            self.status_label.config(text='ERROR: Decompression Failed!')

        dir_name = os.path.split(self.input_file_entry.get())[0]
        file_name = os.path.split(self.input_file_entry.get())[1]
        ext = file_name.split('.')[-2] if len(file_name.split('.')) > 2 else ''

        output_filepath = filedialog \
                          .asksaveasfilename(initialdir=dir_name,
                                             title="Save Decompressed File",
                                             filetypes=(("." + ext,"." + ext),("all files","*.*")))

        output_filepath = output_filepath if output_filepath.split('.')[-1] == ext else output_filepath + '.' + ext
        # output_filepath = output_filepath if output_filepath.split('.')[-1] == 'hc1' else output_filepath + '.hc1'
        
        with open(output_filepath, 'wb') as output_file:
            output_file.write(decompressed_data)
        
        self.status_label.config(text='SUCCESS: File Decompressed Successfully!')


def main():
    root = Tk()
    root.title('Compression Tool ~ Huffman Encoder Decoder')
    root.config(bg='#efefef')
    tabs = ttk.Notebook(root)

    compress_tab = CompressFrame()
    decompress_tab = DecompressFrame()
    
    tabs.add(compress_tab, text='Compress')
    tabs.add(decompress_tab, text='Decompress')
    tabs.pack(padx=6, pady=6)
    root.mainloop()


if __name__ == '__main__':
    main()

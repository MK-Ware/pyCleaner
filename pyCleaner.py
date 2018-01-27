#! /usr/bin/env python
#pyCleaner by Monro Coury
import sys
import os
import random
import shutil
import hashlib
from tkinter import filedialog, messagebox

try:
    from Tkinter import *
except ImportError:
    from tkinter import *

try:
    import ttk
    py3 = 0
except ImportError:
    import tkinter.ttk as ttk
    py3 = 1

if hasattr(sys, "_MEIPASS"):
    os.chdir(os.path.join(sys._MEIPASS))

import GUI_support

def wipeFile(f, passes=2):
    if not os.path.isfile(f):
        return "Could not find the specified file!"
    with open(f, "ba+") as f2w:
        size = f2w.tell()
        for i in range(passes):
            f2w.seek(0)
            f2w.write(os.urandom(size))
    new_name = str(random.randint(1000,1000000000000))
    os.rename(f, new_name)
    os.remove(new_name)
    return "Success!"

def md5(f):
    """takes one file f as an argument and calculates md5checksum for that file"""
    md5Hash=hashlib.md5()
    with open(f,'rb') as f:
        for chunk in iter(lambda: f.read(4096),b""):
            md5Hash.update(chunk)
    return md5Hash.hexdigest()

def vp_start_gui():
    '''Starting point when module is the main routine.'''
    global val, w, root
    root = Tk()
    GUI_support.set_Tk_var()
    top = PySecuWipe (root)
    GUI_support.init(root, top)
    root.mainloop()

w = None
def create_PySecuWipe(root, *args, **kwargs):
    '''Starting point when module is imported by another program.'''
    global w, w_win, rt
    rt = root
    w = Toplevel (root)
    GUI_support.set_Tk_var()
    top = PySecuWipe (w)
    GUI_support.init(w, top, *args, **kwargs)
    return (w, top)

def destroy_PySecuWipe():
    global w
    w.destroy()
    w = None


class PySecuWipe:
    def __init__(self, top=None):
        '''This class configures and populates the toplevel window.
           top is the toplevel containing window.'''
        _bgcolor = '#d9d9d9'  # X11 color: 'gray85'
        _fgcolor = '#000000'  # X11 color: 'black'
        _compcolor = '#d9d9d9' # X11 color: 'gray85'
        _ana1color = '#d9d9d9' # X11 color: 'gray85' 
        _ana2color = '#d9d9d9' # X11 color: 'gray85' 
        self.style = ttk.Style()
        if sys.platform == "win32":
            self.style.theme_use('winnative')
        self.style.configure('.',background=_bgcolor)
        self.style.configure('.',foreground=_fgcolor)
        self.style.configure('.',font="TkDefaultFont")
        self.style.map('.',background=
            [('selected', _compcolor), ('active',_ana2color)])

        top.geometry("526x443+480+140")
        top.title("PySecuWipe")
        top.configure(background="#d9d9d9")
        top.configure(highlightbackground="#d9d9d9")
        top.configure(highlightcolor="black")



        self.images = (

         PhotoImage("img_close", data='''R0lGODlhDAAMAIQUADIyMjc3Nzk5OT09PT
                 8/P0JCQkVFRU1NTU5OTlFRUVZWVmBgYGF hYWlpaXt7e6CgoLm5ucLCwszMzNbW
                 1v//////////////////////////////////// ///////////yH5BAEKAB8ALA
                 AAAAAMAAwAAAUt4CeOZGmaA5mSyQCIwhCUSwEIxHHW+ fkxBgPiBDwshCWHQfc5
                 KkoNUtRHpYYAADs= '''),

         PhotoImage("img_closeactive", data='''R0lGODlhDAAMAIQcALwuEtIzFL46
                 INY0Fdk2FsQ8IdhAI9pAIttCJNlKLtpLL9pMMMNTP cVTPdpZQOBbQd60rN+1rf
                 Czp+zLxPbMxPLX0vHY0/fY0/rm4vvx8Pvy8fzy8P//////// ///////yH5BAEK
                 AB8ALAAAAAAMAAwAAAVHYLQQZEkukWKuxEgg1EPCcilx24NcHGYWFhx P0zANBE
                 GOhhFYGSocTsax2imDOdNtiez9JszjpEg4EAaA5jlNUEASLFICEgIAOw== '''),

         PhotoImage("img_closepressed", data='''R0lGODlhDAAMAIQeAJ8nD64qELE
                 rELMsEqIyG6cyG7U1HLY2HrY3HrhBKrlCK6pGM7lD LKtHM7pKNL5MNtiViNaon
                 +GqoNSyq9WzrNyyqtuzq+O0que/t+bIwubJw+vJw+vTz+zT z////////yH5BAE
                 KAB8ALAAAAAAMAAwAAAVJIMUMZEkylGKuwzgc0kPCcgl123NcHWYW Fs6Gp2mYB
                 IRgR7MIrAwVDifjWO2WwZzpxkxyfKVCpImMGAeIgQDgVLMHikmCRUpMQgA7 ''')
        )

        self.style.element_create("close", "image", "img_close",
               ("active", "pressed", "!disabled", "img_closepressed"),
               ("active", "alternate", "!disabled",
               "img_closeactive"), border=8, sticky='')

        self.style.layout("ClosetabNotebook", [("ClosetabNotebook.client",
                                     {"sticky": "nswe"})])
        self.style.layout("ClosetabNotebook.Tab", [
            ("ClosetabNotebook.tab",
              { "sticky": "nswe",
                "children": [
                    ("ClosetabNotebook.padding", {
                        "side": "top",
                        "sticky": "nswe",
                        "children": [
                            ("ClosetabNotebook.focus", {
                                "side": "top",
                                "sticky": "nswe",
                                "children": [
                                    ("ClosetabNotebook.label", {"side":
                                      "left", "sticky": ''}),
                                    ]})]})]})])

        PNOTEBOOK = "ClosetabNotebook" 

        self.style.configure('TNotebook.Tab', background=_bgcolor)
        self.style.configure('TNotebook.Tab', foreground=_fgcolor)
        self.style.map('TNotebook.Tab', background=
            [('selected', _compcolor), ('active',_ana2color)])
        self.PNotebook1 = ttk.Notebook(top)
        self.PNotebook1.place(relx=0.0, rely=0.0, relheight=1.0, relwidth=1.0)
        self.PNotebook1.configure(width=534)
        self.PNotebook1.configure(takefocus="")
        self.PNotebook1.configure(style=PNOTEBOOK)
        self.PNotebook1_t0 = Frame(self.PNotebook1)
        self.PNotebook1.add(self.PNotebook1_t0, padding=3)
        self.PNotebook1.tab(0, text="PySecuWipe", compound="none", underline="-1"
                ,)
        self.PNotebook1_t0.configure(background="#d9d9d9")
        self.PNotebook1_t0.configure(highlightbackground="#d9d9d9")
        self.PNotebook1_t0.configure(highlightcolor="black")
        self.PNotebook1_t0.configure(width=530)
        self.PNotebook1_t1 = Frame(self.PNotebook1)
        self.PNotebook1.add(self.PNotebook1_t1, padding=3)
        self.PNotebook1.tab(1, text="PySpace",compound="none",underline="-1",)
        self.PNotebook1_t1.configure(background="#d9d9d9")
        self.PNotebook1_t1.configure(highlightbackground="#d9d9d9")
        self.PNotebook1_t1.configure(highlightcolor="#000000")

        self.wipe_files2 = ttk.Button(self.PNotebook1_t0, command=self.browse2WipeFile)
        self.wipe_files2.place(relx=0.04, rely=0.07, height=145, width=176)
        self.wipe_files2.configure(takefocus="")
        self.wipe_files2.configure(text='''Wipe File(s)''')

        self.wipe_dir1 = ttk.Button(self.PNotebook1_t0, command=self.browse2WipeDir)
        self.wipe_dir1.place(relx=0.6, rely=0.07, height=145, width=176)
        self.wipe_dir1.configure(takefocus="")
        self.wipe_dir1.configure(text='''Wipe Directory Contents''')

        self.TLabel1 = ttk.Label(self.PNotebook1_t0)
        self.TLabel1.place(relx=0.81, rely=0.93, height=29, width=91)
        self.TLabel1.configure(background="#d9d9d9")
        self.TLabel1.configure(foreground="#000000")
        self.TLabel1.configure(relief=FLAT)
        self.TLabel1.configure(text='''By Monro Coury''')

        self.Scrolledlistbox1 = ScrolledListBox(self.PNotebook1_t0)
        self.Scrolledlistbox1.place(relx=0.04, rely=0.45, relheight=0.44
                , relwidth=0.89)
        self.Scrolledlistbox1.configure(background="white")
        self.Scrolledlistbox1.configure(disabledforeground="#a3a3a3")
        self.Scrolledlistbox1.configure(font="TkFixedFont")
        self.Scrolledlistbox1.configure(foreground="black")
        self.Scrolledlistbox1.configure(highlightbackground="#d9d9d9")
        self.Scrolledlistbox1.configure(highlightcolor="#d9d9d9")
        self.Scrolledlistbox1.configure(selectbackground="#c4c4c4")
        self.Scrolledlistbox1.configure(selectforeground="black")
        self.Scrolledlistbox1.configure(width=10)
        self.Scrolledlistbox1.insert(0, "The files to be securely deleted will appear here...")

        self.wipe1 = ttk.Button(self.PNotebook1_t0, command = self.wipe)
        self.wipe1.place(relx=0.58, rely=0.9, height=25, width=76)
        self.wipe1.configure(takefocus="")
        self.wipe1.configure(text='''Wipe!''')

        self.help1 = ttk.Button(self.PNotebook1_t0, command=self.showWipeHelp)
        self.help1.place(relx=0.15, rely=0.9, height=25, width=76)
        self.help1.configure(takefocus="")
        self.help1.configure(text='''Help''')

        self.TButton5 = ttk.Button(self.PNotebook1_t1, command=self.browseDups)
        self.TButton5.place(relx=0.04, rely=0.07, height=35, width=486)
        self.TButton5.configure(takefocus="")
        self.TButton5.configure(text='''Choose a Directory''')
        self.TButton5.configure(width=486)

        self.Scrolledlistbox2 = ScrolledListBox(self.PNotebook1_t1)
        self.Scrolledlistbox2.place(relx=0.04, rely=0.29, relheight=0.44
                , relwidth=0.89)
        self.Scrolledlistbox2.configure(background="white")
        self.Scrolledlistbox2.configure(disabledforeground="#a3a3a3")
        self.Scrolledlistbox2.configure(font="TkFixedFont")
        self.Scrolledlistbox2.configure(foreground="black")
        self.Scrolledlistbox2.configure(highlightbackground="#d9d9d9")
        self.Scrolledlistbox2.configure(highlightcolor="#d9d9d9")
        self.Scrolledlistbox2.configure(selectbackground="#c4c4c4")
        self.Scrolledlistbox2.configure(selectforeground="black")
        self.Scrolledlistbox2.configure(width=10)
        self.Scrolledlistbox2.insert(0, "The duplicate files to be deleted will appear here...")

        self.TEntry1 = ttk.Entry(self.PNotebook1_t1)
        self.TEntry1.place(relx=0.3, rely=0.19, relheight=0.05, relwidth=0.29)
        self.TEntry1.configure(width=156)
        self.TEntry1.configure(takefocus="")
        #self.TEntry1.configure(cursor="ibeam")

        self.check_button_state = BooleanVar(root)
        self.check_button_state.set(False)
        self.TCheckbutton1 = ttk.Checkbutton(self.PNotebook1_t1, variable=self.check_button_state, command=self.toggleDupWipe)
        self.TCheckbutton1.place(relx=0.72, rely=0.19, relwidth=0.16
                , relheight=0.0, height=21)
        self.TCheckbutton1.configure(variable=GUI_support.tch64)
        self.TCheckbutton1.configure(takefocus="")
        self.TCheckbutton1.configure(text='''Wipe Files''')
        self.TCheckbutton1.configure(width=86)

        self.TLabel2 = ttk.Label(self.PNotebook1_t1)
        self.TLabel2.place(relx=0.81, rely=0.93, height=29, width=91)
        self.TLabel2.configure(background="#d9d9d9")
        self.TLabel2.configure(foreground="#000000")
        self.TLabel2.configure(relief=FLAT)
        self.TLabel2.configure(text='''By Monro Coury''')
        self.TLabel2.configure(width=91)

        self.help2 = ttk.Button(self.PNotebook1_t1, command=self.showCleanDupsHelp)
        self.help2.place(relx=0.13, rely=0.79, height=25, width=76)
        self.help2.configure(takefocus="")
        self.help2.configure(text='''Help''')

        self.wipe2 = ttk.Button(self.PNotebook1_t1, command=self.cleanDups)
        self.wipe2.place(relx=0.62, rely=0.79, height=25, width=76)
        self.wipe2.configure(takefocus="")
        self.wipe2.configure(text='''Proceed!''')

        self.TLabel3 = ttk.Label(self.PNotebook1_t1)
        self.TLabel3.place(relx=0.06, rely=0.19, height=19, width=113)
        self.TLabel3.configure(background="#d9d9d9")
        self.TLabel3.configure(foreground="#000000")
        self.TLabel3.configure(relief=FLAT)
        self.TLabel3.configure(text='''Extensions to ignore:''')
        self.PNotebook1.bind('<Button-1>',GUI_support.button_press)
        self.PNotebook1.bind('<ButtonRelease-1>',GUI_support.button_release)
        self.PNotebook1.bind('<Motion>',GUI_support.mouse_over)

        self.wipeFilesSelected = False
        self.wipeIsDir = False
        self.tgt_dir = None

        self.dupDirSelected = False

    def toggleDupWipe(self):
        self.check_button_state.set(not self.check_button_state.get())
        

    def browse2WipeFile(self):
        self.Scrolledlistbox1.delete(0, END)
        targets = filedialog.askopenfilenames(parent=root, title='Choose target file(s)')
        for tgt in list(targets):
            self.Scrolledlistbox1.insert(END, tgt)
        self.wipeFilesSelected = True

    def browse2WipeDir(self):
        self.Scrolledlistbox1.delete(0, END)
        target = filedialog.askdirectory()
        self.tgt_dir = target
        for root, dirs, files in os.walk(target):
            for f in files:
                self.Scrolledlistbox1.insert(END, os.path.join(root, f))
        self.wipeFilesSelected = True
        self.wipeIsDir = True

    def showWipeHelp(self):
        hlp = "You can either select multiple files, or a directory -in which case the program will walk through the " + \
              "directory and the sub directories it contains selecting all the files in them. The files that to be wiped " + \
              "will be displayed in the list box below. It goes without saying that you need to be careful, wiping " + \
              "a file means you'll never be able to restore it. Read the contents of the list box before hitting wipe."
        messagebox.showinfo("Help", hlp)

    def wipe(self):
        if not self.wipeFilesSelected:
            messagebox.showerror("Failed!", "Please select target directory or file(s) first!")
        else:
            prompt = messagebox.askquestion("Confirm Action", "This is your last chance to stop, proceed with wiping?")

            if prompt == "yes":
                for f in self.Scrolledlistbox1.get(0, END):
                    wipeFile(f)
                if self.wipeIsDir:
                    shutil.rmtree(self.tgt_dir)
                messagebox.showinfo("Success!", "Operation was successful!")
                self.Scrolledlistbox1.delete(0, END)
                self.Scrolledlistbox1.insert(0, "The files to be securely deleted will appear here...")
                self.wipeFilesSelected = False
                self.wipeIsDir = False

    def scanForDups(self, path):
        md5_dict={}
        for root, dirs, files in os.walk(path):#the os.walk function allows checking subdirectories too...
            for f in files:
                filePath=os.path.join(root,f)
                md5Hash=md5(filePath)
                size=os.path.getsize(filePath)
                fileComb=str(md5Hash)+str(size)
                if fileComb in md5_dict:
                    md5_dict[fileComb].append(filePath)
                else:
                    md5_dict.update({fileComb:[filePath]})

        exp_list = self.TEntry1.get().split("-")
        try:
            exp_list.remove("")
        except:
            pass
        
        for p in exp_list:
            for key in list(md5_dict):
                if any(thing.endswith(p) for thing in md5_dict[key]):
                    md5_dict.pop(key, None)       
        return md5_dict
    
    def browseDups(self):
        self.Scrolledlistbox2.delete(0, END)
        self.Scrolledlistbox2.insert(0, "looking for duplicate files...")
        dup_dict = self.scanForDups(filedialog.askdirectory())
        num = sum([len(dup_dict[key][:-1]) for key in dup_dict])
        self.Scrolledlistbox2.delete(0, END)
        self.Scrolledlistbox2.insert(0, "Found %d duplicates..." % num)
        for key in dup_dict:
            for fl in dup_dict[key][:-1]:
                self.Scrolledlistbox2.insert(END, fl)
        self.dupDirSelected = True

    def cleanDups(self):
        if not self.dupDirSelected:
            messagebox.showerror("Failed!", "Please select a target directory first!")
        else:
            prompt = messagebox.askquestion("Confirm Action", "This is your last chance to stop, proceed with deletion?")
            if prompt == "yes":
                for f in self.Scrolledlistbox2.get(0, END):
                    if self.check_button_state.get():
                        wipeFile(f)
                    else:
                        os.remove(f)
                messagebox.showinfo("Success!", "Operation was successful!")
                self.Scrolledlistbox2.delete(0, END)
                self.Scrolledlistbox2.insert(0, "The duplicate files to be deleted will appear here...")
                self.dupDirSelected = False

    def showCleanDupsHelp(self):
        hlp = "After choosing a root directory, the program will scan that directory " + \
              "and all the sub-directories it contains looking for duplicate files (based " + \
              "on the md5 hashes they generate), and it will display all the files to be " + \
              "deleted in the list box below. Clicking proceed and confirming will result " + \
              "in all the files being deleted (or even securely wiped if you tick the checkbox), " + \
              "so be careful and double check the list box to make sure nothing valuable will " + \
              "be lost. You can choose to ignore certain file types (extensions) by entering them " + \
              "into the specified field separated by a '-', eg: .py-.txt-.xml."

        messagebox.showinfo("Help", hlp)



# The following code is added to facilitate the Scrolled widgets you specified.
class AutoScroll(object):
    '''Configure the scrollbars for a widget.'''

    def __init__(self, master):
        #  Rozen. Added the try-except clauses so that this class
        #  could be used for scrolled entry widget for which vertical
        #  scrolling is not supported. 5/7/14.
        try:
            vsb = ttk.Scrollbar(master, orient='vertical', command=self.yview)
        except:
            pass
        hsb = ttk.Scrollbar(master, orient='horizontal', command=self.xview)

        #self.configure(yscrollcommand=_autoscroll(vsb),
        #    xscrollcommand=_autoscroll(hsb))
        try:
            self.configure(yscrollcommand=self._autoscroll(vsb))
        except:
            pass
        self.configure(xscrollcommand=self._autoscroll(hsb))

        self.grid(column=0, row=0, sticky='nsew')
        try:
            vsb.grid(column=1, row=0, sticky='ns')
        except:
            pass
        hsb.grid(column=0, row=1, sticky='ew')

        master.grid_columnconfigure(0, weight=1)
        master.grid_rowconfigure(0, weight=1)

        # Copy geometry methods of master  (taken from ScrolledText.py)
        if py3:
            methods = Pack.__dict__.keys() | Grid.__dict__.keys() \
                  | Place.__dict__.keys()
        else:
            methods = Pack.__dict__.keys() + Grid.__dict__.keys() \
                  + Place.__dict__.keys()

        for meth in methods:
            if meth[0] != '_' and meth not in ('config', 'configure'):
                setattr(self, meth, getattr(master, meth))

    @staticmethod
    def _autoscroll(sbar):
        '''Hide and show scrollbar as needed.'''
        def wrapped(first, last):
            first, last = float(first), float(last)
            if first <= 0 and last >= 1:
                sbar.grid_remove()
            else:
                sbar.grid()
            sbar.set(first, last)
        return wrapped

    def __str__(self):
        return str(self.master)

def _create_container(func):
    '''Creates a ttk Frame with a given master, and use this new frame to
    place the scrollbars and the widget.'''
    def wrapped(cls, master, **kw):
        container = ttk.Frame(master)
        return func(cls, container, **kw)
    return wrapped

class ScrolledListBox(AutoScroll, Listbox):
    '''A standard Tkinter Text widget with scrollbars that will
    automatically show/hide as needed.'''
    @_create_container
    def __init__(self, master, **kw):
        Listbox.__init__(self, master, **kw)
        AutoScroll.__init__(self, master)

if __name__ == '__main__':
    vp_start_gui()

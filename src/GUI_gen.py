import tkinter as tk

class MainWindow(tk.Frame):
    def __init__(self,root,*args,**kwargs):
        tk.Frame.__init__(self, root, *args, **kwargs)
        #default settings
        self.root = root
        self.root.title("Main Window")
        self.root.geometry("400x400")
        #label for the entry below
        self.keywords_label = tk.Label(root,text="Provide keywords below separated by ;",)
        self.keywords_label.pack()
        #entry for keywords
        self.keyword_entry_window = tk.Entry(root)
        self.keyword_entry_window.pack()
        #button for submitting
        self.submission_button = tk.Button(master=self.root, text="Search", command=self.button_submission)
        self.submission_button.pack()
        
    def button_submission(self):
        keywords = self.keyword_entry_window.get().split(';')
        #make sure there are no blank spaces after/before the keyword
        [keyword.strip() for keyword in keywords]
        #get rid of the empty input
        [keywords.remove(keyword) for keyword in keywords if keyword=='']

        
class ResultsWindow():
    pass

def generate_GUI():
    root = tk.Tk()
    app = MainWindow(root)
    app.pack()
    root.mainloop()
    
if __name__=="__main__":
    generate_GUI()
    
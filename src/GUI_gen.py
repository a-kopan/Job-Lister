import tkinter as tk
from tkinter import ttk
import NoFluffJobs.filter_data as nfj
from Scraping import scrape_req


class MainWindow(tk.Frame):
    def __init__(self, root):
        tk.Frame.__init__(self, root)
        # default settings
        self.root = root
        self.root.title("Main Window")
        self.root.geometry("400x400")
        # label for the entry below
        self.keywords_label = tk.Label(
            root,
            text="Provide keywords below separated by ;",
        )
        self.keywords_label.pack()
        # entry for keywords
        self.keyword_entry_window = tk.Entry(root)
        self.keyword_entry_window.focus()
        self.keyword_entry_window.configure(font=(20))
        self.keyword_entry_window.pack()
        # button for submitting
        self.submission_button = tk.Button(
            master=self.root, text="Search", command=self.button_submission
        )
        self.submission_button.pack()

    def button_submission(self):
        keywords: list = self.keyword_entry_window.get().split(";")
        # make sure there are no blank spaces after/before the keyword
        keywords = [keyword.strip() for keyword in keywords]

        # get rid of the empty input
        keywords = [keyword for keyword in keywords if keyword != ""]

        # check for empty input
        if keywords == [""]:
            return

        URL = nfj.add_keywords_to_url(keywords)
        soup = scrape_req.request_for_soup(URL)
        offers = nfj.soup_to_data(soup)
        self.open_new_window(offers)

    def open_new_window(self, offers):
        new_window = tk.Toplevel(self.root)
        self.new_window = ResultsWindow(new_window, offers)


class ResultsWindow(tk.Frame):
    def __init__(self, root, offers):
        tk.Frame.__init__(self, root)

        # default settings
        self.root = root
        self.root.title("Results")
        self.root.geometry("1200x400")

        # scroll for the listbox
        scrollbar = tk.Scrollbar(self.root)
        scrollbar.pack(side=tk.RIGHT, fill=tk.Y)

        # result listbox
        results_treeview = ttk.Treeview(
            root,
            columns=("Title", "Salary", "Locations", "Remote", "Requirements", "Link"),
        )
        results_treeview.pack(fill=tk.BOTH, expand=True)

        # set the width of the tree column (column #0) to 0 pixels to hide it
        results_treeview.column("#0", width=0, stretch=tk.NO)
        # define column headers
        results_treeview.heading("#1", text="Title")
        results_treeview.heading("#2", text="Salary")
        results_treeview.heading("#3", text="Locations")
        results_treeview.heading("#4", text="Remote")
        results_treeview.heading("#5", text="Requirements")
        results_treeview.heading("#6", text="Link")

        # config the scrollbar
        scrollbar.config(command=results_treeview.yview)

        # go through the provided keywords and add them to listbox
        for offer in offers:
            results_treeview.insert(
                "",
                "end",
                values=(
                    offer["name"],
                    offer["salary"],
                    offer["locations"],
                    offer["remote"],
                    offer["company"],
                    offer["link"],
                ),
            )


def main():
    root = tk.Tk()
    app = MainWindow(root)
    app.pack()
    root.mainloop()


if __name__ == "__main__":
    main()

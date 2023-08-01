from scrape import filter_data_for_titles

def test_testHTML():
    file = open("tests/test.html","r")
    assert filter_data_for_titles(file.read()) == {"Junior Embedded Systems Engineer",
                                                   "Embedded Systems Solutions",
                                                   "Junior DevOps Platform Engineer",
                                                   "Programista Python (Junior/Mid)",
                                                   "Junior Python Developer z Chemi� / Bio",
                                                   "Junior Test System Engineer",
                                                   "Junior Data Engineer",
                                                   "Junior Test Automation Engineer",
                                                   "Junior Software Tester with Python",
                                                   "Junior Test Engineer",
                                                   "Junior DevOps Engineer",
                                                   "Junior Data Engineer (zast�pstwo)",
                                                   "Junior Python Dev (upskill to DevOps)"}
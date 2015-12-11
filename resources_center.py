import data_structure
import fun_list

coursera = data_structure.Resource("Coursera - Algoritmos: Design and Analysis, Part 1",
                                  "In this course you could learn the fundaments of algorith design.",
                                  "Online class",
                                  "C, Python, Java",
                                  "English",
                                  "https://www.coursera.org/course/algo")

code_chef = data_structure.Resource("Code chef",
                                  "Programming community that host contest and training por programmers.",
                                  "Practice",
                                  "C++, Python, Java",
                                  "English, Mandarin Chinese, Russian",
                                  "https://www.codechef.com/")

coding_bat = data_structure.Resource("Coding bat",
                                  "Web site with a list of coding problems to improves skill in Java and Python.",
                                  "Practice",
                                  "Python, Java",
                                  "English",
                                  "http://codingbat.com/")     


omegaup = data_structure.Resource("Omega Up",
                                  "Web project help improve skill ofsoftware developerss through problemas solving.",
                                  "Practice",
                                  "C++, Python, Java",
                                  "Spanish",
                                  "https://omegaup.com/")

resources = [coursera, code_chef, coding_bat, omegaup]
fun_list.open_resources_page(resources)

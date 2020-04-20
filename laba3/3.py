from tkinter import *
from tkinter.messagebox import *
from tkinter import filedialog as fd
import re
from datetime import datetime
import os


class FinderFrame(Frame):
    __count = 1.0

    def __init__(self, parent):
        Frame.__init__(self, parent)
        self.parent = parent
        self.init_ui()

    def open_file(self):
        file_name = fd.askopenfilename(filetypes=(("TXT files", "*.txt"),
                                                  ("HTML files", "*.html;*.htm"),
                                                  ("All files", "*.*")))
        self.find_text(file_name)
        self.status.config(text=file_name + " | " + str(os.path.getsize(file_name)) + " bytes")

    def find_text(self, path):
        self.f = open(path)
        self.lines_arr = self.f.readlines()
        self.f.close()
        now = datetime.now()
        self.text.insert(self.__count, "Файл " + path + " был обработан " + now.strftime("%Y-%m-%d-%H.%M.%S") + "\n")
        self.__count = self.__count + 1
        self.text.insert(self.__count, "\n")
        self.__count = self.__count + 1
        for i in range(len(self.lines_arr)):
            if self.lines_arr[i] == r"\n":
                self.lines_arr.remove(i)
        self.result = list()
        for i in range(len(self.lines_arr)):
            pattern = re.compile(r"[a-zA-Zа-яА-Я]+&{1,3}[a-zA-Zа-яА-Я]+")
            self.result = re.findall(pattern, self.lines_arr[i])
            for j in range(len(self.result)):
                self.text.insert(self.__count, "Строка: " + str(i) + ", позиция: " + str(
                    self.lines_arr[i].find(self.result[j])) + ", найдено: " + str(self.result[j]) + "\n")
                self.__count = self.__count + 1
        self.text.insert(self.__count, "\n")
        self.__count = self.__count + 1

    def writeToFile(self):
        file_name = fd.asksaveasfilename(filetypes=(("TXT files", "*.txt"),
                                                    ("HTML files", "*.html;*.htm"),
                                                    ("All files", "*.*")))
        f = open(file_name, 'wt')
        s = self.text.get(1.0, END)
        f.write(s)
        f.close();

    def writeToLogFile(self):
        f = open(r'script18.log', 'a')
        s = self.text.get(1.0, END)
        f.write(s)
        f.close();

    def readInLogFile(self):
        answer = askyesno(title="Внимание",
                          message="Вы действительно хотите открыть лог? Данные последних поисков будут потеряны!")
        if answer == True:
            f = open(r'script18.log', 'r')
            s = self.text.delete(1.0, END)
            text_arr = f.readlines(s)
            f.close();
            self.__count = 1.0
            for i in text_arr:
                self.text.insert(self.__count, i)
                self.__count = self.__count + 1
        print()

    def init_ui(self):
        self.parent.title("Поиск в файле")
        self.pack(fill=BOTH, expand=True)

        self.text = Text(width=98, height=27, wrap=WORD)
        self.text.pack(side=TOP)
        scroll = Scrollbar(command=self.text.yview)
        scroll.pack(side=LEFT, fill=Y)
        self.text.config(yscrollcommand=scroll.set)

        mainmenu = Menu(self.parent)
        self.parent.config(menu=mainmenu)

        filemenu = Menu(mainmenu, tearoff=0)
        filemenu.add_command(label="Открыть...", command=self.open_file)

        logmenu = Menu(mainmenu, tearoff=0)
        logmenu.add_command(label="Экспорт...", command=self.writeToFile)
        logmenu.add_command(label="Добавить в лог", command=self.writeToLogFile)
        logmenu.add_command(label="Просмотр", command=self.readInLogFile)

        mainmenu.add_cascade(label="Файл", menu=filemenu)
        mainmenu.add_cascade(label="Лог", menu=logmenu)

        self.status = Label(self.parent, text="", bd=1, relief=SUNKEN, anchor=W)
        self.status.pack(side=BOTTOM, fill=X)


def main():
    root = Tk()
    root.geometry("800x460+300+300")
    app = FinderFrame(root)
    if os.path.exists('script18.log') == False:
        showinfo("Ошибка", "Файл лога не найден. Файл будет создан автоматически.")
        open(r'script18.log', 'wt').close()
    root.mainloop()


if __name__ == '__main__':
    main()
import pathlib
from tkinter import END, NO
import sqlite3
import tkinter as tk
from tkinter import messagebox
import tkinter.ttk as ttk

PROJECT_PATH = pathlib.Path(__file__).parent
PROJECT_UI = PROJECT_PATH / "BandScanner.ui"

con = sqlite3.connect('bandscan.db')
cur = con.cursor()

cur.execute("SELECT name FROM sqlite_master WHERE type='table' AND name='frequenze'")
cur.execute("CREATE TABLE IF NOT EXISTS frequenze ("
            "frequenza FLOAT NOT NULL,"
            "portante VARCHAR NOT NULL,"
            "rds VARCHAR NOT NULL,"
            "codiceRDS VARCHAR,"
            "indice FLOAT"
            ") WITHOUT ROWID")
con.commit()

columns = ('frequenza', 'portante', 'rds', 'codiceRDS', 'indice')

class BandscannerApp:
    def __init__(self, master=None):
        # build ui
        self.frameMaster = ttk.Frame(master)
        self.labelframe1 = ttk.Labelframe(self.frameMaster)
        self.lblFrequenza = ttk.Label(self.labelframe1)
        self.lblFrequenza.configure(style='Bandscan.TLabel', text='Frequenza:')
        self.lblFrequenza.grid(column='0', pady='10', row='0', sticky='e')
        self.frequenza = ttk.Combobox(self.labelframe1)
        self.frequenza.configure(justify='center',
                                 values='87.5 87.6 87.7 87.8 87.9 88.0 88.1 88.2 88.3 88.4 88.5 88.6 88.7 88.8 88.9 '
                                        '89.0 89.1 89.2 89.3 89.4 89.5 89.6 89.7 89.8 89.9 90.0 90.1 90.2 90.3 90.4 '
                                        '90.5 90.6 90.7 90.8 90.9 91.0 91.1 91.2 91.3 91.4 91.5 91.6 91.7 91.8 91.9 '
                                        '92.0 92.1 92.2 92.3 92.4 92.5 92.6 92.7 92.8 92.9 93.0 93.1 93.1 93.2 93.3 '
                                        '93.4 93.5 93.6 93.7 93.8 93.9 94.0 94.1 94.2 94.3 94.4 94.5 94.6 94.7 94.8 '
                                        '94.9 95.0 95.1 95.2 95.3 95.4 95.5 95.6 95.7 95.8 95.9 96.0 96.1 96.2 96.3 '
                                        '96.4 96.5 96.6 96.7 96.8 96.9 97.0 97.1 97.2 97.3 97.4 97.5 97.6 97.7 97.8 '
                                        '97.9 98.0 98.1 98.2 98.3 98.4 98.5 98.6 98.7 98.8 98.9 99.0 99.1 99.2 99.3 '
                                        '99.4 99.5 99.6 99.7 99.8 99.9 100.0 100.1 100.2 100.3 100.4 100.5 100.6 100.7 '
                                        '100.8 100.9 101.0 101.1 101.2 101.3 101.4 101.5 101.6 101.7 101.8 101.9 102.0 '
                                        '102.1 102.2 102.3 102.4 102.5 102.6 102.7 102.8 102.9 103.0 103.1 103.2 103.3 '
                                        '103.4 103.5 103.6 103.7 103.8 103.9 104.0 104.1 104.2 104.3 104.4 104.5 104.6 '
                                        '104.7 104.8 104.9 105.0 105.1 105.2 105.3 105.4 105.5 105.6 105.7 105.8 105.9 '
                                        '106.0 106.1 106.2 106.3 106.4 106.5 106.6 106.7 106.8 106.9 107.0 107.1 107.2 '
                                        '107.3 107.4 107.5 107.6 107.7 107.8 107.9 108.0')
        self.frequenza.grid(column='1', padx='10', row='0', sticky='ew')
        self.lblPortante = ttk.Label(self.labelframe1)
        self.lblPortante.configure(style='Bandscan.TLabel', text='Portante:')
        self.lblPortante.grid(column='0', pady='10', row='1', sticky='e')
        self.portante = ttk.Entry(self.labelframe1)
        self.portante.configure(width='70')
        self.portante.grid(column='1', padx='10', row='1', sticky='ew')
        self.label3 = ttk.Label(self.labelframe1)
        self.label3.configure(style='Bandscan.TLabel', text='RDS:')
        self.label3.grid(column='0', pady='10', row='2', sticky='e')
        self.rds = ttk.Entry(self.labelframe1)
        self.rds.grid(column='1', padx='10', row='2', sticky='ew')
        self.label4 = ttk.Label(self.labelframe1)
        self.label4.configure(style='Bandscan.TLabel', text='Codice RDS:')
        self.label4.grid(column='0', pady='10', row='3', sticky='e')
        self.codicerds = ttk.Entry(self.labelframe1)
        self.codicerds.grid(column='1', padx='10', row='3', sticky='ew')
        self.label5 = ttk.Label(self.labelframe1)
        self.label5.configure(style='Bandscan.TLabel', text='Indice:')
        self.label5.grid(column='0', pady='10', row='4', sticky='e')
        self.indice = ttk.Entry(self.labelframe1)
        self.indice.grid(column='1', padx='10', row='4', sticky='ew')
        self.treeview1 = ttk.Treeview(self.labelframe1, columns=columns, show= 'headings')
        self.treeview1.grid(column='0', columnspan='2', padx='10', pady='12', row='6', sticky='ew')
        #self.treeview1.heading('frequenza', text='Frequenza')
        #self.treeview1.heading('portante', text='Portante')
        #self.treeview1.heading('rds', text='RDS')
        #self.treeview1.heading('codiceRDS', text='RDS PI')
        #self.treeview1.heading('indice', text='dBuV/m')
        self.inserisci = ttk.Button(self.labelframe1)
        self.inserisci.configure(style='Bandscan.TButton', text='Inserisci')
        self.inserisci.grid(column='0', columnspan='2', row='5', sticky='ew')
        self.inserisci.configure(command=self.inserisciFx)
        self.btnEliminaRecord = ttk.Button(self.labelframe1)
        self.btnEliminaRecord.configure(style='Bandscan.TButton', text='Elimina record')
        self.btnEliminaRecord.grid(column='0', columnspan='2', row='7', sticky='ew')
        self.btnEliminaRecord.configure(command=self.eliminaRecord)
        self.labelframe1.configure(height='0', style='Bandscan.TLabelframe', text='BandScan', width='200')
        self.labelframe1.grid(column='1', padx='10', row='0')
        '''self.labelframe2 = ttk.Labelframe(self.frameMaster)
        self.label6 = ttk.Label(self.labelframe2)
        self.label6.configure(text='Località:')
        self.label6.grid(column='0', pady='10', row='0', sticky='e')
        self.localita = ttk.Entry(self.labelframe2)
        self.localita.configure(width='40')
        self.localita.grid(column='1', padx='10', row='0', sticky='ew')
        self.label7 = ttk.Label(self.labelframe2)
        self.label7.configure(text='Latitudine:')
        self.label7.grid(column='0', pady='10', row='1', sticky='e')
        self.latitudine = ttk.Entry(self.labelframe2)
        self.latitudine.grid(column='1', padx='10', row='1', sticky='ew')
        self.longitudine = ttk.Entry(self.labelframe2)
        self.longitudine.grid(column='1', padx='10', row='2', sticky='ew')
        self.label8 = ttk.Label(self.labelframe2)
        self.label8.configure(text='Longitudine:')
        self.label8.grid(column='0', pady='10', row='2', sticky='e')
        self.label9 = ttk.Label(self.labelframe2)
        self.label9.configure(text='Altitudine:')
        self.label9.grid(column='0', pady='10', row='3', sticky='e')
        self.altitudine = ttk.Entry(self.labelframe2)
        self.altitudine.grid(column='1', padx='10', row='3', sticky='ew')
        self.label10 = ttk.Label(self.labelframe2)
        self.label10.configure(text='Antenna:')
        self.label10.grid(column='0', pady='10', row='4', sticky='e')
        self.antenna = ttk.Combobox(self.labelframe2)
        self.antenna.configure(values='Boom GroundPlane Veicolare Dipolo Filare Altro', width='40')
        self.antenna.grid(column='1', padx='10', row='4', sticky='ew')
        self.label11 = ttk.Label(self.labelframe2)
        self.label11.configure(text='Coeff. Kc:')
        self.label11.grid(column='0', pady='10', row='5', sticky='e')
        self.kc = ttk.Entry(self.labelframe2)
        self.kc.grid(column='1', padx='10', row='5', sticky='ew')
        self.label12 = ttk.Label(self.labelframe2)
        self.label12.configure(text='Descrizione:')
        self.label12.grid(column='0', pady='10', row='6', sticky='e')
        self.text1 = tk.Text(self.labelframe2)
        self.text1.configure(height='13', tabstyle='wordprocessor', width='40')
        self.text1.grid(column='1', padx='10', pady='10', row='6', sticky='ew')
        self.labelframe2.configure(height='200', text='Punto di ascolto', width='200')
        self.labelframe2.grid(column='0', padx='10', row='0', sticky='n')'''

        self.frameMaster.configure(borderwidth='10', height='600', padding='10', relief='flat')
        self.frameMaster.configure(width='1024')
        self.frameMaster.grid(column='0', row='0', sticky='nw')
        self.frameMaster.grid_anchor('center')
        self.frameMaster.rowconfigure('all', uniform='1')

        # Main widget
        self.mainwindow = self.frameMaster



        self.treeview1.heading('frequenza', text='Frequenza')
        self.treeview1.heading('portante', text='Portante')
        self.treeview1.heading('rds', text='RDS')
        self.treeview1.heading('codiceRDS', text='RDS PI')
        self.treeview1.heading('indice', text='dBuV/m')

        self.treeview1.column(0, width=67, stretch=NO)
        self.treeview1.column(1, width=100)
        self.treeview1.column(2, width=67, stretch=NO)
        self.treeview1.column(3, width=67, stretch=NO)
        self.treeview1.column(4, width=67, stretch=NO)

        cur.execute("SELECT * FROM frequenze")
        records = cur.fetchall()
        con.commit()

        for record in records:
            self.treeview1.insert("", END, values=record)

    def run(self):
        self.mainwindow.mainloop()

    def eliminaRecord(self):
        recordIDX = self.treeview1.focus()
        record = self.treeview1.item(recordIDX)
        valore = record['values'][0]
        cur.execute("DELETE FROM frequenze WHERE frequenza = ?;", (valore,))
        self.treeview1.delete(*self.treeview1.get_children())
        cur.execute("SELECT * FROM frequenze")
        records = cur.fetchall()
        con.commit()

        for record in records:
            self.treeview1.insert("", END, values=record)


    def inserisciFx(self):
        Frequenza = self.frequenza.get()
        Portante = self.portante.get()
        RDS = self.rds.get()
        CodiceRDS = self.codicerds.get()
        Indice = self.indice.get()

        Record = [Frequenza, Portante, RDS, CodiceRDS, Indice]

        if Portante != "":
            #self.treeview1.insert('', END, values=Record)
            Command = "INSERT INTO frequenze VALUES ('?','?','?','?','?')"
            self.treeview1.delete(*self.treeview1.get_children())
            cur.execute("INSERT INTO frequenze VALUES (?,?,?,?,?)", Record)
            con.commit()

            cur.execute("SELECT * FROM frequenze")
            records = cur.fetchall()
            con.commit()

            for record in records:
                self.treeview1.insert("", END, values= record)
        else:
            tk.messagebox.showerror(title="Dati incompleti", message="Inserisci tutti i dati richiesti!")

        self.frequenza.delete(0, END)
        self.indice.delete(0, END)
        self.rds.delete(0, END)
        self.portante.delete(0, END)
        self.codicerds.delete(0, END)



if __name__ == '__main__':
    root = tk.Tk()
    root.resizable(False, False)
    root.title("AB Informatica - ABINF - BandScan Utility")
    root.iconbitmap("Icon.ico")
    app = BandscannerApp(root)
    app.run()



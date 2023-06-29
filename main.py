# Librării importate

import tkinter as tk
from tkinter import*
from tkinter import messagebox

# Declarare variabile globale-------------------------------------------------------------------------------------------
close_sb1_cl1 = False
close_sb2_cl1 = False
connect_i_cl1 = False
close_sl_cl1 = False
close_clp_cl1 = False
close_sb1_cl2 = False
close_sb2_cl2 = False
connect_i_cl2 = False
close_sl_cl2 = False
close_clp_cl2 = False
close_sb1_cc = False
close_sb2_cc = False
connect_i_cc = False
close_clp_cc = False
close_sb11_clt = False
close_sb21_clt = False
close_sb12_clt = False
close_sb22_clt = False
connect_i_clt = False
activate_load_cl1 = False
activate_load_cl2 = False

# Condiții Celulă de linie 1--------------------------------------------------------------------------------------------


def toggle_activate_load_cl1():
    global activate_load_cl1
    if close_sl_cl1 and connect_i_cl1 and close_sb2_cl1 and close_sb21_clt and connect_i_clt and close_sb22_clt and close_sb2_cl2 and connect_i_cl2 and close_sl_cl2:
        activate_load_cl1 = True
        canvas.itemconfigure("l1_cl1", fill="red")
        canvas.itemconfigure("l3_cl1", fill="red")
        canvas.itemconfigure("l4_cl1", fill="red")
        canvas.itemconfigure("l5.2_cl1", fill="red")
        canvas.itemconfigure("b2", fill="red")
        canvas.itemconfigure("l2_clt", fill="red")
        canvas.itemconfigure("l6_clt", fill="red")
        canvas.itemconfigure("l4_clt", fill="red")
        canvas.itemconfigure("l5_clt", fill="red")
        canvas.itemconfigure("b4", fill="red")
        canvas.itemconfigure("l1.2_cc", fill="red")
        canvas.itemconfigure("l5.2_cl2", fill="red")
        canvas.itemconfigure("l4_cl2", fill="red")
        canvas.itemconfigure("l3_cl2", fill="red")
        canvas.itemconfigure("l1_cl2", fill="red")
        #messagebox.showinfo("", "Tensiunea este aplicată pe linie.")
    elif close_sl_cl1 and connect_i_cl1 and close_sb1_cl1 and close_sb11_clt and connect_i_clt and close_sb12_clt and close_sb1_cl2 and connect_i_cl2 and close_sl_cl2:
        activate_load_cl1 = True
        canvas.itemconfigure("l1_cl1", fill="red")
        canvas.itemconfigure("l3_cl1", fill="red")
        canvas.itemconfigure("l4_cl1", fill="red")
        canvas.itemconfigure("l5.1_cl1", fill="red")
        canvas.itemconfigure("b1", fill="red")
        canvas.itemconfigure("l1_clt", fill="red")
        canvas.itemconfigure("l5_clt", fill="red")
        canvas.itemconfigure("l6_clt", fill="red")
        canvas.itemconfigure("l3_clt", fill="red")
        canvas.itemconfigure("b3", fill="red")
        canvas.itemconfigure("l1.1_cc", fill="red")
        canvas.itemconfigure("l5.1_cl2", fill="red")
        canvas.itemconfigure("l4_cl2", fill="red")
        canvas.itemconfigure("l3_cl2", fill="red")
        canvas.itemconfigure("l1_cl2", fill="red")
        #messagebox.showinfo("", "Tensiunea este aplicată pe linie.")
    elif close_sl_cl1 and connect_i_cl1 and close_sb2_cl1 and close_sb21_clt and connect_i_clt and close_sb22_clt and close_sb2_cl2:
        activate_load_cl1 = True
        canvas.itemconfigure("l1_cl1", fill="red")
        canvas.itemconfigure("l3_cl1", fill="red")
        canvas.itemconfigure("l4_cl1", fill="red")
        canvas.itemconfigure("l5.2_cl1", fill="red")
        canvas.itemconfigure("b2", fill="red")
        canvas.itemconfigure("l2_clt", fill="red")
        canvas.itemconfigure("l6_clt", fill="red")
        canvas.itemconfigure("l4_clt", fill="red")
        canvas.itemconfigure("l5_clt", fill="red")
        canvas.itemconfigure("b4", fill="red")
        canvas.itemconfigure("l1.2_cc", fill="red")
        canvas.itemconfigure("l5.2_cl2", fill="red")
        canvas.itemconfigure("l4_cl2", fill="red")
        #messagebox.showinfo("", "Tensiunea este aplicată pe linie.")
    elif close_sl_cl1 and connect_i_cl1 and close_sb1_cl1 and close_sb11_clt and connect_i_clt and close_sb12_clt and close_sb1_cl2:
        activate_load_cl1 = True
        canvas.itemconfigure("l1_cl1", fill="red")
        canvas.itemconfigure("l3_cl1", fill="red")
        canvas.itemconfigure("l4_cl1", fill="red")
        canvas.itemconfigure("l5.1_cl1", fill="red")
        canvas.itemconfigure("b1", fill="red")
        canvas.itemconfigure("l1_clt", fill="red")
        canvas.itemconfigure("l5_clt", fill="red")
        canvas.itemconfigure("l6_clt", fill="red")
        canvas.itemconfigure("l3_clt", fill="red")
        canvas.itemconfigure("b3", fill="red")
        canvas.itemconfigure("l1.1_cc", fill="red")
        canvas.itemconfigure("l5.1_cl2", fill="red")
        canvas.itemconfigure("l4_cl2", fill="red")
        #messagebox.showinfo("", "Tensiunea este aplicată pe linie.")
    if close_sl_cl1 and connect_i_cl1 and close_sb2_cl1 and close_sb21_clt and connect_i_clt and close_sb22_clt and close_sb2_cc and connect_i_cc:
        activate_load_cl1 = True
        canvas.itemconfigure("l1_cl1", fill="red")
        canvas.itemconfigure("l3_cl1", fill="red")
        canvas.itemconfigure("l4_cl1", fill="red")
        canvas.itemconfigure("l5.2_cl1", fill="red")
        canvas.itemconfigure("b2", fill="red")
        canvas.itemconfigure("l2_clt", fill="red")
        canvas.itemconfigure("l6_clt", fill="red")
        canvas.itemconfigure("l4_clt", fill="red")
        canvas.itemconfigure("l5_clt", fill="red")
        canvas.itemconfigure("b4", fill="red")
        canvas.itemconfigure("l1.2_cc", fill="red")
        canvas.itemconfigure("l5.2_cl2", fill="red")
        canvas.itemconfigure("l2_cc", fill="red")
        canvas.itemconfigure("l3_cc", fill="red")
        canvas.itemconfigure("m_cc", fill="red")
        #messagebox.showinfo("", "Tensiunea este aplicată pe linie.")
    elif close_sl_cl1 and connect_i_cl1 and close_sb1_cl1 and close_sb11_clt and connect_i_clt and close_sb12_clt and close_sb1_cc and connect_i_cc:
        activate_load_cl1 = True
        canvas.itemconfigure("l1_cl1", fill="red")
        canvas.itemconfigure("l3_cl1", fill="red")
        canvas.itemconfigure("l4_cl1", fill="red")
        canvas.itemconfigure("l5.1_cl1", fill="red")
        canvas.itemconfigure("b1", fill="red")
        canvas.itemconfigure("l1_clt", fill="red")
        canvas.itemconfigure("l5_clt", fill="red")
        canvas.itemconfigure("l6_clt", fill="red")
        canvas.itemconfigure("l3_clt", fill="red")
        canvas.itemconfigure("b3", fill="red")
        canvas.itemconfigure("l1.1_cc", fill="red")
        canvas.itemconfigure("l5.1_cl2", fill="red")
        canvas.itemconfigure("l2_cc", fill="red")
        canvas.itemconfigure("l3_cc", fill="red")
        canvas.itemconfigure("m_cc", fill="red")
        #messagebox.showinfo("", "Tensiunea este aplicată pe linie.")
    elif close_sl_cl1 and connect_i_cl1 and close_sb2_cl1 and close_sb21_clt and connect_i_clt and close_sb22_clt and close_sb2_cc:
        activate_load_cl1 = True
        canvas.itemconfigure("l1_cl1", fill="red")
        canvas.itemconfigure("l3_cl1", fill="red")
        canvas.itemconfigure("l4_cl1", fill="red")
        canvas.itemconfigure("l5.2_cl1", fill="red")
        canvas.itemconfigure("b2", fill="red")
        canvas.itemconfigure("l2_clt", fill="red")
        canvas.itemconfigure("l6_clt", fill="red")
        canvas.itemconfigure("l4_clt", fill="red")
        canvas.itemconfigure("l5_clt", fill="red")
        canvas.itemconfigure("b4", fill="red")
        canvas.itemconfigure("l1.2_cc", fill="red")
        canvas.itemconfigure("l5.2_cl2", fill="red")
        canvas.itemconfigure("l2_cc", fill="red")
        #messagebox.showinfo("", "Tensiunea este aplicată pe linie.")
    elif close_sl_cl1 and connect_i_cl1 and close_sb1_cl1 and close_sb11_clt and connect_i_clt and close_sb12_clt and close_sb1_cc:
        activate_load_cl1 = True
        canvas.itemconfigure("l1_cl1", fill="red")
        canvas.itemconfigure("l3_cl1", fill="red")
        canvas.itemconfigure("l4_cl1", fill="red")
        canvas.itemconfigure("l5.1_cl1", fill="red")
        canvas.itemconfigure("b1", fill="red")
        canvas.itemconfigure("l1_clt", fill="red")
        canvas.itemconfigure("l5_clt", fill="red")
        canvas.itemconfigure("l6_clt", fill="red")
        canvas.itemconfigure("l3_clt", fill="red")
        canvas.itemconfigure("b3", fill="red")
        canvas.itemconfigure("l1.1_cc", fill="red")
        canvas.itemconfigure("l5.1_cl2", fill="red")
        canvas.itemconfigure("l2_cc", fill="red")
        #messagebox.showinfo("", "Tensiunea este aplicată pe linie.")
    elif close_sl_cl1 and connect_i_cl1 and close_sb2_cl1 and close_sb21_clt and connect_i_clt and close_sb22_clt:
        activate_load_cl1 = True
        canvas.itemconfigure("l1_cl1", fill="red")
        canvas.itemconfigure("l3_cl1", fill="red")
        canvas.itemconfigure("l4_cl1", fill="red")
        canvas.itemconfigure("l5.2_cl1", fill="red")
        canvas.itemconfigure("b2", fill="red")
        canvas.itemconfigure("l2_clt", fill="red")
        canvas.itemconfigure("l6_clt", fill="red")
        canvas.itemconfigure("l4_clt", fill="red")
        canvas.itemconfigure("l5_clt", fill="red")
        canvas.itemconfigure("b4", fill="red")
        canvas.itemconfigure("l1.2_cc", fill="red")
        canvas.itemconfigure("l5.2_cl2", fill="red")
        #messagebox.showinfo("", "Tensiunea este aplicată pe linie.")
    elif close_sl_cl1 and connect_i_cl1 and close_sb1_cl1 and close_sb11_clt and connect_i_clt and close_sb12_clt:
        activate_load_cl1 = True
        canvas.itemconfigure("l1_cl1", fill="red")
        canvas.itemconfigure("l3_cl1", fill="red")
        canvas.itemconfigure("l4_cl1", fill="red")
        canvas.itemconfigure("l5.1_cl1", fill="red")
        canvas.itemconfigure("b1", fill="red")
        canvas.itemconfigure("l1_clt", fill="red")
        canvas.itemconfigure("l5_clt", fill="red")
        canvas.itemconfigure("l6_clt", fill="red")
        canvas.itemconfigure("l3_clt", fill="red")
        canvas.itemconfigure("b3", fill="red")
        canvas.itemconfigure("l1.1_cc", fill="red")
        canvas.itemconfigure("l5.1_cl2", fill="red")
        #messagebox.showinfo("", "Tensiunea este aplicată pe linie.")
    elif close_sl_cl1 and connect_i_cl1 and close_sb2_cl1 and close_sb21_clt:
        activate_load_cl1 = True
        canvas.itemconfigure("l1_cl1", fill="red")
        canvas.itemconfigure("l3_cl1", fill="red")
        canvas.itemconfigure("l4_cl1", fill="red")
        canvas.itemconfigure("l5.2_cl1", fill="red")
        canvas.itemconfigure("b2", fill="red")
        canvas.itemconfigure("l2_clt", fill="red")
        canvas.itemconfigure("l6_clt", fill="red")
        #messagebox.showinfo("", "Tensiunea este aplicată pe linie.")
    elif close_sl_cl1 and connect_i_cl1 and close_sb1_cl1 and close_sb11_clt:
        activate_load_cl1 = True
        canvas.itemconfigure("l1_cl1", fill="red")
        canvas.itemconfigure("l3_cl1", fill="red")
        canvas.itemconfigure("l4_cl1", fill="red")
        canvas.itemconfigure("l5.1_cl1", fill="red")
        canvas.itemconfigure("b1", fill="red")
        canvas.itemconfigure("l1_clt", fill="red")
        canvas.itemconfigure("l5_clt", fill="red")
        #messagebox.showinfo("", "Tensiunea este aplicată pe linie.")
    elif close_sl_cl1 and connect_i_cl1 and close_sb2_cl1:
        activate_load_cl1 = True
        canvas.itemconfigure("l1_cl1", fill="red")
        canvas.itemconfigure("l3_cl1", fill="red")
        canvas.itemconfigure("l4_cl1", fill="red")
        canvas.itemconfigure("l5.2_cl1", fill="red")
        canvas.itemconfigure("b2", fill="red")
        canvas.itemconfigure("l2_clt", fill="red")
        #messagebox.showinfo("", "Tensiunea este aplicată pe linie.")
    elif close_sl_cl1 and connect_i_cl1 and close_sb1_cl1:
        activate_load_cl1 = True
        canvas.itemconfigure("l1_cl1", fill="red")
        canvas.itemconfigure("l3_cl1", fill="red")
        canvas.itemconfigure("l4_cl1", fill="red")
        canvas.itemconfigure("l5.1_cl1", fill="red")
        canvas.itemconfigure("b1", fill="red")
        canvas.itemconfigure("l1_clt", fill="red")
        #messagebox.showinfo("", "Tensiunea este aplicată pe linie.")
    elif close_sl_cl1:
        activate_load_cl1 = True
        canvas.itemconfigure("l1_cl1", fill="red")
        canvas.itemconfigure("l3_cl1", fill="red")
        #messagebox.showinfo("", "Tensiunea este aplicată pe linie.")
    elif close_clp_cl1:
        activate_load_cl1 = True
        canvas.itemconfigure("l1_cl1", fill="red")
        canvas.itemconfigure("l2_cl1", fill="red")
        #messagebox.showinfo("", "Tensiunea este aplicată pe linie.")
    elif not activate_load_cl1:
        activate_load_cl1 = True
        canvas.itemconfigure("l1_cl1", fill="red")
        #messagebox.showinfo("", "Tensiunea este aplicată pe linie.")


def toggle_deactivate_load_cl1():
    global activate_load_cl1
    if activate_load_cl1 and close_sl_cl1:
        activate_load_cl1 = False
        canvas.itemconfigure("l1_cl1", fill="black")
        canvas.itemconfigure("l3_cl1", fill="black")
        canvas.itemconfigure("l4_cl1", fill="black")
        canvas.itemconfigure("l5.1_cl1", fill="black")
        canvas.itemconfigure("l5.2_cl1", fill="black")
        canvas.itemconfigure("b1", fill="black")
        canvas.itemconfigure("b2", fill="black")
        canvas.itemconfigure("l1_clt", fill="black")
        canvas.itemconfigure("l2_clt", fill="black")
        canvas.itemconfigure("l3_clt", fill="black")
        canvas.itemconfigure("l4_clt", fill="black")
        canvas.itemconfigure("l5_clt", fill="black")
        canvas.itemconfigure("l6_clt", fill="black")
        canvas.itemconfigure("b3", fill="black")
        canvas.itemconfigure("b4", fill="black")
        canvas.itemconfigure("l5.1_cl2", fill="black")
        canvas.itemconfigure("l5.2_cl2", fill="black")
        canvas.itemconfigure("l1.1_cc", fill="black")
        canvas.itemconfigure("l1.2_cc", fill="black")
        canvas.itemconfigure("l2_cc", fill="black")
        canvas.itemconfigure("l3_cc", fill="black")
        canvas.itemconfigure("m_cc", fill="white")
        canvas.itemconfigure("l4_cl2", fill="black")
        canvas.itemconfigure("l3_cl2", fill="black")
        canvas.itemconfigure("l1_cl2", fill="black")
        #messagebox.showinfo("", "Tensiunea este întreruptă de pe linie.")
    if activate_load_cl1 and close_clp_cl1:
        activate_load_cl1 = False
        canvas.itemconfigure("l1_cl1", fill="black")
        canvas.itemconfigure("l2_cl1", fill="black")
        #messagebox.showinfo("", "Tensiunea este întreruptă de pe linie.")
    if activate_load_cl1:
        activate_load_cl1 = False
        canvas.itemconfigure("l1_cl1", fill="black")
        #messagebox.showinfo("", "Tensiunea este întreruptă de pe linie.")


def toggle_close_clp_cl1():
    global close_clp_cl1
    if close_sl_cl1:
        messagebox.showerror("Interblocaj", "Separatorul de linie este închis.")
    elif connect_i_cl1:
        messagebox.showerror("Interblocaj!", "întrerupătorul este conectat.")
    elif not close_clp_cl1 and activate_load_cl1:
        close_clp_cl1 = True
        canvas.itemconfigure(clp_cl1, fill="red")
        canvas.itemconfigure("l2_cl1", fill="red")
        #messagebox.showinfo("", "CLP este închis.")
    elif not close_clp_cl1:
        close_clp_cl1 = True
        canvas.itemconfigure(clp_cl1, fill="red")
        #messagebox.showinfo("", "CLP este închis.")


def toggle_open_clp_cl1():
    global close_clp_cl1
    if close_clp_cl1:
        close_clp_cl1 = False
        canvas.itemconfigure(clp_cl1, fill="green")
        canvas.itemconfigure("l2_cl1", fill="black")
        #messagebox.showinfo("", "CLP este deschis.")


def toggle_close_sl_cl1():
    global close_sl_cl1
    if close_clp_cl1:
        messagebox.showerror("Interblocaj!", "CLP este închis.")
    elif not close_sl_cl1 and activate_load_cl1:
        close_sl_cl1 = True
        canvas.itemconfigure(sl_cl1, fill="red")
        canvas.itemconfigure("l3_cl1", fill="red")
        #messagebox.showinfo("", "Separatorul de linie este închis.")
    elif not close_sl_cl1:
        close_sl_cl1 = True
        canvas.itemconfigure(sl_cl1, fill="red")
        #messagebox.showinfo("", "Separatorul de linie este închis.")


def toggle_open_sl_cl1():
    global close_sl_cl1
    if connect_i_cl1:
        messagebox.showerror("Interblocaj!", "Întrerupătorul este conectat.")
    elif close_sl_cl1:
        close_sl_cl1 = False
        canvas.itemconfigure(sl_cl1, fill="green")
        canvas.itemconfigure("l3_cl1", fill="black")
        #messagebox.showinfo("", "Separatorul de linie este deschis.")


def toggle_connect_i_cl1():
    global connect_i_cl1
    if not (close_sb1_cl1 or close_sb2_cl1):
        messagebox.showerror("Interblocaj!", "Amândouă separatoare de bare sunt deschise.")
    elif not close_sl_cl1:
        messagebox.showerror("Interblocaj!",
                             "Separatorul de linie este deschis.")
    elif close_clp_cl1:
        messagebox.showerror("Interblocaj!", "CLP este închis.")
    elif not activate_load_cl1 and not connect_i_cl1:
        connect_i_cl1 = True
        canvas.itemconfigure(i_cl1, fill="red")
    if activate_load_cl2 and close_sl_cl2 and connect_i_cl2 and close_sb1_cl2 and close_sb11_clt and connect_i_clt and close_sb12_clt and close_sb1_cl1 and close_sl_cl1:
        connect_i_cl1 = True
        canvas.itemconfigure(i_cl1, fill="red")
        canvas.itemconfigure("l1_cl1", fill="red")
        canvas.itemconfigure("l3_cl1", fill="red")
        #messagebox.showinfo("", "Întrerupătorul este conectat.")
    elif activate_load_cl2 and close_sl_cl2 and connect_i_cl2 and close_sb2_cl2 and close_sb21_clt and connect_i_clt and close_sb22_clt and close_sb2_cl1 and close_sl_cl1:
        connect_i_cl1 = True
        canvas.itemconfigure(i_cl1, fill="red")
        canvas.itemconfigure("l1_cl1", fill="red")
        canvas.itemconfigure("l3_cl1", fill="red")
        #messagebox.showinfo("", "Întrerupătorul este conectat.")
    elif activate_load_cl1 and close_sl_cl1 and close_sb1_cl1 and close_sb11_clt and connect_i_clt and close_sb12_clt and close_sb1_cl2 and connect_i_cl2 and close_sl_cl2:
        connect_i_cl1 = True
        canvas.itemconfigure(i_cl1, fill="red")
        canvas.itemconfigure("l4_cl1", fill="red")
        canvas.itemconfigure("l5.1_cl1", fill="red")
        canvas.itemconfigure("b1", fill="red")
        canvas.itemconfigure("l1_clt", fill="red")
        canvas.itemconfigure("l5_clt", fill="red")
        canvas.itemconfigure("l6_clt", fill="red")
        canvas.itemconfigure("l3_clt", fill="red")
        canvas.itemconfigure("b3", fill="red")
        canvas.itemconfigure("l1.1_cc", fill="red")
        canvas.itemconfigure("l5.1_cl2", fill="red")
        canvas.itemconfigure("l4_cl2", fill="red")
        canvas.itemconfigure("l3_cl2", fill="red")
        canvas.itemconfigure("l1_cl2", fill="red")
        #messagebox.showinfo("", "Întrerupătorul este conectat.")
    elif activate_load_cl1 and close_sl_cl1 and close_sb2_cl1 and close_sb21_clt and connect_i_clt and close_sb22_clt and close_sb2_cl2 and connect_i_cl2 and close_sl_cl2:
        connect_i_cl1 = True
        canvas.itemconfigure(i_cl1, fill="red")
        canvas.itemconfigure("l4_cl1", fill="red")
        canvas.itemconfigure("l5.2_cl1", fill="red")
        canvas.itemconfigure("b2", fill="red")
        canvas.itemconfigure("l2_clt", fill="red")
        canvas.itemconfigure("l6_clt", fill="red")
        canvas.itemconfigure("l4_clt", fill="red")
        canvas.itemconfigure("l5_clt", fill="red")
        canvas.itemconfigure("b4", fill="red")
        canvas.itemconfigure("l1.2_cc", fill="red")
        canvas.itemconfigure("l5.2_cl2", fill="red")
        canvas.itemconfigure("l4_cl2", fill="red")
        canvas.itemconfigure("l3_cl2", fill="red")
        canvas.itemconfigure("l1_cl2", fill="red")
        #messagebox.showinfo("", "Întrerupătorul este conectat.")
    elif activate_load_cl1 and close_sl_cl1 and close_sb1_cl1 and close_sb11_clt and connect_i_clt and close_sb12_clt and close_sb1_cl2:
        connect_i_cl1 = True
        canvas.itemconfigure(i_cl1, fill="red")
        canvas.itemconfigure("l4_cl1", fill="red")
        canvas.itemconfigure("l5.1_cl1", fill="red")
        canvas.itemconfigure("b1", fill="red")
        canvas.itemconfigure("l1_clt", fill="red")
        canvas.itemconfigure("l5_clt", fill="red")
        canvas.itemconfigure("l6_clt", fill="red")
        canvas.itemconfigure("l3_clt", fill="red")
        canvas.itemconfigure("b3", fill="red")
        canvas.itemconfigure("l1.1_cc", fill="red")
        canvas.itemconfigure("l5.1_cl2", fill="red")
        canvas.itemconfigure("l4_cl2", fill="red")
        #messagebox.showinfo("", "Întrerupătorul este conectat.")
    elif activate_load_cl1 and close_sl_cl1 and close_sb2_cl1 and close_sb21_clt and connect_i_clt and close_sb22_clt and close_sb2_cl2:
        connect_i_cl1 = True
        canvas.itemconfigure(i_cl1, fill="red")
        canvas.itemconfigure("l4_cl1", fill="red")
        canvas.itemconfigure("l5.2_cl1", fill="red")
        canvas.itemconfigure("b2", fill="red")
        canvas.itemconfigure("l2_clt", fill="red")
        canvas.itemconfigure("l6_clt", fill="red")
        canvas.itemconfigure("l4_clt", fill="red")
        canvas.itemconfigure("l5_clt", fill="red")
        canvas.itemconfigure("b4", fill="red")
        canvas.itemconfigure("l1.2_cc", fill="red")
        canvas.itemconfigure("l5.2_cl2", fill="red")
        canvas.itemconfigure("l4_cl2", fill="red")
        #messagebox.showinfo("", "Întrerupătorul este conectat.")
    if activate_load_cl1 and close_sl_cl1 and close_sb1_cl1 and close_sb11_clt and connect_i_clt and close_sb12_clt and close_sb1_cc and connect_i_cc:
        connect_i_cl1 = True
        canvas.itemconfigure(i_cl1, fill="red")
        canvas.itemconfigure("l4_cl1", fill="red")
        canvas.itemconfigure("l5.1_cl1", fill="red")
        canvas.itemconfigure("b1", fill="red")
        canvas.itemconfigure("l1_clt", fill="red")
        canvas.itemconfigure("l5_clt", fill="red")
        canvas.itemconfigure("l6_clt", fill="red")
        canvas.itemconfigure("l3_clt", fill="red",)
        canvas.itemconfigure("b3", fill="red")
        canvas.itemconfigure("l1.1_cc", fill="red")
        canvas.itemconfigure("l5.1_cl2", fill="red")
        canvas.itemconfigure("l2_cc", fill="red")
        canvas.itemconfigure("l3_cc", fill="red")
        canvas.itemconfigure("m_cc", fill="red")
        #messagebox.showinfo("", "Întrerupătorul este conectat.")
    elif activate_load_cl1 and close_sl_cl1 and close_sb2_cl1 and close_sb21_clt and connect_i_clt and close_sb22_clt and close_sb2_cc and connect_i_cc:
        connect_i_cl1 = True
        canvas.itemconfigure(i_cl1, fill="red")
        canvas.itemconfigure("l4_cl1", fill="red")
        canvas.itemconfigure("l5.2_cl1", fill="red")
        canvas.itemconfigure("b2", fill="red")
        canvas.itemconfigure("l2_clt", fill="red")
        canvas.itemconfigure("l6_clt", fill="red")
        canvas.itemconfigure("l4_clt", fill="red")
        canvas.itemconfigure("l5_clt", fill="red")
        canvas.itemconfigure("b4", fill="red")
        canvas.itemconfigure("l1.2_cc", fill="red")
        canvas.itemconfigure("l5.2_cl2", fill="red")
        canvas.itemconfigure("l2_cc", fill="red")
        canvas.itemconfigure("l3_cc", fill="red")
        canvas.itemconfigure("m_cc", fill="red")
        #messagebox.showinfo("", "Întrerupătorul este conectat.")
    elif activate_load_cl1 and close_sl_cl1 and close_sb1_cl1 and close_sb11_clt and connect_i_clt and close_sb12_clt and close_sb1_cc:
        connect_i_cl1 = True
        canvas.itemconfigure(i_cl1, fill="red")
        canvas.itemconfigure("l4_cl1", fill="red")
        canvas.itemconfigure("l5.1_cl1", fill="red")
        canvas.itemconfigure("b1", fill="red")
        canvas.itemconfigure("l1_clt", fill="red")
        canvas.itemconfigure("l5_clt", fill="red")
        canvas.itemconfigure("l6_clt", fill="red")
        canvas.itemconfigure("l3_clt", fill="red",)
        canvas.itemconfigure("b3", fill="red")
        canvas.itemconfigure("l1.1_cc", fill="red")
        canvas.itemconfigure("l5.1_cl2", fill="red")
        canvas.itemconfigure("l2_cc", fill="red")
        #messagebox.showinfo("", "Întrerupătorul este conectat.")
    elif activate_load_cl1 and close_sl_cl1 and close_sb2_cl1 and close_sb21_clt and connect_i_clt and close_sb22_clt and close_sb2_cc:
        connect_i_cl1 = True
        canvas.itemconfigure(i_cl1, fill="red")
        canvas.itemconfigure("l4_cl1", fill="red")
        canvas.itemconfigure("l5.2_cl1", fill="red")
        canvas.itemconfigure("b2", fill="red")
        canvas.itemconfigure("l2_clt", fill="red")
        canvas.itemconfigure("l6_clt", fill="red")
        canvas.itemconfigure("l4_clt", fill="red")
        canvas.itemconfigure("l5_clt", fill="red")
        canvas.itemconfigure("b4", fill="red")
        canvas.itemconfigure("l1.2_cc", fill="red")
        canvas.itemconfigure("l5.2_cl2", fill="red")
        canvas.itemconfigure("l2_cc", fill="red")
        #messagebox.showinfo("", "Întrerupătorul este conectat.")
    elif activate_load_cl1 and close_sl_cl1 and close_sb1_cl1 and close_sb11_clt and connect_i_clt and close_sb12_clt:
        connect_i_cl1 = True
        canvas.itemconfigure(i_cl1, fill="red")
        canvas.itemconfigure("l4_cl1", fill="red")
        canvas.itemconfigure("l5.1_cl1", fill="red")
        canvas.itemconfigure("b1", fill="red")
        canvas.itemconfigure("l1_clt", fill="red")
        canvas.itemconfigure("l5_clt", fill="red")
        canvas.itemconfigure("l6_clt", fill="red")
        canvas.itemconfigure("l3_clt", fill="red")
        canvas.itemconfigure("b3", fill="red")
        canvas.itemconfigure("l1.1_cc", fill="red")
        canvas.itemconfigure("l5.1_cl2", fill="red")
        #messagebox.showinfo("", "Întrerupătorul este conectat.")
    elif activate_load_cl1 and close_sl_cl1 and close_sb2_cl1 and close_sb21_clt and connect_i_clt and close_sb22_clt:
        connect_i_cl1 = True
        canvas.itemconfigure(i_cl1, fill="red")
        canvas.itemconfigure("l4_cl1", fill="red")
        canvas.itemconfigure("l5.2_cl1", fill="red")
        canvas.itemconfigure("b2", fill="red")
        canvas.itemconfigure("l2_clt", fill="red")
        canvas.itemconfigure("l6_clt", fill="red")
        canvas.itemconfigure("l4_clt", fill="red")
        canvas.itemconfigure("l5_clt", fill="red")
        canvas.itemconfigure("b4", fill="red")
        canvas.itemconfigure("l1.2_cc", fill="red")
        canvas.itemconfigure("l5.2_cl2", fill="red")
        #messagebox.showinfo("", "Întrerupătorul este conectat.")
    elif activate_load_cl1 and close_sl_cl1 and close_sb1_cl1 and close_sb11_clt:
        connect_i_cl1 = True
        canvas.itemconfigure(i_cl1, fill="red")
        canvas.itemconfigure("l4_cl1", fill="red")
        canvas.itemconfigure("l5.1_cl1", fill="red")
        canvas.itemconfigure("b1", fill="red")
        canvas.itemconfigure("l1_clt", fill="red")
        canvas.itemconfigure("l5_clt", fill="red")
        #messagebox.showinfo("", "Întrerupătorul este conectat.")
    elif activate_load_cl1 and close_sl_cl1 and close_sb2_cl1 and close_sb21_clt:
        connect_i_cl1 = True
        canvas.itemconfigure(i_cl1, fill="red")
        canvas.itemconfigure("l4_cl1", fill="red")
        canvas.itemconfigure("l5.2_cl1", fill="red")
        canvas.itemconfigure("b2", fill="red")
        canvas.itemconfigure("l2_clt", fill="red")
        canvas.itemconfigure("l6_clt", fill="red")
        #messagebox.showinfo("", "Întrerupătorul este conectat.")
    elif activate_load_cl1 and close_sl_cl1 and close_sb1_cl1:
        connect_i_cl1 = True
        canvas.itemconfigure(i_cl1, fill="red")
        canvas.itemconfigure("l4_cl1", fill="red")
        canvas.itemconfigure("l5.1_cl1", fill="red")
        canvas.itemconfigure("b1", fill="red")
        canvas.itemconfigure("l1_clt", fill="red")
        #messagebox.showinfo("", "Întrerupătorul este conectat.")
    elif activate_load_cl1 and close_sl_cl1 and close_sb2_cl1:
        connect_i_cl1 = True
        canvas.itemconfigure(i_cl1, fill="red")
        canvas.itemconfigure("l4_cl1", fill="red")
        canvas.itemconfigure("l5.2_cl1", fill="red")
        canvas.itemconfigure("b2", fill="red")
        canvas.itemconfigure("l2_clt", fill="red")
        #messagebox.showinfo("", "Întrerupătorul este conectat.")


def toggle_disconnect_i_cl1():
    global connect_i_cl1
    if connect_i_cl1 and activate_load_cl1:
        connect_i_cl1 = False
        canvas.itemconfigure(i_cl1, fill="green")
        canvas.itemconfigure("l4_cl1", fill="black")
        canvas.itemconfigure("l5.1_cl1", fill="black")
        canvas.itemconfigure("l5.2_cl1", fill="black")
        canvas.itemconfigure("b1", fill="black")
        canvas.itemconfigure("b2", fill="black")
        canvas.itemconfigure("l1_clt", fill="black")
        canvas.itemconfigure("l2_clt", fill="black")
        canvas.itemconfigure("l3_clt", fill="black")
        canvas.itemconfigure("l4_clt", fill="black")
        canvas.itemconfigure("l5_clt", fill="black")
        canvas.itemconfigure("l6_clt", fill="black")
        canvas.itemconfigure("b3", fill="black")
        canvas.itemconfigure("b4", fill="black")
        canvas.itemconfigure("l5.1_cl2", fill="black")
        canvas.itemconfigure("l5.2_cl2", fill="black")
        canvas.itemconfigure("l1.1_cc", fill="black")
        canvas.itemconfigure("l1.2_cc", fill="black")
        canvas.itemconfigure("l2_cc", fill="black")
        canvas.itemconfigure("l3_cc", fill="black")
        canvas.itemconfigure("m_cc", fill="white")
        canvas.itemconfigure("l4_cl2", fill="black")
        canvas.itemconfigure("l3_cl2", fill="black")
        canvas.itemconfigure("l1_cl2", fill="black")
        #messagebox.showinfo("", "Întrerupătorul este deconectat.")
    elif connect_i_cl1:
        connect_i_cl1 = False
        canvas.itemconfigure(i_cl1, fill="green")
        #messagebox.showinfo("", "Întrerupătorul este deconectat.")


def toggle_close_sb1_cl1():
    global close_sb1_cl1
    if connect_i_clt and close_sb11_clt and close_sb21_clt:
        close_sb1_cl1 = True
        canvas.itemconfigure(sb1_cl1, fill="red")
        #messagebox.showinfo("", "Separatorul de bare 1 este închis.")
    elif close_sb2_cl1:
        messagebox.showerror("Interblocaj!", "Separatorul de bare 2 este deja închis.")
    elif activate_load_cl2 and close_sl_cl2 and connect_i_cl2 and close_sb1_cl2 and close_sb12_clt and close_sb11_clt and connect_i_clt:
        close_sb1_cl1 = True
        canvas.itemconfigure(sb1_cl1, fill="red")
        canvas.itemconfigure("l4_cl1", fill="red")
        # messagebox.showinfo("", "Separatorul de bare 1 este închis.")
    elif not close_sb1_cl1:
        close_sb1_cl1 = True
        canvas.itemconfigure(sb1_cl1, fill="red")
        #messagebox.showinfo("", "Separatorul de bare 1 este închis.")


def toggle_open_sb1_cl1():
    global close_sb1_cl1
    if activate_load_cl1 and close_sl_cl1 and connect_i_cl1 and close_sb1_cl1 and close_sb2_cl1 and connect_i_clt and close_sb11_clt and close_sb21_clt:
        close_sb1_cl1 = False
        canvas.itemconfigure(sb1_cl1, fill="green")
        #messagebox.showinfo("", "Separatorul de bare 1 este deschis.")
    elif activate_load_cl2 and close_sl_cl2 and connect_i_cl2 and close_sb1_cl2 and close_sb11_clt and connect_i_clt and close_sb12_clt:
        close_sb1_cl1 = False
        canvas.itemconfigure(sb1_cl1, fill="green")
        canvas.itemconfigure("l4_cl1", fill="black")
        #messagebox.showinfo("", "Separatorul de bare 3 este deschis.")
    elif connect_i_cl1:
        messagebox.showerror("Interblocaj!", "Întrerupătorul este conectat.")
    elif close_sb1_cl1:
        close_sb1_cl1 = False
        canvas.itemconfigure(sb1_cl1, fill="green")
        #essagebox.showinfo("", "Separatorul de bare 1 este deschis.")


def toggle_close_sb2_cl1():
    global close_sb2_cl1
    if connect_i_clt and close_sb11_clt and close_sb21_clt:
        close_sb2_cl1 = True
        canvas.itemconfigure(sb2_cl1, fill="red")
        #messagebox.showinfo("", "Separatorul de bare 2 este închis.")
    elif close_sb1_cl1:
        messagebox.showerror("Interblocaj!", "Separatorul de bare 1 este deja închis.")
    elif activate_load_cl2 and close_sl_cl2 and connect_i_cl2 and close_sb2_cl2 and close_sb22_clt and close_sb21_clt and connect_i_clt:
        close_sb2_cl1 = True
        canvas.itemconfigure(sb2_cl1, fill="red")
        canvas.itemconfigure("l4_cl1", fill="red")
        # messagebox.showinfo("", "Separatorul de bare 1 este închis.")
    elif not close_sb2_cl1:
        close_sb2_cl1 = True
        canvas.itemconfigure(sb2_cl1, fill="red")
        #messagebox.showinfo("", "Separatorul de bare 2 este închis.")


def toggle_open_sb2_cl1():
    global close_sb2_cl1
    if activate_load_cl1 and close_sl_cl1 and connect_i_cl1 and close_sb1_cl1 and close_sb2_cl1 and connect_i_clt and close_sb11_clt and close_sb21_clt:
        close_sb2_cl1 = False
        canvas.itemconfigure(sb2_cl1, fill="green")
        #messagebox.showinfo("", "Separatorul de bare 2 este deschis.")
    elif activate_load_cl2 and close_sl_cl2 and connect_i_cl2 and close_sb2_cl2 and close_sb21_clt and connect_i_clt and close_sb22_clt:
        close_sb2_cl1 = False
        canvas.itemconfigure(sb2_cl1, fill="green")
        canvas.itemconfigure("l4_cl1", fill="black")
        #messagebox.showinfo("", "Separatorul de bare 3 este deschis.")
    elif connect_i_cl1:
        messagebox.showerror("Interblocaj!", "Întrerupătorul este conectat.")
    elif close_sb2_cl1:
        close_sb2_cl1 = False
        canvas.itemconfigure(sb2_cl1, fill="green")
        #messagebox.showinfo("", "Separatorul de bare 2 este deschis.")


# Condiții Celulă cu cuplă longo-transversală---------------------------------------------------------------------------


def toggle_close_sb11_clt():
    global close_sb11_clt
    if close_sb22_clt:
        messagebox.showerror("Interblocaj!", "Nu puteți închide simultan separatoarele de bare 1 și 4.")
    elif activate_load_cl1 and close_sl_cl1 and connect_i_cl1 and close_sb1_cl1:
        close_sb11_clt = True
        canvas.itemconfigure(sb11_clt, fill="red")
        canvas.itemconfigure("l5_clt", fill="red")
        #messagebox.showinfo("Stare:", "Separatorul de bare 1 este închis.")
    elif not close_sb11_clt:
        close_sb11_clt = True
        canvas.itemconfigure(sb11_clt, fill="red")
        #messagebox.showinfo("Stare:", "Separatorul de bare 1 este închis.")


def toggle_open_sb11_clt():
    global close_sb11_clt
    if connect_i_clt:
        messagebox.showerror("Interblocaj!", "Întrerupătorul este conectat.")
    elif activate_load_cl1 and close_sl_cl1 and connect_i_cl1 and close_sb1_cl1:
        close_sb11_clt = False
        canvas.itemconfigure(sb11_clt, fill="green")
        canvas.itemconfigure("l5_clt", fill="black")
        #messagebox.showinfo("Stare:", "Separatorul de bare 1 este deschis.")
    elif close_sb11_clt:
        close_sb11_clt = False
        canvas.itemconfigure(sb11_clt, fill="green")
        #messagebox.showinfo("Stare:", "Separatorul de bare 1 este deschis.")


def toggle_close_sb21_clt():
    global close_sb21_clt
    if close_sb12_clt:
        messagebox.showerror("Interblocaj!", "Nu puteți închide simultan separatoarele de bare 2 și 3.")
    elif activate_load_cl1 and close_sl_cl1 and connect_i_cl1 and close_sb2_cl1:
        close_sb21_clt = True
        canvas.itemconfigure(sb21_clt, fill="red")
        canvas.itemconfigure("l6_clt", fill="red")
        #messagebox.showinfo("Stare:", "Separatorul de bare 2 este închis.")
    elif not close_sb21_clt:
        close_sb21_clt = True
        canvas.itemconfigure(sb21_clt, fill="red")
        #messagebox.showinfo("Stare:", "Separatorul de bare 2 este închis.")


def toggle_open_sb21_clt():
    global close_sb21_clt
    if connect_i_clt:
        messagebox.showerror("Interblocaj!", "Întrerupătorul este conectat.")
    elif activate_load_cl1 and close_sl_cl1 and connect_i_cl1 and close_sb2_cl1:
        close_sb21_clt = False
        canvas.itemconfigure(sb21_clt, fill="green")
        canvas.itemconfigure("l6_clt", fill="black")
        #messagebox.showinfo("Stare:", "Separatorul de bare 2 este deschis.")
    elif close_sb21_clt:
        close_sb21_clt = False
        canvas.itemconfigure(sb21_clt, fill="green")
        #messagebox.showinfo("Stare:", "Separatorul de bare 2 este deschis.")


def toggle_connect_i_clt():
    global connect_i_clt
    if activate_load_cl2 and close_sl_cl2 and connect_i_cl2 and close_sb2_cl2 and close_sb12_clt and close_sb22_clt:
        canvas.itemconfigure(i_clt, fill="red")
        canvas.itemconfigure("l3_clt", fill="red")
        canvas.itemconfigure("l6_clt", fill="red")
        canvas.itemconfigure("b3", fill="red")
        canvas.itemconfigure("l1.1_cc", fill="red")
        canvas.itemconfigure("l5.1_cl2", fill="red")
        connect_i_clt = True
        #messagebox.showinfo("Stare:", "Întrerupătorul este conectat.")
    elif activate_load_cl2 and close_sl_cl2 and connect_i_cl2 and close_sb1_cl2 and close_sb12_clt and close_sb22_clt:
        canvas.itemconfigure(i_clt, fill="red")
        canvas.itemconfigure("l4_clt", fill="red")
        canvas.itemconfigure("l5_clt", fill="red")
        canvas.itemconfigure("b4", fill="red")
        canvas.itemconfigure("l1.2_cc", fill="red")
        canvas.itemconfigure("l5.2_cl2", fill="red")
        connect_i_clt = True
        #messagebox.showinfo("Stare:", "Întrerupătorul este conectat.")
    if activate_load_cl1 and close_sl_cl1 and connect_i_cl1 and close_sb2_cl1 and close_sb11_clt and close_sb21_clt:
        canvas.itemconfigure(i_clt, fill="red")
        canvas.itemconfigure("l1_clt", fill="red")
        canvas.itemconfigure("l5_clt", fill="red")
        canvas.itemconfigure("b1", fill="red")
        canvas.itemconfigure("l5.1_cl1", fill="red")
        connect_i_clt = True
        #messagebox.showinfo("Stare:", "Întrerupătorul este conectat.")
    elif activate_load_cl1 and close_sl_cl1 and connect_i_cl1 and close_sb1_cl1 and close_sb11_clt and close_sb21_clt:
        canvas.itemconfigure(i_clt, fill="red")
        canvas.itemconfigure("l2_clt", fill="red")
        canvas.itemconfigure("l6_clt", fill="red")
        canvas.itemconfigure("b2", fill="red")
        canvas.itemconfigure("l5.2_cl1", fill="red")
        connect_i_clt = True
        #messagebox.showinfo("Stare:", "Întrerupătorul este conectat.")
    if activate_load_cl2 and close_sl_cl2 and connect_i_cl2 and close_sb2_cl2 and close_sb22_clt and close_sb21_clt and close_sb2_cl1 and connect_i_cl1 and close_sl_cl1:
        canvas.itemconfigure(i_clt, fill="red")
        canvas.itemconfigure("l2_clt", fill="red")
        canvas.itemconfigure("l6_clt", fill="red")
        canvas.itemconfigure("b2", fill="red")
        canvas.itemconfigure("l5.2_cl1", fill="red")
        canvas.itemconfigure("l4_cl1", fill="red")
        canvas.itemconfigure("l3_cl1", fill="red")
        canvas.itemconfigure("l1_cl1", fill="red")
        connect_i_clt = True
        #messagebox.showinfo("Stare:", "Întrerupătorul este conectat.")
    elif activate_load_cl2 and close_sl_cl2 and connect_i_cl2 and close_sb1_cl2 and close_sb11_clt and close_sb12_clt and close_sb1_cl1 and connect_i_cl1 and close_sl_cl1:
        canvas.itemconfigure(i_clt, fill="red")
        canvas.itemconfigure("l5_clt", fill="red")
        canvas.itemconfigure("l1_clt", fill="red")
        canvas.itemconfigure("b1", fill="red")
        canvas.itemconfigure("l5.1_cl1", fill="red")
        canvas.itemconfigure("l4_cl1", fill="red")
        canvas.itemconfigure("l3_cl1", fill="red")
        canvas.itemconfigure("l1_cl1", fill="red")
        connect_i_clt = True
        #messagebox.showinfo("Stare:", "Întrerupătorul este conectat.")
    elif activate_load_cl2 and close_sl_cl2 and connect_i_cl2 and close_sb2_cl2 and close_sb22_clt and close_sb21_clt and close_sb2_cl1:
        canvas.itemconfigure(i_clt, fill="red")
        canvas.itemconfigure("l2_clt", fill="red")
        canvas.itemconfigure("l6_clt", fill="red")
        canvas.itemconfigure("b2", fill="red")
        canvas.itemconfigure("l5.2_cl1", fill="red")
        canvas.itemconfigure("l4_cl1", fill="red")
        connect_i_clt = True
        #messagebox.showinfo("Stare:", "Întrerupătorul este conectat.")
    elif activate_load_cl2 and close_sl_cl2 and connect_i_cl2 and close_sb1_cl2 and close_sb11_clt and close_sb12_clt and close_sb1_cl1:
        canvas.itemconfigure(i_clt, fill="red")
        canvas.itemconfigure("l5_clt", fill="red")
        canvas.itemconfigure("l1_clt", fill="red")
        canvas.itemconfigure("b1", fill="red")
        canvas.itemconfigure("l5.1_cl1", fill="red")
        canvas.itemconfigure("l4_cl1", fill="red")
        connect_i_clt = True
        #messagebox.showinfo("Stare:", "Întrerupătorul este conectat.")
    elif activate_load_cl2 and close_sl_cl2 and connect_i_cl2 and close_sb2_cl2 and close_sb22_clt and close_sb21_clt:
        canvas.itemconfigure(i_clt, fill="red")
        canvas.itemconfigure("l2_clt", fill="red")
        canvas.itemconfigure("l6_clt", fill="red")
        canvas.itemconfigure("b2", fill="red")
        canvas.itemconfigure("l5.2_cl1", fill="red")
        connect_i_clt = True
        #messagebox.showinfo("Stare:", "Întrerupătorul este conectat.")
    elif activate_load_cl2 and close_sl_cl2 and connect_i_cl2 and close_sb1_cl2 and close_sb11_clt and close_sb12_clt:
        canvas.itemconfigure(i_clt, fill="red")
        canvas.itemconfigure("l5_clt", fill="red")
        canvas.itemconfigure("l1_clt", fill="red")
        canvas.itemconfigure("b1", fill="red")
        canvas.itemconfigure("l5.1_cl1", fill="red")
        connect_i_clt = True
        #messagebox.showinfo("Stare:", "Întrerupătorul este conectat.")
    if activate_load_cl1 and close_sl_cl1 and connect_i_cl1 and close_sb2_cl1 and close_sb21_clt and close_sb22_clt and close_sb2_cl2 and connect_i_cl2 and close_sl_cl2:
        canvas.itemconfigure(i_clt, fill="red")
        canvas.itemconfigure("l4_clt", fill="red")
        canvas.itemconfigure("l5_clt", fill="red")
        canvas.itemconfigure("b4", fill="red")
        canvas.itemconfigure("l1.2_cc", fill="red")
        canvas.itemconfigure("l5.2_cl2", fill="red")
        canvas.itemconfigure("l4_cl2", fill="red")
        canvas.itemconfigure("l3_cl2", fill="red")
        canvas.itemconfigure("l1_cl2", fill="red")
        connect_i_clt = True
        #messagebox.showinfo("Stare:", "Întrerupătorul este conectat.")
    elif activate_load_cl1 and close_sl_cl1 and connect_i_cl1 and close_sb1_cl1 and close_sb11_clt and close_sb12_clt and close_sb1_cl2 and connect_i_cl2 and close_sl_cl2:
        canvas.itemconfigure(i_clt, fill="red")
        canvas.itemconfigure("l6_clt", fill="red")
        canvas.itemconfigure("l3_clt", fill="red")
        canvas.itemconfigure("b3", fill="red")
        canvas.itemconfigure("l1.1_cc", fill="red")
        canvas.itemconfigure("l5.1_cl2", fill="red")
        canvas.itemconfigure("l4_cl2", fill="red")
        canvas.itemconfigure("l3_cl2", fill="red")
        canvas.itemconfigure("l1_cl2", fill="red")
        connect_i_clt = True
        #messagebox.showinfo("Stare:", "Întrerupătorul este conectat.")
    elif activate_load_cl1 and close_sl_cl1 and connect_i_cl1 and close_sb2_cl1 and close_sb21_clt and close_sb22_clt and close_sb2_cl2:
        canvas.itemconfigure(i_clt, fill="red")
        canvas.itemconfigure("l4_clt", fill="red")
        canvas.itemconfigure("l5_clt", fill="red")
        canvas.itemconfigure("b4", fill="red")
        canvas.itemconfigure("l1.2_cc", fill="red")
        canvas.itemconfigure("l5.2_cl2", fill="red")
        canvas.itemconfigure("l4_cl2", fill="red")
        connect_i_clt = True
        #messagebox.showinfo("Stare:", "Întrerupătorul este conectat.")
    elif activate_load_cl1 and close_sl_cl1 and connect_i_cl1 and close_sb1_cl1 and close_sb11_clt and close_sb12_clt and close_sb1_cl2:
        canvas.itemconfigure(i_clt, fill="red")
        canvas.itemconfigure("l6_clt", fill="red")
        canvas.itemconfigure("l3_clt", fill="red")
        canvas.itemconfigure("b3", fill="red")
        canvas.itemconfigure("l1.1_cc", fill="red")
        canvas.itemconfigure("l5.1_cl2", fill="red")
        canvas.itemconfigure("l4_cl2", fill="red")
        connect_i_clt = True
        #messagebox.showinfo("Stare:", "Întrerupătorul este conectat.")
    if activate_load_cl1 and close_sl_cl1 and connect_i_cl1 and close_sb2_cl1 and close_sb21_clt and close_sb22_clt and close_sb2_cc and connect_i_cc:
        canvas.itemconfigure(i_clt, fill="red")
        canvas.itemconfigure("l4_clt", fill="red")
        canvas.itemconfigure("l5_clt", fill="red")
        canvas.itemconfigure("b4", fill="red")
        canvas.itemconfigure("l1.2_cc", fill="red")
        canvas.itemconfigure("l5.2_cl2", fill="red")
        canvas.itemconfigure("l2_cc", fill="red")
        canvas.itemconfigure("l3_cc", fill="red")
        canvas.itemconfigure("m_cc", fill="red")
        connect_i_clt = True
        #messagebox.showinfo("Stare:", "Întrerupătorul este conectat.")
    elif activate_load_cl1 and close_sl_cl1 and connect_i_cl1 and close_sb1_cl1 and close_sb11_clt and close_sb12_clt and close_sb1_cc and connect_i_cc:
        canvas.itemconfigure(i_clt, fill="red")
        canvas.itemconfigure("l6_clt", fill="red")
        canvas.itemconfigure("l3_clt", fill="red")
        canvas.itemconfigure("b3", fill="red")
        canvas.itemconfigure("l1.1_cc", fill="red")
        canvas.itemconfigure("l5.1_cl2", fill="red")
        canvas.itemconfigure("l2_cc", fill="red")
        canvas.itemconfigure("l3_cc", fill="red")
        canvas.itemconfigure("m_cc", fill="red")
        connect_i_clt = True
        #messagebox.showinfo("Stare:", "Întrerupătorul este conectat.")
    elif activate_load_cl1 and close_sl_cl1 and connect_i_cl1 and close_sb2_cl1 and close_sb21_clt and close_sb22_clt and close_sb2_cc:
        canvas.itemconfigure(i_clt, fill="red")
        canvas.itemconfigure("l4_clt", fill="red")
        canvas.itemconfigure("l5_clt", fill="red")
        canvas.itemconfigure("b4", fill="red")
        canvas.itemconfigure("l1.2_cc", fill="red")
        canvas.itemconfigure("l5.2_cl2", fill="red")
        canvas.itemconfigure("l2_cc", fill="red")
        connect_i_clt = True
        #messagebox.showinfo("Stare:", "Întrerupătorul este conectat.")
    elif activate_load_cl1 and close_sl_cl1 and connect_i_cl1 and close_sb1_cl1 and close_sb11_clt and close_sb12_clt and close_sb1_cc:
        canvas.itemconfigure(i_clt, fill="red")
        canvas.itemconfigure("l6_clt", fill="red")
        canvas.itemconfigure("l3_clt", fill="red")
        canvas.itemconfigure("b3", fill="red")
        canvas.itemconfigure("l1.1_cc", fill="red")
        canvas.itemconfigure("l5.1_cl2", fill="red")
        canvas.itemconfigure("l2_cc", fill="red")
        connect_i_clt = True
        #messagebox.showinfo("Stare:", "Întrerupătorul este conectat.")
    elif activate_load_cl1 and close_sl_cl1 and connect_i_cl1 and close_sb2_cl1 and close_sb21_clt and close_sb22_clt:
        canvas.itemconfigure(i_clt, fill="red")
        canvas.itemconfigure("l4_clt", fill="red")
        canvas.itemconfigure("l5_clt", fill="red")
        canvas.itemconfigure("b4", fill="red")
        canvas.itemconfigure("l1.2_cc", fill="red")
        canvas.itemconfigure("l5.2_cl2", fill="red")
        connect_i_clt = True
        #messagebox.showinfo("Stare:", "Întrerupătorul este conectat.")
    elif activate_load_cl1 and close_sl_cl1 and connect_i_cl1 and close_sb1_cl1 and close_sb11_clt and close_sb12_clt:
        canvas.itemconfigure(i_clt, fill="red")
        canvas.itemconfigure("l6_clt", fill="red")
        canvas.itemconfigure("l3_clt", fill="red")
        canvas.itemconfigure("b3", fill="red")
        canvas.itemconfigure("l1.1_cc", fill="red")
        canvas.itemconfigure("l5.1_cl2", fill="red")
        connect_i_clt = True
        #messagebox.showinfo("Stare:", "Întrerupătorul este conectat.")
    elif (close_sb11_clt and close_sb12_clt) or (close_sb21_clt and close_sb22_clt) or (
            close_sb11_clt and close_sb21_clt) or (close_sb12_clt and close_sb22_clt):
        connect_i_clt = True
        canvas.itemconfigure(i_clt, fill="red")
        #messagebox.showinfo("Stare:", "Întrerupătorul este conectat.")
    else:
        messagebox.showerror("Interblocaj!", "Separatoarele de bare sunt deschise.")


def toggle_disconnect_i_clt():
    global connect_i_clt
    if activate_load_cl2 and close_sl_cl2 and connect_i_cl2 and close_sb1_cl2 and close_sb12_clt and close_sb22_clt:
        connect_i_clt = False
        canvas.itemconfigure(i_clt, fill="green")
        canvas.itemconfigure("l5_clt", fill="black")
        canvas.itemconfigure("l4_clt", fill="black")
        canvas.itemconfigure("b4", fill="black")
        canvas.itemconfigure("l1.2_cc", fill="black")
        canvas.itemconfigure("l5.2_cl2", fill="black")
        #messagebox.showinfo("Stare:", "Întrerupătorul este deconectat.")
    elif activate_load_cl2 and close_sl_cl2 and connect_i_cl2 and close_sb2_cl2 and close_sb12_clt and close_sb22_clt:
        connect_i_clt = False
        canvas.itemconfigure(i_clt, fill="green")
        canvas.itemconfigure("l6_clt", fill="black")
        canvas.itemconfigure("l3_clt", fill="black")
        canvas.itemconfigure("b3", fill="black")
        canvas.itemconfigure("l1.1_cc", fill="black")
        canvas.itemconfigure("l5.1_cl2", fill="black")
        #messagebox.showinfo("Stare:", "Întrerupătorul este deconectat.")
    if activate_load_cl1 and close_sl_cl1 and connect_i_cl1 and close_sb1_cl1 and close_sb11_clt and close_sb21_clt:
        connect_i_clt = False
        canvas.itemconfigure(i_clt, fill="green")
        canvas.itemconfigure("l6_clt", fill="black")
        canvas.itemconfigure("l2_clt", fill="black")
        canvas.itemconfigure("b2", fill="black")
        canvas.itemconfigure("l5.2_cl1", fill="black")
        #messagebox.showinfo("Stare:", "Întrerupătorul este deconectat.")
    elif activate_load_cl1 and close_sl_cl1 and connect_i_cl1 and close_sb2_cl1 and close_sb11_clt and close_sb21_clt:
        connect_i_clt = False
        canvas.itemconfigure(i_clt, fill="green")
        canvas.itemconfigure("l5_clt", fill="black")
        canvas.itemconfigure("l1_clt", fill="black")
        canvas.itemconfigure("b1", fill="black")
        canvas.itemconfigure("l5.1_cl1", fill="black")
        #messagebox.showinfo("Stare:", "Întrerupătorul este deconectat.")
    if activate_load_cl2 and close_sl_cl2 and connect_i_cl2 and close_sb2_cl2 and close_sb21_clt and close_sb22_clt and close_sb2_cl1 and connect_i_cl1 and close_sl_cl1:
        connect_i_clt = False
        canvas.itemconfigure(i_clt, fill="green")
        canvas.itemconfigure("l2_clt", fill="black")
        canvas.itemconfigure("l6_clt", fill="black")
        canvas.itemconfigure("b2", fill="black")
        canvas.itemconfigure("l5.2_cl1", fill="black")
        canvas.itemconfigure("l4_cl1", fill="black")
        canvas.itemconfigure("l3_cl1", fill="black")
        canvas.itemconfigure("l1_cl1", fill="black")
        #messagebox.showinfo("Stare:", "Întrerupătorul este deconectat.")
    elif activate_load_cl2 and close_sl_cl2 and connect_i_cl2 and close_sb1_cl2 and close_sb11_clt and close_sb12_clt and close_sb1_cl1 and connect_i_cl1 and close_sl_cl1:
        connect_i_clt = False
        canvas.itemconfigure(i_clt, fill="green")
        canvas.itemconfigure("l5_clt", fill="black")
        canvas.itemconfigure("l1_clt", fill="black")
        canvas.itemconfigure("b1", fill="black")
        canvas.itemconfigure("l5.1_cl1", fill="black")
        canvas.itemconfigure("l4_cl1", fill="black")
        canvas.itemconfigure("l3_cl1", fill="black")
        canvas.itemconfigure("l1_cl1", fill="black")
        #messagebox.showinfo("Stare:", "Întrerupătorul este deconectat.")
    elif activate_load_cl2 and close_sl_cl2 and connect_i_cl2 and close_sb2_cl2 and close_sb21_clt and close_sb22_clt and close_sb2_cl1:
        connect_i_clt = False
        canvas.itemconfigure(i_clt, fill="green")
        canvas.itemconfigure("l2_clt", fill="black")
        canvas.itemconfigure("l6_clt", fill="black")
        canvas.itemconfigure("b2", fill="black")
        canvas.itemconfigure("l5.2_cl1", fill="black")
        canvas.itemconfigure("l4_cl1", fill="black")
        #messagebox.showinfo("Stare:", "Întrerupătorul este deconectat.")
    elif activate_load_cl2 and close_sl_cl2 and connect_i_cl2 and close_sb1_cl2 and close_sb11_clt and close_sb12_clt and close_sb1_cl1:
        connect_i_clt = False
        canvas.itemconfigure(i_clt, fill="green")
        canvas.itemconfigure("l5_clt", fill="black")
        canvas.itemconfigure("l1_clt", fill="black")
        canvas.itemconfigure("b1", fill="black")
        canvas.itemconfigure("l5.1_cl1", fill="black")
        canvas.itemconfigure("l4_cl1", fill="black")
        #messagebox.showinfo("Stare:", "Întrerupătorul este deconectat.")
    elif activate_load_cl2 and close_sl_cl2 and connect_i_cl2 and close_sb2_cl2 and close_sb21_clt and close_sb22_clt:
        connect_i_clt = False
        canvas.itemconfigure(i_clt, fill="green")
        canvas.itemconfigure("l2_clt", fill="black")
        canvas.itemconfigure("l6_clt", fill="black")
        canvas.itemconfigure("b2", fill="black")
        canvas.itemconfigure("l5.2_cl1", fill="black")
        #messagebox.showinfo("Stare:", "Întrerupătorul este deconectat.")
    elif activate_load_cl2 and close_sl_cl2 and connect_i_cl2 and close_sb1_cl2 and close_sb11_clt and close_sb12_clt:
        connect_i_clt = False
        canvas.itemconfigure(i_clt, fill="green")
        canvas.itemconfigure("l5_clt", fill="black")
        canvas.itemconfigure("l1_clt", fill="black")
        canvas.itemconfigure("b1", fill="black")
        canvas.itemconfigure("l5.1_cl1", fill="black")
        #messagebox.showinfo("Stare:", "Întrerupătorul este deconectat.")
    if activate_load_cl1 and close_sl_cl1 and connect_i_cl1 and close_sb2_cl1 and close_sb21_clt and close_sb22_clt and close_sb2_cl2 and connect_i_cl2 and close_sl_cl2:
        connect_i_clt = False
        canvas.itemconfigure(i_clt, fill="green")
        canvas.itemconfigure("l4_clt", fill="black")
        canvas.itemconfigure("l5_clt", fill="black")
        canvas.itemconfigure("b4", fill="black")
        canvas.itemconfigure("l1.2_cc", fill="black")
        canvas.itemconfigure("l5.2_cl2", fill="black")
        canvas.itemconfigure("l4_cl2", fill="black")
        canvas.itemconfigure("l3_cl2", fill="black")
        canvas.itemconfigure("l1_cl2", fill="black")
        #messagebox.showinfo("Stare:", "Întrerupătorul este deconectat.")
    elif activate_load_cl1 and close_sl_cl1 and connect_i_cl1 and close_sb1_cl1 and close_sb11_clt and close_sb12_clt and close_sb1_cl2 and connect_i_cl2 and close_sl_cl2:
        connect_i_clt = False
        canvas.itemconfigure(i_clt, fill="green")
        canvas.itemconfigure("l6_clt", fill="black")
        canvas.itemconfigure("l3_clt", fill="black")
        canvas.itemconfigure("b3", fill="black")
        canvas.itemconfigure("l1.1_cc", fill="black")
        canvas.itemconfigure("l5.1_cl2", fill="black")
        canvas.itemconfigure("l4_cl2", fill="black")
        canvas.itemconfigure("l3_cl2", fill="black")
        canvas.itemconfigure("l1_cl2", fill="black")
        #messagebox.showinfo("Stare:", "Întrerupătorul este deconectat.")
    elif activate_load_cl1 and close_sl_cl1 and connect_i_cl1 and close_sb2_cl1 and close_sb21_clt and close_sb22_clt and close_sb2_cl2:
        connect_i_clt = False
        canvas.itemconfigure(i_clt, fill="green")
        canvas.itemconfigure("l4_clt", fill="black")
        canvas.itemconfigure("l5_clt", fill="black")
        canvas.itemconfigure("b4", fill="black")
        canvas.itemconfigure("l1.2_cc", fill="black")
        canvas.itemconfigure("l5.2_cl2", fill="black")
        canvas.itemconfigure("l4_cl2", fill="black")
        #messagebox.showinfo("Stare:", "Întrerupătorul este deconectat.")
    elif activate_load_cl1 and close_sl_cl1 and connect_i_cl1 and close_sb1_cl1 and close_sb11_clt and close_sb12_clt and close_sb1_cl2:
        connect_i_clt = False
        canvas.itemconfigure(i_clt, fill="green")
        canvas.itemconfigure("l6_clt", fill="black")
        canvas.itemconfigure("l3_clt", fill="black")
        canvas.itemconfigure("b3", fill="black")
        canvas.itemconfigure("l1.1_cc", fill="black")
        canvas.itemconfigure("l5.1_cl2", fill="black")
        canvas.itemconfigure("l4_cl2", fill="black")
        #messagebox.showinfo("Stare:", "Întrerupătorul este deconectat.")
    if activate_load_cl1 and close_sl_cl1 and connect_i_cl1 and close_sb2_cl1 and close_sb21_clt and close_sb22_clt and close_sb2_cc and connect_i_cc:
        connect_i_clt = False
        canvas.itemconfigure(i_clt, fill="green")
        canvas.itemconfigure("l4_clt", fill="black")
        canvas.itemconfigure("l5_clt", fill="black")
        canvas.itemconfigure("b4", fill="black")
        canvas.itemconfigure("l1.2_cc", fill="black")
        canvas.itemconfigure("l5.2_cl2", fill="black")
        canvas.itemconfigure("l2_cc", fill="black")
        canvas.itemconfigure("l3_cc", fill="black")
        canvas.itemconfigure("m_cc", fill="white")
        #messagebox.showinfo("Stare:", "Întrerupătorul este deconectat.")
    elif activate_load_cl1 and close_sl_cl1 and connect_i_cl1 and close_sb1_cl1 and close_sb11_clt and close_sb12_clt and close_sb1_cc and connect_i_cc:
        connect_i_clt = False
        canvas.itemconfigure(i_clt, fill="green")
        canvas.itemconfigure("l6_clt", fill="black")
        canvas.itemconfigure("l3_clt", fill="black")
        canvas.itemconfigure("b3", fill="black")
        canvas.itemconfigure("l1.1_cc", fill="black")
        canvas.itemconfigure("l5.1_cl2", fill="black")
        canvas.itemconfigure("l2_cc", fill="black")
        canvas.itemconfigure("l3_cc", fill="black")
        canvas.itemconfigure("m_cc", fill="white")
        #messagebox.showinfo("Stare:", "Întrerupătorul este deconectat.")
    elif activate_load_cl1 and close_sl_cl1 and connect_i_cl1 and close_sb2_cl1 and close_sb21_clt and close_sb22_clt and close_sb2_cc:
        connect_i_clt = False
        canvas.itemconfigure(i_clt, fill="green")
        canvas.itemconfigure("l4_clt", fill="black")
        canvas.itemconfigure("l5_clt", fill="black")
        canvas.itemconfigure("b4", fill="black")
        canvas.itemconfigure("l1.2_cc", fill="black")
        canvas.itemconfigure("l5.2_cl2", fill="black")
        canvas.itemconfigure("l2_cc", fill="black")
        #messagebox.showinfo("Stare:", "Întrerupătorul este deconectat.")
    elif activate_load_cl1 and close_sl_cl1 and connect_i_cl1 and close_sb1_cl1 and close_sb11_clt and close_sb12_clt and close_sb1_cc:
        connect_i_clt = False
        canvas.itemconfigure(i_clt, fill="green")
        canvas.itemconfigure("l6_clt", fill="black")
        canvas.itemconfigure("l3_clt", fill="black")
        canvas.itemconfigure("b3", fill="black")
        canvas.itemconfigure("l1.1_cc", fill="black")
        canvas.itemconfigure("l5.1_cl2", fill="black")
        canvas.itemconfigure("l2_cc", fill="black")
        #messagebox.showinfo("Stare:", "Întrerupătorul este deconectat.")
    elif activate_load_cl1 and close_sl_cl1 and connect_i_cl1 and close_sb2_cl1 and close_sb21_clt and close_sb22_clt:
        connect_i_clt = False
        canvas.itemconfigure(i_clt, fill="green")
        canvas.itemconfigure("l4_clt", fill="black")
        canvas.itemconfigure("l5_clt", fill="black")
        canvas.itemconfigure("b4", fill="black")
        canvas.itemconfigure("l1.2_cc", fill="black")
        canvas.itemconfigure("l5.2_cl2", fill="black")
        #messagebox.showinfo("Stare:", "Întrerupătorul este deconectat.")
    elif activate_load_cl1 and close_sl_cl1 and connect_i_cl1 and close_sb1_cl1 and close_sb11_clt and close_sb12_clt:
        connect_i_clt = False
        canvas.itemconfigure(i_clt, fill="green")
        canvas.itemconfigure("l6_clt", fill="black")
        canvas.itemconfigure("l3_clt", fill="black")
        canvas.itemconfigure("b3", fill="black")
        canvas.itemconfigure("l1.1_cc", fill="black")
        canvas.itemconfigure("l5.1_cl2", fill="black")
        #messagebox.showinfo("Stare:", "Întrerupătorul este deconectat.")
    elif connect_i_clt:
        connect_i_clt = False
        canvas.itemconfigure(i_clt, fill="green")
        #messagebox.showinfo("Stare:", "Întrerupătorul este deconectat.")


def toggle_close_sb12_clt():
    global close_sb12_clt
    if close_sb21_clt:
        messagebox.showerror("Interblocaj!", "Nu puteți închide simultan separatoarele de bare 2 și 3.")
    elif activate_load_cl2 and close_sl_cl2 and connect_i_cl2 and close_sb1_cl2:
        close_sb12_clt = True
        canvas.itemconfigure(sb12_clt, fill="red")
        canvas.itemconfigure("l6_clt", fill="red")
        # messagebox.showinfo("Stare:", "Separatorul de bare 3 este închis.")
    elif not close_sb12_clt:
        close_sb12_clt = True
        canvas.itemconfigure(sb12_clt, fill="red")
        #messagebox.showinfo("Stare:", "Separatorul de bare 3 este închis.")


def toggle_open_sb12_clt():
    global close_sb12_clt
    if connect_i_clt:
        messagebox.showerror("Interblocaj!", "Întrerupătorul este conectat.")
    elif activate_load_cl2 and close_sl_cl2 and connect_i_cl2 and close_sb1_cl2:
        close_sb12_clt = False
        canvas.itemconfigure(sb12_clt, fill="green")
        canvas.itemconfigure("l6_clt", fill="black")
        # messagebox.showinfo("Stare:", "Separatorul de bare 3 este deschis.")
    elif close_sb12_clt:
        close_sb12_clt = False
        canvas.itemconfigure(sb12_clt, fill="green")
        #messagebox.showinfo("Stare:", "Separatorul de bare 3 este deschis.")


def toggle_close_sb22_clt():
    global close_sb22_clt
    if close_sb11_clt:
        messagebox.showerror("Interblocaj!", "Nu puteți închide simultan separatoarele de bare 1 și 4.")
    elif activate_load_cl2 and close_sl_cl2 and connect_i_cl2 and close_sb2_cl2:
        close_sb22_clt = True
        canvas.itemconfigure(sb22_clt, fill="red")
        canvas.itemconfigure("l5_clt", fill="red")
        # messagebox.showinfo("Stare:", "Separatorul de bare 4 este închis.")
    elif not close_sb22_clt:
        close_sb22_clt = True
        canvas.itemconfigure(sb22_clt, fill="red")
        #messagebox.showinfo("Stare:", "Separatorul de bare 4 este închis.")


def toggle_open_sb22_clt():
    global close_sb22_clt
    if connect_i_clt:
        messagebox.showerror("Interblocaj!", "Întrerupătorul este conectat.")
    elif activate_load_cl2 and close_sl_cl2 and connect_i_cl2 and close_sb2_cl2:
        close_sb22_clt = False
        canvas.itemconfigure(sb22_clt, fill="green")
        canvas.itemconfigure("l5_clt", fill="black")
        # messagebox.showinfo("Stare:", "Separatorul de bare 1 este deschis.")
    elif close_sb22_clt:
        close_sb22_clt = False
        canvas.itemconfigure(sb22_clt, fill="green")
        #messagebox.showinfo("Stare:", "Separatorul de bare 4 este deschis.")


# Condiții Celulă cu consumator-----------------------------------------------------------------------------------------


def toggle_close_sb1_cc():
    global close_sb1_cc
    if connect_i_clt and close_sb12_clt and close_sb22_clt:
        close_sb1_cc = True
        canvas.itemconfigure(sb1_cc, fill="red")
        canvas.itemconfigure("l2_cc", fill="red")
        #messagebox.showinfo("", "Separatorul de bare 3 este închis.")
    elif close_sb2_cc:
        messagebox.showerror("Interblocaj!", "Separatorul de bare 4 este deja închis.")
    elif activate_load_cl2 and close_sl_cl2 and connect_i_cl2 and close_sb1_cl2 and not connect_i_cc:
        close_sb1_cc = True
        canvas.itemconfigure(sb1_cc, fill="red")
        canvas.itemconfigure("l2_cc", fill="red")
        #messagebox.showinfo("", "Separatorul de bare 3 este închis.")
    elif activate_load_cl1 and close_sl_cl1 and connect_i_cl1 and close_sb1_cl1 and close_sb11_clt and connect_i_clt and close_sb12_clt and not connect_i_cc:
        close_sb1_cc = True
        canvas.itemconfigure(sb1_cc, fill="red")
        canvas.itemconfigure("l2_cc", fill="red")
        #messagebox.showinfo("", "Separatorul de bare 3 este închis.")
    elif not close_sb1_cc:
        close_sb1_cc = True
        canvas.itemconfigure(sb1_cc, fill="red")
        #messagebox.showinfo("", "Separatorul de bare 3 este închis.")


def toggle_open_sb1_cc():
    global close_sb1_cc
    if activate_load_cl2 and close_sl_cl2 and connect_i_cl2 and close_sb1_cc and close_sb2_cc and connect_i_clt and close_sb12_clt and close_sb22_clt:
        close_sb1_cc = False
        canvas.itemconfigure(sb1_cc, fill="green")
        #messagebox.showinfo("", "Separatorul de bare 1 este deschis.")
    elif activate_load_cl2 and close_sl_cl2 and connect_i_cl2 and close_sb1_cl2 and not connect_i_cc:
        close_sb1_cc = False
        canvas.itemconfigure(sb1_cc, fill="green")
        canvas.itemconfigure("l2_cc", fill="black")
        #messagebox.showinfo("", "Separatorul de bare 3 este deschis.")
    elif activate_load_cl1 and close_sl_cl1 and connect_i_cl1 and close_sb1_cl1 and close_sb11_clt and connect_i_clt and close_sb12_clt and not connect_i_cc:
        close_sb1_cc = False
        canvas.itemconfigure(sb1_cc, fill="green")
        canvas.itemconfigure("l2_cc", fill="black")
        #messagebox.showinfo("", "Separatorul de bare 3 este deschis.")
    elif connect_i_cc:
        messagebox.showerror("Interblocaj!", "Întrerupătorul este conectat.")
    elif close_sb1_cc:
        close_sb1_cc = False
        canvas.itemconfigure(sb1_cc, fill="green")
        #messagebox.showinfo("", "Separatorul de bare 3 este deschis.")


def toggle_close_sb2_cc():
    global close_sb2_cc
    if connect_i_clt and close_sb12_clt and close_sb22_clt:
        close_sb2_cc = True
        canvas.itemconfigure(sb2_cc, fill="red")
        canvas.itemconfigure("l2_cc", fill="red")
        #messagebox.showinfo("", "Separatorul de bare 4 este închis.")
    elif close_sb1_cc:
        messagebox.showerror("Interblocaj!", "Separatorul de bare 3 este deja închis.")
    elif activate_load_cl2 and close_sl_cl2 and connect_i_cl2 and close_sb2_cl2 and not connect_i_cc:
        close_sb2_cc = True
        canvas.itemconfigure(sb2_cc, fill="red")
        canvas.itemconfigure("l2_cc", fill="red")
        #messagebox.showinfo("", "Separatorul de bare 4 este închis.")
    elif activate_load_cl1 and close_sl_cl1 and connect_i_cl1 and close_sb2_cl1 and close_sb21_clt and connect_i_clt and close_sb22_clt and not connect_i_cc:
        close_sb2_cc = True
        canvas.itemconfigure(sb2_cc, fill="red")
        canvas.itemconfigure("l2_cc", fill="red")
        #messagebox.showinfo("", "Separatorul de bare 4 este închis.")
    elif not close_sb2_cc:
        close_sb2_cc = True
        canvas.itemconfigure(sb2_cc, fill="red")
        #messagebox.showinfo("", "Separatorul de bare 3 este închis.")


def toggle_open_sb2_cc():
    global close_sb2_cc
    if activate_load_cl2 and close_sl_cl2 and connect_i_cl2 and close_sb1_cc and close_sb2_cc and connect_i_clt and close_sb12_clt and close_sb22_clt:
        close_sb2_cc = False
        canvas.itemconfigure(sb2_cc, fill="green")
        #messagebox.showinfo("", "Separatorul de bare 1 este deschis.")
    elif activate_load_cl2 and close_sl_cl2 and connect_i_cl2 and close_sb2_cl2 and not connect_i_cc:
        close_sb2_cc = False
        canvas.itemconfigure(sb2_cc, fill="green")
        canvas.itemconfigure("l2_cc", fill="black")
        #messagebox.showinfo("", "Separatorul de bare 4 este deschis.")
    elif activate_load_cl1 and close_sl_cl1 and connect_i_cl1 and close_sb2_cl1 and close_sb12_clt and connect_i_clt and close_sb22_clt and not connect_i_cc:
        close_sb2_cc = False
        canvas.itemconfigure(sb2_cc, fill="green")
        canvas.itemconfigure("l2_cc", fill="black")
        #messagebox.showinfo("", "Separatorul de bare 4 este deschis.")
    elif connect_i_cc:
        messagebox.showerror("Interblocaj!", "Întrerupătorul este conectat.")
    elif close_sb2_cc:
        close_sb2_cc = False
        canvas.itemconfigure(sb2_cc, fill="green")
        #messagebox.showinfo("", "Separatorul de bare 4 este deschis.")


def toggle_connect_i_cc():
    global connect_i_cc
    if not (close_sb1_cc or close_sb2_cc):
        messagebox.showerror("Interblocaj!", "Amândouă separatoare de bare sunt deschise.")
    elif close_clp_cl1:
        messagebox.showerror("Interblocaj!", "CLP este închis.")
    if not connect_i_cc and activate_load_cl2 and close_sl_cl2 and connect_i_cl2 and close_sb2_cl2 and close_sb2_cc:
        connect_i_cc = True
        canvas.itemconfigure(i_cc, fill="red")
        canvas.itemconfigure("l3_cc", fill="red")
        canvas.itemconfigure("m_cc", fill="red")
        # messagebox.showinfo("", "Întrerupătorul este conectat.")
    elif not connect_i_cc and activate_load_cl2 and close_sl_cl2 and connect_i_cl2 and close_sb1_cl2 and close_sb1_cc:
        connect_i_cc = True
        canvas.itemconfigure(i_cc, fill="red")
        canvas.itemconfigure("l3_cc", fill="red")
        canvas.itemconfigure("m_cc", fill="red")
        # messagebox.showinfo("", "Întrerupătorul este conectat.")
    if not connect_i_cc and activate_load_cl1 and close_sl_cl1 and connect_i_cl1 and close_sb2_cl1 and close_sb21_clt and close_sb22_clt and close_sb2_cc:
        connect_i_cc = True
        canvas.itemconfigure(i_cc, fill="red")
        canvas.itemconfigure("l3_cc", fill="red")
        canvas.itemconfigure("m_cc", fill="red")
        #messagebox.showinfo("", "Întrerupătorul este conectat.")
    elif not connect_i_cc and activate_load_cl1 and close_sl_cl1 and connect_i_cl1 and close_sb1_cl1 and close_sb11_clt and close_sb12_clt and close_sb1_cc:
        connect_i_cc = True
        canvas.itemconfigure(i_cc, fill="red")
        canvas.itemconfigure("l3_cc", fill="red")
        canvas.itemconfigure("m_cc", fill="red")
        #messagebox.showinfo("", "Întrerupătorul este conectat.")
    elif not connect_i_cc:
        connect_i_cc = True
        canvas.itemconfigure(i_cc, fill="red")
        #messagebox.showinfo("", "Întrerupătorul este conectat.")


def toggle_disconnect_i_cc():
    global connect_i_cc
    if connect_i_cc:
        connect_i_cc = False
        canvas.itemconfigure(i_cc, fill="green")
        canvas.itemconfigure("l3_cc", fill="black")
        canvas.itemconfigure("m_cc", fill="white")
        #messagebox.showinfo("", "Întrerupătorul este deconectat.")


def toggle_close_clp_cc():
    global close_clp_cc
    if connect_i_cc:
        messagebox.showerror("Interblocaj!", "întrerupătorul este conectat.")
    elif not close_clp_cc:
        close_clp_cc = True
        canvas.itemconfigure(clp_cc, fill="red")
        #messagebox.showinfo("", "CLP este închis.")


def toggle_open_clp_cc():
    global close_clp_cc
    if close_clp_cc:
        close_clp_cc = False
        canvas.itemconfigure(clp_cc, fill="green")
        #messagebox.showinfo("", "CLP este deschis.")


# Condiții Celulă de linie 2--------------------------------------------------------------------------------------------


def toggle_activate_load_cl2():
    global activate_load_cl2
    if close_sl_cl2 and connect_i_cl2 and close_sb2_cl2 and close_sb22_clt and close_sb21_clt and close_sb2_cl1 and connect_i_cl1 and close_sl_cl1:
        activate_load_cl2 = True
        canvas.itemconfigure("l1_cl2", fill="red")
        canvas.itemconfigure("l3_cl2", fill="red")
        canvas.itemconfigure("l4_cl2", fill="red")
        canvas.itemconfigure("l5.2_cl2", fill="red")
        canvas.itemconfigure("l1.2_cc", fill="red")
        canvas.itemconfigure("b4", fill="red")
        canvas.itemconfigure("l4_clt", fill="red")
        canvas.itemconfigure("l5_clt", fill="red")
        canvas.itemconfigure("l6_clt", fill="red")
        canvas.itemconfigure("l2_clt", fill="red")
        canvas.itemconfigure("b2", fill="red")
        canvas.itemconfigure("l5.2_cl1", fill="red")
        canvas.itemconfigure("l4_cl1", fill="red")
        canvas.itemconfigure("l3_cl1", fill="red")
        canvas.itemconfigure("l1_cl1", fill="red")
        # messagebox.showinfo("", "Tensiunea este aplicată pe linie.")
    elif close_sl_cl2 and connect_i_cl2 and close_sb1_cl2 and close_sb12_clt and close_sb11_clt and close_sb1_cl1 and connect_i_cl1 and close_sl_cl1:
        activate_load_cl2 = True
        canvas.itemconfigure("l1_cl2", fill="red")
        canvas.itemconfigure("l3_cl2", fill="red")
        canvas.itemconfigure("l4_cl2", fill="red")
        canvas.itemconfigure("l5.1_cl2", fill="red")
        canvas.itemconfigure("l1.1_cc", fill="red")
        canvas.itemconfigure("b3", fill="red")
        canvas.itemconfigure("l3_clt", fill="red")
        canvas.itemconfigure("l6_clt", fill="red")
        canvas.itemconfigure("l1_clt", fill="red")
        canvas.itemconfigure("l5_clt", fill="red")
        canvas.itemconfigure("b1", fill="red")
        canvas.itemconfigure("l5.1_cl1", fill="red")
        canvas.itemconfigure("l4_cl1", fill="red")
        canvas.itemconfigure("l3_cl1", fill="red")
        canvas.itemconfigure("l1_cl1", fill="red")
        # messagebox.showinfo("", "Tensiunea este aplicată pe linie.")
    elif close_sl_cl2 and connect_i_cl2 and close_sb2_cl2 and close_sb22_clt and close_sb21_clt and close_sb2_cl1:
        activate_load_cl2 = True
        canvas.itemconfigure("l1_cl2", fill="red")
        canvas.itemconfigure("l3_cl2", fill="red")
        canvas.itemconfigure("l4_cl2", fill="red")
        canvas.itemconfigure("l5.2_cl2", fill="red")
        canvas.itemconfigure("l1.2_cc", fill="red")
        canvas.itemconfigure("b4", fill="red")
        canvas.itemconfigure("l4_clt", fill="red")
        canvas.itemconfigure("l5_clt", fill="red")
        canvas.itemconfigure("l6_clt", fill="red")
        canvas.itemconfigure("l2_clt", fill="red")
        canvas.itemconfigure("b2", fill="red")
        canvas.itemconfigure("l5.2_cl1", fill="red")
        canvas.itemconfigure("l4_cl1", fill="red")
        # messagebox.showinfo("", "Tensiunea este aplicată pe linie.")
    elif close_sl_cl2 and connect_i_cl2 and close_sb1_cl2 and close_sb12_clt and close_sb11_clt and close_sb1_cl1:
        activate_load_cl2 = True
        canvas.itemconfigure("l1_cl2", fill="red")
        canvas.itemconfigure("l3_cl2", fill="red")
        canvas.itemconfigure("l4_cl2", fill="red")
        canvas.itemconfigure("l5.1_cl2", fill="red")
        canvas.itemconfigure("l1.1_cc", fill="red")
        canvas.itemconfigure("b3", fill="red")
        canvas.itemconfigure("l3_clt", fill="red")
        canvas.itemconfigure("l6_clt", fill="red")
        canvas.itemconfigure("l1_clt", fill="red")
        canvas.itemconfigure("l5_clt", fill="red")
        canvas.itemconfigure("b1", fill="red")
        canvas.itemconfigure("l5.1_cl1", fill="red")
        canvas.itemconfigure("l4_cl1", fill="red")
        # messagebox.showinfo("", "Tensiunea este aplicată pe linie.")
    elif close_sl_cl2 and connect_i_cl2 and close_sb2_cl2 and close_sb22_clt and close_sb21_clt:
        activate_load_cl2 = True
        canvas.itemconfigure("l1_cl2", fill="red")
        canvas.itemconfigure("l3_cl2", fill="red")
        canvas.itemconfigure("l4_cl2", fill="red")
        canvas.itemconfigure("l5.2_cl2", fill="red")
        canvas.itemconfigure("l1.2_cc", fill="red")
        canvas.itemconfigure("b4", fill="red")
        canvas.itemconfigure("l4_clt", fill="red")
        canvas.itemconfigure("l5_clt", fill="red")
        canvas.itemconfigure("l6_clt", fill="red")
        canvas.itemconfigure("l2_clt", fill="red")
        canvas.itemconfigure("b2", fill="red")
        canvas.itemconfigure("l5.2_cl1", fill="red")
        # messagebox.showinfo("", "Tensiunea este aplicată pe linie.")
    elif close_sl_cl2 and connect_i_cl2 and close_sb1_cl2 and close_sb12_clt and close_sb11_clt:
        activate_load_cl2 = True
        canvas.itemconfigure("l1_cl2", fill="red")
        canvas.itemconfigure("l3_cl2", fill="red")
        canvas.itemconfigure("l4_cl2", fill="red")
        canvas.itemconfigure("l5.1_cl2", fill="red")
        canvas.itemconfigure("l1.1_cc", fill="red")
        canvas.itemconfigure("b3", fill="red")
        canvas.itemconfigure("l3_clt", fill="red")
        canvas.itemconfigure("l6_clt", fill="red")
        canvas.itemconfigure("l1_clt", fill="red")
        canvas.itemconfigure("l5_clt", fill="red")
        canvas.itemconfigure("b1", fill="red")
        canvas.itemconfigure("l5.1_cl1", fill="red")
        # messagebox.showinfo("", "Tensiunea este aplicată pe linie.")
    elif close_sl_cl2 and connect_i_cl2 and close_sb2_cl2 and close_sb22_clt:
        activate_load_cl2 = True
        canvas.itemconfigure("l1_cl2", fill="red")
        canvas.itemconfigure("l3_cl2", fill="red")
        canvas.itemconfigure("l4_cl2", fill="red")
        canvas.itemconfigure("l5.2_cl2", fill="red")
        canvas.itemconfigure("l1.2_cc", fill="red")
        canvas.itemconfigure("b4", fill="red")
        canvas.itemconfigure("l4_clt", fill="red")
        canvas.itemconfigure("l5_clt", fill="red")
        # messagebox.showinfo("", "Tensiunea este aplicată pe linie.")
    elif close_sl_cl2 and connect_i_cl2 and close_sb1_cl2 and close_sb12_clt:
        activate_load_cl2 = True
        canvas.itemconfigure("l1_cl2", fill="red")
        canvas.itemconfigure("l3_cl2", fill="red")
        canvas.itemconfigure("l4_cl2", fill="red")
        canvas.itemconfigure("l5.1_cl2", fill="red")
        canvas.itemconfigure("l1.1_cc", fill="red")
        canvas.itemconfigure("b3", fill="red")
        canvas.itemconfigure("l3_clt", fill="red")
        canvas.itemconfigure("l6_clt", fill="red")
        # messagebox.showinfo("", "Tensiunea este aplicată pe linie.")
    if close_sl_cl2 and connect_i_cl2 and close_sb2_cl2 and close_sb2_cc and connect_i_cc:
        activate_load_cl2 = True
        canvas.itemconfigure("l1_cl2", fill="red")
        canvas.itemconfigure("l3_cl2", fill="red")
        canvas.itemconfigure("l4_cl2", fill="red")
        canvas.itemconfigure("l5.2_cl2", fill="red")
        canvas.itemconfigure("l1.2_cc", fill="red")
        canvas.itemconfigure("l2_cc", fill="red")
        canvas.itemconfigure("l3_cc", fill="red")
        canvas.itemconfigure("m_cc", fill="red")
        canvas.itemconfigure("b4", fill="red")
        canvas.itemconfigure("l4_clt", fill="red")
        # messagebox.showinfo("", "Tensiunea este aplicată pe linie.")
    elif close_sl_cl2 and connect_i_cl2 and close_sb1_cl2 and close_sb1_cc and connect_i_cc:
        activate_load_cl2 = True
        canvas.itemconfigure("l1_cl2", fill="red")
        canvas.itemconfigure("l3_cl2", fill="red")
        canvas.itemconfigure("l4_cl2", fill="red")
        canvas.itemconfigure("l5.1_cl2", fill="red")
        canvas.itemconfigure("l1.1_cc", fill="red")
        canvas.itemconfigure("l2_cc", fill="red")
        canvas.itemconfigure("l3_cc", fill="red")
        canvas.itemconfigure("m_cc", fill="red")
        canvas.itemconfigure("b3", fill="red")
        canvas.itemconfigure("l3_clt", fill="red")
        # messagebox.showinfo("", "Tensiunea este aplicată pe linie.")
    elif close_sl_cl2 and connect_i_cl2 and close_sb2_cl2 and close_sb2_cc:
        activate_load_cl2 = True
        canvas.itemconfigure("l1_cl2", fill="red")
        canvas.itemconfigure("l3_cl2", fill="red")
        canvas.itemconfigure("l4_cl2", fill="red")
        canvas.itemconfigure("l5.2_cl2", fill="red")
        canvas.itemconfigure("l1.2_cc", fill="red")
        canvas.itemconfigure("l2_cc", fill="red")
        canvas.itemconfigure("b4", fill="red")
        canvas.itemconfigure("l4_clt", fill="red")
        # messagebox.showinfo("", "Tensiunea este aplicată pe linie.")
    elif close_sl_cl2 and connect_i_cl2 and close_sb1_cl2 and close_sb1_cc:
        activate_load_cl2 = True
        canvas.itemconfigure("l1_cl2", fill="red")
        canvas.itemconfigure("l3_cl2", fill="red")
        canvas.itemconfigure("l4_cl2", fill="red")
        canvas.itemconfigure("l5.1_cl2", fill="red")
        canvas.itemconfigure("l1.1_cc", fill="red")
        canvas.itemconfigure("l2_cc", fill="red")
        canvas.itemconfigure("b3", fill="red")
        canvas.itemconfigure("l3_clt", fill="red")
        # messagebox.showinfo("", "Tensiunea este aplicată pe linie.")
    elif close_sl_cl2 and connect_i_cl2 and close_sb2_cl2:
        activate_load_cl2 = True
        canvas.itemconfigure("l1_cl2", fill="red")
        canvas.itemconfigure("l3_cl2", fill="red")
        canvas.itemconfigure("l4_cl2", fill="red")
        canvas.itemconfigure("l5.2_cl2", fill="red")
        canvas.itemconfigure("l1.2_cc", fill="red")
        canvas.itemconfigure("b4", fill="red")
        canvas.itemconfigure("l4_clt", fill="red")
        # messagebox.showinfo("", "Tensiunea este aplicată pe linie.")
    elif close_sl_cl2 and connect_i_cl2 and close_sb1_cl2:
        activate_load_cl2 = True
        canvas.itemconfigure("l1_cl2", fill="red")
        canvas.itemconfigure("l3_cl2", fill="red")
        canvas.itemconfigure("l4_cl2", fill="red")
        canvas.itemconfigure("l5.1_cl2", fill="red")
        canvas.itemconfigure("l1.1_cc", fill="red")
        canvas.itemconfigure("b3", fill="red")
        canvas.itemconfigure("l3_clt", fill="red")
        # messagebox.showinfo("", "Tensiunea este aplicată pe linie.")
    elif close_sl_cl2:
        activate_load_cl2 = True
        canvas.itemconfigure("l1_cl2", fill="red")
        canvas.itemconfigure("l3_cl2", fill="red")
        #messagebox.showinfo("", "Tensiunea este aplicată pe linie.")
    elif close_clp_cl2:
        activate_load_cl2 = True
        canvas.itemconfigure("l1_cl2", fill="red")
        canvas.itemconfigure("l2_cl2", fill="red")
        #messagebox.showinfo("", "Tensiunea este aplicată pe linie.")
    elif not activate_load_cl2:
        activate_load_cl2 = True
        canvas.itemconfigure("l1_cl2", fill="red")
        #messagebox.showinfo("", "Tensiunea este aplicată pe linie.")


def toggle_deactivate_load_cl2():
    global activate_load_cl2
    if activate_load_cl2 and close_sl_cl2:
        activate_load_cl2 = False
        canvas.itemconfigure("l1_cl2", fill="black")
        canvas.itemconfigure("l3_cl2", fill="black")
        canvas.itemconfigure("l4_cl2", fill="black")
        canvas.itemconfigure("l5.1_cl2", fill="black")
        canvas.itemconfigure("l5.2_cl2", fill="black")
        canvas.itemconfigure("b3", fill="black")
        canvas.itemconfigure("b4", fill="black")
        canvas.itemconfigure("l1.1_cc", fill="black")
        canvas.itemconfigure("l1.2_cc", fill="black")
        canvas.itemconfigure("l2_cc", fill="black")
        canvas.itemconfigure("l3_cc", fill="black")
        canvas.itemconfigure("m_cc", fill="white")
        canvas.itemconfigure("l3_clt", fill="black")
        canvas.itemconfigure("l4_clt", fill="black")
        canvas.itemconfigure("l5_clt", fill="black")
        canvas.itemconfigure("l6_clt", fill="black")
        canvas.itemconfigure("l1_clt", fill="black")
        canvas.itemconfigure("l2_clt", fill="black")
        canvas.itemconfigure("b1", fill="black")
        canvas.itemconfigure("b2", fill="black")
        canvas.itemconfigure("l5.1_cl1", fill="black")
        canvas.itemconfigure("l5.2_cl1", fill="black")
        canvas.itemconfigure("l4_cl1", fill="black")
        canvas.itemconfigure("l1_cl1", fill="black")
        canvas.itemconfigure("l3_cl1", fill="black")
        # messagebox.showinfo("", "Tensiunea este întreruptă de pe linie.")
    if activate_load_cl2 and close_clp_cl2:
        activate_load_cl2 = False
        canvas.itemconfigure("l1_cl2", fill="black")
        canvas.itemconfigure("l2_cl2", fill="black")
        # messagebox.showinfo("", "Tensiunea este întreruptă de pe linie.")
    if activate_load_cl2:
        activate_load_cl2 = False
        canvas.itemconfigure("l1_cl2", fill="black")
        # messagebox.showinfo("", "Tensiunea este întreruptă de pe linie.")


def toggle_close_sb1_cl2():
    global close_sb1_cl2
    if connect_i_clt and close_sb12_clt and close_sb22_clt:
        close_sb1_cl2 = True
        canvas.itemconfigure(sb1_cl2, fill="red")
        # messagebox.showinfo("", "Separatorul de bare 1 este închis.")
    elif close_sb2_cl2:
        messagebox.showerror("Interblocaj!", "Separatorul de bare 4 este deja închis.")
    elif activate_load_cl1 and close_sl_cl1 and connect_i_cl1 and close_sb1_cl1 and close_sb11_clt and connect_i_clt and close_sb12_clt:
        close_sb1_cl2 = True
        canvas.itemconfigure(sb1_cl2, fill="red")
        canvas.itemconfigure("l4_cl2", fill="red")
        #messagebox.showinfo("", "Separatorul de bare 3 este închis.")
    elif not close_sb1_cl2:
        close_sb1_cl2 = True
        canvas.itemconfigure(sb1_cl2, fill="red")
        #messagebox.showinfo("", "Separatorul de bare 3 este închis.")


def toggle_open_sb1_cl2():
    global close_sb1_cl2
    if activate_load_cl2 and close_sl_cl2 and connect_i_cl2 and close_sb1_cl2 and close_sb2_cl2 and connect_i_clt and close_sb12_clt and close_sb22_clt:
        close_sb1_cl2 = False
        canvas.itemconfigure(sb1_cl2, fill="green")
        # messagebox.showinfo("", "Separatorul de bare 1 este deschis.")
    elif activate_load_cl1 and close_sl_cl1 and connect_i_cl1 and close_sb1_cl1 and close_sb11_clt and connect_i_clt and close_sb12_clt:
        close_sb1_cl2 = False
        canvas.itemconfigure(sb1_cl2, fill="green")
        canvas.itemconfigure("l4_cl2", fill="black")
        #messagebox.showinfo("", "Separatorul de bare 3 este deschis.")
    elif connect_i_cl2:
        messagebox.showerror("Interblocaj!", "Întrerupătorul este conectat.")
    elif close_sb1_cl2:
        close_sb1_cl2 = False
        canvas.itemconfigure(sb1_cl2, fill="green")
        #messagebox.showinfo("", "Separatorul de bare 3 este deschis.")


def toggle_close_sb2_cl2():
    global close_sb2_cl2
    if connect_i_clt and close_sb12_clt and close_sb22_clt:
        close_sb2_cl2 = True
        canvas.itemconfigure(sb2_cl2, fill="red")
        #messagebox.showinfo("", "Separatorul de bare 2 este închis.")
    elif close_sb1_cl2:
        messagebox.showerror("Interblocaj!", "Separatorul de bare 3 este deja închis.")
    elif activate_load_cl1 and close_sl_cl1 and connect_i_cl1 and close_sb2_cl1 and close_sb21_clt and connect_i_clt and close_sb22_clt:
        close_sb2_cl2 = True
        canvas.itemconfigure(sb2_cl2, fill="red")
        canvas.itemconfigure("l4_cl2", fill="red")
        #messagebox.showinfo("", "Separatorul de bare 4 este închis.")
    elif not close_sb2_cl2:
        close_sb2_cl2 = True
        canvas.itemconfigure(sb2_cl2, fill="red")
        #messagebox.showinfo("", "Separatorul de bare 4 este închis.")


def toggle_open_sb2_cl2():
    global close_sb2_cl2
    if activate_load_cl2 and close_sl_cl2 and connect_i_cl2 and close_sb1_cl2 and close_sb2_cl2 and connect_i_clt and close_sb12_clt and close_sb22_clt:
        close_sb2_cl2 = False
        canvas.itemconfigure(sb2_cl2, fill="green")
        # messagebox.showinfo("", "Separatorul de bare 2 este deschis.")
    elif activate_load_cl1 and close_sl_cl1 and connect_i_cl1 and close_sb2_cl1 and close_sb21_clt and connect_i_clt and close_sb22_clt:
        close_sb2_cl2 = False
        canvas.itemconfigure(sb2_cl2, fill="green")
        canvas.itemconfigure("l4_cl2", fill="black")
        #messagebox.showinfo("", "Separatorul de bare 4 este deschis.")
    elif connect_i_cl2:
        messagebox.showerror("Interblocaj!", "Întrerupătorul este conectat.")
    elif close_sb2_cl2:
        close_sb2_cl2 = False
        canvas.itemconfigure(sb2_cl2, fill="green")
        #messagebox.showinfo("", "Separatorul de bare 4 este deschis.")


def toggle_connect_i_cl2():
    global connect_i_cl2
    if not (close_sb1_cl2 or close_sb2_cl2):
        messagebox.showerror("Interblocaj!", "Amândouă separatoare de bare sunt deschise.")
    elif not close_sl_cl2:
        messagebox.showerror("Interblocaj!",
                             "Separatorul de linie este deschis.")
    elif close_clp_cl2:
        messagebox.showerror("Interblocaj!", "CLP este închis.")
    elif not activate_load_cl2 and not connect_i_cl2:
        connect_i_cl2 = True
        canvas.itemconfigure(i_cl2, fill="red")
    if activate_load_cl1 and close_sl_cl1 and connect_i_cl1 and close_sb1_cl1 and close_sb11_clt and connect_i_clt and close_sb12_clt and close_sb1_cl2 and close_sl_cl2:
        connect_i_cl2 = True
        canvas.itemconfigure(i_cl2, fill="red")
        canvas.itemconfigure("l1_cl2", fill="red")
        canvas.itemconfigure("l3_cl2", fill="red")
        #messagebox.showinfo("", "Întrerupătorul este conectat.")
    elif activate_load_cl1 and close_sl_cl1 and connect_i_cl1 and close_sb2_cl1 and close_sb21_clt and connect_i_clt and close_sb22_clt and close_sb2_cl2 and close_sl_cl2:
        connect_i_cl2 = True
        canvas.itemconfigure(i_cl2, fill="red")
        canvas.itemconfigure("l1_cl2", fill="red")
        canvas.itemconfigure("l3_cl2", fill="red")
        #messagebox.showinfo("", "Întrerupătorul este conectat.")
    elif activate_load_cl2 and close_sl_cl2 and close_sb1_cl2 and close_sb12_clt and close_sb11_clt and close_sb1_cl1 and connect_i_cl1 and close_sl_cl1:
        connect_i_cl2 = True
        canvas.itemconfigure(i_cl2, fill="red")
        canvas.itemconfigure("l4_cl2", fill="red")
        canvas.itemconfigure("l5.1_cl2", fill="red")
        canvas.itemconfigure("l1.1_cc", fill="red")
        canvas.itemconfigure("b3", fill="red")
        canvas.itemconfigure("l3_clt", fill="red")
        canvas.itemconfigure("l1_clt", fill="red")
        canvas.itemconfigure("l6_clt", fill="red")
        canvas.itemconfigure("l5_clt", fill="red")
        canvas.itemconfigure("b1", fill="red")
        canvas.itemconfigure("l5.1_cl1", fill="red")
        canvas.itemconfigure("l4_cl1", fill="red")
        canvas.itemconfigure("l3_cl1", fill="red")
        canvas.itemconfigure("l1_cl1", fill="red")
        #messagebox.showinfo("", "Întrerupătorul este conectat.")
    elif activate_load_cl2 and close_sl_cl2 and close_sb2_cl2 and close_sb22_clt and close_sb21_clt and close_sb2_cl1 and connect_i_cl1 and close_sl_cl1:
        connect_i_cl2 = True
        canvas.itemconfigure(i_cl2, fill="red")
        canvas.itemconfigure("l4_cl2", fill="red")
        canvas.itemconfigure("l5.2_cl2", fill="red")
        canvas.itemconfigure("l1.2_cc", fill="red")
        canvas.itemconfigure("b4", fill="red")
        canvas.itemconfigure("l4_clt", fill="red")
        canvas.itemconfigure("l2_clt", fill="red")
        canvas.itemconfigure("l5_clt", fill="red")
        canvas.itemconfigure("l6_clt", fill="red")
        canvas.itemconfigure("b2", fill="red")
        canvas.itemconfigure("l5.2_cl1", fill="red")
        canvas.itemconfigure("l4_cl1", fill="red")
        canvas.itemconfigure("l3_cl1", fill="red")
        canvas.itemconfigure("l1_cl1", fill="red")
        #messagebox.showinfo("", "Întrerupătorul este conectat.")
    elif activate_load_cl2 and close_sl_cl2 and close_sb1_cl2 and close_sb12_clt and close_sb11_clt and close_sb1_cl1:
        connect_i_cl2 = True
        canvas.itemconfigure(i_cl2, fill="red")
        canvas.itemconfigure("l4_cl2", fill="red")
        canvas.itemconfigure("l5.1_cl2", fill="red")
        canvas.itemconfigure("l1.1_cc", fill="red")
        canvas.itemconfigure("b3", fill="red")
        canvas.itemconfigure("l3_clt", fill="red")
        canvas.itemconfigure("l1_clt", fill="red")
        canvas.itemconfigure("l6_clt", fill="red")
        canvas.itemconfigure("l5_clt", fill="red")
        canvas.itemconfigure("b1", fill="red")
        canvas.itemconfigure("l5.1_cl1", fill="red")
        canvas.itemconfigure("l4_cl1", fill="red")
        #messagebox.showinfo("", "Întrerupătorul este conectat.")
    elif activate_load_cl2 and close_sl_cl2 and close_sb2_cl2 and close_sb22_clt and close_sb21_clt and close_sb2_cl1:
        connect_i_cl2 = True
        canvas.itemconfigure(i_cl2, fill="red")
        canvas.itemconfigure("l4_cl2", fill="red")
        canvas.itemconfigure("l5.2_cl2", fill="red")
        canvas.itemconfigure("l1.2_cc", fill="red")
        canvas.itemconfigure("b4", fill="red")
        canvas.itemconfigure("l4_clt", fill="red")
        canvas.itemconfigure("l2_clt", fill="red")
        canvas.itemconfigure("l5_clt", fill="red")
        canvas.itemconfigure("l6_clt", fill="red")
        canvas.itemconfigure("b2", fill="red")
        canvas.itemconfigure("l5.2_cl1", fill="red")
        canvas.itemconfigure("l4_cl1", fill="red")
        #messagebox.showinfo("", "Întrerupătorul este conectat.")
    elif activate_load_cl2 and close_sl_cl2 and close_sb1_cl2 and close_sb12_clt and close_sb11_clt:
        connect_i_cl2 = True
        canvas.itemconfigure(i_cl2, fill="red")
        canvas.itemconfigure("l4_cl2", fill="red")
        canvas.itemconfigure("l5.1_cl2", fill="red")
        canvas.itemconfigure("l1.1_cc", fill="red")
        canvas.itemconfigure("b3", fill="red")
        canvas.itemconfigure("l3_clt", fill="red")
        canvas.itemconfigure("l1_clt", fill="red")
        canvas.itemconfigure("l6_clt", fill="red")
        canvas.itemconfigure("l5_clt", fill="red")
        canvas.itemconfigure("b1", fill="red")
        canvas.itemconfigure("l5.1_cl1", fill="red")
        #messagebox.showinfo("", "Întrerupătorul este conectat.")
    elif activate_load_cl2 and close_sl_cl2 and close_sb2_cl2 and close_sb22_clt and close_sb21_clt:
        connect_i_cl2 = True
        canvas.itemconfigure(i_cl2, fill="red")
        canvas.itemconfigure("l4_cl2", fill="red")
        canvas.itemconfigure("l5.2_cl2", fill="red")
        canvas.itemconfigure("l1.2_cc", fill="red")
        canvas.itemconfigure("b4", fill="red")
        canvas.itemconfigure("l4_clt", fill="red")
        canvas.itemconfigure("l2_clt", fill="red")
        canvas.itemconfigure("l5_clt", fill="red")
        canvas.itemconfigure("l6_clt", fill="red")
        canvas.itemconfigure("b2", fill="red")
        canvas.itemconfigure("l5.2_cl1", fill="red")
        #messagebox.showinfo("", "Întrerupătorul este conectat.")
    elif activate_load_cl2 and close_sl_cl2 and close_sb1_cl2 and close_sb12_clt:
        connect_i_cl2 = True
        canvas.itemconfigure(i_cl2, fill="red")
        canvas.itemconfigure("l4_cl2", fill="red")
        canvas.itemconfigure("l5.1_cl2", fill="red")
        canvas.itemconfigure("l1.1_cc", fill="red")
        canvas.itemconfigure("b3", fill="red")
        canvas.itemconfigure("l3_clt", fill="red")
        canvas.itemconfigure("l6_clt", fill="red")
        #messagebox.showinfo("", "Întrerupătorul este conectat.")
    elif activate_load_cl2 and close_sl_cl2 and close_sb2_cl2 and close_sb22_clt:
        connect_i_cl2 = True
        canvas.itemconfigure(i_cl2, fill="red")
        canvas.itemconfigure("l4_cl2", fill="red")
        canvas.itemconfigure("l5.2_cl2", fill="red")
        canvas.itemconfigure("l1.2_cc", fill="red")
        canvas.itemconfigure("b4", fill="red")
        canvas.itemconfigure("l4_clt", fill="red")
        canvas.itemconfigure("l5_clt", fill="red")
        #messagebox.showinfo("", "Întrerupătorul este conectat.")
    elif activate_load_cl2 and close_sl_cl2 and close_sb1_cl2 and close_sb1_cc and connect_i_cc:
        connect_i_cl2 = True
        canvas.itemconfigure(i_cl2, fill="red")
        canvas.itemconfigure("l4_cl2", fill="red")
        canvas.itemconfigure("l5.1_cl2", fill="red")
        canvas.itemconfigure("l1.1_cc", fill="red")
        canvas.itemconfigure("l2_cc", fill="red")
        canvas.itemconfigure("3_cc", fill="red")
        canvas.itemconfigure("m_cc", fill="red")
        canvas.itemconfigure("b3", fill="red")
        canvas.itemconfigure("l3_clt", fill="red")
        #messagebox.showinfo("", "Întrerupătorul este conectat.")
    elif activate_load_cl2 and close_sl_cl2 and close_sb2_cl2 and close_sb2_cc and connect_i_cc:
        connect_i_cl2 = True
        canvas.itemconfigure(i_cl2, fill="red")
        canvas.itemconfigure("l4_cl2", fill="red")
        canvas.itemconfigure("l5.2_cl2", fill="red")
        canvas.itemconfigure("l1.2_cc", fill="red")
        canvas.itemconfigure("l2_cc", fill="red")
        canvas.itemconfigure("3_cc", fill="red")
        canvas.itemconfigure("m_cc", fill="red")
        canvas.itemconfigure("b4", fill="red")
        canvas.itemconfigure("l4_clt", fill="red")
        #messagebox.showinfo("", "Întrerupătorul este conectat.")
    elif activate_load_cl2 and close_sl_cl2 and close_sb1_cl2 and close_sb1_cc:
        connect_i_cl2 = True
        canvas.itemconfigure(i_cl2, fill="red")
        canvas.itemconfigure("l4_cl2", fill="red")
        canvas.itemconfigure("l5.1_cl2", fill="red")
        canvas.itemconfigure("l1.1_cc", fill="red")
        canvas.itemconfigure("l2_cc", fill="red")
        canvas.itemconfigure("b3", fill="red")
        canvas.itemconfigure("l3_clt", fill="red")
        #messagebox.showinfo("", "Întrerupătorul este conectat.")
    elif activate_load_cl2 and close_sl_cl2 and close_sb2_cl2 and close_sb2_cc:
        connect_i_cl2 = True
        canvas.itemconfigure(i_cl2, fill="red")
        canvas.itemconfigure("l4_cl2", fill="red")
        canvas.itemconfigure("l5.2_cl2", fill="red")
        canvas.itemconfigure("l1.2_cc", fill="red")
        canvas.itemconfigure("l2_cc", fill="red")
        canvas.itemconfigure("b4", fill="red")
        canvas.itemconfigure("l4_clt", fill="red")
        #messagebox.showinfo("", "Întrerupătorul este conectat.")
    elif activate_load_cl2 and close_sl_cl2 and close_sb1_cl2:
        connect_i_cl2 = True
        canvas.itemconfigure(i_cl2, fill="red")
        canvas.itemconfigure("l4_cl2", fill="red")
        canvas.itemconfigure("l5.1_cl2", fill="red")
        canvas.itemconfigure("l1.1_cc", fill="red")
        canvas.itemconfigure("b3", fill="red")
        canvas.itemconfigure("l3_clt", fill="red")
        #messagebox.showinfo("", "Întrerupătorul este conectat.")
    elif activate_load_cl2 and close_sl_cl2 and close_sb2_cl2:
        connect_i_cl2 = True
        canvas.itemconfigure(i_cl2, fill="red")
        canvas.itemconfigure("l4_cl2", fill="red")
        canvas.itemconfigure("l5.2_cl2", fill="red")
        canvas.itemconfigure("l1.2_cc", fill="red")
        canvas.itemconfigure("b4", fill="red")
        canvas.itemconfigure("l4_clt", fill="red")
        #messagebox.showinfo("", "Întrerupătorul este conectat.")


def toggle_disconnect_i_cl2():
    global connect_i_cl2
    if activate_load_cl1 and close_sl_cl1 and connect_i_cl1 and close_sb1_cl1 and close_sb11_clt and connect_i_clt and close_sb12_clt and close_sb1_cl2 and close_sl_cl2:
        connect_i_cl2 = False
        canvas.itemconfigure(i_cl2, fill="green")
        canvas.itemconfigure("l1_cl2", fill="black")
        canvas.itemconfigure("l3_cl2", fill="black")
        #messagebox.showinfo("", "Întrerupătorul este deconectat.")
    elif activate_load_cl1 and close_sl_cl1 and connect_i_cl1 and close_sb2_cl1 and close_sb21_clt and connect_i_clt and close_sb22_clt and close_sb2_cl2 and close_sl_cl2:
        connect_i_cl2 = False
        canvas.itemconfigure(i_cl2, fill="green")
        canvas.itemconfigure("l1_cl2", fill="black")
        canvas.itemconfigure("l3_cl2", fill="black")
        #messagebox.showinfo("", "Întrerupătorul este deconectat.")
    if connect_i_cl2 and activate_load_cl2:
        connect_i_cl2 = False
        canvas.itemconfigure(i_cl2, fill="green")
        canvas.itemconfigure("l4_cl2", fill="black")
        canvas.itemconfigure("l5.1_cl2", fill="black")
        canvas.itemconfigure("l5.2_cl2", fill="black")
        canvas.itemconfigure("b3", fill="black")
        canvas.itemconfigure("b4", fill="black")
        canvas.itemconfigure("l1.1_cc", fill="black")
        canvas.itemconfigure("l1.2_cc", fill="black")
        canvas.itemconfigure("l2_cc", fill="black")
        canvas.itemconfigure("l3_cc", fill="black")
        canvas.itemconfigure("m_cc", fill="white")
        canvas.itemconfigure("l3_clt", fill="black")
        canvas.itemconfigure("l4_clt", fill="black")
        canvas.itemconfigure("l1_clt", fill="black")
        canvas.itemconfigure("l2_clt", fill="black")
        canvas.itemconfigure("l5_clt", fill="black")
        canvas.itemconfigure("l6_clt", fill="black")
        canvas.itemconfigure("b1", fill="black")
        canvas.itemconfigure("b2", fill="black")
        canvas.itemconfigure("l5.1_cl1", fill="black")
        canvas.itemconfigure("l5.2_cl1", fill="black")
        canvas.itemconfigure("l4_cl1", fill="black")
        canvas.itemconfigure("l3_cl1", fill="black")
        canvas.itemconfigure("l1_cl1", fill="black")
        # messagebox.showinfo("", "Întrerupătorul este deconectat.")
    elif connect_i_cl2:
        connect_i_cl2 = False
        canvas.itemconfigure(i_cl2, fill="green")
        #messagebox.showinfo("", "Întrerupătorul este deconectat.")


def toggle_close_sl_cl2():
    global close_sl_cl2
    if close_clp_cl2:
        messagebox.showerror("Interblocaj!", "CLP este închis.")
    elif not close_sl_cl2 and activate_load_cl2:
        close_sl_cl2 = True
        canvas.itemconfigure(sl_cl2, fill="red")
        canvas.itemconfigure("l3_cl2", fill="red")
        #messagebox.showinfo("", "Separatorul de linie este închis.")
    elif not close_sl_cl2:
        close_sl_cl2 = True
        canvas.itemconfigure(sl_cl2, fill="red")
        #messagebox.showinfo("", "Separatorul de linie este închis.")


def toggle_open_sl_cl2():
    global close_sl_cl2
    if connect_i_cl2:
        messagebox.showerror("Interblocaj!", "Întrerupătorul este conectat.")
    elif close_sl_cl2:
        close_sl_cl2 = False
        canvas.itemconfigure(sl_cl2, fill="green")
        canvas.itemconfigure("l3_cl2", fill="black")
        #messagebox.showinfo("", "Separatorul de linie este deschis.")


def toggle_close_clp_cl2():
    global close_clp_cl2
    if close_sl_cl2:
        messagebox.showerror("Interblocaj", "Separatorul de linie este închis.")
    elif connect_i_cl2:
        messagebox.showerror("Interblocaj!", "întrerupătorul este conectat.")
    elif not close_clp_cl2 and activate_load_cl2:
        close_clp_cl2 = True
        canvas.itemconfigure(clp_cl2, fill="red")
        canvas.itemconfigure("l2_cl2", fill="red")
        #messagebox.showinfo("", "CLP este închis.")
    elif not close_clp_cl2:
        close_clp_cl2 = True
        canvas.itemconfigure(clp_cl2, fill="red")
        #messagebox.showinfo("", "CLP este închis.")


def toggle_open_clp_cl2():
    global close_clp_cl2
    if close_clp_cl2:
        close_clp_cl2 = False
        canvas.itemconfigure(clp_cl2, fill="green")
        canvas.itemconfigure("l2_cl2", fill="black")
        #messagebox.showinfo("", "CLP este deschis.")


# Schema aplicației-----------------------------------------------------------------------------------------------------


def draw_schema():
    global sb1_cl1, sb2_cl1, i_cl1, sl_cl1, clp_cl1, sb1_cl2, sb2_cl2, i_cl2, sl_cl2, clp_cl2, sb1_cc, sb2_cc, \
        i_cc, clp_cc, sb11_clt, sb21_clt, sb12_clt, sb22_clt, i_clt

    # Titluri-----------------------------------------------------------------------------------------------------------
    canvas.create_text(165, 30, text="Celulă de linie 1", font=('Times', '18', 'bold'))
    canvas.create_text(740, 30, text="Celulă cu cuplă longo-transversală", font=('Times', '18', 'bold'))
    canvas.create_text(1325, 30, text="Celulă cu consumator", font=('Times', '18', 'bold'))
    canvas.create_text(1675, 30, text="Celulă de linie 2", font=('Times', '18', 'bold'))
    canvas.create_rectangle(505, 630, 1015, 770, outline="red", width="3")
    canvas.create_text(1000, 700, text="     ⚡ SIMULARE \n INTERBLOCAJE ⚡", font=('Times', '40', 'bold', 'italic'),
                       anchor="e")
    canvas.create_text(1810, 1000, text="made by Teodor-Andrei Lungu ©", font='Times')

    # Denumire echipamente----------------------------------------------------------------------------------------------

    canvas.create_text(50, 60, text="BARA I", font=('Times', '10', 'bold'), anchor="e")
    canvas.create_text(55, 120, text="BARA II", font=('Times', '10', 'bold'), anchor="e")
    canvas.create_text(1905, 60, text="BARA III", font=('Times', '10', 'bold'), anchor="e")
    canvas.create_text(1905, 120, text="BARA IV", font=('Times', '10', 'bold'), anchor="e")
    canvas.create_text(110, 185, text="SB1", font=('Times', '14'), anchor="e")
    canvas.create_text(270, 185, text="SB2", font=('Times', '14'), anchor="e")
    canvas.create_text(160, 312, text="Î", font=('Times', '14', 'bold'), anchor="e")
    canvas.create_text(160, 405, text="SL", font=('Times', '14'), anchor="e")
    canvas.create_text(310, 625, text="CLP", font=('Times', '14'), anchor="e")
    canvas.create_text(1620, 185, text="SB3", font=('Times', '14'), anchor="e")
    canvas.create_text(1780, 185, text="SB4", font=('Times', '14'), anchor="e")
    canvas.create_text(1670, 312, text="Î", font=('Times', '14', 'bold'), anchor="e")
    canvas.create_text(1670, 405, text="SL", font=('Times', '14'), anchor="e")
    canvas.create_text(1820, 625, text="CLP", font=('Times', '14'), anchor="e")
    canvas.create_text(1270, 185, text="SB3", font=('Times', '14'), anchor="e")
    canvas.create_text(1430, 185, text="SB4", font=('Times', '14'), anchor="e")
    canvas.create_text(1320, 392, text="Î", font=('Times', '14', 'bold'), anchor="e")
    canvas.create_text(1470, 625, text="CLP", font=('Times', '14'), anchor="e")
    canvas.create_text(490, 185, text="SB1", font=('Times', '14'), anchor="e")
    canvas.create_text(700, 185, text="SB2", font=('Times', '14'), anchor="e")
    canvas.create_text(790, 185, text="SB3", font=('Times', '14'), anchor="e")
    canvas.create_text(1000, 185, text="SB4", font=('Times', '14'), anchor="e")
    canvas.create_text(715, 332, text="Î", font=('Times', '14', 'bold'), anchor="e")

    # ------Barele desen------------------------------------------------------------------------------------------------

    canvas.create_line(0, 70, 680, 70, tags="b1", fill="black", width="3")
    canvas.create_line(0, 130, 680, 130, tags="b2", fill="black", width="3")
    canvas.create_line(770, 70, 1920, 70, tags="b3", fill="black", width="3")
    canvas.create_line(770, 130, 1920, 130, tags="b4", fill="black", width="3")

    # -----Celulă de Linie 1 desen--------------------------------------------------------------------------------------

    canvas.create_line(120, 70, 120, 200, tags="l5.1_cl1", fill="black", width="2")
    canvas.create_line(220, 130, 220, 200, tags="l5.2_cl1", fill="black", width="2")
    sb1_cl1 = canvas.create_rectangle(110, 200, 130, 230, outline="black", fill="green", width="2")
    canvas.create_line(120, 231, 120, 280, tags="l4_cl1", fill="black", width="2")
    canvas.create_line(220, 231, 220, 280, tags="l4_cl1", fill="black", width="2")
    sb2_cl1 = canvas.create_rectangle(210, 200, 230, 230, outline="black", fill="green", width="2")
    canvas.create_line(120, 280, 220, 280, tags="l4_cl1", fill="black", width="2")
    canvas.create_line(170, 280, 170, 330, tags="l4_cl1", fill="black", width="2")
    i_cl1 = canvas.create_rectangle(155, 330, 185, 360, outline="black", fill="green", width="2")
    canvas.create_line(170, 361, 170, 420, tags="l3_cl1", fill="black", width="2")
    sl_cl1 = canvas.create_rectangle(160, 420, 180, 450, outline="black", fill="green", width="2")
    canvas.create_line(170, 451, 170, 900, tags="l1_cl1", fill="black", width="2")
    canvas.create_line(170, 520, 260, 520, tags="l1_cl1", fill="black", width="2")
    canvas.create_line(260, 520, 260, 640, tags="l1_cl1", fill="black", width="2")
    clp_cl1 = canvas.create_rectangle(250, 640, 270, 670, outline="black", fill="green", width="2")
    canvas.create_line(260, 671, 260, 750, tags="l2_cl1", fill="black", width="2")
    canvas.create_line(250, 750, 270, 750, tags="l2_cl1", fill="black", width="2")
    canvas.create_line(253, 755, 267, 755, tags="l2_cl1", fill="black", width="2")
    canvas.create_line(255, 760, 265, 760, tags="l2_cl1", fill="black", width="2")
    x = 170
    y1 = 660
    y2 = 680
    canvas.create_polygon(x, y1, x - 10, y2, x + 10, y2, tags="l1_cl1", outline="black", fill="black")

    # ----Celulă cu cuplă longo-transversală desen----------------------------------------------------------------------

    canvas.create_line(500, 70, 500, 200, tags="l1_clt", fill="black", width="2")
    sb11_clt = canvas.create_rectangle(490, 200, 510, 230, outline="black", fill="green", width="2")
    canvas.create_line(500, 231, 500, 450, tags="l5_clt", fill="black", width="2")

    canvas.create_line(650, 130, 650, 200, tags="l2_clt", fill="black", width="2")
    sb21_clt = canvas.create_rectangle(640, 200, 660, 230, outline="black", fill="green", width="2")
    canvas.create_line(650, 231, 650, 280, tags="l6_clt", fill="black", width="2")

    canvas.create_line(650, 280, 800, 280, tags="l6_clt", fill="black", width="2")
    canvas.create_line(725, 280, 725, 350, tags="l6_clt", fill="black", width="2")
    i_clt = canvas.create_rectangle(710, 350, 740, 380, outline="black", fill="green", width="2")
    canvas.create_line(725, 381, 725, 450, tags="l5_clt", fill="black", width="2")
    canvas.create_line(500, 450, 950, 450, tags="l5_clt", fill="black", width="2")

    canvas.create_line(800, 70, 800, 200, tags="l3_clt", fill="black", width="2")
    sb12_clt = canvas.create_rectangle(790, 200, 810, 230, outline="black", fill="green", width="2")
    canvas.create_line(800, 231, 800, 280, tags="l6_clt", fill="black", width="2")

    canvas.create_line(950, 130, 950, 200, tags="l4_clt", fill="black", width="2")
    sb22_clt = canvas.create_rectangle(940, 200, 960, 230, outline="black", fill="green", width="2")
    canvas.create_line(950, 231, 950, 450, tags="l5_clt", fill="black", width="2")

    # ----Celula cu consumator desen------------------------------------------------------------------------------------

    canvas.create_line(1280, 70, 1280, 200, tags="l1.1_cc", fill="black", width="2")
    sb1_cc = canvas.create_rectangle(1270, 200, 1290, 230, outline="black", fill="green", width="2")  # Separator
    canvas.create_line(1280, 231, 1280, 280, tags="l2_cc", fill="black", width="2")

    canvas.create_line(1380, 130, 1380, 200, tags="l1.2_cc", fill="black", width="2")
    sb2_cc = canvas.create_rectangle(1370, 200, 1390, 230, outline="black", fill="green", width="2")  # Separator
    canvas.create_line(1380, 231, 1380, 280, tags="l2_cc", fill="black", width="2")

    canvas.create_line(1280, 280, 1380, 280, tags="l2_cc", fill="black", width="2")

    canvas.create_line(1330, 280, 1330, 410, tags="l2_cc", fill="black", width="2")

    i_cc = canvas.create_rectangle(1315, 410, 1345, 440, outline="black", fill="green", width="2")  # Întrerupător

    canvas.create_line(1330, 441, 1330, 650, tags="l3_cc", fill="black", width="2")
    canvas.create_oval(1290, 650, 1370, 730, tags="m_cc", outline="black", width="2")
    canvas.create_text(1346, 690, text="M", font=('Helvetica', '30', 'bold'), fill="black", anchor="e")
    canvas.create_line(1330, 520, 1420, 520, tags="l3_cc", fill="black", width="2")

    canvas.create_line(1420, 520, 1420, 640, tags="l3_cc", fill="black", width="2")

    clp_cc = canvas.create_rectangle(1410, 640, 1430, 670, outline="black", fill="green", width="2")  # CLP

    canvas.create_line(1420, 750, 1420, 670, tags="l4_cc", fill="black", width="2")

    canvas.create_line(1410, 750, 1430, 750, tags="l4_cc", fill="black", width="2")
    canvas.create_line(1413, 755, 1427, 755, tags="l4_cc", fill="black", width="2")
    canvas.create_line(1415, 760, 1425, 760, tags="l4_cc", fill="black", width="2")

    # -----Celula de linie 2 desen--------------------------------------------------------------------------------------

    canvas.create_line(1630, 70, 1630, 200, tags="l5.1_cl2", fill="black", width="2")
    sb1_cl2 = canvas.create_rectangle(1620, 200, 1640, 230, outline="black", fill="green", width="2")  # Separator
    canvas.create_line(1630, 231, 1630, 280, tags="l4_cl2", fill="black", width="2")

    canvas.create_line(1730, 130, 1730, 200, tags="l5.2_cl2", fill="black", width="2")
    sb2_cl2 = canvas.create_rectangle(1720, 200, 1740, 230, outline="black", fill="green", width="2")  # Separator
    canvas.create_line(1730, 231, 1730, 280, tags="l4_cl2", fill="black", width="2")

    canvas.create_line(1630, 280, 1730, 280, tags="l4_cl2", fill="black", width="2")

    canvas.create_line(1680, 280, 1680, 330, tags="l4_cl2", fill="black", width="2")

    i_cl2 = canvas.create_rectangle(1665, 330, 1695, 360, outline="black", fill="green", width="2")  # Întrerupător

    canvas.create_line(1680, 361, 1680, 420, tags="l3_cl2", fill="black", width="2")
    sl_cl2 = canvas.create_rectangle(1670, 420, 1690, 450, outline="black", fill="green", width="2")
    canvas.create_line(1680, 451, 1680, 900, tags="l1_cl2", fill="black", width="2")
    canvas.create_line(1680, 520, 1770, 520, tags="l1_cl2", fill="black", width="2")

    canvas.create_line(1770, 520, 1770, 640, tags="l1_cl2", fill="black", width="2")

    clp_cl2 = canvas.create_rectangle(1760, 640, 1780, 670, outline="black", fill="green", width="2")  # CLP

    canvas.create_line(1770, 671, 1770, 750, tags="l2_cl2", fill="black", width="2")

    canvas.create_line(1760, 750, 1780, 750, tags="l2_cl2", fill="black", width="2")
    canvas.create_line(1763, 755, 1777, 755, tags="l2_cl2", fill="black", width="2")
    canvas.create_line(1765, 760, 1775, 760, tags="l2_cl2", fill="black", width="2")

    x = 1680
    y1 = 660
    y2 = 680
    canvas.create_polygon(x, y1, x - 10, y2, x + 10, y2, tags="l1_cl2", outline="black", fill="black")


window = tk.Tk()
img = PhotoImage(file='C:\\Users\\Gaming\\PycharmProjects\\LicentaFinal\\Lighting.png')
window.iconphoto(False, img)
window.title("Simulare interblocaje")
window.geometry("1920x1080")
canvas = tk.Canvas(width=1920, height=1080, bg="white")
draw_schema()
canvas.place(x=0, y=0)


# ---------------Butoane celulă de linie 1------------------------------------------------------------------------------

open_sb1_cl1_button = tk.Button(window, text="D", command=toggle_open_sb1_cl1, bg='green1', height='1', width='2')
open_sb1_cl1_button.place(x=82, y=203)

close_sb1_cl1_button = tk.Button(window, text="Î", command=toggle_close_sb1_cl1, bg='red1', height='1', width='2')
close_sb1_cl1_button.place(x=135, y=203)

open_sb2_cl1_button = tk.Button(window, text="D", command=toggle_open_sb2_cl1, bg='green1', height='1', width='2')
open_sb2_cl1_button.place(x=182, y=203)

close_sb2_cl1_button = tk.Button(window, text="Î", command=toggle_close_sb2_cl1, bg='red1', height='1', width='2')
close_sb2_cl1_button.place(x=235, y=203)

disconnect_i_cl1_button = tk.Button(window, text="D", command=toggle_disconnect_i_cl1, bg='green1', height='1',
                                    width='2')
disconnect_i_cl1_button.place(x=127, y=332)

connect_i_cl1_button = tk.Button(window, text="C", command=toggle_connect_i_cl1, bg='red1', height='1', width='2')
connect_i_cl1_button.place(x=191, y=332)

open_sl_cl1_button = tk.Button(window, text="D", command=toggle_open_sl_cl1, bg='green1', height='1', width='2')
open_sl_cl1_button.place(x=132, y=422)

close_sl_cl1_button = tk.Button(window, text="Î", command=toggle_close_sl_cl1, bg='red1', height='1', width='2')
close_sl_cl1_button.place(x=186, y=422)

open_clp_cl1_button = tk.Button(window, text="D", command=toggle_open_clp_cl1, bg='green1', height='1', width='2')
open_clp_cl1_button.place(x=222, y=642)

close_clp_cl1_button = tk.Button(window, text="Î", command=toggle_close_clp_cl1, bg='red1', height='1', width='2')
close_clp_cl1_button.place(x=275, y=642)

# ---------------Butoane celulă cu cuplă longo-transversală-------------------------------------------------------------

open_sb11_clt_button = tk.Button(window, text="D", command=toggle_open_sb11_clt, bg='green1', height='1', width='2')
open_sb11_clt_button.place(x=462, y=203)

close_sb11_clt_button = tk.Button(window, text="Î", command=toggle_close_sb11_clt, bg='red1', height='1', width='2')
close_sb11_clt_button.place(x=515, y=203)

open_sb21_clt_button = tk.Button(window, text="D", command=toggle_open_sb21_clt, bg='green1', height='1', width='2')
open_sb21_clt_button.place(x=612, y=203)

close_sb21_clt_button = tk.Button(window, text="Î", command=toggle_close_sb21_clt, bg='red1', height='1', width='2')
close_sb21_clt_button.place(x=665, y=203)

open_sb12_clt_button = tk.Button(window, text="D", command=toggle_open_sb12_clt, bg='green1', height='1', width='2')
open_sb12_clt_button.place(x=762, y=203)

close_sb12_clt_button = tk.Button(window, text="Î", command=toggle_close_sb12_clt, bg='red1', height='1', width='2')
close_sb12_clt_button.place(x=815, y=203)

open_sb22_clt_button = tk.Button(window, text="D", command=toggle_open_sb22_clt, bg='green1', height='1', width='2')
open_sb22_clt_button.place(x=912, y=203)

close_sb22_clt_button = tk.Button(window, text="Î", command=toggle_close_sb22_clt, bg='red1', height='1', width='2')
close_sb22_clt_button.place(x=965, y=203)

disconnect_i_clt_button = tk.Button(window, text="D", command=toggle_disconnect_i_clt, bg='green1', height='1',
                                    width='2')
disconnect_i_clt_button.place(x=682, y=352)

connect_i_clt_button = tk.Button(window, text="C", command=toggle_connect_i_clt, bg='red1', height='1', width='2')
connect_i_clt_button.place(x=745, y=352)

# ----------------Butoane celulă cu consumator--------------------------------------------------------------------------
open_sb1_cc_button = tk.Button(window, text="D", command=toggle_open_sb1_cc, bg='green1', height='1', width='2')
open_sb1_cc_button.place(x=1242, y=203)

close_sb1_cc_button = tk.Button(window, text="Î", command=toggle_close_sb1_cc, bg='red1', height='1', width='2')
close_sb1_cc_button.place(x=1295, y=203)

open_sb2_cc_button = tk.Button(window, text="D", command=toggle_open_sb2_cc, bg='green1', height='1', width='2')
open_sb2_cc_button.place(x=1342, y=203)

close_sb2_cc_button = tk.Button(window, text="Î", command=toggle_close_sb2_cc, bg='red1', height='1', width='2')
close_sb2_cc_button.place(x=1395, y=203)

disconnect_i_cc_button = tk.Button(window, text="D", command=toggle_disconnect_i_cc, bg='green1', height='1',
                                   width='2')
disconnect_i_cc_button.place(x=1287, y=412)

connect_i_cc_button = tk.Button(window, text="C", command=toggle_connect_i_cc, bg='red1', height='1', width='2')
connect_i_cc_button.place(x=1351, y=412)

open_clp_cc_button = tk.Button(window, text="D", command=toggle_open_clp_cc, bg='green1', height='1', width='2')
open_clp_cc_button.place(x=1382, y=642)

close_clp_cc_button = tk.Button(window, text="Î", command=toggle_close_clp_cc, bg='red1', height='1', width='2')
close_clp_cc_button.place(x=1435, y=642)

# ---------------Butoane celulă de linie 2------------------------------------------------------------------------------

open_sb1_cl2_button = tk.Button(window, text="D", command=toggle_open_sb1_cl2, bg='green1', height='1', width='2')
open_sb1_cl2_button.place(x=1592, y=203)

close_sb1_cl2_button = tk.Button(window, text="Î", command=toggle_close_sb1_cl2, bg='red1', height='1', width='2')
close_sb1_cl2_button.place(x=1645, y=203)

open_sb2_cl2_button = tk.Button(window, text="D", command=toggle_open_sb2_cl2, bg='green1', height='1', width='2')
open_sb2_cl2_button.place(x=1692, y=203)

close_sb2_cl2_button = tk.Button(window, text="Î", command=toggle_close_sb2_cl2, bg='red1', height='1', width='2')
close_sb2_cl2_button.place(x=1745, y=203)

disconnect_i_cl2_button = tk.Button(window, text="D", command=toggle_disconnect_i_cl2, bg='green1', height='1',
                                    width='2')
disconnect_i_cl2_button.place(x=1637, y=332)

connect_i_cl2_button = tk.Button(window, text="C", command=toggle_connect_i_cl2, bg='red1', height='1', width='2')
connect_i_cl2_button.place(x=1701, y=332)

open_sl_cl2_button = tk.Button(window, text="D", command=toggle_open_sl_cl2, bg='green1', height='1', width='2')
open_sl_cl2_button.place(x=1642, y=422)

close_sl_cl2_button = tk.Button(window, text="Î", command=toggle_close_sl_cl2, bg='red1', height='1', width='2')
close_sl_cl2_button.place(x=1696, y=422)

open_clp_cl2_button = tk.Button(window, text="D", command=toggle_open_clp_cl2, bg='green1', height='1', width='2')
open_clp_cl2_button.place(x=1732, y=642)

close_clp_cl2_button = tk.Button(window, text="Î", command=toggle_close_clp_cl2, bg='red1', height='1', width='2')
close_clp_cl2_button.place(x=1785, y=642)

# ------------- Butoane control sarcină --------------------------------------------------------------------------------


activate_load_cl1_button = tk.Button(window, text="Aplicare \n tensiune ⚡", command=toggle_activate_load_cl1, bg='red1', height='2',
                                     width='9')
activate_load_cl1_button.place(x=70, y=620)

deactivate_load_cl1_button = tk.Button(window, text="Întrerupere \n tensiune ⚡", command=toggle_deactivate_load_cl1, bg='green1',
                                       height='2', width='9')
deactivate_load_cl1_button.place(x=70, y=680)

activate_load_cl2_button = tk.Button(window, text="Aplicare \n tensiune ⚡", command=toggle_activate_load_cl2, bg='red1', height='2',
                                     width='10')
activate_load_cl2_button.place(x=1580, y=620)

deactivate_load_cl2_button = tk.Button(window, text="Întrerupere \n tensiune ⚡", command=toggle_deactivate_load_cl2, bg='green1',
                                       height='2', width='10')
deactivate_load_cl2_button.place(x=1580, y=680)

# Maximizare fereastră

window.state('zoomed')

# Creare fereastră

window.mainloop()

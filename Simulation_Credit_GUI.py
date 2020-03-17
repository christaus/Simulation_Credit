# -*- coding:utf-8 -*-
#
# Copyright © 2020 cGIfl300
#
# Permission is hereby granted, free of charge, to any person obtaining a
# copy of this software and associated documentation files (the “Software”),
# to deal in the Software without restriction, including without limitation
# the rights to use, copy, modify, merge, publish, distribute, sublicense,
# and/or sell copies of the Software, and to permit persons to whom the
# Software is furnished to do so, subject to the following conditions:
#
# The above copyright notice and this permission notice shall be included
# in all copies or substantial portions of the Software.
#
# THE SOFTWARE IS PROVIDED “AS IS”, WITHOUT WARRANTY OF ANY KIND, EXPRESS OR
# IMPLIED, INCLUDING BUT NOT LIMITED TO THE WARRANTIES OF MERCHANTABILITY,
# FITNESS FOR A PARTICULAR PURPOSE AND NONINFRINGEMENT. IN NO EVENT SHALL
# THE AUTHORS OR COPYRIGHT HOLDERS BE LIABLE FOR ANY CLAIM, DAMAGES OR OTHER
# LIABILITY, WHETHER IN AN ACTION OF CONTRACT, TORT OR OTHERWISE, ARISING FROM,
# OUT OF OR IN CONNECTION WITH THE SOFTWARE OR THE USE OR OTHER DEALINGS IN
# THE SOFTWARE.

from tkinter import *
from Simulation_Credit import *

class Simulation_Credit_GUI(Toplevel):
    ''' Interface graphique pour la simulation d'un crédit
    '''
    def __init__(self, debug = False):
        Toplevel.__init__(self)
        self.debug = debug
        
    def interface(self):
        ''' Interface de la fenêtre
        '''
        
        couleur_fond = 'green'
        couleur_texte = 'red'
        couleur_fond_saisie = 'purple'
        couleur_texte_saisie = 'yellow'
        couleur_activebackground = couleur_texte_saisie
        couleur_activeforeground = couleur_fond_saisie
        self.mensualite = StringVar()
        
        self.title('Simulation Crédit')
        self.geometry('400x200')
        
        self.panel_001 = Label(self, bg = couleur_fond)
        
        self.label_montant = Label(self.panel_001,
                                   fg = couleur_texte,
                                   bg = couleur_fond,
                                   text = 'Montant :')
        
        self.value_montant = Scale(self.panel_001,
                                  fg = couleur_texte,
                                  bg = couleur_fond,
                                  from_= 1,
                                  to = 1000000,
                                  orient=HORIZONTAL)
        
        self.label_taux = Label(self.panel_001,
                                fg = couleur_texte,
                                bg = couleur_fond,
                                text = 'Taux :')
        
        self.entry_taux = Entry(self.panel_001,
                                bg = couleur_fond_saisie,
                                fg = couleur_texte_saisie,
                                relief = 'flat')
        
        self.btn_valider = Button(self.panel_001,
                                  bg = couleur_fond_saisie,
                                  fg = couleur_texte_saisie,
                                  text = 'Calculer',
                                  command = lambda: self.do_calculer(taux = self.entry_taux.get(),
                                                                   duree = self.value_duree.get(),
                                                                   montant = self.value_montant.get()),
                                  activebackground = couleur_activebackground,
                                  activeforeground = couleur_activeforeground)
        
        self.label_duree = Label(self.panel_001,
                                 fg = couleur_texte,
                                 bg = couleur_fond,
                                 text = 'Durée :')
        
        self.value_duree = Scale(self.panel_001,
                                 fg = couleur_texte,
                                 bg = couleur_fond,
                                 from_= 2,
                                 to = 1200,
                                 orient=HORIZONTAL)
        
        self.label_mensualité = Label(self.panel_001,
                                      fg = couleur_texte,
                                      bg = couleur_fond,
                                      textvariable = self.mensualite)
                                  
        """ Implantation des composants
        """
        
        self.panel_001.pack(fill = BOTH,
                            expand = True)
        
        Grid.rowconfigure(self.panel_001, 0, weight=1)
        Grid.rowconfigure(self.panel_001, 1, weight=1)
        Grid.rowconfigure(self.panel_001, 2, weight=1)
        Grid.rowconfigure(self.panel_001, 3, weight=1)
        Grid.rowconfigure(self.panel_001, 4, weight=1)
        Grid.columnconfigure(self.panel_001, 0, weight=1)
        Grid.columnconfigure(self.panel_001, 1, weight=1)
        
        self.label_montant.grid(column = 0,
                                row = 0,
                                sticky = W+E)
        
        self.value_montant.grid(column = 1,
                               row = 0,
                               sticky = W+E)
        
        self.label_taux.grid(column = 0,
                             row = 1,
                             sticky = W+E)
        
        self.entry_taux.grid(column = 1,
                             row = 1,
                             sticky = W+E)
        
        self.label_duree.grid(column = 0,
                                row = 2,
                                sticky = W+E)
        
        self.value_duree.grid(column = 1,
                               row = 2,
                               sticky = W+E)
        
        self.btn_valider.grid(column = 0,
                              row = 3,
                              sticky=W+E+N+S,
                              columnspan = 2)
        
        self.label_mensualité.grid(column = 0,
                              row = 4,
                              sticky=W+E+N+S,
                              columnspan = 2)
    
    def run(self):
        self.interface()
        
    def do_calculer(self, montant, taux, duree):
        ''' Simulation du crédit
        '''
        if self.is_float(taux):
            App = Simulation_Credit(montant = montant,
                                    debug = self.debug,
                                    duree = duree,
                                    taux = float(taux))
            App.run()
            self.mensualite.set('La menssualité est de {}\nLe montant total à rembourser est de {}'.format(App.menssualite, App.montant_total))
            
        else:
            if self.debug:
                print('Oops, ça a foiré!')
            pass
    
    def is_float(self, str):
        try:
            float(str)
        except ValueError:
            return False
        return True

if __name__ == '__main__':
    w = Tk()
    w.after(30000, w.destroy)
    w.wm_state('icon')
    App = Simulation_Credit_GUI(debug = True)
    App.run()
    w.mainloop()

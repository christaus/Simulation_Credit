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

import time

class Simulation_Credit():
    ''' Calcul le montant des mensualités d'un crédit
    
    montant: montant à emprunter
    
    duree: durée du crédit en mois
    
    taux:  taux d'emprunt en % (i.e.: 3.4)
    
    debug affiche la sortie de debug ou pas
    '''
    
    def __init__(self, montant = 0, duree = 0, taux = 0, debug = False):
        self.montant = montant
        self.duree = duree
        self.taux = taux
        self.debug = debug
        if debug:
            self.start_time = time.time()
    
    def run(self):
        ''' mensualite = montant des mensualite
        
        montant_total = montant total à rembourses
        '''
        if self.debug:
            print('Montant {} | Durée {} | Taux {}'.format(self.montant,
                                                           self.duree,
                                                           self.taux))
        
        if self.taux != 0:
            self.mensualite = round((self.montant * self.taux / 100 / 12)
                                    /
                                    (1 - (1 + ((self.taux / 100) / 12)) ** (-1 * self.duree)))
        else:
            self.mensualite = round(self.montant / self.duree)
            
        self.montant_total = round(self.mensualite * self.duree)
        
        if self.debug:
            self.do_simuletxt()
    
    def do_simuletxt(self):
        ''' Affiche le tableau de prélèvements du crédit.
        '''
                
        montant_restant = self.montant_total
        
        for a in range (1, self.duree):
            
            montant_restant -= self.mensualite
            
            print('Paiement {} sur {} : {} | Reste à payer {} sur {}'.format(a,
                                                                             self.duree,
                                                                             self.mensualite,
                                                                             montant_restant,
                                                                             self.montant_total))
        
        # Dernière mensualité couvrant donc la totalitée des sommes dûes
        print('Paiement {} sur {} : {} | Reste à payer {} sur {}'.format(a+1,
                                                                         self.duree,
                                                                         montant_restant,
                                                                         0,
                                                                         self.montant_total))
        
        if self.debug:
            print("Temps d\'execution : %s secondes" % (time.time() - self.start_time))
        

if __name__ == '__main__':
    
    App = Simulation_Credit(montant = 100000,
                            debug = True,
                            duree = 7*12,
                            taux = 3.14)
    App.run()
    
    print('La mensualité est de {}\nLe montant total à rembourser est de {}'.format(App.mensualite,
                                                                                    App.montant_total))

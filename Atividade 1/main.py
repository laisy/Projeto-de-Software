from syntax_analisys import *

def main():
  a = SyntaxAnalisys(open_arq())
  a.analyze(open_arq())
  show_text(a)

  print('Done')
  return

def open_arq():
  arq = open('text.txt', 'r')
  return arq

def show_text(a):
  print("Verbos:", a.verbos)
  print("Verbos Auxiliares:", a.verbos_aux)
  print("Pronomes:", a.pronomes)
  print("Substantivos Comuns:", a.subst_comuns)
  print("Substantivos Próprios:", a.subst_proprios)
  print("Conjunções:", a.conjuncoes)

main()



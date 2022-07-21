from syntax_analisys import *

def main():
  arq = open('text.txt', 'r')

  a = SyntaxAnalisys(arq)
  a.analyze(arq)

  arq.close()
  show_text(a)
  close_arq(a)

  return

def close_arq(a):
  arq = open('result.txt', 'w')

  arq.write("Verbos: " + str(a.verbos) + "\n")
  arq.write("Verbos Auxiliares: " + str(a.verbos_aux) + "\n")
  arq.write("Pronomes: " + str(a.pronomes) + "\n")
  arq.write("Substantivos Comuns: " + str(a.subst_comuns) + "\n")
  arq.write("Substantivos Próprios: " + str(a.subst_proprios) + "\n")
  arq.write("Conjunções: " + str(a.conjuncoes) + "\n")

  arq.close()
  
def show_text(a):
  print("Verbos:", a.verbos)
  print("Verbos Auxiliares:", a.verbos_aux)
  print("Pronomes:", a.pronomes)
  print("Substantivos Comuns:", a.subst_comuns)
  print("Substantivos Próprios:", a.subst_proprios)
  print("Conjunções:", a.conjuncoes)

main()



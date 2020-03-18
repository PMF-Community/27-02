print(1/(1+1/(2+1/(3+1/(4+1/(5+(1/6)))))))
#u cemu je caka, tj trik? trik je u zagradama
#ako zelis da razumijes matematicki,
#zapisi na papir
#razlozi problem
#sve sto se dijeli, mora se zagradom
#izolovati
#jer cim 'veci' izraz poput 5+(1/6)
#dijelimo nekim cijelim brojem, tj
#integerom, moramo da ga zagradom izolujemo
#inace interpreter se 'veze' za prvi broj 'pored sebe'

# 5+(1/6)
# 1/(5+1/6)
# 4+1/(5+1/6)
#
# 1/(4+1/(5+1/6))
# 3+1/(4+1/(5+1/6))
#
# 1/(3+1/(4+1/(5+1/6)))
# 2+(1/(3+1/(4+1/(5+1/6))))
#
# 1+1/(2+(1/(3+1/(4+1/(5+1/6)))))
# 1/(1+1/(2+1/(3+1/(4+1/(5+1/6))))))

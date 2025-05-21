'''class D:
    pass
class E:
    pass
class F:
    pass
class B(D,E):
    pass
class C(E,F):
    pass
class A(B,C):
    pass
print(A.__mro__)
'''

'''
step1:
L[A] = A + merge(L[B],L[C],[B,C])

step2：
L[B] = B + merge(L[D],L[E],[D,E])
L[C] = C + merge(L[E],L[F],[E,F])

step3:
merge(L[D],L[E],[D,E]) =  merge([D,O] + [E,O] + [D,E]) = [D] + merge([O],[E,O],[E]) = [D,E,O]
merge(L[E],L[F],[E,F]) = merge([E,O],[F,O],[E,F]) = [E] + merge([O],[F,O],[F]) = [E,F,O]
L[B] = [B,D,E,O]
L[C] = [C,E,F,O]

step3:
L[A] = A + merge([B,D,E,O],[C,E,F,O],[B,C]) = [A,B] + merge([D,E,O],[C,E,F,O],[C]) = [A,B,D] + merge([E,O],[C,E,F,O],[C])
= [A,B,D,C] + merge([E,O],[E,F,O]) = [A,B,D,C,E] + merge([O],[F,O]) = [A,B,D,C,E,F,O]
'''


class A:
    pass
class B(A):
    pass
class C(A):
    pass
class D(B, C):
    pass
class E:
    pass
class F(D, E):
    pass
class G(F, D):
    pass
class H:
    pass
class I(H, G):
    pass


'''
step1:
L[I] = I + merge(L[H]),L[G],[H,G])

step2:
L[H] = [H,O]
L[G] = G + merge(L[F],L[D],[F,D])

step3:
L[F] = F + merge(L[D],L[E],[D,E])
L[D] = D + merge(L[B],L[C],[B,C])

step4:
L[B] = [B,A,O]
L[C] = [C,A,O]

step5:
L[D] = D + merge([B,A,O],[C,A,O],[B,C]) = [D,B] + merge([A,O],[C,A,O],[C]) = [D,B,C] + merge([A,O],[A,O]) = [D,B,C,A,O]
L[F] = F + merge([D,B,C,A,O],[E,O],[D,E]) = [F,D] + merge([B,C,A,O],[E,O],[E]) = [F,D,B] + merge([C,A,O],[E,O],[E])
     = [F,D,B,C] + merge([A,O],[E,O],[E]) = [F,D,B,C,A] + merge([O],[E,O],[E]) = [F,D,B,C,A,E,O] 
     
step6:
L[G] =  G + merge([F,D,B,C,A,E,O] ,[D,B,C,A,O],[F,D]) = [G,F,D,B,C,A,E,O]

step7:
L[I] = I + merge([H,O],[G,F,D,B,C,A,E,O],[H,G]) = [I,H,G,F,D,B,C,A,E,O]

'''
#print(D.__mro__)
#print(F.__mro__)
#print(G.__mro__)
#print(I.__mro__)
import lex as lex
import math
#tolkens/atomos e codigo
Dic_Reserved_Atom_Cod = {
'Bool': '310' , 
'End' : '318',
'diferenteIgual' : '410',  
'diferente' : '421', 
'While' : '311', 
'Return' : '319', 
 'comentario' : '410', 
 'porcento': '422', 
'Break':"312", 
 'False':"320" ,  
'and' : "411",  
'fechaparentese' : "423", 
'Void' : "313", 
 'Program' : "321", 
 'abreparentese' : "412",  
'vezes' : "424",  
'Char' : "314", 
 'Float' : "322", 
 'dividido' : "413", 
 'virgula': "425",  
'True' : "315",  
 'Int' : "323", 
 'pontoevirgula' : "414",  
'fechachave' : "426",  
'Else' : "316",  
'If' : "324", 
 'abrechave' : "415",  
'ou' : "427", 
'String' : "317",  
'Begin' : "325",  
'abrecolchete' : "416",  
'fechacolchete' : "428", 
'mais' : "417", 
 'menorigual' : "418",
 'maiorigual' : "420",
 'igualigual' : "430", 
 'menor' : "429", 
'igual' : "419",  
'maior' : "431", 
'menos' : "432"
}

#Character 510
    #< Character > ::= "'" < letra > "'" //inicia e termina com aspas simples
    #  < letra > ::= a | b | c | d | e | f | g | h | i | j | k | l | m | n | o | p | q | r | s | t | u | v | w | x | y | z
#  Constant-String 511
    # < Constant-String > ::= "''" < Middle-String > "''"
    # < Middle-String > ::= ( < letra > | < branco > | < digito> | $ | _ | . ) < Middle-String > | < letra > | < branco > | < digito> | $ | _ | .
    # < letra > ::= a | b | c | d | e | f | g | h | i | j | k | l | m | n | o | p | q | r | s | t | u | v | w | x | y | z
    # < digito > ::= 0 | 1 | 2 | 3 | 4 | 5 | 6 | 7 | 8 | 9
    # < branco > ::= “caracter de espaço em branco”.
#  Float-Number 512 
    # < Float-Number > ::= < decimal_digits > . < decimal_digits > | < decimal_digits > . < decimal_digits > < exponent_part >
    # < decimal_digits > ::= < digito > | < decimal_digits > < digito >
    # < exponent_part > ::= e < decimal_digits > | e - < decimal_digits > | e + < decimal_digits >
    #   
# Function 513
    #< Function > ::= < letra > | < Identifier > <letra> | < Identifier > < digito >
    #< letra > ::= a | b | c | d | e | f | g | h | i | j | k | l | m | n | o | p | q | r | s | t | u | v | w | x | y | z

#  Identifier 514
    #< Identifier > ::= < letra > | _ | < Identifier > <letra> | < Identifier > < digito > | < Identifier > _
# Integer-Number 515
    #< Integer-Number > ::= < decimal_digits >
    # <decimal_digits > ::= < digito > | < decimal_digits > < digito >
    #< digito > ::= 0 | 1 | 2 | 3 | 4 | 5 | 6 | 7 | 8 | 9

tokens = (
'Bool', 
'End',
'diferenteIgual',  
'diferente', 
'While', 
'Return', 
 'comentario', 
 'porcento', 
'Break', 
 'False',  
'and',  
'fechaparentese', 
'Void', 
 'Program', 
 'abreparentese',  
'vezes',  
'Char', 
 'Float', 
 'dividido', 
 'virgula',  
'True', 
 'Int', 
 'pontoevirgula',  
'fechachave',  
'Else',  
'If', 
 'abrechave',  
'ou', 
'String',  
'Begin',  
'abrecolchete',  
'fechacolchete', 
'mais', 
 'menorigual',
 'maiorigual',
 'igualigual', 
 'menor', 
'igual',  
'maior', 
'menos'
)


# Tokens
t_Bool =  r'Bool'
t_End = r'End'
t_diferenteIgual = r'!=' 
t_diferente = r'!'
t_While = r'While'
t_Return = r'Return'
t_comentario = r'\#'
t_porcento = r'%'
t_Break = r'Break'
t_False = r'False'
t_and =  r'&'
t_fechaparentese = r'\)'
t_Void = r'Void'
t_Program = r'Program'
t_abreparentese  =  r'\('
t_vezes =  r'\*'
t_Char = r'Char'
t_Float = r'Float'
t_dividido = r'/'
t_virgula = r','
t_True = r'True'
t_Int = r'Int'
t_pontoevirgula = r';' 
t_fechachave =  r'\]'
t_Else =  r'Else'
t_If = r'If'
t_abrechave = r'\['
t_ou = r'\|'
t_String = r'String'
t_Begin = r'Begin' 
t_abrecolchete = r'\{'
t_fechacolchete =r'\}'
t_mais = r'\+'
t_menorigual = r'<='
t_maiorigual = r'>='
t_igualigual = r'=='
t_menor = r'<'
t_igual = r'='
t_maior = r'>'
t_menos = r'-'


# Tokens

# t_PLUS    = r'\+'
# t_MINUS   = r'-'
# t_TIMES   = r'\*'
# t_DIVIDE  = r'/'
# t_EQUALS  = r'='
# t_LPAREN  = r'\('
# t_RPAREN  = r'\)'
# t_NAME    = r'[a-zA-Z_][a-zA-Z0-9_]*'


# def t_Bool(t):
#     print(t)
#     print("dentro de tbool")
#     return t

# Ignored characters
t_ignore = " \t"

# Error handling rule
def t_error(t):
    print("Illegal character '%s'" % t.value[0])
    t.lexer.skip(1)




def getlinha(pos):
    tamlinha = 30
    pos = int(pos)
    pos = math.floor(pos/tamlinha)
    return pos


# Build the lexer
lexer = lex.lex()

data = "Program If (  ) Bool Bool == + - = If (  ) Bool Bool == + - = If (  ) Bool Bool == + - = While Int"


lexer.input(data)

Cabeçalho = " nome, email ... "
SaidaLex = Cabeçalho + "\n" + "Elemento lexico , Codigo , indicie tabela simb , linha  \n" 

# Tokenize
while True:
    tok = lexer.token()
    #tok lexpos, lineno,type,value
    if not tok: #quando tok fica vazio 
        break      # No more input

    if tok.type in Dic_Reserved_Atom_Cod:
        SaidaLex += tok.value + " , " +  Dic_Reserved_Atom_Cod[tok.type] + " , " + "none"+" , "+  str(getlinha(tok.lexpos)) +"\n"
    else:
        pass #caso n seja um atomo reservado, puxa a tabela de simbolos

    
    print(tok) # saida = token, simbolo, linha,coluna
                #linha tem que ser feita uma função especial

print(SaidaLex)
import lex as lex
import math

# tolkens/atomos e codigo
Dic_Reserved_Atom_Cod = {
    'Bool': '310',
    'End': '318',
    'diferenteIgual': '410',
    'diferente': '421',
    'While': '311',
    'Return': '319',
    'comentario': '410',
    'porcento': '422',
    'Break': "312",
    'False': "320",
    'and': "411",
    'fechaparentese': "423",
    'Void': "313",
    'Program': "321",
    'abreparentese': "412",
    'vezes': "424",
    'Char': "314",
    'Float': "322",
    'dividido': "413",
    'virgula': "425",
    'True': "315",
    'Int': "323",
    'pontoevirgula': "414",
    'fechachave': "426",
    'Else': "316",
    'If': "324",
    'abrechave': "415",
    'ou': "427",
    'String': "317",
    'Begin': "325",
    'abrecolchete': "416",
    'fechacolchete': "428",
    'mais': "417",
    'menorigual': "418",
    'maiorigual': "420",
    'igualigual': "430",
    'menor': "429",
    'igual': "419",
    'maior': "431",
    'menos': "432",
    'character': "510",
    'constantString': "511",
    'floatNum': "512",
    'intergerNum': "515",
    'identifier': "514",
    'function': "513"

}

Dic_not_Reserved_Atom = ['function', 'identifier','intergerNum','floatNum','constantString','character' ]

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
    'menos',
    'character',
    'constantString',
    'floatNum',
    'intergerNum',
    'identifier',
    'function'

)

# Tokens
t_Bool = r'Bool'
t_End = r'End'
t_diferenteIgual = r'!='
t_diferente = r'!'
t_While = r'While'
t_Return = r'Return'
t_comentario = r'\#'
t_porcento = r'%'
t_Break = r'Break'
t_False = r'False'
t_and = r'&'
t_fechaparentese = r'\)'
t_Void = r'Void'
t_Program = r'Program'
t_abreparentese = r'\('
t_vezes = r'\*'
t_Char = r'Char'
t_Float = r'Float'
t_dividido = r'/'
t_virgula = r','
t_True = r'True'
t_Int = r'Int'
t_pontoevirgula = r';'
t_fechachave = r'\]'
t_Else = r'Else'
t_If = r'If'
t_abrechave = r'\['
t_ou = r'\|'
t_String = r'String'
t_Begin = r'Begin'
t_abrecolchete = r'\{'
t_fechacolchete = r'\}'
t_mais = r'\+'
t_menorigual = r'<='
t_maiorigual = r'>='
t_igualigual = r'=='
t_menor = r'<'
t_igual = r'='
t_maior = r'>'
t_menos = r'-'
# regex derivados
letra = r'[a-z]'
digito = r'[0-9]'
t_character = r'\'' + letra + r'\''
branco = r'\s'

t_constantString = r'\"' + r'[a-z\s0-9.&]*' + r'\"'

decimalDigit = r'[0-9]+'
# expPart = r'e[-+\s]{1}' + decimalDigit
t_floatNum = decimalDigit + r'\.' + decimalDigit + r'(e[-+]?[0-9]+)?'

t_intergerNum = decimalDigit

t_identifier = r'[a-z_][a-z_0-9]*'

t_function = r'[a-z]\s|[a-z_][a-z_0-9]*([0-9]|[a-z])'

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
    pos = math.floor(pos / tamlinha)
    return pos


#tabelaSimboloscount = 600



def executarLexico(data):
    # Build the lexer
    lexer = lex.lex()
    tabelaSimbolos = []
    tabelaSimboloscount = 600
    # data = " Int batata = 3.5 float bb = 12.21e3 a_0 'a' Program If ( ) Bool Bool == \"stringtest\" + - = If ( -5 ) Bool Bool == + - = If (  ) Bool Bool == + - = While Int"

    lexer.input(data)

    Cabeçalho = '''
    EQUIPE	E04	\n
    COMPONENTES:     \n
    Nome	Email	Telefone\n
    Rafael Bessa Loureiro	xxx	xxx\n
    Pedro De Carvalho Marcelo	xxxxx	xxx\n
    Neilton Melgaço Lisboa Junior	xxx	xxx\n
    '''
    SaidaLex = Cabeçalho + "\n" + "tipo, Elemento lexico , Codigo , indicie tabela simb , linha  \n"
    strTAB =  "tipo, value, indice \n"
    # Tokenize
    while True:
        tok = lexer.token()
        # tok lexpos, lineno,type,value
        if not tok:  # quando tok fica vazio
            break  # No more input

        if tok.type in Dic_Reserved_Atom_Cod:
            SaidaLex += tok.type + " , " + tok.value + " , " + Dic_Reserved_Atom_Cod[
                tok.type] + " , " + "none" + " , " + str(getlinha(tok.lexpos)) + "\n"

        elif tok.type in Dic_not_Reserved_Atom:
            SaidaLex += tok.type + " , " + tok.value + " , " + "none" + " , " + str(tabelaSimboloscount) + "," + str(
                getlinha(tok.lexpos)) + "\n"
            tabelaSimbolos.append({
                "tipo": str(tok.type),
                "value": str(tok.value),
                "indice": str(tabelaSimboloscount)
            })
            tabelaSimboloscount += 1

        else:
            pass  # caso n seja um atomo reservado, puxa a tabela de simbolos

       # print(tok)  # saida = token, simbolo, linha,coluna
        # linha tem que ser feita uma função especial

    # f = open("meuteste.LEX", "w")
    # f.write(SaidaLex)
    # f.close()
    # print(SaidaLex)
    return SaidaLex, lexer.token()

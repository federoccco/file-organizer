import os
import shutil
import argparse

files_list = os.listdir("files")  # Creo una lista dei file e cartelle contenuti nella cartella files

extensions = {
    "Images": [".jpg", ".jpeg", ".png"],
    "Docs": [".doc", ".txt", ".odt"],
    "Audio": [".mp3"]
}


def files_order(file_to_move):
    """the function is defined to work along with the argparse module, it takes one argument (input from the command
    line), which will be parsed. The argument must be a valid file name. The function will then identify it and, in case
    it's a file, it will automatically move it in a directory based on the file's extension E.g. .txt will be moved in
    the doc directory, .mp3 will be moved in the audio directory. If a directory does not exist, the function will
    automatically create it and then move the file in it. If the file will be correctly moved, the function return a
    string stating the directory from which the file was taken, and the directory in which the file was moved. If the
    argument passed is not a valid name or the file does not exist in the files directory, the function will return a
    string stating that the file does not exist indeed."""
    cwd = os.getcwd()  # Ottengo il path della current working directory
    if os.path.isfile(f"files/{file_to_move}"):

        """
        ho eliminato il ciclo, al posto di controllare che esiste un file che si chiami come il nome fornito dall' 
        utente controllo direttamente che quel file esista e se esiste utilizzo le sue info per (eventualmente) creare
        una cartella e stampare informazioni
        """
        file_name, extension = os.path.splitext(file_to_move)  # Isolo l' estensione del file
        for key in extensions:  # Ciclo nel dizionario, "key" sarà uguale alla chiave del dizionario ad ogni ciclo
            if extension in extensions[key]:  # Controllo che l' estensione del file sia presente nel mio dizionario

                # Controllo che esista una directory che si chiami come la chiave del dizionario, nel caso non
                # dovesse esistere, la creo.
                if not os.path.isdir(f"files/{key}"):
                    os.makedirs(f"files/{key}")
                src = f"files/{file_to_move}"  # Creo una variabile con il path di origine
                dst = f"files/{key}/{file_to_move}"  # E una con il path di destinazione
                shutil.move(src=src, dst=dst)  # Sposto il file da origine a destinazione
                file_info = f"{file_name} type: {key} size: {os.path.getsize(dst)}B"  # Le informazioni del file
                return f"{file_info} was correctly moved from {cwd}/{src} to {cwd}/{dst}"
    else:
        return f"{file_to_move} does not exist"

    """
    l' else di prima aspettava di verificare che l' intero ciclo finisse, e nel caso di risposta negativa veniva 
    eseguito, l' ho inserito come else clause del ciclo for perché se indentavo come else clause dell' if statement
    di controllo, mi veniva stampato per ogni ciclo del file.  Però come nell' esempio dei commenti, l' else viene 
    eseguito comunque a fine ciclo a meno che non ci sia una prova di interruzione. La mia idea era quella di 
    utilizzare return come prova del successo o meno del ciclo (e come prova di interruzione). Nel caso in cui  non 
    avessi avuto un return, allora sarebbe stato eseguito l' else clause. Forse questo è un caso particolar in cui me 
    la sono cavata grazie alla presenza di return, che deve essere univoco, ma invece che comunicare subito che il file
    non esiste, lo script eseguiva prima tutto il ciclo, con un carico inutile, per poi comunicare all' utente che 
    il file non esiste. Di norma l' else di un for loop viene sempre eseguito ad esaurimento ciclo a meno che non 
    incontri un break statement, che avrei dovuto implementare.  la clausola diventi falsa (while loop)
     
     Ora è semplicemente un else in alternativa al False state dell' if statement di controllo 
     per l' esistenza del file fornito dall' utente
    """


# Creo un oggetto di tipo ArgumentParser a cui andrò ad associare i vari argomenti ed opzioni che voglio utilizzare
parser = argparse.ArgumentParser(
    description="""
The script will move a file from his original directory to another based on its extension. If the directory doesn't
exist, the script will automatically create one, named with the extension's type name. E.g. .mp3 -->Audio, .txt -->Docs
""")

# Tramite parser.add_argument, aggiungo i parametri richiesti ed opzionali che è necessario scrivere nel cmd.
# in questo caso aggiungerò il nome del file che voglio spostare, nonché parametro della funzione definita ad inizio
# script. La funzione che ho creato prende un solo argomento, quindi lo aggiungo rendendo obbligatorio il suo
# inserimento al fine del funzionamento corretto dello script, in caso di mancato inserimento, l' utente verrà avvisato
parser.add_argument(
    # L' argomento è richiesto implicitamente in quanto dichiarato come positional argument e non come series of flags
    # pertanto il parametro "required=True" non è necessario, dato che serve solo nel caso di argomenti opzionali
    "file_to_move",  # l' argomento ricevuto come input dall' utente che sarà processato poi nella funzione
    type=str,  # il tipo che assumerà l' argomento
    # Una breve descrizione di cosa rappresenta l' argomento inserito
    help="This is the name of the file to move, type the name of the file with its extension E.g. 'Hello.txt'"
)

# Dopo aver definito l' assegnazione degli argomenti, procedo con l' assegnazione vera e propria richiamando
# parse_args sull' oggetto creato (parser)
args = parser.parse_args()

# Richiamo poi la funzione definita passando come argomento args.file_to_move, in questo modo verranno applicate le
# istruzioni definite tramite il modulo argparse sul parametro passato alla funzione, per poter visualizzare il
# risultato, lo mando in stampa
print(files_order(args.file_to_move))


# Penso che questo step avrei potuto risolverlo in diverse maniere, usando solo sys o solo argparse, ma non vedo la
# necessità di usarli entrambi. L' unico modo in cui avrei potuto sarebbe stato quello di usare sys.argv[1] come
# variabile, e invece che fare un else statement nella funziona che ritorna una stringa, scrivere un if statement con
# sys.argv maggiore di, minore di, o uguale a, per poi specificare dei comportamenti in base alle condizioni
# soddisfatte.

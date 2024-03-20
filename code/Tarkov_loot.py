import random
import qrcode
import time

#lista degli items ottenibili :

items = ["KIT MEDICO SALEWA", "BARATTOLO TERMITE", "CHIAVE A CRICCHETTO","ADRENALINA INIETTABILE","FIALA DI MORFINA","BATTERIA PER AUTO","PANETTO DI TRITOLO", "KIT MEDICO GRIZZLY","KIT MEDICO AUTO","KIT MEDICO IFAK", "BARATTOLO DI LATTE IN POLVERE","BOTTIGLIA DI VODKA","CARNE IN BARATTOLO","BITCOIN FISICO","LINGOTTO D'ARGENTO","SACCA DI SANGUE","AMPOLLA DI SOLUZIONE FISIOLOGICA","ATTREZZI PER IL LAVORO DI BASE", "ATTREZZI PER IL LAVORO AVANZATO","STRUMENTI DI CALIBRAZIONE", "STRUMENTI DI RIPARAZIONE EQUIPAGGIAMENTO", "PIASTRE BALISTICHE TIPO II", "PIASTRE BALISTICHE TIPO III", "PIASTRE BALISTICHE TIPO IV", "BARATTOLO DI ANTIDOLORIFICI", "BARATTOLO DI AMOXICILLINA", "CONFEZIONE DI AMFETAMINA AD USO MEDICO", "BARATTOLO DI VITAMINE"]

#funzione che ci fa ottenere 5 oggetti casuali
def random_obj_generator():
    return [random.choice(items) for _ in range(5)]
#funzione che dona un'id univoco basato su un timestamp e lo unisce alla nostra lista casuale
def qr_code_per_time_generator():
    unique_id = str(int(time.time())) 

    object_result_random = random_obj_generator()

    object_result_random.append(unique_id)
#generazione del qr code
    qr = qrcode.QRCode(
        version=1,
        error_correction=qrcode.constants.ERROR_CORRECT_L,
        box_size=10,
        border=4,
    )
    qr.add_data(", ".join(object_result_random))
    qr.make(fit=True)
    img = qr.make_image(fill_color="black", back_color="white")
    img.save("Tarkov_game_random_obj.png")

qr_code_per_time_generator()
    

import random
import qrcode
import time

# Lista degli items ottenibili
items = ["KIT MEDICO SALEWA", "BARATTOLO TERMITE", "CHIAVE A CRICCHETTO", "ADRENALINA INIETTABILE", "FIALA DI MORFINA", "BATTERIA PER AUTO", "PANETTO DI TRITOLO", "KIT MEDICO GRIZZLY", "KIT MEDICO AUTO", "KIT MEDICO IFAK", "BARATTOLO DI LATTE IN POLVERE", "BOTTIGLIA DI VODKA", "CARNE IN BARATTOLO", "BITCOIN FISICO", "LINGOTTO D'ARGENTO", "SACCA DI SANGUE", "AMPOLLA DI SOLUZIONE FISIOLOGICA", "ATTREZZI PER IL LAVORO DI BASE", "ATTREZZI PER IL LAVORO AVANZATO", "STRUMENTI DI CALIBRAZIONE", "STRUMENTI DI RIPARAZIONE EQUIPAGGIAMENTO", "PIASTRE BALISTICHE TIPO II", "PIASTRE BALISTICHE TIPO III", "PIASTRE BALISTICHE TIPO IV", "BARATTOLO DI ANTIDOLORIFICI", "BARATTOLO DI AMOXICILLINA", "CONFEZIONE DI AMFETAMINA AD USO MEDICO", "BARATTOLO DI VITAMINE"]

def random_obj_generator():
    return [random.choice(items) for _ in range(5)]

    # Genera i nostri 5 oggetti casuali
def generate_and_save_qr_code():
    object_result_random = random_obj_generator()
    print("Oggetti ottenuti:", object_result_random)

    # genera un id unico, in modo tale che i qr code siano identificabili da un timestamp
    unique_id = str(int(time.time()))

    # Genera il QR code
    qr = qrcode.QRCode(
        version=1,
        error_correction=qrcode.constants.ERROR_CORRECT_L,
        box_size=10,
        border=4,
    )
    qr.add_data(", ".join(object_result_random))
    qr.make(fit=True)
    img = qr.make_image(fill_color="black", back_color="white")
    img.save(f"Tarkov_game_random_obj_{unique_id}.png")

# genera e salva il nostro qr code
generate_and_save_qr_code()


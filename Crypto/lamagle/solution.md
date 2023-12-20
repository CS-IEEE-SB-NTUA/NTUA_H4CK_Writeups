Κάποιες πρώτες παρατηρήσεις που προκύπτουν από την ανάλυση του αρχείου `source.py` του challenge:
- Πρόκειται για challenge που σχετίζεται με το κρυπτοσύστημα [ElGamal](https://en.wikipedia.org/wiki/ElGamal_encryption).
- Η τυχαιότητα που χρείαζεται το encryption στο ElGamal, αντί να είναι καινούρια κάθε φορά, προκύπτει από την προηγούμενη τυχαιότητα με right shift 8 bits.
- Το πρώτο μήνυμα που κρυπτογραφείται είναι το flag.
- Στη συνέχεια κρυπτογραφούνται τυχαία μηνύματα μήκους 30 χαρακτήρων μέχρις ότου η τυχαιότητα μηδενιστεί(λόγω το right shifts, με κάθε encryption η τυχαιότητα μειώνεται)
- Δε δίνονται ολόκληρα τα ciphertexts `(c1, c2)` αλλά μόνο τα `c2`

Συνοπτικά(και με αρκετές απλουστεύσεις, περισσότερες λεπτομέρειες στο wikipedia link), στο ElGamal υπάρχει ένας δημόσιος πρώτος αριθμός `p`, ένας δημόσιος αριθμός `g`, και το δημόσιο κλειδί `h` ενώ παράλληλα, ο νόμιμος παραλήπτης έχει και ένα ιδιωτικό κλειδί `x` για το οποίο ισχύει: $$g^x \equiv h \\\\(mod \\\\ p)$$.\
Όταν κάποιος θέλει να κρυπτογραφήσει ένα μήνυμα `m` με κάποιο δημόσιο κλειδί του αλγορίθμου ElGamal κάνει τα εξής:
- Επιλέγει τυχαίο αριθμό `y`.
- Υπολογίζει το `c1 = g^y % p`.
- Υπολογίζει το "shared secret" `s = h^y % p`.
- Τέλος, βρίσκει το `c2 = m*s % p`.
- Το ciphertext θα είναι το tuple `(c1, c2)`.

Στο συγκεκριμένο challenge όπως αναφέρθηκε δεν έχουμε καν τα `c1` οπότε καταλαβαίνουμε ότι θα χρειαστεί να παίξουμε με τη σχέση `c2 = m*s % p`. Πιο συγκεκριμένα, έχουμε τα `c2` αν είχαμε κάποιο τρόπο να βρούμε και τα `s` μπορούμε απλα να πολλαπλασιάσουμε με τον ανίστροφο του `s` και να πάρουμε το `m = c2 * s^(-1) % p`.\
\
Ας δούμε τι ισχύει για το τελευταίο μήνυμα:
- Το randomness `y` μειώνεται κατα 8 bits με κάθε encryption μέχρι να γίνει 0, οπότε στο τελευταίο μήνυμα θα έχει μήκος **ακριβώς** 8 bits.
- Το `s` για το τελευταίο μήνυμα προκύπτει από αυτό το 8-bit `y`
- Τα 8 bits είναι λίγα(aka bruteforcable) οπότε μπορούμε να δοκιμάσουμε όλους τους συνδυασμούς μέχρι να βρούμε το σωστό `y` και κατ'επέκταση το σωστό `s`. 

Πώς όμως θα ελέγξουμε ότι έχουμε βρει το σωστό `s`; Μπορούμε απλά να κάνουμε την πράξη `m = c2 * s^(-1) % p` για όλα τα `s` και καθώς ξέρουμε ότι το `m` έχει μήκος ακριβως 30 και αποτελείται από printable χαρακτήρες μονο, το σωστό `s` θα είναι αυτό που θα δώσει `m` που πληρεί αυτές τις προϋποθέσεις!\
\
Τους παραπάνω ελέγχους μπορούμε έυκολα να τους κάνουμε χρησιμοποιώντας τη συνάρτηση `isPrintable()` από το ακόλουθο τμήμα κώδικα python:
```python
from Crypto.Util.number import *
from string import ascii_letters, digits

ALPHABET = ascii_letters + digits
ALPHABET = [ord(char) for char in ALPHABET]

def isPrintable(num):
    msg = long_to_bytes(num)
    if len(msg) != 30:
        return False
    for b in msg:
        if b not in ALPHABET:
            return False
    return True
```
Ωραία, τώρα έχουμε το τελευταίο μήνυμα καθώς και το 8-bit `y` που χρησιμοποιήθηκε για το encryption του. Πως από αυτά θα κάνουμε decrypt το flag;\
\
Αρκεί να ρίξουμε μια ματιά στο τι συμβαίνει για το encryption του *προ*-τελευταίου μηνύματος και η ιδέα θα φανεί. Για το προτελευταίο μήνυμα το `y'` που χρησιμοποιήθηκε είναι `y' = (y << 8) + 8_unknown_bits`, όπου `y` το `y` που βρήκαμε για το τελευταίο μήνυμα! Αυτό σημβαίνει επειδη από κάθε `y` στο επόμενο κάνουμε ένα right shift 8 bits, και χάνονται αυτα τα τελευταια `8_unknown_bits` οπότε για να ανακτήσουμε το προηγούμενο `y'` από το `y` πρέπει να βρούμε αυτα τα 8 bits.\
\
Όπως αναφέραμε και πριν όμως, 8 bits είναι πολύ λίγα οπότε μπορούμε απλά να δοκιμάσουμε όλους τους συνδυασμούς μέχρι πάλι το *προ*-τελευταίο `c2` να γίνει decrypt με σωστό τρόπο και να βρεθεί κατάλληλο `m` για το οποίο η `isPrintable()` θα επιστρέψει `True`. Κάνοντας αυτή τη διαδικασία θα ανακτήσουμε 8 ακόμα bits του αρχικού randomness!\
\
Αρκεί να το επαναλάβουμε αυτό για όλα τα μηνύματα και θα βρούμε το `y` που χρησιμοποιήθηκε για το flag πέρα από τα τελευταία 8 bits. Ξανά, δοκιμάζουμε όλους τους συνδυασμούς μέχρι να βρεθεί το σωστό flag(το ελέγχουμε χρησιμοποιώντας το flag format).\
\
Full solver:
```python
from Crypto.Util.number import *
from string import ascii_letters, digits

ALPHABET = ascii_letters + digits
ALPHABET = [ord(char) for char in ALPHABET]

def isPrintable(num):
    msg = long_to_bytes(num)
    if len(msg) != 30:
        return False
    for b in msg:
        if b not in ALPHABET:
            return False
    return True

with open("output.txt", "r") as f:
    flag_enc = eval(f.readline().strip())
    pubkey = eval(f.readline().strip())
    c2s = eval(f.readline().strip())

p, q, g, h = pubkey

y = 0
for c in c2s[::-1]:
    shifted_y = y * 2**8
    for ynewbits in range(2**8):
        if isPrintable(c * pow(h, -(shifted_y + ynewbits), p) % p):
            print(long_to_bytes(c * pow(h, -(shifted_y + ynewbits), p) % p))
            y = shifted_y + ynewbits
            break
    else:
        print("error")

y = y * 2**8
for i in range(2**8):
    y_final = y + i
    flag = long_to_bytes(flag_enc[1] * pow(h, -y_final, p) % p)
    if b"NH4CK" in flag:
        print(flag)

```

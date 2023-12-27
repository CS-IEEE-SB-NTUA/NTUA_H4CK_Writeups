Μας δίνεται ένα windows executable αρχείο. Δοκιμάζοντας την IDA βλέπουμε ότι δεν μπορεί να το κάνει decompile καθώς όπως αναγράφει πρόκειται για `.NET` assembly οπότε μάλλον πρόκειται για `C#` πρόγραμμα. Το εργαλείο που θα μας βοηθήσει για το decompilation ενός τέτοιου executable είναι το [dnSpy](https://github.com/dnSpy/dnSpy/releases).\
\
Πράγματι, ανοίγοντας το αρχείο με το dnSpy, μπορούμε επιτυχώς να το κάνουμε decompile. Ψάχνοντας λίγο μέσα στο πρόγραμμα βρίσκουμε αυτή τη συνάρητησ που φαίνεται ιδιαίτερου ενδιαφέροντος:
![](https://github.com/Babafaba/NTUA_H4CK_crypto_challs/blob/main/writeups_for_challs_by_other_authors/Windows%20Rev/windows_dnspy_1.png)
![](https://github.com/Babafaba/NTUA_H4CK_crypto_challs/blob/main/writeups_for_challs_by_other_authors/Windows%20Rev/windows_dnspy_2.png)

Και μόνο από το decompiled κώδικα μπορούμε να πάρουμε μια αρκετά καλή ιδέα του τι κάνει το πρόγραμμα. Για να μην παιδευόμαστε όμως, μπορούμε να τρέξουμε το πρόγραμμα για να δούμε τι συμβαίνει και να κάνουμε πιο έυκολη την κατανόηση του στεγνού κώδικα.\
![](https://github.com/Babafaba/NTUA_H4CK_crypto_challs/blob/main/writeups_for_challs_by_other_authors/Windows%20Rev/windows_img_1.png)
Παρατηρώντας τον κώδικα αλλά και βλέποντας τι γίνεται κατά την εκτέλεση του συμπεραίνουμε ότι:
- Το πρόγραμμα μας πετάει 16 παράθυρα στα οποία μπορούμε να απαντήσουμε με `"Yes"` ή `"No"`.
- Οι απαντήσεις μας αποθηκεύονται σε ένα array με bytes(θα δούμε σε λίγο σε ποιο byte αντιστοιχούν τα `"Yes"` και `"No"`).
- Ελέγχεται αν το base64 encoding του MD5 hash του array είναι ίσο με την τιμή `"MzvpdyERG+esD0ekN2wAYg=="`. Αν όχι, τότε παίρνουμε το error message `"I'm sorry, Dave. I’m afraid I can’t do that"` και το πρόγραμμα κάνει exit.
- Αν όμως είναι ίσα τότε τα bytes `"9da249b7dffd91e8d0e0d26bb3def4e017ee1fb670d3efefc3635d887ab37a1ca36daced32d4429461cd186e67468500"` γίνονται decrypt με AES-CBC, με κλειδί το array μας και IV ένα άλλο array από bytes το οποίο είναι hardcoded στο πρόγραμμα και φαίνεται στα παραπάνω screenshots. Έπειτα, τυπώνεται το αποτέλεσμα του decryption.

Από αυτές τις παρατηρήσεις μπορούμε εύκολα να υποθέσουμε ότι το hexstring είναι το encrypted flag και αν δώσουμε το κατάλληλο input στο πρόγραμμα απαντώντας σωστά στα Message Boxes τότε αυτό θα γίνει decrypt και θα τυπωθεί!\
\
Για να βρούμε τις κατάλληλες απαντήσεις χρειάζεται να βρούμε πρώτα ακριβώς τι αποθηκεύεται στο array αναλόγως την απάντηση μας. Ο πρώτος τρόπος είναι να googlάρουμε το `.NET` documentation και να βρούμε ότι οι standard απαντήσεις των κλάσσεων MessageBox αντιστοιχούν σε συγκεκριμένες τιμές, σύμφωνα με το documentation της DialogResult που φαίνεται [εδώ](https://learn.microsoft.com/en-us/dotnet/api/system.windows.forms.dialogresult?view=windowsdesktop-8.0). Από τον πίνακα στο link φαίνεται ότι το `"Yes"` αντιστοιχεί στην τιμή 6 ενώ το `"No"` στην τιμή 7. Ο δεύτερος τρόπος είναι απλά να πατήσουμε στο `MessageBox` στο dnSpy και εκείνο θα κάνει decompile την κλάση αποκαλύπτοντας όλα της τα μυστικά:
![](https://github.com/Babafaba/NTUA_H4CK_crypto_challs/blob/main/writeups_for_challs_by_other_authors/Windows%20Rev/windows_dnspy_3.png)

Τέλεια, το dnSpy επιβεβαιώνει την αντιστοιχία `"Yes"` -> 6, `"No"` -> 7. Ξέρουμε επίσης ότι το array μήκους 16 με τις σωστές απαντήσεις(δηλαδή με 6αρια και 7αρια στις κατάλληλες θέσεις) αν γίνει hash με MD5 και έπειτα base64 encode θα δώσει μια συγκεριμένη γνωστή τιμή. Όλα τα πιθανά τέτοια arrays είναι μόλις `2**16 = 65536`. Μπορούμε λοιπόν απλά να δοκιμάσουμε **όλους** τους πιθανούς συνδυασμούς μέχρι να βρούμε εκείνον με το σωστό hash!\
Python script που κανει αυτό το mini bruteforce:
```python
from hashlib import md5
from base64 import b64decode

target = b64decode("MzvpdyERG+esD0ekN2wAYg==")
for i in range(2**16):
    bits = [int(b) for b in f'{i:016b}']
    answers = [6 + j for j in bits]
    hash = md5(bytes(answers)).digest()
    if hash == target:
        print(["No" if b else "Yes" for b in bits])
        break
```
Τρέχοντας το script παίρνουμε το output `['Yes', 'Yes', 'Yes', 'No', 'Yes', 'No', 'No', 'Yes', 'No', 'Yes', 'Yes', 'Yes', 'No', 'No', 'No', 'Yes']` το οποίο μπορούμε να δώσουμε στο πρόγραμμα για να πάρουμε το flag!
![](https://github.com/Babafaba/NTUA_H4CK_crypto_challs/blob/main/writeups_for_challs_by_other_authors/Windows%20Rev/windows_flag.png)

**Σημείωση**: εφόσον έχουμε το IV καθώς και το ciphertext, αφού βρούμε το κλειδί με το mini bruteforce, μπορούμε να κάνουμε μόνοι μας το decryption. Έχει περισσότερη πλάκα όμως να δώσουμε τις σωστές απαντήσεις στο πρόγραμμα για να το κάνει αυτό για εμάς ;)



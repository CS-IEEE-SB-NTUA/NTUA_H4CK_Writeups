# Description

A Dangerous virus is spreading and invading more and more cities around the world. An unknown specimen is located near Greece, but we do not know the name of the specimen so we can neutralise it. Some people say the virus can be transmited by animals such as exotic birds. Can you find its name and save the planet?

Flag Format NH4CK{******}

![img](https://github.com/Babafaba/NTUA_H4CK_crypto_challs/assets/94315580/bd7362ba-8679-41ee-bcc2-0dc7a809d769)

Hint: You are looking for the name of the virus. NOT the name OR the species of the bird carrying the virus. Try to find how the bird got there (or by whom). When you find the virus you will know.

Author: SeekerRook

# Flag

NH4CK{IST_18}

# Solution

Στην εικόνα μπορούμε να δούμε τμήμα μιας οδού: "DE LA HUCHETTE"

Ύστερα από λίγο googling, βρίσκουμε ότι η οδός πρόκειται για την `Rue de la Huchette` του Παρισιού.
Στο Street View, βρίσκουμε το εστιατόριο της φωτογραφίας.

![εικόνα](https://github.com/Babafaba/NTUA_H4CK_crypto_challs/assets/94315580/88944e5c-a639-4907-8bfb-48b527fa8cf5)

Αμέσως μας κεντρίζει το ενδιαφέρον η εικόνα του pixel πιγκουίνου (Η περιγραφή μιλούσε για "exotic birds"). Κάνοντας reverse image search στην εικόνα μέσω google lens και κλικάροντας στο πρώτο αποτέλεσμα:

![εικόνα](https://github.com/Babafaba/NTUA_H4CK_crypto_challs/assets/94315580/bdcb4348-681a-4662-8dde-d35896b29677)

μαθαίνουμε ότι ο δημιουργός του πιγκουίνου ονομάζεται (Space) Invader:

![εικόνα](https://github.com/Babafaba/NTUA_H4CK_crypto_challs/assets/94315580/74bfc91b-6acc-4744-b265-5951e51aa277)

Αναζητώντας τον στο google με keywords Space Invader Artist, οδηγούμαστε στην official ιστοσελίδα του Invader: [https://www.space-invaders.com/home/](https://www.space-invaders.com/home/)

Στην καρτέλα World Invasion βλέπουμε ότι ο πιο κοντινός 'στόχος' του καλλιτέχνη είναι η Κωνσταντινούπολη:

![εικόνα](https://github.com/Babafaba/NTUA_H4CK_crypto_challs/assets/94315580/a500db26-e4ef-43d1-ab30-3889724219ea)

Κλικάρουμε πάνω στον ιό και βλέπουμε έναν δρόμο στην Κωνσταντινούπολη, και σε έναν τοίχο το pixel art VIRUS του Invader. Bingo!!

![εικόνα](https://github.com/Babafaba/NTUA_H4CK_crypto_challs/assets/94315580/2c57bf1e-996e-4e91-bcf1-3a14c206b159)

Παρατηρούμε ότι όλα τα υπόλοιπα έργα στη συγκεκριμένη σελίδα έχουν ένα ξεχωριστό κωδικο (πχ PA_08, IST_12) που αντιστοιχεί στο όνομα του έργου. 
![εικόνα](https://github.com/Babafaba/NTUA_H4CK_crypto_challs/assets/68130661/4014e718-ea61-4782-93db-d4985403cfba)


Για να βρούμε το 'όνομα' του ιού(δηλαδή το όνομα του έργου, το οποίο όμως δεν φαίνεται στη σελίδα καθότι αποτελεί πρωτη εικόνα για τη συγκεκριμένη πόλη), κοιτάμε το όνομα της εικόνας (π.χ. με επιθεώρηση στοιχείου). Η εικόνα έχει όνομα:
`IST_18_b_wuRJgBn.jpg`, από όπου παίρνουμε ότι το όνομα του ιού είναι IST_18.
![εικόνα](https://github.com/Babafaba/NTUA_H4CK_crypto_challs/assets/68130661/82570ad5-924f-4bbf-919d-3da4e578239d)





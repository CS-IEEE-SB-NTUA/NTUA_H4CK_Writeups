# Description

The Christmas Holidays are approaching. Who would expect that you would be eager to leave your dream job as a penetration tester!
However there is one more task in your list One task you know your job will not be happy if you postpone till after  Christmas.

You have been assigned to perform a security assesment for the work accounts of the employees of SRVSL  LTD.

The last person on your list is "**Leonidas  Kalogirakidis**". 
Will you pull off this hack before Christmas?

The Company Service is running on the following URL below.

<!-- Screenshot of service -->

Flag: `NH4CK{T4k3_C@r3_0f_Wh47_U_P0$T} `

# Solution
Όπως φαίνεται από την ιστοσελίδα της εταιρίας χρειαζόμαστε
- το email του στόχου
- ενα 4ψήφιο pin (το οποίο μιας και το challenge χαρακτηρίζεται ως OSINT υποθέτουμε ότι πιθανότατα προκειτε για ημερομηνία)
- το όνομα ενός κατοικιδίου.

Αρχικά ψάχνουμε το όνομα του στόχου σε μηχανες αναζήτησης\* και μέσα κοινωνικής δικτύωσης. 
Εντοπίζουμε τον λογαριασμό Facebook [https://www.facebook.com/profile.php?id=61554836484306](https://www.facebook.com/profile.php?id=61554836484306)

Από τον παραπάνω λογαριασμό μπορούμε να εξάγουμε 
- 3 πιθανές ημερομηνίες (1968,1986,1990,2009,2015) τις οποίες μπορύμε να δοκιμάσουμε αφού βρούμε τα υπόλοιπα στοιχεία
- Ενα url για τον λογαριασμό gitlab [https://gitlab.com/QuirkMuffin](https://gitlab.com/QuirkMuffin)

Ακολουθόντας το url οδηγούμαστε σε ένα λογαριασμό gitlab που φαίνεται οτι ανοικει στον στόχο, αλλά χρησιμοποιεί σαν username το ψευδώνυμο "**QuirkMuffin**". 
με περιγραφή 
```
Full Time Project Specialist at SRVSL LTD, Part TIme Gamer, Youtuber and Linux enthusiast 
``` 

Παρατηρώντας το προφίλ βλέπουμε ότι το μονο prοject στο οποίο έχουμε πρόσβαση είναι ένα project με όνομα Stealth.

Πατώντας το συγκεκριμένο Project βλέπουμε ότι πρόκειτε για fork ενός Reddit Client. Μάλιστα παρατηρούμε ότι στην περιγραφή του project αναφέρει το εξής 
```
I want to implement a custom search for reddit on the top of the default one, that will allow new user profiles to show. The basic idea is that it will search for the following url: https://www.reddit.com/user/username/ and add the result on the search results. No pattern matching at the moment.
```
Το οποίο δεν υπάρχει στο original project. 


Απο τα παραπάνω μπορούμε να εξάγουμε τα εξής:

- το email του στόχου είναι leonidaskalogirakidis@gmail.com
- Ο στόχος είναι πιθανότατα χρήστης του reddit
- Ο στόχος χρησιμοποιεί το ψευδώνυμο QuirkMuffin
- Ο στόχος ασχολείτε τόσο με Gaming όσο και με Linux
- Στην πλατφόρμα του reddit, οι λογαριασμοι νέων χρηστών δεν εμφανίζονται στην αναζήτηση, αλλά μπορούν να εμφανιστούν αντικαθιστώντας το username στο url `https://www.reddit.com/user/username/`

Πράγματι στο reddit αναζητώντας τοσο Leonidas Kalogirakidis όσο και QuirkMuffin δεν εμφανίζονται αποτελέσματα. Όμως αν πλοηγηθούμε στη διέυθυνση [https://www.reddit.com/user/QuirkMuffin](https://www.reddit.com/user/QuirkMuffin) εμφανίζεται ένα προφίλ χρήστη, στο οποίο υπάρχει ένα μονο post, σχετικά με την εγκατάσταση κατάλληλης διανόμης Linux σε συγκεκριμένο Gaming Laptop, για το οποίο υπάρχει σύνδεσμος στην πλατφόρμα αγορών [skroutz](https://www.skroutz.gr/s/42799863/MSI-Cyborg-15-A12VF-271XPL-15-6-FHD-144Hz-i7-12650H-16GB-512GB-SSD-GeForce-RTX-4060-No-OS-US-Keyboard.html).
Από αυτα συμπαιρένουμε ότι:
- Ο λογαριασμός ανήκει πιθανότατα στον στόχο (ίδιο username, παρόμοια ενδιαφέροντα)
- Ο στόχος πιθανότατα αγόρασε πρόσφατα το συγκεκριμένο Laptop από την πλατφόρμα skroutz.

Ακολουθώντας τον σύνδεσμο στο post οδηγούμαστε στην σελίδα του προϊόντος. Στης αξιολογήσεις βλέπουμε μία μόνο αξιολόγηση από χρήστη με username QuirkMuffin

Πατώντας το όνομα στην κεφαλίδα της αξιολόγησης οδηγούμαστε στο προσωπικό προφίλ του χρήστη ([https://www.skroutz.gr/u/QuirkMuffin/](https://www.skroutz.gr/u/QuirkMuffin/)). Εκεί μπορούμε να δούμε όλες τις αξιολογήσεις που έχει κάνει ο συγκεκριμένος χρήστης, Μεταξύ των οποίων βρίσκεται και η εξής αξιολόγηση για ρούχο που προορίζεται για κατοικίδια:

```
# ΟΛΟΣΩΜΟ ΡΟΥΧΟ ΧΡΙΣΤΟΥΓΕΝΝΙΑΤΙΚΟ-medium

Πήρα ένα τέτοιο φορμάκι για τον Winston μου και είναι υπέροχο.
Εξαιρετική ποιότητα και υφή!
Πάει και κάθεται διαρκώς δίπλα στο χριστουγεννιάτικο δέντρο και είναι πολύ ταιριαστοί.
```

από το παραπάνω μπορούμε να συμπεράνουμε ότι:
- ο στόχος έχει κατοικίδιο με το όνομα **Winston**.

Παρατηρούμε ότι πλέον έχουμε αρκετά στοιχεία για να δοκιμάσουμε συνδιασμούς κωδικών.

Δοκιμάζοντας τον συνδιασμό `leonidaskalogirakidis@gmail.com | 1968 | Winston` παίρνουμε πρόσβαση στον λογαριασμό του στόχου.

*\*Σημείωση: Αναζητώντας το όνομα του χρήστη στο google βρίσκουμε ένα λογαριασμό στο YouTube μέ ένα βίντεο μίας γάτας. Το συγκεκριμένο βίντεο πράγματι συνδέεται με τον στόχο (εξ άλλου γνωρίζουμε ότι έχει κατοικίδιο και ότι θεωρεί τον εαυτό του part-time Youtuber), παρόλα αυτά δεν μας βοηθά στην επίλυση του challenge.
*




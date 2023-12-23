Αρχικά ελέγχουμε τα mitigations του εκτελέσιμου.\
![image](https://github.com/Babafaba/NTUA_H4CK_crypto_challs/assets/56980206/996f27da-9b12-4f7e-8e0f-3c3f408334ca)

Παρατηρούμε πως το binary έχει γίνει compiled χωρίς canary αλλά με Pie και Partial Relero. Από αυτά, εν τέλει δε θα μας χρειαστεί κάτι.\

Ανοίγουμε το δοσμένο binary με Ghidra (ωωωωω ναι!!). Βλέπουμε πως αποτελείται μόνο από τη συνάρτηση `main` η οποία παρουσιάζεται κάτωθι.

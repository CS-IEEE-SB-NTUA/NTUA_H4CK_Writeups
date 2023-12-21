Μας δίνεται ένα `.pyc` αρχείο και ενα netcat connection. Επιπλέον, στην περιγραφή γίνεται αναφορά σε κάτι που λέγεται `pycdc` και ίσως βοηθήσει.\
Έπειτα από λίγο googling(ή ίσως το ξέραμε ήδη) βρίσκουμε ότι τα `.pyc` αρχεία περιέχουν compiled Python κώδικα. Το pycdc είναι ενα εργαλείο που (προσπαθεί να) κάνει decompile τα `.pyc` πίσω σε απλά `.py` αρχεία τα οποία είναι σαφώς πιο κατανοητά από εμάς. \
\
Αφού εγκαταστήσουμε σωστά το `pycdc` από [εδώ](https://github.com/zrax/pycdc), τρέχουμε την εντολή ` ./pycdc <path to weird_game.pyc>`. Το output είναι ένας εύκολα κατανοητός python κωδικας!
```python
# Source Generated with Decompyle++
# File: weird_game.pyc (Python 3.8)

import random
import numpy as np
a = np.empty(225)

def fa():
    v = np.where(a.sum(1, **('axis',)) == 15, 1, 0)
    h = np.where(a.sum(0, **('axis',)) == 15, 1, 0)
    d = np.where(np.sum(np.trace(a, int, **('dtype',))) == 15, 1, 0)
    sd = np.where(np.sum(np.diag(np.fliplr(a))) == 15, 1, 0)
    if v.any() and h.any() and d.any() or sd.any():
        return 1


def fb():
    a.shape = (15, 15)
    if fa():
        return 0
    v = None.where(a.sum(1, **('axis',)) == 14, 1, 0)
    h = np.where(a.sum(0, **('axis',)) == 14, 1, 0)
    d = np.where(np.sum(np.trace(a, int, **('dtype',))) == 14, 1, 0)
    sd = np.where(np.sum(np.diag(np.fliplr(a))) == 14, 1, 0)
    if v.any() and h.any() and d.any() or sd.any():
        return 1


def fc():
    a.shape = 225
    a.fill(0)
    for i in range(196):
        a[random.randint(0, 224)] = 1
    if fb():
        a.shape = 225
        print(a)
        return None


def fd(m):
    a[m] = 1
    a.shape = (15, 15)
    return fa()

for i in range(20):
    fc()
    r = []
    m = int(input())
    if m > 224:
        exit()
    if not fd(m):
        exit()
    r.append(m)
f = open('flag.txt', 'r').read()
print(f)
```
**Σημείωση**: στην πορεία του CTF δόθηκε για βοήθεια το αρχικό source πριν γίνει compile, αν κάποιος δει αυτό το αρχείο, θα παρατηρήσει κάποιες μικροδιαφορές από το output του `pycdc`. Αυτό είναι λογικό αφού το `pycdc` δεν είναι τέλειο, κάνει όμως αρκετά καλή δουλεία ώστε να μπορεί κάποιος να καταλάβει τι κάνει το πρόγραμμα. \
\
Παρατηρούμε στο τέλος του προγράμματος ότι το flag θα τυπωθεί μόνο του. Αρκεί να δώσουμε κατάλληλο input ώστε να αποφύγουμε τα `if` statements που κάνουν το πρόγραμμα να κάνει `exit()`. Ώρα να κανουμε reverse το πρόγραμμα για αν βρούμε το σωστό input.\
\
Από μια σύνδεση μέσω netcat βλέπουμε ότι το μας δίνεται ένας μονοδιάστατος πίνακας με 225 στοιχεία, είτε άσσους είτε μηδέν. Μια σύντομη ανάλυση του decompiled κώδικα το επιβεβαιώνει αυτό, αλλά επιπλέον αποκαλύπτει ότι πολλά από τα operations που εκτελεί το πρόγραμμα σε αυτόν τον πίνακα απαιτεί αυτος να μετατραπεί πρώτα σε δισδιάστατο 15χ15 πίνακα.\
\
Αρχικά καλείται η συνάρτηση `fc()` η οποία φαίνεται να αρχικοποιεί τον πίνακα με ακριβώς 196 άσσους σε τυχαίες θέσεις. Έπειτα, καλούνται οι συναρτήσεις `fb(), fa()`(η `fa()` καλείται από την `fb()`) οι οποίες μετατρέπουν τον πίνακα σε 15χ15 και φαίνεται να πραγματοποιούν 2 ελέγχους. Η `fa()` ελέγχει ότι καμία στήλη, γραμμή ή διαγώνιος δεν έχει άθροισμα 15, οπότε αφού όλα τα στοιχεία είναι 0 ή 1 και έχουμε 15χ15 πίνακα ουσιαστικά ελέγχει οτί καμια στήλη, γραμμή ή διαγώνιος δεν είναι **όλη** γεμάτη με άσσους. Η `fb()` ελέγχει αντίστοιχα ότι οι στήλες, γραμμές και διαγώνιοι του πίνακα έχουν άθροισμα 14. Υπάρχει μια περιέργη ασυνέπεια με τη χρήση or/and στο τελικό `if` statement των `fa(), fb()` αλλά μπορούμε να το αποδώσουμε στο κακό decompilation του `pycdc`\
\
Έπειτα, δίνουμε ένα input μικρότερο από 225 και καλείται η συνάρτηση `fd()` με όρισμα το input που δώσαμε. Η `fd()` θα τοποθετήσει έναν άσσο στο index του πίνακα ίσο με το input `m` και στη συνέχεια θα χρησιμοποιήσει την `fa()` για να ελέγξει ότι αυτή τη φορά **υπάρχει** στήλη, γραμμή ή διαγώνιος με άθροισμα 15.\
\
Από τα παραπάνω καταλαβαίνουμε ότι ουσιαστικά μας δίνεται ένας πίνακας 15χ15 που έχει δεν έχει καμία ολοκλήρωμενη(δλδ γεμάτη άσσους) στήλη/γραμμή/διαγώνιο και εμείς χρειάζεται να βρούμε το index στο οποίο αν βάλουμε έναν άσσο, η γραμμή/στήλη/διαγώνιος θα ολοκληρωθεί. Είναι λοιπόν μια περίεργη εκδοχή της τρίλιζας σε 15χ15 ταμπλό, την οποία πρέπει να νικήσουμε!\
\
**Σημείωση**: Άλλο ένα σημείο στο οποίο φαίνεται το κακό decompilation του `pycdc` είναι στο ότι αν ο τυχαίος τρόπος με τον οποίο αρχικοποιεί η `fc()` τον πίνακα **δεν** περάσει τα checks, φαίνεται(στο δικό μου decompilation, ίσως σε εσάς διαφέρει) ότι απλά θα τυπωθεί ο "λάθος" πίνακας κανονικά ο οποίος μπορεί πιθανώς να είναι ήδη "νικητήριος" ανεξάρτητα από δικό μας input. Προφανώς κάτι τέτοιο δεν ισχύει όπως μπορούμε εύκολα να ελέγξουμε με μερικές συνδέσεις στο netcat, το κανονικό `.py` source έχει ένα `while` loop που εγγυάται τη σωστή αρχικοποιήση του πίνακα. Παρά την ελλειπή πληροφορία βέβαια, το υπόλοιπο πρόγραμμα καθώς και το netcat, συμπληρώνουν την εικόνα, ξεκαθαρίζοντας πως δουλεύει το πρόγραμμα.\
\
Τώρα που έχουμε κατανοήσει το ζητούμενο, το reverse engineering έχει τελειώσει. Μένει απλά να γράψουμε έναν αυτοματοποιημένο solver που θα parsaρει τον πίνακα και θα βρίσκει που πρέπει να τοποθετηθεί ο άσσος ώστε να νικήσουμε στην "τρίλιζα".\
\
Solver:
```python
from pwn import *

ip = "0.cloud.chals.io"
port = 27764

def find_sol(arrstr):
    arr = eval(arrstr.replace(".", ","))
    block_arr = [[arr[15*i + j] for j in range(15)] for i in range(15)]
    diag1 = [block_arr[i][i] for i in range(15)]
    diagsum = sum(diag1)
    if diagsum == 14:
        diag1 = [block_arr[i][i] for i in range(15)]
        for i in range(15):
            if diag1[i] == 0:
                return i, i

    diag2 = [block_arr[i][14 - i] for i in range(15)]
    diagsum2 = sum(diag2)
    if diagsum2 == 14:
        for i in range(15):
            if diag2[i] == 0:
                return i, 14 - i

    for i in range(15):
        row = block_arr[i]
        col = [block_arr[k][i] for k in range(15)]
        sum1 = sum(row)
        sum2 = sum(col)
        if sum1 == 14:
            for k in range(15):
                if row[k] == 0:
                    return i, k
        elif sum2 == 14:
            for k in range(15):
                if col[k] == 0:
                    return k, i
    for i in range(15):
        print(block_arr[i])


def find_num(i, j):
    return 15*i + j

def assemble_arr(conn):
    arr = ""
    while True:
        next_row = conn.recvline().decode().strip()
        arr += next_row
        if "]" in next_row:
            return arr

conn = remote(ip, port)
for i in range(20):
    arr = assemble_arr(conn)
    i, j = find_sol(arr)
    res = find_num(i, j)
    print(res)
    conn.sendline(str(res).encode())
flag = conn.recvline()
print(flag.decode().strip())
```


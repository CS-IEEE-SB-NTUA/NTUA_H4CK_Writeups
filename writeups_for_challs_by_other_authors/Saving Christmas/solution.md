# Saving Christmas 

Ξεκινώντας έχουμε ενα .zip αρχείο το οποίο περιέχει 2 αρχεία. Το 1ο είναι ενα Encrypted.txt και το 2ο είναι ενα Win10.raw. Προφανώς θα χρειαστεί με κάποιο τρόπο να βρούμε τον τρόπο κρυπτογράφησης του .txt για να το αποκρυπτογραφήσουμε.

Προκειμένου να αναλύσουμε το .raw αρχείο θα χρησιμοποιήσουμε το volatility3 framework το οποίο αναλύει αρχεία memory dumps.

Θα ξεκινήσουμε κοιτώντας το process tree για να δούμε τι έτρεχε την στιγμή που έγινε το memory capture.
```$ python3 ~/volatility3/vol.py -f Win10.raw windows.pstree```
``` 
Volatility 3 Framework 2.5.2
Progress:  100.00               PDB scanning finished                        
PID     PPID    ImageFileName   Offset(V)       Threads Handles SessionId       Wow64   CreateTime      ExitTime

4       0       System  0x8a05cba83040  157     -       N/A     False   2023-12-07 20:33:44.000000      N/A
* 396   4       smss.exe        0x8a05cc2d6040  2       -       N/A     False   2023-12-07 20:33:44.000000      N/A
* 140   4       Registry        0x8a05cbbd9040  4       -       N/A     False   2023-12-07 20:33:34.000000      N/A
* 1828  4       MemCompression  0x8a05ce6ce080  30      -       N/A     False   2023-12-07 20:33:51.000000      N/A
504     492     csrss.exe       0x8a05cd1d3080  11      -       0       False   2023-12-07 20:33:49.000000      N/A
580     492     wininit.exe     0x8a05cdba9080  1       -       0       False   2023-12-07 20:33:49.000000      N/A
* 744   580     lsass.exe       0x8a05ce2dd080  9       -       0       False   2023-12-07 20:33:49.000000      N/A
* 724   580     services.exe    0x8a05cdbeb080  8       -       0       False   2023-12-07 20:33:49.000000      N/A
** 1544 724     svchost.exe     0x8a05ce620300  6       -       0       False   2023-12-07 20:33:50.000000      N/A
** 2572 724     spoolsv.exe     0x8a05cea070c0  9       -       0       False   2023-12-07 20:33:51.000000      N/A
** 1552 724     svchost.exe     0x8a05ce617240  3       -       0       False   2023-12-07 20:33:50.000000      N/A
** 1560 724     svchost.exe     0x8a05ce615280  6       -       0       False   2023-12-07 20:33:50.000000      N/A
** 1056 724     svchost.exe     0x8a05ce4bf300  0       -       0       False   2023-12-07 20:33:50.000000      2023-12-07 10:37:50.000000 
** 1568 724     svchost.exe     0x8a05ce619240  3       -       0       False   2023-12-07 20:33:50.000000      N/A
** 3104 724     svchost.exe     0x8a05cec1f240  6       -       0       False   2023-12-07 20:33:52.000000      N/A
** 1584 724     svchost.exe     0x8a05ce61b2c0  7       -       0       False   2023-12-07 20:33:51.000000      N/A
** 4660 724     TrustedInstall  0x8a05cf626080  5       -       0       False   2023-12-07 10:38:27.000000      N/A
** 1080 724     svchost.exe     0x8a05ce3a1300  3       -       0       False   2023-12-07 20:33:50.000000      N/A
** 2620 724     svchost.exe     0x8a05cea0b0c0  13      -       0       False   2023-12-07 20:33:51.000000      N/A
** 4164 724     svchost.exe     0x8a05cf7a0080  7       -       1       False   2023-12-07 20:34:25.000000      N/A
** 6216 724     svchost.exe     0x8a05d423b300  8       -       0       False   2023-12-07 20:35:14.000000      N/A
** 4172 724     svchost.exe     0x8a05cf5ce2c0  14      -       0       False   2023-12-07 20:34:01.000000      N/A
** 4688 724     svchost.exe     0x8a05cf5aa080  1       -       0       False   2023-12-07 20:34:21.000000      N/A
** 9812 724     SgrmBroker.exe  0x8a05d532b080  6       -       0       False   2023-12-07 20:35:52.000000      N/A
** 88   724     svchost.exe     0x8a05ce404240  4       -       0       False   2023-12-07 20:33:50.000000      N/A
** 9820 724     svchost.exe     0x8a05ceac10c0  7       -       0       False   2023-12-07 10:44:02.000000      N/A
** 620  724     svchost.exe     0x8a05cfabd240  5       -       0       False   2023-12-07 20:34:20.000000      N/A
** 1144 724     svchost.exe     0x8a05ce442300  8       -       0       False   2023-12-07 20:33:50.000000      N/A
** 2184 724     svchost.exe     0x8a05ce93d2c0  10      -       0       False   2023-12-07 20:33:51.000000      N/A
*** 8764        2184    audiodg.exe     0x8a05cc3ab2c0  4       -       0       False   2023-12-07 10:46:22.000000      N/A
** 2696 724     svchost.exe     0x8a05ceacf300  5       -       0       False   2023-12-07 20:33:52.000000      N/A
** 5268 724     svchost.exe     0x8a05cf868080  3       -       0       False   2023-12-07 20:34:25.000000      N/A
*** 5360        5268    ctfmon.exe      0x8a05d0d522c0  12      -       1       False   2023-12-07 20:34:25.000000      N/A
** 4756 724     svchost.exe     0x8a05d0ef0280  7       -       0       False   2023-12-07 20:34:28.000000      N/A
** 1172 724     svchost.exe     0x8a05cea860c0  19      -       0       False   2023-12-07 10:48:54.000000      N/A
** 2204 724     svchost.exe     0x8a05ce94d300  4       -       0       False   2023-12-07 20:33:51.000000      N/A
** 4768 724     svchost.exe     0x8a05d4394300  1       -       0       False   2023-12-07 20:34:59.000000      N/A
** 1700 724     svchost.exe     0x8a05ce690300  1       -       0       False   2023-12-07 20:33:51.000000      N/A
** 1192 724     svchost.exe     0x8a05ce4492c0  2       -       0       False   2023-12-07 20:33:50.000000      N/A
** 5296 724     svchost.exe     0x8a05cda2a080  4       -       0       False   2023-12-07 10:47:07.000000      N/A
** 4288 724     svchost.exe     0x8a05cf5ac280  5       -       0       False   2023-12-07 20:34:01.000000      N/A
** 7888 724     svchost.exe     0x8a05d0bed300  4       -       1       False   2023-12-07 20:35:07.000000      N/A
** 1756 724     svchost.exe     0x8a05ce6d0240  2       -       0       False   2023-12-07 20:33:51.000000      N/A
** 736  724     svchost.exe     0x8a05d49e8080  8       -       0       False   2023-12-07 20:35:53.000000      N/A
** 1772 724     svchost.exe     0x8a05d0fe2340  4       -       1       False   2023-12-07 20:34:30.000000      N/A
** 7916 724     svchost.exe     0x8a05d472d240  0       -       0       False   2023-12-07 20:34:39.000000      2023-12-07 10:36:41.000000 
** 2292 724     svchost.exe     0x8a05ce9cd300  10      -       0       False   2023-12-07 20:33:51.000000      N/A
** 1272 724     svchost.exe     0x8a05ce42f2c0  4       -       0       False   2023-12-07 20:33:50.000000      N/A
** 2812 724     svchost.exe     0x8a05ceac4080  17      -       0       False   2023-12-07 20:33:52.000000      N/A
** 2824 724     svchost.exe     0x8a05ceb5d240  13      -       0       False   2023-12-07 20:33:52.000000      N/A
** 4880 724     svchost.exe     0x8a05d08d12c0  3       -       0       False   2023-12-07 20:34:19.000000      N/A
** 2836 724     svchost.exe     0x8a05ceb5f300  5       -       0       False   2023-12-07 20:33:52.000000      N/A
** 3868 724     svchost.exe     0x8a05cfbe7340  7       -       1       False   2023-12-07 20:34:25.000000      N/A
** 2336 724     svchost.exe     0x8a05ce9df2c0  4       -       0       False   2023-12-07 20:33:51.000000      N/A
** 3880 724     svchost.exe     0x8a05cefda0c0  5       -       0       False   2023-12-07 20:33:57.000000      N/A
** 2352 724     svchost.exe     0x8a05cea03080  7       -       0       False   2023-12-07 20:33:51.000000      N/A
** 2868 724     svchost.exe     0x8a05ceb9c280  3       -       0       False   2023-12-07 20:33:52.000000      N/A
** 2876 724     svchost.exe     0x8a05ceb61240  16      -       0       False   2023-12-07 20:33:52.000000      N/A
** 5948 724     svchost.exe     0x8a05d0f5c240  3       -       0       False   2023-12-07 20:34:27.000000      N/A
** 1344 724     svchost.exe     0x8a05ce535240  5       -       0       False   2023-12-07 20:33:50.000000      N/A
** 2376 724     svchost.exe     0x8a05cecd3240  5       -       0       False   2023-12-07 20:33:52.000000      N/A
** 2896 724     svchost.exe     0x8a05ceb9a0c0  7       -       0       False   2023-12-07 20:33:52.000000      N/A
** 5968 724     SearchIndexer.  0x8a05d08bd2c0  14      -       0       False   2023-12-07 20:34:31.000000      N/A
*** 9840        5968    SearchProtocol  0x8a05d533d080  3       -       1       False   2023-12-07 10:46:42.000000      N/A
*** 6068        5968    SearchFilterHo  0x8a05d5337080  4       -       0       False   2023-12-07 10:46:42.000000      N/A
*** 9592        5968    SearchProtocol  0x8a05d4f35080  6       -       0       False   2023-12-07 10:46:42.000000      N/A
** 1876 724     svchost.exe     0x8a05ce7622c0  9       -       0       False   2023-12-07 20:33:51.000000      N/A
** 3924 724     svchost.exe     0x8a05cf064280  2       -       0       False   2023-12-07 20:33:57.000000      N/A
** 4948 724     svchost.exe     0x8a05d089f080  2       -       0       False   2023-12-07 20:34:21.000000      N/A
** 860  724     svchost.exe     0x8a05ce4d4240  15      -       0       False   2023-12-07 20:33:49.000000      N/A
*** 4580        860     MoUsoCoreWorke  0x8a05cf63b080  13      -       0       False   2023-12-07 20:34:02.000000      N/A
**** 3960       4580    wuauclt.exe     0x8a05cea770c0  5       -       0       False   2023-12-07 10:39:33.000000      N/A
*** 8100        860     HxTsr.exe       0x8a05d41f4300  0       -       1       False   2023-12-07 20:34:59.000000      2023-12-07 20:35:16.000000 
*** 6820        860     RuntimeBroker.  0x8a05d43072c0  5       -       1       False   2023-12-07 20:35:02.000000      N/A
*** 7300        860     TextInputHost.  0x8a05d5334080  12      -       1       False   2023-12-07 10:45:25.000000      N/A
*** 10056       860     ApplicationFra  0x8a05d5188240  1       -       1       False   2023-12-07 20:35:30.000000      N/A
*** 8044        860     smartscreen.ex  0x8a05d4861340  14      -       1       False   2023-12-07 20:34:40.000000      N/A
*** 6320        860     StartMenuExper  0x8a05d4183080  6       -       1       False   2023-12-07 20:34:34.000000      N/A
*** 5328        860     RuntimeBroker.  0x8a05d45ac340  7       -       1       False   2023-12-07 20:34:36.000000      N/A
*** 7928        860     TiWorker.exe    0x8a05d4515080  6       -       0       False   2023-12-07 10:39:39.000000      N/A
*** 6740        860     SearchApp.exe   0x8a05d43ca080  37      -       1       False   2023-12-07 20:34:35.000000      N/A
*** 7768        860     dllhost.exe     0x8a05d0cf5080  7       -       1       False   2023-12-07 20:34:38.000000      N/A
*** 6524        860     RuntimeBroker.  0x8a05d43cc340  3       -       1       False   2023-12-07 20:34:34.000000      N/A
** 5476 724     svchost.exe     0x8a05d0e152c0  12      -       0       False   2023-12-07 20:34:25.000000      N/A
** 9580 724     svchost.exe     0x8a05d46f02c0  2       -       0       False   2023-12-07 20:35:24.000000      N/A
** 1392 724     svchost.exe     0x8a05ce547300  6       -       0       False   2023-12-07 20:33:50.000000      N/A
** 884  724     svchost.exe     0x8a05ce37f280  2       -       0       False   2023-12-07 20:33:50.000000      N/A
** 2420 724     svchost.exe     0x8a05ce9dd080  2       -       0       False   2023-12-07 20:33:51.000000      N/A
** 1912 724     svchost.exe     0x8a05ce818280  3       -       0       False   2023-12-07 20:33:51.000000      N/A
** 1920 724     svchost.exe     0x8a05ce81b2c0  4       -       0       False   2023-12-07 20:33:51.000000      N/A
** 2432 724     svchost.exe     0x8a05ce9dc080  3       -       0       False   2023-12-07 20:33:51.000000      N/A
** 3968 724     svchost.exe     0x8a05cf3430c0  18      -       0       False   2023-12-07 20:33:58.000000      N/A
** 6020 724     svchost.exe     0x8a05d0fa3240  3       -       0       False   2023-12-07 20:34:27.000000      N/A
** 9612 724     svchost.exe     0x8a05ccb4c080  4       -       0       False   2023-12-07 10:38:53.000000      N/A
** 3472 724     svchost.exe     0x8a05ce8a8080  30      -       0       False   2023-12-07 20:33:53.000000      N/A
** 1424 724     SecurityHealth  0x8a05cf214080  8       -       0       False   2023-12-07 20:34:00.000000      N/A
** 4524 724     svchost.exe     0x8a05cefe2080  9       -       0       False   2023-12-07 20:34:02.000000      N/A
** 2476 724     svchost.exe     0x8a05d64ce340  3       -       0       False   2023-12-07 10:41:29.000000      N/A
** 1468 724     svchost.exe     0x8a05ce587240  13      -       0       False   2023-12-07 20:33:50.000000      N/A
*** 10024       1468    taskhostw.exe   0x8a05d5341080  9       -       1       False   2023-12-07 10:48:56.000000      N/A
*** 3004        1468    taskhostw.exe   0x8a05cf7f6080  2       -       1       False   2023-12-07 10:41:29.000000      N/A
*** 2892        1468    taskhostw.exe   0x8a05cfade340  7       -       1       False   2023-12-07 20:34:25.000000      N/A
** 1988 724     svchost.exe     0x8a05ce8ad240  5       -       0       False   2023-12-07 20:33:51.000000      N/A
*** 4816        1988    sihost.exe      0x8a05cf63d080  8       -       1       False   2023-12-07 20:34:24.000000      N/A
**** 7488       4816    msedge.exe      0x8a05cce7d340  0       -       1       False   2023-12-07 20:34:55.000000      2023-12-07 20:34:56.000000 
** 976  724     svchost.exe     0x8a05ce7fb2c0  10      -       0       False   2023-12-07 20:33:50.000000      N/A
** 3028 724     svchost.exe     0x8a05cec072c0  2       -       0       False   2023-12-07 20:33:52.000000      N/A
** 2020 724     svchost.exe     0x8a05ce44a080  6       -       0       False   2023-12-07 20:34:21.000000      N/A
** 6120 724     svchost.exe     0x8a05d0fe4280  3       -       0       False   2023-12-07 20:34:28.000000      N/A
** 6636 724     MsMpEng.exe     0x8a05d532c080  43      -       0       False   2023-12-07 20:35:51.000000      N/A
** 5612 724     svchost.exe     0x8a05d5328080  4       -       0       False   2023-12-07 20:35:53.000000      N/A
** 8176 724     NisSrv.exe      0x8a05ce29f340  8       -       0       False   2023-12-07 20:35:56.000000      N/A
* 888   580     fontdrvhost.ex  0x8a05ce4de140  5       -       0       False   2023-12-07 20:33:50.000000      N/A
680     572     winlogon.exe    0x8a05cdbdf080  4       -       1       False   2023-12-07 20:33:49.000000      N/A
* 896   680     fontdrvhost.ex  0x8a05ce4da2c0  5       -       1       False   2023-12-07 20:33:50.000000      N/A
572     680     dwm.exe 0x8a05ce4a2080  18      -       1       False   2023-12-07 20:33:50.000000      N/A
* 600   572     csrss.exe       0x8a05cdbad140  12      -       1       False   2023-12-07 20:33:49.000000      N/A
* 5368  680     userinit.exe    0x8a05d0d56080  0       -       1       False   2023-12-07 20:34:25.000000      2023-12-07 20:34:54.000000 
** 5412 5368    explorer.exe    0x8a05d0d5a080  57      -       1       False   2023-12-07 20:34:25.000000      N/A
*** 3008        5412    SecurityHealth  0x8a05d46c5080  2       -       1       False   2023-12-07 20:35:10.000000      N/A
*** 1224        5412    notepad.exe     0x8a05d8fd32c0  1       -       1       False   2023-12-07 10:47:56.000000      N/A
8308    6232    msedge.exe      0x8a05cd04b080  0       -       1       False   2023-12-07 20:35:11.000000      2023-12-07 10:47:52.000000 
7996    9244    OneDrive.exe    0x8a05d5237080  23      -       1       False   2023-12-07 10:36:54.000000      N/A
1164    6232    msedge.exe      0x8a05cda94080  47      -       1       False   2023-12-07 10:47:53.000000      N/A
* 7684  1164    msedge.exe      0x8a05d5aec2c0  14      -       1       False   2023-12-07 10:48:02.000000      N/A
* 6892  1164    msedge.exe      0x8a05d452b2c0  9       -       1       False   2023-12-07 10:47:53.000000      N/A
* 2140  1164    msedge.exe      0x8a05d4273300  17      -       1       False   2023-12-07 10:47:53.000000      N/A
* 9172  1164    msedge.exe      0x8a05d519e2c0  23      -       1       False   2023-12-07 10:47:58.000000      N/A
* 9564  1164    msedge.exe      0x8a05d47ea340  22      -       1       False   2023-12-07 10:47:53.000000      N/A
* 5692  1164    msedge.exe      0x8a05cd00e080  8       -       1       False   2023-12-07 10:47:53.000000      N/A
```

Με μια γρήγορη ματιά βλέπουμε οτι το μοναδικό αρχείο που μας κινεί το ενδιαφέρον είναι το notepad.exe που έχει τρέξει με γονέα το explorer.exe. Δηλαδή κάποιος χρήστης έχει ανοίξει ενα άρχειο με notepad. Για να βρούμε τι είναι αυτό που έχει ανοιξεί θα χρησιμοποιήσουμε το plugin windows.cmdline προκειμένου να δούμε τα arguments και εφόσον ψάχνουμε κάτι συγκεκριμένο θα φιλτράρουμε απευθείας την εξόδο ως εξής:

```$ python3 ~/volatility3/vol.py -f Win10.raw windows.cmdline | grep notepad```

και έχουμε το εξής output:
```
1224ressnotepad.exe     "C:\Windows\System32\notepad.exe" "C:\Users\shell\Downloads\gift_prep_automation.ps1"
```

Επομένως βλέπουμε οτι έχει ανοίξει με notepad ένα αρχείο powershell με όνομα ***gift_prep_automation.ps1***
Για να ψάξουμε το αρχείο και να δούμε αν μπορούμε  να το κάνουμε extract απο το memory dump θα το αναζητήσουμε με το εξής plugin:

```$ python3 ~/volatility3/vol.py -f Win10.raw windows.filescan |  grep gift_prep_automation.ps1```

Επειδή το output του συγκεκριμένου plugin είναι τεράστιο είναι απαραίτητο να χρησιμοποιήσουμε το φίλτρο. Μετά απο λίγη ώρα αφού τρέξει θα μας δώσει το εξής output:

```
0x8a05e41417f0.0\Users\shell\Downloads\gift_prep_automation.ps1 216
0x8a05e422f6e0  \Users\shell\Downloads\gift_prep_automation.ps1 216
```
Τώρα για να κάνουμε extract το αρχείο θα χρησιμοποιήσουμε το εξής plugin:
```$ python3 ~/volatility3/vol.py -f Win10.raw windows.dumpfiles --virtaddr=0x8a05e41417f0```

Μόλις ολοκληρωθεί μένει απλά να δούμε το περιεχόμενο του:

```
$desktopPath = [System.IO.Path]::Combine($env:USERPROFILE, 'Desktop')

$filePath = [System.IO.Path]::Combine($desktopPath, 'Secret_Recipe.txt')

$fileBytes = Get-Content -Raw -Path $filePath -Encoding Byte
$key = [System.Text.Encoding]::UTF8.GetBytes('Christmas')

for ($i = 0; $i -lt $fileBytes.Length; $i++) {
    $fileBytes[$i] = $fileBytes[$i] -bxor $key[$i % $key.Length]
}

[byte[]]$fileBytes | Set-Content -Path ([System.IO.Path]::Combine($desktopPath, 'Encrypted.txt')) -Encoding Byte -Force

Remove-Item -Path $filePath

Write-Host "Encryption completed."
```

Με λίγη προσοχή στον κώδικα παρατηρούμε οτι έχει γίνει ένα απλό XOR του αρχικού αρχείου με το string **Christmas**. Επομένως για να αποκτήσουμε το αρχικό μπορούμε να χρησιμοποιήσουμε ενα οποιοδήποτε αντίστοιχο κώδικα. Για πιο γρήγορα θα μετατρέψω τα περιεχόμενα του αρχείου σε Base64 encoding για να μπορώ να τα αντιγράψω και στην συνέχεια θα χρησιμοποιήσω CyberChef για το decryption.

```
$ cat Encrypted.txt| base64
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
EyEND1NGKzBCMAQXAVggDlo3ERUlUFw=
```

Μόλις ολοκληρωθεί και αυτό το μέρος θα πρέπει να έχουμε στην κατοχή μας την μυστική συνταγή και πλέον μπορούμε να την διαβάσουμε. Παρατηρώντας προσεκτικά στο τέλος του κειμένου έχουμε το εξής string:
```
Congrats you made Melomakarona: Here is your gift:TkhBQ0t7TTRsMG1hazRyb25hX0Ywcl9SM2ExfQ==
```
Οπότε κάνουμε ενα απλό Base64 decode το περίεργο string και πήραμε το flag.


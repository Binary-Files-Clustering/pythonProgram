from zipfile import ZipFile
import os
import urllib
import shutil
from time import sleep
from lib.cuckoo.core.database import Database

db = Database()

def get_malwares():
	malware_string = """ dd66bcf26c50c12f2d1036ada8cc8c14
SHA1: 55489696953a0e1a24a047009a36fb285340465f
SHA256: e57572a0bec0e9302b7a57707dbff54c1cc683e055183b687d73173f41d2210f 	435348	kaspersky: UDS:DangerousObject.Multi.Generic
avast: Win32:Malware-gen
	File detection : 10/57 (18%) 2016-09-17 15:07:02
	N/A
	ASN : N/A
Pays : N/A
Netname : N/A
	Fri, 16 Sep 2016 22:33:17 +0200	MD5: 6fe994ad77806b7fa8e57e702369a878
SHA1: 2cb50ec91afbc4cd9b9a4ed4cded42d5cf098c87
SHA256: 616958d1b66a978c983c9ad023531f03ccd658a776d28d3a0ac15567e6af3310 	581120	kaspersky: Backdoor.Win32.Androm.kqxo
microsoft: VirTool:MSIL/Injector
malwarebytes: Trojan.Injector.MSIL
	File detection : 22/57 (39%) 2016-09-17 08:59:49
	N/A
	ASN : N/A
Pays : N/A
Netname : N/A
	Fri, 16 Sep 2016 22:32:13 +0200	MD5: 5826138beaa257757e8aa57c9b9f8f7f
SHA1: 25afded56e4f00adcbced4807c42d0fa18eb7c3c
SHA256: 9a4e672f8c8bc3758a74af3e5fdc16dd519090ccbfbfb44ae1b83281912fd85f 	573440	kaspersky: Backdoor.Win32.Androm.kqxm
microsoft: VirTool:MSIL/Injector
malwarebytes: Trojan.Injector.MSIL
	File detection : 22/57 (39%) 2016-09-17 08:58:35
	N/A
	ASN : N/A
Pays : N/A
Netname : N/A
	Fri, 16 Sep 2016 22:31:24 +0200	MD5: 2094ed242ba494a5f8da8124403cdf70
SHA1: c913b52f78a9726b56948ae0900b3f3d1d557b35
SHA256: 50b8b938b4717354499cb06f40c4873e5a9ea880b9046bee0e7a0962854f8b33 	581120	kaspersky: UDS:DangerousObject.Multi.Generic
microsoft: VirTool:MSIL/Injector
	File detection : 22/57 (39%) 2016-09-16 22:23:23
	N/A
	ASN : N/A
Pays : N/A
Netname : N/A
	Fri, 16 Sep 2016 08:02:40 +0200	MD5: 660055a8fc235aff3e013d9dda19555e
SHA1: 3df0a9420713aea4e5c2c3c21b84c093d5b0086c
SHA256: 438bec89c432b53fb5951bbb386c7bc6229e662aa8b68c101f9379085f8ab2b1 	420844	kaspersky: UDS:DangerousObject.Multi.Generic
malwarebytes: Ransom.Cerber.NSIS
	File detection : 10/57 (18%) 2016-09-16 03:20:27
	N/A
	ASN : N/A
Pays : N/A
Netname : N/A
	Fri, 16 Sep 2016 08:01:13 +0200	MD5: 2c349a73b524692a308b0d24b2c40ba3
SHA1: ceca1042a341f644f4930c07cbd26b4fb79fda68
SHA256: f72bc8f6b4095aa4a3b91a70d8b53f4d61dfa6aa07a9d4bf630cf1b44cd60296 	420844	kaspersky: UDS:DangerousObject.Multi.Generic
malwarebytes: Ransom.Cerber.NSIS
	File detection : 12/57 (21%) 2016-09-16 06:07:07
	N/A
	ASN : N/A
Pays : N/A
Netname : N/A
	Thu, 15 Sep 2016 13:48:28 +0200	MD5: 7219807ecbd2eed997ad4873dbd2bef8
SHA1: 630840d9b17669c0cc71f282d03730b254bb5360
SHA256: 70d21eb4e53b696ec8fc4c28917d5dc4a9a1b9eae14701b1af4fee2f35e2fbe5 	147456	kaspersky: UDS:DangerousObject.Multi.Generic
	File detection : 10/56 (18%) 2016-09-15 10:52:57
	N/A
	ASN : N/A
Pays : N/A
Netname : N/A
	Thu, 15 Sep 2016 08:51:06 +0200	MD5: d4002a51167f3bebea29370a19f1a523
SHA1: e23101daa223d00fbc8568dfef80fd4d8fec9c2a
SHA256: 13e39ad17460e55bc80cfb3f0601d51d8897a6beba55add6fbf39cc64925d03c 	184440	kaspersky: Backdoor.Win32.Androm.kqbs
	File detection : 20/57 (35%) 2016-09-15 05:07:45
	N/A
	ASN : N/A
Pays : N/A
Netname : N/A
	Thu, 15 Sep 2016 08:49:58 +0200	MD5: 0e88bef8a0dc876651e983c2bbadcc7f
SHA1: e125169b006e21e362f5592a8caac352bcc30000
SHA256: b2091810a40479e7cc4abea9ad2293aa9e9a3cabae178d2024b6a04cf77d3df7 	106616	kaspersky: Trojan.Win32.IRCbot.amhv
avast: Win32:Malware-gen
	File detection : 22/57 (39%) 2016-09-15 05:10:25
	N/A
	ASN : N/A
Pays : N/A
Netname : N/A
	Wed, 14 Sep 2016 23:05:18 +0200	MD5: 2a165e21a6f51fedb4b7d0d32fb712ec
SHA1: 861faf6a0bc20a29bc3e159e6fe1640924df239d
SHA256: 652f4e046a9765efa05d8eee719c2318d5a058cc5602881326f0a96c35a8f2ba 	270352	kaspersky: Trojan-Spy.Win32.Zbot.wuuc
	File detection : 43/57 (75%) 2016-09-14 20:57:27
	N/A
	ASN : N/A
Pays : N/A
Netname : N/A
	Wed, 14 Sep 2016 20:45:55 +0200	MD5: 7bb5453458f755c0637700fa1635e5db
SHA1: a8db0aed10e7a9fe45e3ff7af9aee8c9fd60103b
SHA256: 7fa880f8e3d456b1ae7b33400d9b381cacf6a71eaad2a0c24c702ad8a6ba0ed5 	335933	kaspersky: UDS:DangerousObject.Multi.Generic
malwarebytes: Trojan.Zbot.CXgen
	File detection : 13/57 (23%) 2016-09-14 19:14:07
	N/A
	ASN : N/A
Pays : N/A
Netname : N/A
	Wed, 14 Sep 2016 16:02:06 +0200	MD5: dde36b6143b0b0f1cc2bfe5adb005e81
SHA1: c6c6bfa0c5705bb9e3bc52fa4463f8c6e92171e3
SHA256: 1ce94901d7c2cc0d1846f6790c13aa931b7c1f277e87aa1c73f6e2e14397fcde 	328328	kaspersky: UDS:DangerousObject.Multi.Generic
avast: Win32:Trojan-gen
malwarebytes: Trojan.Dropper.NSIS
	File detection : 10/57 (18%) 2016-09-14 13:47:32
	N/A
	ASN : N/A
Pays : N/A
Netname : N/A
	Wed, 14 Sep 2016 15:47:11 +0200	MD5: b47c13b0e1a8b4baae66583c79767fae
SHA1: ca500beceea03f1d4e25f584e33342655dfc0e85
SHA256: c9a6f008cef3d237a089c98ab131977c7865b0773695391021a132b3df47a01f 	581632	kaspersky: Trojan.MSIL.Inject.epyj
avast: Win32:Malware-gen
malwarebytes: Trojan.Injector
	File detection : 19/56 (34%) 2016-09-14 13:48:28
	N/A
	ASN : N/A
Pays : N/A
Netname : N/A
	Wed, 14 Sep 2016 15:46:09 +0200	MD5: d0345765ebef26f4e09910d2e74cd894
SHA1: 7c18d3a6e2cc3d1ec7ddc46c6d2a4ea5d890049e
SHA256: 834c9832c9ba4439698cbfad5a62fe7857a65c4bf03a463e33349602e70b4296 	568320	kaspersky: Trojan.MSIL.Inject.epyj
avast: Win32:Malware-gen
malwarebytes: Trojan.Injector
	File detection : 18/57 (32%) 2016-09-14 13:37:21
	N/A
	ASN : N/A
Pays : N/A
Netname : N/A
	Wed, 14 Sep 2016 15:45:19 +0200	MD5: 4a84096a83bfd1709d9308d9ab99ebfb
SHA1: b92c372592375796e335ab9427c4b2fb7237735c
SHA256: 51abeaad1d2fe93bd7534cb5ce7985a5408ac3d9d8186482b71f00c682209df8 	581632	kaspersky: Trojan.MSIL.Inject.epyj
avast: Win32:Malware-gen
malwarebytes: Trojan.Injector
	File detection : 19/58 (33%) 2016-09-14 13:37:12
	N/A
	ASN : N/A
Pays : N/A
Netname : N/A
	Wed, 14 Sep 2016 14:46:45 +0200	MD5: 283f2c9a8fc3bf7bb658be696981da27
SHA1: 5ccf04ba9544a0a834975c8f2342d3e628a3806d
SHA256: f3a27f3d4a44f3c4615a2a3066d766f1c0281d350a20d96ef579ec8f3e24459f 	572928	kaspersky: Trojan-Downloader.Win32.Agent.wusef
microsoft: HackTool:MSIL/Boilod.B
avast: Win32:Trojan-gen
	File detection : 13/57 (23%) 2016-09-12 14:38:22
	N/A
	ASN : N/A
Pays : N/A
Netname : N/A
	Wed, 14 Sep 2016 14:45:55 +0200	MD5: cd144cdec9f3d28d277a484bb731537f
SHA1: a72862187a54fec624b0cdd4fc55621fbda8bf70
SHA256: ea3049624ea76ac35126a973df1a941ce67f1262af775a161a8be2f67dc7f9a5 	207169	kaspersky: HEUR:Packed.NSIS.MyxaH.gen
	File detection : 7/57 (12%) 2016-09-14 12:36:37
	N/A
	ASN : N/A
Pays : N/A
Netname : N/A
	Tue, 13 Sep 2016 15:01:21 +0200	MD5: 5b3583ed6524c0be8cce757ef81f56b0
SHA1: c12c8793637fca56fd6851a79eb8e839b1fd1a33
SHA256: c7b60a72609a41406481311cf49a811dc55724d486044da28a032a2bf8dcd947 	330928	kaspersky: UDS:DangerousObject.Multi.Generic
	File detection : 6/58 (10%) 2016-09-13 12:56:53
	N/A
	ASN : N/A
Pays : N/A
Netname : N/A
	Tue, 13 Sep 2016 14:15:04 +0200	MD5: 2ecceb5712e58df9b73c908ec0664ff5
SHA1: 3e218d3482c31162e64320316841244d9658a7a1
SHA256: 8887099b5c80df26548e5c1e9d6f314d63d9c21c727c1d25d72e52d8351a88cf 	173480	kaspersky: HEUR:Trojan.Win32.Generic
microsoft: Backdoor:Win32/Kirts.A
	File detection : 22/57 (39%) 2016-09-13 12:22:53
	N/A
	ASN : N/A
Pays : N/A
Netname : N/A
	Tue, 13 Sep 2016 13:37:39 +0200	MD5: 5cb3dbd7432d25b5860ada5b894ba519
SHA1: 2d575f4d59fd72d0d590bde6be8b1d5a3ebae926
SHA256: e5f9f2dd4cbeed1821052a294b8084def863c472bd2d1b505355e4ecc0ec2826 	189864	kaspersky: UDS:DangerousObject.Multi.Generic
microsoft: Backdoor:Win32/Kirts.A
malwarebytes: Trojan.Injector
	File detection : 17/57 (30%) 2016-09-13 08:14:30
	N/A
	ASN : N/A
Pays : N/A
Netname : N/A
	Tue, 13 Sep 2016 12:34:43 +0200	MD5: 78090aa9660d0ac121b164cc72e7f528
SHA1: 7a09dfd38e0f98b012d58abf8c3dd6ebb1b2218b
SHA256: c0e9553a235aa29e86710c4466e6aaf9ef82d0a055fb6e021016c38a503f3d80 	243112	kaspersky: Trojan-Dropper.Win32.Injector.posn
microsoft: Backdoor:Win32/Kirts.A
avast: Win32:Malware-gen
malwarebytes: Trojan.Injector
	File detection : 23/58 (40%) 2016-09-13 09:22:22
	N/A
	ASN : N/A
Pays : N/A
Netname : N/A
	Tue, 13 Sep 2016 09:39:12 +0200	MD5: 421a688ec466162a12b6fe7191e775d0
SHA1: e9ac85780b23de3b4fa8092e0e705e7c0c2ae1d4
SHA256: 8a01a64d3123ec567bc8d9d69de78d113777b5f2e240978627b52c21f686d1dd 	226728	kaspersky: Backdoor.Win32.Androm.kphb
microsoft: Backdoor:Win32/Kirts.A
avast: Win32:Malware-gen
malwarebytes: Trojan.Injector
	File detection : 32/58 (55%) 2016-09-13 05:56:19
	N/A
	ASN : N/A
Pays : N/A
Netname : N/A
	Tue, 13 Sep 2016 09:38:19 +0200	MD5: 7554244ea84457f53ab9d4989c4d363d
SHA1: 43be8c385b69dfb21bbee8e655068aa2aafb22a2
SHA256: 1e278e78a4261ebd65d2fc9b2d477bb8c19e15a22aea669947b531859cd12216 	81920	kaspersky: Trojan-Ransom.Win32.Locky.bwk
avast: Win32:Trojan-gen
	File detection : 22/57 (39%) 2016-09-13 00:34:30
	N/A
	ASN : N/A
Pays : N/A
Netname : N/A
	Tue, 13 Sep 2016 09:37:28 +0200	MD5: 59801b34dea794f88172332dce88dfc3
SHA1: 36a07a7ebe4aa693485f9855814733c48d9866c1
SHA256: 637e60fbf5af8148c3fd9056e1c724a33f707d5ca456df88976e168222622b0a 	230824	kaspersky: Trojan-PSW.Win32.Tepfer.psxoqh
microsoft: Backdoor:Win32/Kirts.A
avast: Win32:Malware-gen
malwarebytes: Trojan.Injector
	File detection : 29/58 (50%) 2016-09-13 04:26:56
	N/A
	ASN : N/A
Pays : N/A
Netname : N/A
	Tue, 13 Sep 2016 09:36:09 +0200	MD5: 8384042f9d889245e5d2405dbb20679e
SHA1: 0ff5da3aacf592fc30bccad71be44f4211fdd54f
SHA256: cc6e90286ed80e36fad1899fd0c5fd8f9fd849235378b5a0a7afb1df6bf5c9de 	220964	kaspersky: UDS:DangerousObject.Multi.Generic
	File detection : 7/57 (12%) 2016-09-13 07:32:47
	N/A
	ASN : N/A
Pays : N/A
Netname : N/A
	Tue, 13 Sep 2016 09:35:16 +0200	MD5: baf9e357a90ccf15bcf875719b01ebbc
SHA1: ddc92ae95c68145fd5331e408cdb58dafd637821
SHA256: 89e156f42cd465a1af2d927aa59a0d65789b2321ae1a45a0485801a6535a9fe7 	137216	kaspersky: HEUR:Trojan.Win32.Generic
microsoft: Ransom:Win32/Locky.A
avast: Win32:Malware-gen
malwarebytes: Ransom.Locky
	File detection : 28/57 (49%) 2016-09-12 11:20:31
	N/A
	ASN : N/A
Pays : N/A
Netname : N/A
	Mon, 12 Sep 2016 12:37:54 +0200	MD5: 07d1e487327e04ab24aa5babeaa9ab39
SHA1: d756b8cb921624145103af4d5a00d9fb0f478f5f
SHA256: 12c68e230024168c617862ebb941ccc225fc7f5332e5cbd0be29fd7d547e1c6a 	198056	kaspersky: UDS:DangerousObject.Multi.Generic
malwarebytes: Trojan.Injector
	File detection : 13/58 (22%) 2016-09-12 10:23:10
	N/A
	ASN : N/A
Pays : N/A
Netname : N/A
	Mon, 12 Sep 2016 12:37:01 +0200	MD5: fba6bece50e7bc4e388d6b1c5e54afac
SHA1: 7bffb7eaae7780cd8546c4b1a00747c89fb57cdd
SHA256: 7b9a9474fee608bf1e7f6e2217f68abe098e167ff5bf03bbea47bb86e0ef03a5 	304552	kaspersky: UDS:DangerousObject.Multi.Generic
malwarebytes: Trojan.Injector
	File detection : 13/58 (22%) 2016-09-12 10:25:00
	N/A
	ASN : N/A
Pays : N/A
Netname : N/A
	Mon, 12 Sep 2016 12:34:22 +0200	MD5: a8712a3a86cf61b98641cf9710978272
SHA1: e9e0a949caccb143d4913ae6214880b134968b70
SHA256: aad79e6398bc81c383a3d1f7b243e034e84b9d743eacdae18896665cafc445ae 	534016	kaspersky: UDS:DangerousObject.Multi.Generic
	File detection : 20/57 (35%) 2016-09-12 12:27:53
	N/A
	ASN : N/A
Pays : N/A
Netname : N/A
	Mon, 12 Sep 2016 12:33:32 +0200	MD5: 36a0cae178cc10d82d701457b923450a
SHA1: dcb1e13fc0ba770c36ae6c1b8363d4b4b42a68df
SHA256: 42340201215ebbb9f4a07c9548623c40d5aebb93d89c6762337019fb0878078c 	528384	kaspersky: UDS:DangerousObject.Multi.Generic
	File detection : 21/57 (37%) 2016-09-12 12:29:43
	N/A
	ASN : N/A
Pays : N/A
Netname : N/A
	Mon, 12 Sep 2016 12:32:42 +0200	MD5: 09a9f8150603cbeab0b5cfff24340930
SHA1: 8108849fef15056823e15d8b3bd5b4a2aee21eb0
SHA256: c9994c8c52027a32cac4e37fa8e3a7e177e7e440503f7ccb424a27c9525fd659 	541184	kaspersky: UDS:DangerousObject.Multi.Generic
	File detection : 21/57 (37%) 2016-09-12 12:33:33
	N/A
	ASN : N/A
Pays : N/A
Netname : N/A
	Sun, 11 Sep 2016 09:35:47 +0200	MD5: 49b7d93e11c1e338121a656db8097042
SHA1: 8c86dfa3564912cdbd514b29d8e1e9ce9d134444
SHA256: ab8c74dcaf553df88d1d892f42f815b7a35190b9218c193221570de124f6a686 	202152	kaspersky: Backdoor.Win32.Androm.kpdh
avast: Win32:Malware-gen
malwarebytes: Trojan.Injector
	File detection : 26/57 (46%) 2016-09-11 17:43:18
	N/A
	ASN : N/A
Pays : N/A
Netname : N/A
	Sun, 11 Sep 2016 09:34:58 +0200	MD5: 8b4101f06ec2f56a0f9d332d618844a1
SHA1: 930edd31a15c498a5b218b8771b43a74ee737854
SHA256: 68db35e915a308834a6dcf0ae456711e61c30460d364e90febae76e8c378803d 	297371	kaspersky: Trojan-Ransom.Win32.Zerber.nqg
avast: Win32:Malware-gen
malwarebytes: Ransom.Cerber.NSIS
	File detection : 24/57 (42%) 2016-09-11 17:42:45
	N/A
	ASN : N/A
Pays : N/A
Netname : N/A
	Sat, 10 Sep 2016 14:01:03 +0200	MD5: b976c8bead9e68646c708822e32064fc
SHA1: 6dcade52903e4acea36eb63ef52875225720c369
SHA256: 7b070699acab974dc6cbfdd6465584e60deee9a3048b42b01643ef4caddf1d50 	169384	kaspersky: Backdoor.Win32.Androm.kpaq
avast: Win32:Trojan-gen
malwarebytes: Trojan.Injector.MSIL
	File detection : 10/58 (17%) 2016-09-10 02:04:57
	N/A
	ASN : N/A
Pays : N/A
Netname : N/A
	Sat, 10 Sep 2016 14:00:15 +0200	MD5: c2bccc6e7015c394c69e47f5ab5e5beb
SHA1: 26bf4766138f6e3f0bb71cca8eeba42ff9936f6b
SHA256: cfb33dfccc94492002af6177971ab3471375d977b08d190db686a3ac6c5e36da 	255400	kaspersky: Trojan-Dropper.Win32.Injector.pnwb
avast: Win32:Malware-gen
	File detection : 11/58 (19%) 2016-09-10 06:23:12
	N/A
	ASN : N/A
Pays : N/A
Netname : N/A
	Fri, 09 Sep 2016 15:14:29 +0200	MD5: b981e264555e02168afa6421bd06f073
SHA1: eb34325e98345d0caa5977d0b1fe4807f961d36c
SHA256: 841473e23392bd575891bff0533d8f7a67fde1f7c5d7082088aa25d328c8d955 	161192	kaspersky: HEUR:Trojan.Win32.Generic
avast: Win32:Malware-gen
	File detection : 15/57 (26%) 2016-09-09 15:51:18
	N/A
	ASN : N/A
Pays : N/A
Netname : N/A
	Fri, 09 Sep 2016 15:13:39 +0200	MD5: 6d02ce6c2d6765f0f96575af56d4aee3
SHA1: 386ec98e006d0a3e88d064a4e9353d83d0ded147
SHA256: b19b5ae07fb8123cb48498563b3ea2d5bcb539dd497e9fe6b5f2d4e92261ee91 	202152	kaspersky: UDS:DangerousObject.Multi.Generic
	File detection : 9/57 (16%) 2016-09-09 13:05:54
	N/A
	ASN : N/A
Pays : N/A
Netname : N/A
	Fri, 09 Sep 2016 15:12:51 +0200	MD5: 1711464a23e9a0c222a361c3fcf3c318
SHA1: f5e437ee0e6ceab67f97b1741a32f47a4fbc22e2
SHA256: 71af8666392acad2080a816b9f1196fe9ccb950e1db8a549f8312c4d231f55a8 	235600		File detection : 0/56 (0%) 2016-09-07 17:16:24
	N/A
	ASN : N/A
Pays : N/A
Netname : N/A
	Fri, 09 Sep 2016 15:12:03 +0200	MD5: abde01a47298e1b75403ea03b482de05
SHA1: e64336b07fc723a5591215379b10c142ec4025ce
SHA256: 21fb40ad372b511b6c5ad0e9fc2e4fb2fb89c5c7da7cfbdd5d69da5fa712bc53 	226728	kaspersky: UDS:DangerousObject.Multi.Generic
avast: Win32:Malware-gen
	File detection : 11/57 (19%) 2016-09-09 13:04:43
	N/A
	ASN : N/A
Pays : N/A
Netname : N/A
	Wed, 07 Sep 2016 18:28:36 +0200	MD5: 2b8e4c792bed0e5882702720bc528ae5
SHA1: e7638b294a4f1409f87e449643a02bbd49a481c8
SHA256: 6d7cb027bc6014cb268c49b46049cdff3ba94d07102a65bd053335a28e83d125 	150648		File detection : 0/56 (0%) 2016-08-30 09:17:16
	N/A
	ASN : N/A
Pays : N/A
Netname : N/A
	Wed, 07 Sep 2016 18:27:23 +0200	MD5: d3de32089b31c8606aeca2f13055ba21
SHA1: 054491c480cd69487df2037b3f331d8bc15a81c7
SHA256: 3d8993b7468e6994c4a2a973a02a27f83571731df2df6841a4bca0312aa5a8f7 	222683	kaspersky: HEUR:Packed.NSIS.MyxaH.gen
	File detection : 4/56 (7%) 2016-09-07 16:15:50
	N/A
	ASN : N/A
Pays : N/A
Netname : N/A
	Wed, 07 Sep 2016 18:26:20 +0200	MD5: ca7933c9ceb85ccd8d4c92afc8c3d6be
SHA1: 3ed868b7cffd3cf3067a1075141a60265755206b
SHA256: b586c11f5485e3a38a156cba10379a4135a8fe34aa2798af8d543c059f0ac9a4 	203776	kaspersky: Trojan-Downloader.VBS.Banload.ae
	File detection : 5/55 (9%) 2016-09-07 16:24:10
	N/A
	ASN : N/A
Pays : N/A
Netname : N/A
	Wed, 07 Sep 2016 18:24:52 +0200	MD5: 55b597304e8004f4e1dc5e68f934d01e
SHA1: 54bb851e6c6b3ce54898ceade884e7ac80403400
SHA256: 1ff9063b4d06b0a686d68eae71bf548cf39f45716b8458a0a7af84d94ba88100 	77824	avast: Win32:Malware-gen
malwarebytes: Ransom.Cerber
	File detection : 4/56 (7%) 2016-09-07 15:48:17
	N/A
	ASN : N/A
Pays : N/A
Netname : N/A
	Wed, 07 Sep 2016 17:57:53 +0200	MD5: 86a97c113c88d3b26c9960877c6b3321
SHA1: 2dedd9cd2b47f6d4b5edd1a4f5cf67e5b60deb03
SHA256: c4e057e22de707fcb435185eae479b1e1abb73dfa39eb0bd105275cf249bff42 	46080	kaspersky: UDS:DangerousObject.Multi.Generic
	File detection : 28/55 (51%) 2016-09-07 10:02:36
	N/A
	ASN : N/A
Pays : N/A
Netname : N/A
	Wed, 07 Sep 2016 17:57:03 +0200	MD5: 5b99b211a6d06422ad1b1fd4ea86aa36
SHA1: fec86945882c4d9bfddc0a03dd1edd684e19ecc8
SHA256: 47e732b1d04ae1912701683fa35a7ffb7a7ae590456379e6e160c576c6e9c311 	267688	kaspersky: UDS:DangerousObject.Multi.Generic
	File detection : 7/57 (12%) 2016-09-07 14:00:53
	N/A
	ASN : N/A
Pays : N/A
Netname : N/A
	Wed, 07 Sep 2016 17:56:12 +0200	MD5: 651b57f42eb936776ea90e698a53c996
SHA1: 836c6c0f1dc28183c5fd0dba0138f435d3f6adf5
SHA256: f5f9cca98083e32f41519b8ae4cf085a6e29a2c6ab2685967a7eb9d65de60b53 	337320	kaspersky: UDS:DangerousObject.Multi.Generic
	File detection : 7/58 (12%) 2016-09-07 17:32:56
	N/A
	ASN : N/A
Pays : N/A
Netname : N/A
	Wed, 07 Sep 2016 17:55:22 +0200	MD5: aae5aa33973db91cecadca07f0672c26
SHA1: fe6b89e71d559c54a2cec2a0da6c5bcd6d541986
SHA256: a790232b37260ed4a8135057d732a6d96bb19c39074d790d164405e4e0432700 	292264	kaspersky: UDS:DangerousObject.Multi.Generic
	File detection : 6/57 (11%) 2016-09-07 07:28:31
	N/A
	ASN : N/A
Pays : N/A
Netname : N/A
	Wed, 07 Sep 2016 17:54:30 +0200	MD5: 2bce860f1df22a170bf163b531bbd854
SHA1: 31221d3bc4e87dcdcb34531de690c70713abd9f2
SHA256: bdf4fa92397d86227ec171f19d94a39492855393181728295a2ef84dbd5922da 	292264	kaspersky: UDS:DangerousObject.Multi.Generic
	File detection : 6/56 (11%) 2016-09-07 15:49:40
	N/A
	ASN : N/A
Pays : N/A
Netname : N/A
	Wed, 07 Sep 2016 17:02:24 +0200	MD5: cd58a866591382d5d346e93b081abd15
SHA1: bc07057567dfe1b1dcffa41d0c5daca302be7c8e
SHA256: 940f355a4350194779a197ff12d914d39bf608f12fa07e7efc020d43d811ccb7 	572928	kaspersky: Backdoor.Win32.Androm.kopy
microsoft: TrojanSpy:MSIL/Omaneat.C
avast: Win32:Malware-gen
malwarebytes: Spyware.HawkEyeKeyLogger
	File detection : 15/57 (26%) 2016-09-07 17:48:09
	N/A
	ASN : N/A
Pays : N/A
Netname : N/A
	Wed, 07 Sep 2016 17:01:32 +0200	MD5: 871676694b2b3691f2fa51aa154fbba2
SHA1: e58ec145183a31ebe777a52851e625b885de4f7e
SHA256: 311f438279938d9db717d08247291eb75d28de79c312e5a1318e8ac4595d77e6 	565248	kaspersky: UDS:DangerousObject.Multi.Generic
	File detect
"""

	malware_list = malware_string.split("MD5: ")
	malware_md5s = [i[:i.find("\n")] for i in malware_list]
	malware_descrps = [i[i.find("kaspersky"):i.find("\n\t")] for i in malware_list]

	malwares_finished = []
	cnt = 0

	for i in range(len(malware_md5s)):
		md5, desc, = malware_md5s[i], malware_descrps[i]
		index = desc.find("malwarebytes: ")	
		if index != -1:
			malwares_finished.append((md5, desc[index+len("malwarebytes: "):]+str(cnt)))
			cnt+=1

	return malwares_finished

def submit(name):
	file_path = "tasks/"+name
	return db.add_path(file_path=file_path,
                                      package="",
                                      timeout=0,
                                      options="",
                                      priority=1,
                                      machine="",
                                      platform="",
                                      custom="",
                                      owner="",
                                      memory=False,
                                      enforce_timeout=False,
                                      clock=None,
                                      tags=None)

def download_malware(md5, name):
	md5, name
	base_url = "http://malwaredb.malekal.com/files.php?file="
	url = base_url + md5
	urllib.urlretrieve(url, name+".zip")
	password = "infected"
	ZipFile(name+".zip").extractall(pwd=password)
	os.remove(name+".zip")

	os.rename(md5, "tasks/"+name)

def share_file(file_path,name):
	shutil.move(file_path, "Host/"+name+".json")

def wait_for_report(tid, name):
	report_path = "storage/analyses/"+str(tid)+"/reports/report.json"	
	while not os.path.exists(report_path):
		sleep(2)
	sleep(10)
	share_file(report_path, name)

def delete_analysis_files(tid):
	shutil.rmtree("storage/analyses/"+str(tid))

def download_all(malwares):
	for malware in malwares:
		md5, name = malware[0], malware[1]
		download_malware(md5, name)
		print "finished downloading " + name

def do_assessment(md5_name):
	md5, name = md5_name[0], md5_name[1]
	print "assessing "+name
	task_id=submit(name)
	print "submitted "+name+ " with task id" + str(task_id)
	wait_for_report(task_id, name)
	print "shared report"
	delete_analysis_files(task_id)
	print "deleting analysis with task id" + str(task_id)
	
malwares = get_malwares()
#download_all(malwares)
for malware in malwares:
	do_assessment(malware)

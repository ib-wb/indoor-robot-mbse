# Repository-Umfang und Pflege

<!--
SPDX-FileCopyrightText: 2026 Wolfgang Becker
SPDX-License-Identifier: CC-BY-4.0
-->

Dieses Repository enthält das SysML-v2-Modell eines mobilen Materialtransportroboters
und die zugehörigen technischen Entwicklungsartefakte.

## Enthaltener Stand

- Vollständiges SysML-Modell mit Baseline A.1, Baseline B.1 und Namensfassade.
- Anforderungen, Schnittstellen, Verhalten, Traceability und Verifikationsideen.
- Vorläufige Hardware-/Software- und ROS-2-Zuordnung.
- Modellprüfwerkzeuge und GitHub-Actions-Workflow.

Der Veröffentlichungsstand beginnt mit einer eigenen Git-Historie.
Buchmanuskripte, private Arbeitsdaten und KiCad-Entwürfe sind nicht enthalten.
Eine automatische Synchronisation aus anderen Repositories ist nicht eingerichtet.

## Änderungen prüfen

Die Datei [`.publication-files.txt`](../.publication-files.txt) nennt jede
freigegebene Datei einzeln. Vor einem Push ausführen:

```sh
python tools/check_public_scope.py
python tools/validate_sysml.py --self-test --negative-tests
git diff --cached --stat
git diff --cached
```

`check_public_scope.py` vergleicht die Freigabeliste mit dem Git-Index und den
lokal vorhandenen Dateien außerhalb von `.git`. Es lehnt zusätzliche Dateien,
fehlende Einträge, symbolische Links und Submodule ab. Neue technische Artefakte
müssen bewusst aufgenommen und inhaltlich geprüft werden. Die CI führt dieselbe
Umfangsprüfung aus. Die lokale Prüfung vor dem Push ist notwendig, weil eine
nachträgliche CI-Prüfung bereits übertragene Inhalte nicht zurückholen kann.

`.gitignore` verhindert das versehentliche Vormerken typischer lokaler Dateien.
Eine Änderung der Freigabeliste erfordert weiterhin eine inhaltliche Prüfung.

## Weitere Implementierungen

Künftige Software-, Firmware- und Hardwareartefakte werden in diesem Repository
gezielt ergänzt und mit dem Modell verknüpft. Die Freigabe eines technischen
Artefakts gilt nur für dessen geprüfte Dateien und zugehörige Informationen.

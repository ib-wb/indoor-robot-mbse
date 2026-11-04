# Lizenzen und Geltungsbereich

<!--
SPDX-FileCopyrightText: 2026 Wolfgang Becker
SPDX-License-Identifier: CC-BY-4.0
-->

Copyright © 2026 Wolfgang Becker.

Die Inhalte dieses Repositorys verwenden zwei Lizenzen. Die Zuordnung erfolgt
nach Dateityp und Pfad; die einzelnen Projektdateien tragen entsprechende
SPDX-Lizenzkennzeichnungen.

| Inhalte | Pfade | Lizenz |
| --- | --- | --- |
| SysML-v2-Modellquellen | `sysml/**/*.sysml` | Apache License 2.0 (`Apache-2.0`) |
| Prüfwerkzeuge und deren Konfiguration | `tools/` | Apache License 2.0 (`Apache-2.0`) |
| CI-Workflow und Repository-Konfiguration | `.github/workflows/sysml.yml`, `.gitattributes`, `.gitignore`, `.publication-files.txt` | Apache License 2.0 (`Apache-2.0`) |
| Dokumentation und Tabellen | `README.md`, `LICENSING.md`, `docs/**/*.md`, `sysml/**/*.md` | Creative Commons Attribution 4.0 International (`CC-BY-4.0`) |

Die Pfadmuster schließen jeweils auch Dateien direkt im genannten Verzeichnis ein.
Die verbindlichen Bedingungen ergeben sich aus den vollständigen Lizenztexten:

- [Apache License 2.0](LICENSE), unveränderter englischer Originaltext der
  [Apache Software Foundation](https://www.apache.org/licenses/LICENSE-2.0).
- [Creative Commons Attribution 4.0 International](LICENSES/CC-BY-4.0.txt),
  vollständiger englischer Originaltext von
  [Creative Commons](https://creativecommons.org/licenses/by/4.0/).

Die Lizenztexte selbst werden unverändert wiedergegeben; sie sind keine unter
den Projektlizenzen neu lizenzierten Projektbeiträge.

## Namensnennung für die Dokumentation

Bei Weitergabe oder Bearbeitung der unter CC BY 4.0 stehenden Dokumentation
sind die nach der Lizenz erforderlichen Angaben beizubehalten: insbesondere
Urheberangabe, Lizenzverweis und gegebenenfalls ein Hinweis auf Änderungen.
Eine mögliche Namensnennung lautet:

> Indoor Robot MBSE — Wolfgang Becker, 2026.
> Quelle: https://github.com/ib-wb/indoor-robot-mbse.
> Lizenz: CC BY 4.0, https://creativecommons.org/licenses/by/4.0/.

Eigene Änderungen sind zusätzlich kenntlich zu machen.

## Abgrenzung und weitere Inhalte

Die Freigabe gilt für die entsprechend gekennzeichneten Inhalte dieses
Repositorys. Außerhalb des Repositorys gehaltene Buchmanuskripte, private
Arbeitsdateien und nicht veröffentlichte Entwürfe sind davon nicht umfasst.

Hardwaredesigns und KiCad-Entwürfe sind derzeit nicht enthalten. Vor ihrer
Aufnahme ist ihre Lizenz ausdrücklich festzulegen. Neue Projektdateien erhalten
eine passende SPDX-Kennzeichnung; bei neuen Dateikategorien wird die Zuordnung
in diesem Dokument ergänzt.

Die vom Prüfwerkzeug heruntergeladene SysML v2 Pilot Implementation und ihre
Standardbibliothek gehören nicht zum veröffentlichten Dateibestand. Für diese
Abhängigkeiten gelten die jeweiligen eigenen Lizenzbedingungen.

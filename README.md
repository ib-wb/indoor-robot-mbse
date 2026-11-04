# Indoor Robot MBSE

<!--
SPDX-FileCopyrightText: 2026 Wolfgang Becker
SPDX-License-Identifier: CC-BY-4.0
-->

Dieses Repository begleitet die modellbasierte Entwicklung eines mobilen
Materialtransportroboters: vom SysML-v2-Modell über nachvollziehbare
Architekturentscheidungen bis zur späteren Umsetzung in Software und Hardware.

Der aktuelle Stand enthält ein prüfbares Engineering-Modell und ein vorläufiges
Umsetzungskonzept. Ausführbare ROS-2-Nodes, MCU-Firmware und freigegebene
Hardwareentwürfe sind noch nicht enthalten.

## Einstieg

- [Modellübersicht](sysml/README.md): den gesamten Ordner `sysml` laden.
- [Technische Umsetzung](docs/technical-implementation.md): Verantwortlichkeiten,
  Hardware-/Software-Zuordnung und mögliche ROS-2-Anbindung.
- [Modellprüfung](docs/model-validation.md): Werkzeugstand, Prüfumfang und Grenzen.
- [Betrieblicher Stopp und Wiederfreigabe](docs/operational-pause.md).
- [Repository-Umfang und Pflege](docs/repository-scope.md).

## Struktur

| Pfad | Inhalt |
| --- | --- |
| `sysml/baseline_a1/` | Kontext, 22 Anforderungen, Struktur, Schnittstellen, Verhalten, Verifikation, ROS-2-Mapping und Simulationsprüfstand |
| `sysml/baseline_b1/` | Zehn Use Cases und 17 Kandidatenanforderungen |
| `sysml/mobile_material_robot_overview.sysml` | Kompatibilitätsfassade für frühere Modellnamen |
| `docs/` | Technische Beschreibung, Prüfverfahren und Modellentscheidungen |
| `tools/` | Reproduzierbare Modellprüfung und Prüfung des Veröffentlichungsumfangs |
| `.github/workflows/sysml.yml` | Automatische Prüfung bei Änderungen |

Kanonischer Robotertyp:
`MobileMaterialRobot_Structure_A1::MobileMaterialRobot`.

## Modell prüfen

Voraussetzungen: Python 3.10 oder neuer und ein Java-JDK ab Version 21.
Im Hauptverzeichnis ausführen:

```sh
python tools/check_public_scope.py
python tools/validate_sysml.py --self-test --negative-tests
```

Die Modellprüfung lädt die offizielle SysML v2 Pilot Implementation 0.53.0
(Release 2025-10), prüft den festgelegten SHA-256-Wert und verwendet die zugehörige
Standardbibliothek. Bei mehreren Java-Installationen `JAVA_HOME` setzen oder
`--java` angeben. Eine vorhandene Pilot-Installation kann mit `--pilot-home`
verwendet werden.

Der Prüfumfang umfasst das Gesamtmodell, die Abdeckung der A.1-Anforderungen,
15 synthetische Auswertungen sowie drei absichtlich beschädigte Modellkopien.
Synthetische Ergebnisse belegen Modelllogik; reale Fahr-, Nutzlast- und
Sicherheitsnachweise sind noch zu erbringen.

## Weiterentwicklung

Die Zuordnung zu ROS 2 beschreibt mögliche Implementierungsbausteine.
Simulator, Rechnerplattform, Sensorik, Antrieb und Energiekonfiguration bleiben
offen. Neue Implementierungen sollen die vorhandenen Anforderungen,
Schnittstellen und Verifikationsideen referenzieren.

## Lizenzen

Copyright © 2026 Wolfgang Becker.

- **Apache-2.0** für die SysML-Modelldateien, den Programmcode und die
  technischen Konfigurationsdateien.
- **CC BY 4.0** für die Dokumentation einschließlich README-Dateien und
  Traceability-Tabellen in Markdown.

Die genaue Zuordnung und die vollständigen Lizenztexte stehen in
[LICENSING.md](LICENSING.md). Diese Freigabe umfasst ausschließlich die
entsprechend gekennzeichneten Inhalte dieses Repositorys.

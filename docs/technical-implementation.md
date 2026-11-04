# Technische Umsetzung des SysML-Modells

<!--
SPDX-FileCopyrightText: 2026 Wolfgang Becker
SPDX-License-Identifier: CC-BY-4.0
-->

## Ausgangspunkt

Die logische Architektur trennt Verantwortlichkeiten für Mission, Navigation,
Wahrnehmung, Bewegung, Nutzlast, Energie, Kommunikation, Bedienung, Sicherheit
und Diagnose. Die zentrale Definition steht in
[`03_structure.sysml`](../sysml/baseline_a1/03_structure.sysml).
Kontext, Tests und Simulationsprüfstand verwenden denselben Robotertyp.

Hardware und Software werden aus Funktionen, Schnittstellen und Nachweisen
abgeleitet. Der Modellstand legt noch keine konkrete Stückliste, Rechnerplattform
oder ausführbare Steuerungssoftware fest.

## Vorläufige Hardware-/Software-Zuordnung

| Verantwortung im Modell | Möglicher Hardware-Anteil | Möglicher Software-Anteil | Stand |
| --- | --- | --- | --- |
| `MissionSystem` | Onboard-Rechner | Auftragsprüfung, Missionszustand und Ablaufkoordination | Logisch modelliert |
| `NavigationSystem` | Rechner und Kartenspeicher | Kartenverwaltung, Lokalisierung, globale und lokale Planung | Kandidatenzuordnung |
| `PerceptionSystem` | Noch auszuwählende Sensorik | Treiber, Filterung und Hindernisinterpretation | Sensorwahl offen |
| `MotionSystem` | Motoren, Motorcontroller, Encoder; gegebenenfalls MCU | Hardwarenahe Regelung und Ausführung freigegebener Bewegungsbefehle | Antrieb und Firmware offen |
| `TransportSystem` | Mechanische Werkstückträgeraufnahme und Sicherung | Spätere Handhabungs- und Verriegelungslogik | Nutzlastdaten und Mechanik offen |
| `EnergySystem` | Energiespeicher und Messtechnik | Energieüberwachung und Koordination der Rückkehr | Auslegung und Ladeumfang offen |
| `SafetySystem` | Noch festzulegende Sicherheits- und Stoppeinrichtungen | Sicherheitsbewertung, Stoppentscheidung und Status | Sicherheitskonzept offen |
| `CommunicationSystem`, `UserInterfaceSystem` | Kommunikationsschnittstelle und Rechner | Befehls-/Statusaustausch und roboterseitiger Bedienanschluss | Protokoll und Deployment offen |
| `DiagnosticsSystem` | Spätere Diagnosequellen | Diagnosemeldungen für Betrieb und Tests | Quellen offen |

Die externe `WebApp` gehört zum Systemkontext. `UserInterfaceSystem` bezeichnet
den roboterseitigen Anschluss. Kartenverwaltung und Lokalisierung sind
Verantwortlichkeiten des vorhandenen `NavigationSystem`.

## Kandidaten für ROS 2

Verbindliche Quelle für die derzeitigen Kandidatennamen ist
[`07_ros2_mapping.sysml`](../sysml/baseline_a1/07_ros2_mapping.sysml).
Die dortigen Abhängigkeiten dokumentieren eine mögliche Technologiezuordnung.
Eine endgültige Allokation oder ein Implementierungsnachweis steht noch aus.

| SysML-Kandidat | Zugeordnetes logisches System | Möglicher Node / Aufgabe | Beispiele für Schnittstellen |
| --- | --- | --- | --- |
| `MissionManagerNode` | `MissionSystem` | `mission_manager_node`: Auftrag und Missionszustand | `/transport_order`, `/goal_pose`, `/mission_state` |
| `WebInterfaceNode` | `UserInterfaceSystem`, `CommunicationSystem` | `web_interface_node`: externer Bedienanschluss | `/operator_command`, `/mission_state`, `/diagnostics` |
| `MapManagementNode` | `NavigationSystem` | `map_management_node`: Karten und Änderungskandidaten | `/map`, `/map_update_candidate`, `/local_obstacles` |
| `LocalizationNode` | `NavigationSystem` | `localization_node`: Pose relativ zur Karte | `/map`, `/robot_pose`, Sensordaten |
| `PerceptionNode` | `PerceptionSystem` | `perception_node`: lokale Hindernisse | Sensordaten, `/local_obstacles` |
| `NavigationNode` | `NavigationSystem` | `navigation_node`: Ziel, Weg und Bewegungsvorgaben | `/goal_pose`, `/robot_pose`, `/cmd_vel`, `/navigation_result`, `/safety_state` |
| `MotionControllerNode` | `MotionSystem` | Bewegungsbefehle im zulässigen Zustand ausführen | `/cmd_vel`, `/safety_state` |
| `SafetySupervisorNode` | `SafetySystem` | `safety_supervisor_node`: Sicherheitszustand | `/local_obstacles`, `/cmd_vel`, `/safety_state`, Sicherheitseingänge |
| `EnergyMonitorNode` | `EnergySystem` | `energy_monitor_node`: Energiezustand | Batterieschnittstelle, `/battery_state` |
| `DiagnosticsNode` | `DiagnosticsSystem` | Diagnosequellen zusammenführen | `/diagnostics` |

Nachrichtentypen, Topic-/Service-/Action-Auswahl, Frequenzen, QoS,
Zeitverhalten und konkrete ROS-2-Pakete sind noch zu spezifizieren.
Die Datentypen und gerichteten Ports in
[`04_interfaces.sysml`](../sysml/baseline_a1/04_interfaces.sysml)
bilden den fachlichen Ausgangspunkt dafür. Physische Ports enthalten derzeit
Vertragshalter für später festzulegende mechanische und elektrische Eigenschaften.

## Verhalten und Nachweise

Der nominale Ablauf und die Betriebszustände stehen in
[`05_behavior.sysml`](../sysml/baseline_a1/05_behavior.sysml).
Ein betrieblicher Stopp pausiert den bestehenden Transportauftrag.
Auftrags-ID, Start und Ziel bleiben erhalten. Die Fortsetzung erfordert eine
ausdrückliche manuelle Freigabe sowie die vorhandenen Sicherheitsvoraussetzungen.
Nach der Freigabe folgt `orderAccepted`; erst `RouteReady` erlaubt wieder
`driving`. Details beschreibt die [Pausenregel](operational-pause.md).

Der logische Simulationsprüfstand trennt Roboter, Welt, Steuerungsadapter und
Beobachter. Referenzdaten des Beobachters dienen der Verifikation; sie dürfen
nicht implizit als Sensordaten in die Navigationssteuerung gelangen.
Die Struktur startet noch keinen Simulator und berechnet keine Fahrzeugphysik.

Die [A.1-Traceability-Matrix](../sysml/baseline_a1/traceability_matrix.md)
verknüpft Anforderungen, Verantwortlichkeiten, Schnittstellen und geplante Tests.
Die [B.1-Matrix](../sysml/baseline_b1/traceability_matrix.md) ergänzt Use Cases
und Kandidatenanforderungen. Für eine spätere Implementierung müssen
Codeartefakt, Konfiguration, Testaufbau und beobachtetes Ergebnis ergänzt werden.

## Noch festzulegen

- Simulator, Weltgeometrie und Kopplung der Steuerungssoftware.
- Rechner, Sensorik, Motorregelung und Energieversorgung.
- Nutzlastdaten, Aufnahme und Sicherung des Werkstückträgers.
- Quantitative Toleranzen, Messverfahren und Sicherheitskonzept.
- Wiederanlauf nach Blockade, technischem Fehler oder Sicherheitsstopp.

Etwa 0,5 m/s und etwa zwei Stunden Betrieb sind bisherige Zielwerte.
Auslegung, Toleranzen und reale Nachweise bleiben offen.

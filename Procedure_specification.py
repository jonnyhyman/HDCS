"""
    This file is part of HDCS.

    HDCS is free software: you can redistribute it and/or modify
    it under the terms of the GNU General Public License as published by
    the Free Software Foundation, either version 3 of the License, or
    (at your option) any later version.

    HDCS is distributed in the hope that it will be useful,
    but WITHOUT ANY WARRANTY; without even the implied warranty of
    MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the
    GNU General Public License for more details.

    You should have received a copy of the GNU General Public License
    along with HDCS.  If not, see <http://www.gnu.org/licenses/>.
"""

Procedures = {}

# BE CAREFUL TO KEEP THE TRAILING "," ; and NEVER USE : COLONS
# THESE COMMANDS RUN THROUGH AN EVAL() SO BE CAREFUL!
'''
Procedures[0.00] = [ ('Stp: ADCS Connect',"self.gui.State['adcs']"),
                        ("""Nte: If attempts failing, \n try "connect to adcs" button""",),

                     ('Stp: Power up BUS 1',"self.gui.State['B1']"),
                        ('Sub: Observe V1 to 12V',"self.gui.State['v1']>11"),
                     ('Stp: Power up BUS 2',"self.gui.State['B2']"),
                        ('Sub: Observe V2 to 12V',"self.gui.State['v2']>11"),
                   ]

Procedures[0.02] = [("Nte: Countdown Procedure",),
                    ('Stp: Test Matrix Upload Successful',),
                    ('Stp: Engage ARM & Observe State',"self.gui.State['a']","self.gui.arm_button.isChecked()"),
                    ('Stp: Engage Countdown',"self.gui.State['Cm']==1","self.gui.count_button.isChecked()"),
                    ]
'''

# ---------- NORMAL PROCEDURES

Procedures[0.00] = [("Nte: Welcome to HDCS!",),
                    ("Nte: Always confirm procedures!",),
                    ("Nte: Test safely!",),
                    ]

Procedures[0.1] = [("Nte: N2O Tank Fill",),
                    ('Stp: Confirm UFA CLOSED',),
                    ('Stp: Confirm Ball Valve CLOSED',),
                    ('Stp: Confirm Fill Valve CLOSED',),

                    ('Stp: Run tank mass sensor tared',),
                    ('Stp: Confirm location of nearest fire extinguisher',),

                    ('Stp: Thermal gloves ON',),

                    ('Stp: Valve opening flow',),
                    ('Stp: While Mass < Tgt Mass',),
                        ('Sub: Tank fill flow',),

                    ('Stp: Valve closing flow',),

                    ('Nte: Now we must purge the lines',),
                    ('Stp: Thermal gloves ON',),

                    ('Stp: Venting flow',),

                    ('Stp: Confirm UFA CLOSED',),
                    ('Stp: Confirm Ball Valve CLOSED',),
                    ('Stp: Confirm Fill Valve CLOSED',),
                    ('Stp: 0.2 N2O Tank Storage',),
                    ('Stp: Power buses OFF',"self.gui.State['B1']==0","self.gui.State['B2']==0"),
                    ('Stp: Closeout Flow',),
                    ]

Procedures[0.2] = [("Nte: N2O Tank Storage",),
                    ('Stp: Affix in storage location, with the area properties',),
                        ('Sub: Tie tank to an electrical earth',),
                        ('Sub: Ensure area allows tank ambient temperature to never exceed 52C / 125F',),
                    ('Nte: No combustibles in the vicinity',),
                    ('Nte: No electrical cabling in the vicinity',),
                    ('Nte: Not near emergency exits (or in the path of any)',),
                    ('Nte: Upon a non-combustible surface',),
                    ('Nte: Has an easily accessible fire extinguisher nearby',),
                    ('Nte: Do not weld in the vicinity',),
                    ]

Procedures[0.5] = [("Nte: Power Up [below the line]",),
                    ('Stp: Connect to F2_NET',),
                    ('Nte: Passkey  = BeSafe_UseOften',),
                    ('Stp: Open Command_F2 on HCS2',),
                    ('Stp: ADCS Checkout',),
                        ('Sub: Verify internal temperature OK',
                            "self.gui.State['it'] > self.gui.State_Limits['it'][0]",
                            "self.gui.State['it'] < self.gui.State_Limits['it'][1]"),
                        ('Sub: Verify HACS connected by pulsing STOP & ARM',),
                        ('Sub: Verify HDCS connected by pulsing STOP & ARM',),
                    ('Stp: Pressurize fire suppression',),
                        ('Sub: Open primary valve slowly, entirely',),
                        ('Sub: Open secondary valve slowly, entirely',),
                        ('Sub: Verify no leaks on fire suppression',),

                    ('Stp: Firing Zone closeout',),
                        ('Sub: Water douse w/F3',),
                        ('Sub: Test F1',),
                        ('Sub: Test F2',),
                        ('Sub: Test load cell calibrations with 10lb / 44.48N reference',),
                        ('Sub: Mount cameras and verify WiFi active',),
                  ]

Procedures[0.6] = [("Nte: Test Run Activation [below the line]",),
                    ('Stp: Verify DCL GO',
                        "self.gui.State['dt'] < 1",
                        "self.gui.State['adcs']"),
                    ('Stp: Sensors check, announce each "GO/NOGO"',),
                        ('Sub: avg ||Zx|| > 0.3N? > 1.2',
                            "abs(self.gui.averages['zf']['avg'])<1.2"),
                        ('Sub: T1 or T2 intermittent? > 1.1',
                            "self.gui.averages['t1']['avg']>0",
                            "self.gui.averages['t2']['avg']>0"),
                        ('Sub: IT >= 44C, abort > 0.7',
                            "self.gui.State['it'] < 44"),
                    ('Stp: Test-Matrix Upload, note log #',),
                    ('Stp: “Log #(X), Test #(Y) [list events]”',),
                    ('Stp: Initiate camera recording',),
                    ('Stp: First test after hardware-reset?',),
                        ('Sub: Safety briefing',),
                    ('Stp: Valve opening on F3',),
                    ('Stp: Valve opening on N2O',"self.gui.State['p0']>1"),
                        ('Nte: Do not open quickly,',),
                        ('Nte: prevent adiabatic compression',),

                    ('Stp: Initiate COUNT, 3,2,1 MARK',
                        "self.gui.State['Cm']==1",
                        "self.gui.count_button.isChecked()"),
                    ('Stp: T-360 All Cameras Recording',),
                    ('Stp: T-120 Verify HACS RSSI 970 or less',),
                    ('Stp: T-90 ARM & OBSERVE STATE',
                        "self.gui.State['a']",
                        "self.gui.arm_button.isChecked()"),
                    ('Stp: T-40 HDCS Log ON','self.gui.log.active',),
                    ('Stp: T-30 F1 ON',
                        "self.gui.State['F1']",
                        "self.gui.f1_button.isChecked()"),
                    ('Stp: T-20 Announce "Controllers in Auto Idle"',),
                    ('Stp: >> FIRE CONTROL <<',),
                        ('Sub: >> No Fire? <<',),
                        ('Sub: >> Mild Fire? <<',),
                        ('Sub: >> 911 911 911? <<',),
                    ('Stp: STOP',
                        "self.gui.State['E']",
                        "self.gui.stop_button.isChecked()"),
                    ('Stp: Power buses OFF',"self.gui.State['B1']==0","self.gui.State['B2']==0"),
                    ('Stp: Secure the data',),
                        ('Sub: HDCS Log OFF','self.gui.log.active==0',),
                        ('Sub: Stop camera recording',),
                        ('Nte: Next step disables F1 temp.',),
                        ('Sub: Reset ADCS',),



                    ('Stp: Go to 0.7 [Deactivation]',),
                  ]

Procedures[0.7] = [("Nte: Test Run Deactivation",),
                    ('Stp: Confirm solenoids closed',),
                    ('Stp: Close tertiary fire suppression valve',),
                    ('Nte: Last test? Continue',),
                    ('Stp: Close ALL N2O valves',),
                    ('Sub: Power Buses OFF',"self.gui.State['B1']==0","self.gui.State['B2']==0"),
                    ('Stp: N2O Purge',),
                        ('Sub: Thermal Gloves ON',),
                        ('Sub: Detach injector cap feed line',),
                        ('Nte: [expect venting]',),
                        ('Sub: Power Buses ON',"self.gui.State['B1']==1","self.gui.State['B2']==1"),
                        ('Sub: Open ball valve 1/2 turn',),
                        ('Sub: Open A, B until pressure released from run tank',),
                        ('Sub: Open A, B until pressure released from lines',),
                        ('Stp: Close ALL N2O valves',),
                        ('Sub: Disconnect run tank',),
                        ('Sub: Go to 0.2 [Tank Storage]',),
                  ]

Procedures[0.8] = [("Nte: Power Down",),
                    ('Stp: Power buses OFF',"self.gui.State['B1']==0","self.gui.State['B2']==0"),
                    ('Stp: ADCS OFF',
                        "self.gui.State['dt']>1"),
                    ('Stp: sudo shutdown now',),
                    ("Nte: Monitor HACS LED",),
                    ('Stp: GFCI TEST (OFF)',),
                    ('Stp: N2O BATT DISC',),
                    ('Stp: F2 BATT DISC',),
                    ('Stp: Depressurize all 3 fire suppressions',),

                  ]

# ---------- ABNORMAl PROCEDURES

Procedures[1.0] = [("Nte: ADCS SSH Repeated Failure",),
                    ('Stp: Disable HDCS ethernet',),
                    ('Stp: Connect WLAN to ControlNet',),
                    ('Stp: Try SSH',),
                    ('Stp: sudo ifconfig wlan0 down',),
                        ('Nte: SSH will disconnect',),
                    ('Stp: Reconnect HDCS Ethernet',),
                    ('Stp: Try SSH',),
                  ]

Procedures[1.1] = [("Nte: TC Intermittent Data",),
                    ('Stp: Verify DCL GO',
                        "self.gui.State['dt'] < 1",
                        "self.gui.State['adcs']"),
                    ('Stp: Verify DISARMED',
                        "self.gui.State['a']==0",
                        "self.gui.arm_button.isChecked()==0"),
                    ('Stp: Verify Fire Sup. OFF',
                        "self.gui.State['F1']==0",
                        "self.gui.State['F2']==0",
                        "self.gui.fire_button.isChecked()==0"),
                    ('Stp: Proceed to check connections',),
                        ('Sub: Check affected TC',),
                        ('Nte: 1=left, 2=right',),
                        ('Sub: Check TC braid integrity',),
                  ]


Procedures[1.2] = [("Nte: Loads Retare",),
                    ('Stp: Power buses OFF',"self.gui.State['B1']==0","self.gui.State['B2']==0"),
                    ('Stp: Power buses ON',"self.gui.State['B1']","self.gui.State['B2']"),
                    ('Stp: Reset Micros',),
                    ('Nte: This step needed to reset Micro3',),
                    ('Stp: Wait 1 minute',),
                    ('Stp: If Test Matrix Uploaded, Reupload',),
                  ]

Procedures[1.3] = [("Nte: Gases Software Update",),
                    ('Stp: Power buses OFF',"self.gui.State['B1']==0","self.gui.State['B2']==0"),
                    ('Stp: Unplug the SI Connector',),
                    ('Stp: USB Upload',),
                    ('Stp: Confirm USB cable unplugged and power off',),
                    ('Stp: Plug in the SI connector',),
                    ('Nte: Go for [Power Buses ON] ',),
                  ]

# ---------- EMERGENCY PROCEDURES

Procedures[1.4] = [("Nte: Internal Overtemperature",),
                    ('Stp: Power buses OFF',"self.gui.State['B1']==0","self.gui.State['B2']==0"),
                    ('Nte: ADCS may have done the below',),
                    ('Stp: ADCS OFF',),
                    ('Stp: sudo shutdown now',),
                    ('Stp: GFCI OFF',),
                    ('Stp: N2O BATTERY DISCONN',),
                  ]

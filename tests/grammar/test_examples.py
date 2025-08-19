"""
This module tests examples from the Logix 5000 Controllers Import/Export
Reference Manual, Rockwell Automation publication 1756-RM014C-EN-P
September 2024. The intent is solely to verify the applicable expressions
parse example content without error.
"""

import unittest

import l5k


class Controller(unittest.TestCase):
    """Chapter 2."""

    def test_standard(self):
        """Ref p60.

        CONFIG blocks with invalid attribute placeholders removed.
        """
        l5k.grammar.CONTROLLER.parse_string(
            r"""
            CONTROLLER example_controller (Description := "controller
            description",
            ProcessorType := "1756-L73",
            Major := 22,
            TimeSlice := 20,
            ShareUnusedTimeSlice := 1,
            RedundancyEnabled := 0,
            KeepTestEditsOnSwitchOver := 0,
            DataTablePadPercentage := 50,
            SecurityCode := 0,
            ChangesToDetect := 16#ffff_ffff_ffff_ffff,
            SFCExecutionControl := "CurrentActive",
            SFCRestartPosition := "MostRecent",
            SFCLastScan := "DontScan",
            SerialNumber := 16#0000_0000,
            MatchProjectToController := No,
            CanUseRPIFromProducer := No,
            InhibitAutomaticFirmwareUpdate := 0,
            PassThroughConfiguration := EnabledWithAppend,
            DownloadProjectDocumentationAndExtendedProperties :=
            Yes)
            MODULE Local (Parent := "Local",
            ParentModPortId := 1,
            CatalogNumber := "1756-L73",
            Vendor := 1,
            ProductType := 14,
            ProductCode := 94,
            Major := 22,
            Minor := 1,
            PortLabel := "RxBACKPLANE",
            ChassisSize := 7,
            Slot := 0,
            Mode := 2#0000_0000_0000_0001,
            CompatibleModule := 0,
            KeyMask := 2#0000_0000_0001_1111)
            END_MODULE
            TAG
            END_TAG
            PROGRAM MainProgram (MAIN := "MainRoutine",
            MODE := 0, DisableFlag := 0)
            TAG
            END_TAG
            ROUTINE MainRoutine
            END_ROUTINE
            END_PROGRAM
            TASK MainTask (Type := CONTINUOUS,
            Rate := 10, Priority := 10, Watchdog := 500,
            DisableUpdateOutputs := No, InhibitTask := No)
            MainProgram;
            END_TASK
            PARAMETER_CONNECTION
            END_PARAMETER_CONNECTION
            CONFIG ASCII(XONXOFFEnable := 0,
            DeleteMode := 0, EchoMode := 0,
            TerminationChars := 65293, AppendChars := 2573,
            BufferSize := 82)
            END_CONFIG
            CONFIG ControllerDevice END_CONFIG
            CONFIG CST(SystemTimeMasterID := 0) END_CONFIG
            CONFIG DF1(DuplicateDetection := 1,
            ErrorDetection := BCC Error, EmbeddedResponseEnable
            := 0,
            DF1Mode := Pt to Pt, ACKTimeout := 50,
            NAKReceiveLimit := 3, ENQTransmitLimit := 3,
            TransmitRetries := 3, StationAddress := 0,
            ReplyMessageWait := 5, PollingMode := 1,
            MasterMessageTransmit := 0, NormalPollNodeFile :=
            "<NA>",
            NormalPollGroupSize := 0, PriorityPollNodeFile :=
            "<NA>",
            ActiveStationFile := "<NA>", SlavePollTimeout :=
            3000,
            EOTSuppression := 0, MaxStationAddress := 31,
            TokenHoldFactor := 1, EnableStoreFwd := 0,
            StoreFwdFile := "<NA>")
            END_CONFIG
            CONFIG FileManager END_CONFIG
            CONFIG SerialPort(BaudRate := 19200,
            Parity := No Parity, DataBits := 8 Bits of Data,
            StopBits := 1 Stop Bit, ComDriverId := DF1,
            PendingComDriverId := DF1, RTSOffDelay := 0,
            RTSSendDelay := 0, ControlLine := No Handshake,
            PendingControlLine := No Handshake,
            RemoteModeChangeFlag := 0,
            PendingRemoteModeChangeFlag := 0,
            ModeChangeAttentionChar := 27,
            PendingModeChangeAttentionChar := 27,
            SystemModeCharacter := 83,
            PendingSystemModeCharacter := 83,
            UserModeCharacter := 85,
            PendingUserModeCharacter := 85,
            DCDWaitDelay := 0)
            END_CONFIG
            CONFIG WallClockTime(LocalTimeAdjustment := 0, TimeZone := 0)
            END_CONTROLLER
            """
        )

    def test_safety(self):
        """Ref p63.

        CONFIG blocks with invalid attribute placeholders removed.
        """
        l5k.grammar.CONTROLLER.parse_string(
            r"""
            CONTROLLER example_safety_controller (Description :=
            "Safety Project",
            ProcessorType := "1756-L73S",
            Major := 22,
            TimeSlice := 20,
            ShareUnusedTimeSlice := 1,
            RedundancyEnabled := 0,
            KeepTestEditsOnSwitchOver := 0,
            DataTablePadPercentage := 50,
            SecurityCode := 0,
            ChangesToDetect := 16#ffff_ffff_ffff_ffff,
            SFCExecutionControl := "CurrentActive",
            SFCRestartPosition := "MostRecent",
            SFCLastScan := "DontScan",
            SerialNumber := 16#0000_0000,
            MatchProjectToController := No,
            CanUseRPIFromProducer := No,
            SafetyLocked := No,
            SignatureRunModeProtect := No,
            ConfigureSafetyIOAlways := No,
            InhibitAutomaticFirmwareUpdate := 0,
            PassThroughConfiguration := EnabledWithAppend,
            DownloadProjectDocumentationAndExtendedProperties :=
            Yes)
            MODULE Local (Parent := "Local",
            ParentModPortId := 1,
            CatalogNumber := "1756-L73S",
            Vendor := 1,
            ProductType := 14,
            ProductCode := 148,
            Major := 22,
            Minor := 1,
            PortLabel := "RxBACKPLANE",
            ChassisSize := 7,
            Slot := 0,
            Mode := 2#0000_0000_0000_0001,
            CompatibleModule := 0,
            KeyMask := 2#0000_0000_0001_1111,
            SafetyNetwork :=
            16#0000_3c77_0315_5105)
            END_MODULE
            MODULE example_safety_controller:Partner
            (Parent := "Local", ParentModPortId := 1,
            CatalogNumber := "1756-L7SP", Vendor := 1,
            ProductType := 14, ProductCode := 146,
            Major := 22, Minor := 1,
            PortLabel := "RxBACKPLANE", Slot := 1,
            Mode := 2#0000_0000_0000_0000,
            CompatibleModule := 0,
            KeyMask := 2#0000_0000_0001_1111,
            SafetyNetwork := 16#0000_0000_0000_0000)
            END_MODULE
            TAG
            END_TAG
            PROGRAM MainProgram (Class := Standard,
            MAIN := "MainRoutine", MODE := 0,
            DisableFlag := 0)
            TAG
            END_TAG
            ROUTINE MainRoutine
            END_ROUTINE
            END_PROGRAM
            PROGRAM SafetyProgram (Class := Safety,
            MAIN := "MainRoutine", MODE := 0,
            DisableFlag := 0)
            TAG
            END_TAG
            ROUTINE MainRoutine
            END_ROUTINE
            END_PROGRAM
            TASK MainTask (Type := CONTINUOUS,
            Class := Standard, Rate := 10,
            Priority := 10, Watchdog := 500,
            DisableUpdateOutputs := No, InhibitTask := No)
            MainProgram;
            END_TASK
            TASK SafetyTask (Type := PERIODIC,
            Class := Safety, Rate := 20,
            Priority := 10, Watchdog := 20,
            DisableUpdateOutputs := No, InhibitTask := No)
            SafetyProgram;
            END_TASK
            PARAMETER_CONNECTION
            END_PARAMETER_CONNECTION
            CONFIG ASCII(XONXOFFEnable := 0,
            DeleteMode := 0, EchoMode := 0,
            TerminationChars := 65293,
            AppendChars := 2573, BufferSize := 82)
            END_CONFIG
            CONFIG ControllerDevice END_CONFIG
            CONFIG CST(SystemTimeMasterID := 0) END_CONFIG
            CONFIG DF1(DuplicateDetection := 1,
            ErrorDetection := BCC Error,
            EmbeddedResponseEnable := 0,
            DF1Mode := Pt to Pt, ACKTimeout := 50,
            NAKReceiveLimit := 3, ENQTransmitLimit := 3,
            TransmitRetries := 3, StationAddress := 0,
            ReplyMessageWait := 5, PollingMode := 1,
            MasterMessageTransmit := 0,
            NormalPollNodeFile := "<NA>",
            NormalPollGroupSize := 0,
            PriorityPollNodeFile := "<NA>",
            ActiveStationFile := "<NA>",
            SlavePollTimeout := 3000, EOTSuppression := 0,
            MaxStationAddress := 31, TokenHoldFactor := 1,
            EnableStoreFwd := 0, StoreFwdFile := "<NA>")
            END_CONFIG
            CONFIG FileManager END_CONFIG
            CONFIG SerialPort(BaudRate := 19200,
            Parity := No Parity, DataBits := 8 Bits of Data,
            StopBits := 1 Stop Bit, ComDriverId := DF1,
            PendingComDriverId := DF1, RTSOffDelay := 0,
            RTSSendDelay := 0, ControlLine := No Handshake,
            PendingControlLine := No Handshake,
            RemoteModeChangeFlag := 0,
            PendingRemoteModeChangeFlag := 0,
            ModeChangeAttentionChar := 27,
            PendingModeChangeAttentionChar := 27,
            SystemModeCharacter := 83,
            PendingSystemModeCharacter := 83,
            UserModeCharacter := 85,
            PendingUserModeCharacter := 85, DCDWaitDelay :=
            0) END_CONFIG
            CONFIG WallClockTime(LocalTimeAdjustment := 0,
            TimeZone := 0)
            END_CONTROLLER
            """
        )


class DataType(unittest.TestCase):
    """Chapter 3."""

    def test_bits(self):
        """Ref p73."""
        l5k.grammar.DATATYPE.parse_string(
            r"""
            DATATYPE MyBits (FamilyType := NoFamily)
            SINT ZZZZZZZZZZMyBits0 (Hidden := 1);
            BIT MyBit0 ZZZZZZZZZZMyBits0 : 0 (Radix := Binary);
            BIT MyBit1 ZZZZZZZZZZMyBits0 : 1 (Radix := Binary);
            END_DATATYPE
            """
        )

    def test_datatype(self):
        """Ref p75."""
        l5k.grammar.DATATYPE.parse_string(
            r"""
            DATATYPE MyStructure (FamilyType := NoFamily)
            DINT x;
            TIMER y[3] (Radix := Decimal);
            SINT MyFlags (Hidden :=1);
            BIT aBit0 MyFlags : 0 (Radix := Binary);
            BIT aBit1 MyFlags : 1 (Radix := Binary);
            END_DATATYPE
            """
        )


class Module(unittest.TestCase):
    """Chapter 4."""

    def test_module(self):
        """Ref p90.

        Converted via OCR.
        """
        l5k.grammar.MODULE[3].parse_string(
            r"""
            MODULE Local (Parent := Local ,
            ParentModPortid := 1,
            Catalognumber := "1756-L62",
            vendor := 1,
            ProductType := 14,
            Productcode := 55,
            Major := 17,
            Minor := 1,
            PortLabel := "RxBACKPLANE",
            Chassissize := 10,
            Slot := 0,
            Mode := 2#0000_0000_0000_0001,
            Compatiblemodule := 0,
            KeyMask := 2#0000_0000_0001_1111)
            END_MODULE
            MODULE DHRIO_Module (Parent := "Local",
            ParentModPortid := 1,
            Catalognumber := "1756-DHRIO/B",
            vendor := 1,
            ProductType := 12,
            Productcode := 18,
            Major := 2,
            Minor := 1,
            PortLabel := "RxBACKPLANE",
            Slot :=1,
            Commmethod := 536870913,
            Configmethod := 8388609,
            Mode := 2#0000_0000_0000_0000,
            Compatiblemodule := 1,
            KeyMask := 2#0000_0000_0001_1111,
            ChaBaud := 57.6,
            CheBaud := 57.6)
            CONNECTION Standard (Rate := 25000,
            EventID := 0)
            InputData := [0,0];
            InputForceData := [0,0,0,0,0,0,0,0,0,0,0,0];
            END_CONNECTION
            END_MODULE
            MODULE Output_Module (Parent := Local ,
            ParentModPortid := 1,
            Catalognumber := "1756-0B16D",
            vendor := 1,
            ProductType := 7,
            Productcode := 4,
            Major := 3,
            Minor := 1,
            PortLabel := "RxBACKPLANE",
            Slot := 2,
            Commmethod := 536870914,
            Configmethod := 8388612,
            Mode := 2#0000_0000_0000_0000,
            Compatiblemodule := 1,
            KeyMask := 2#0000_0000_0001_1111)
            Configdata := [44,19,1,0,0,0,0,0,0,0,65535, 65535, 65535,0];
            CONNECTION Diagnostic (Rate := 20000,
            EventID := 0)
            InputData := [0,0, [0,0],0,0,0,0];
            InputForceData :=
            [0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,
            0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0
            ,0,0,0,0,0,0,0,0,0,0,0,0,0, 0];
            OutputData := [0];
            OutputForceData := [0,0,0,0,0,0,0,0,0,0,0,0];
            END_CONNECTION
            END_MODULE
            """
        )

    def test_safety_partner(self):
        """Ref p91.

        Converted via OCR.
        """
        l5k.grammar.MODULE.parse_string(
            r"""
            MODULE SaTetyProject:Partner (Description := "My SaTtety Project!",
            Parent := "Local",
            ParentModPortid := 1,
            Catalognumber := "1756-LSP",
            vendor := 1,
            ProductType := 14,
            Productcode := 69,
            Major := 17,
            Minor := 1,
            PortLabel := "RxBACKPLANE",
            Slot := 4,
            Mode := 2#0000_0000_0000_0000,
            Compatiblemodule := 0,
            Keymask := 2#0000_0000_0001_1111,
            safetynetwork := 16#0000_0000_0000_0000)
            END_MODULE
            """
        )


class AddOnInstruction(unittest.TestCase):
    """Chapter 5."""

    def test_encoded(self):
        """Ref p110."""
        l5k.grammar.ADD_ON_INSTRUCTION.parse_string(
            r"""
            ENCODED_DATA (EncodedType := ADD_ON_INSTRUCTION_DEFINITION,
            Name := "Conveyor_Control",
            Description := "This is the description",
            Revision := "1.0",
            RevisionNote := "This is a Revision Note",
            Vendor := "vendor",
            SignatureID := AC2CCC57,
            SignatureTimestamp := "2014-05-20T14:04:14.807Z",
            EditedDate := "2014-05-20T14:04:14.807Z",
            AdditionalHelpText := "This is help text",
            EncryptionConfig := 3)
            HISTORY_ENTRY (User := RA-INT\JBieder2,
            Timestamp := "2014-05-20T00:15:08.867Z",
            SignatureID := 16#52db_eb8a,
            Description := "History description")
            END_HISTORY_ENTRY
            PARAMETERS
            EnableIn : BOOL (Description := "Enable Input - System Defined Parameter",
            Usage := Input,
            RADIX := Decimal
            Required := No,
            Visible := No,
            ExternalAccess := Read Only);
            EnableOut : BOOL (Description := "Enable Output - System Defined Parameter",
            Usage := Output,
            RADIX := Decimal,
            Required := No,
            Visible := No,
            ExternalAccess := Read Only);
            END_PARAMETERS
            5PC4UUeSPrD8+QMe30neT5/97J+VmK95qgOApHiZ7VpmkuGyeYVmzDm3ceYND35YMmzC4xyFQfJYld...
            END_ENCODED_DATA
            """
        )

    def test_unencoded_standard(self):
        """Ref p113.

        Slanted quotation marks replaced with straight quotes.
        """
        l5k.grammar.ADD_ON_INSTRUCTION.parse_string(
            r"""
            ADD_ON_INSTRUCTION_DEFINITION Valve (Description := "Simple valve control",
            Revision := "1.0", RevisionExtension := "B",
            Vendor := "RaesUDICreationsUnlimited", ExecutePrescan := Yes,
            ExecutePostscan := No, ExecuteEnableInFalse := No,
            CreatedBy := "apollo\drjones", EditedDate := "2005-01-05T15:24:59.188Z",
            EditedBy := "apollo\drjones",
            AdditionalHelpText := "My first Add-On Instruction – how cool!")
            PARAMETERS
            Valve_Command : BOOL (Description := "0 - Close valve$N1 - Open valve",
            Radix := Decimal, Required := Yes, Visible := Yes, DefaultData := "1");
            Array_Parameter : REAL[5] (Type := InOut, Radix := Float, Required := Yes,
            Visible := Yes); Valve_Out : DINT (Type := Output, Radix := Decimal,
            Required := No, Visible := Yes, DefaultData := "0");
            Reset : BOOL (Description := "Used by Prescan routine to run Reset code",
            Type := Input, Radix := Decimal, Required := No, Visible := No,
            DefaultData := "1");
            END_PARAMETERS
            LOCAL_TAGS
            Valve_Type : DISCRETE_2STATE (Description := "The valve is a 2 state valve",
            DefaultData := "[49,0.00000000e+000,0,0,0.00000000e+000,0.00000000e+000,
            0.00000000e+000,0.00000000e+000,0.00000000e+000,0.00000000e+000]");
            END_LOCAL_TAGS
            FBD_ROUTINE Logic (Description := "This UDI Logic routine is nonsense but shows the
            format sufficiently. In fact, it does not even use the InOut Parameter",
            SheetSize := "Letter (8.5x11in)", SheetOrientation := Landscape)
            SHEET (Name := "")
            D2SD_BLOCK (ID := 0, X := 200, Y := 160, Operand := Valve_Type,
            VisiblePins := "ProgCommand, State0Perm, State1Perm, FB0, FB1,
            HandFB, ProgProgReq, ProgOperReq, ProgOverrideReq, ProgHandReq,
            Out, Device0State, Device1State, CommandStatus, FaultAlarm,
            ModeAlarm, ProgOper, Override, Hand")
            END_D2SD_BLOCK
            IREF (ID := 1, X := 120, Y := 100, Operand := Valve_Command)
            END_IREF
            OREF (ID := 2, X := 460, Y := 140, Operand := Valve_Out)
            END_OREF
            END_SHEET
            END_FBD_ROUTINE
            ST_ROUTINE Prescan (Description := "This should run before the Instruction does")
            '//If Reset is True - do something
            'IF (Reset) THEN
            ' //do something
            'END_IF;
            '
            END_ST_ROUTINE
            END_ADD_ON_INSTRUCTION_DEFINITION
            """
        )

    def test_unencoded_safety(self):
        """Ref p115.

        Brevity deletion comment removed & END_HISTORY_ENTRY spacing
        corrected.

        Slanted quotation marks replaced with straight quotes.
        """
        l5k.grammar.ADD_ON_INSTRUCTION.parse_string(
            r"""
            ADD_ON_INSTRUCTION_DEFINITION HI_SafetyAOI (Description
            := "sealed safety AOI",
            Revision := "1.0", RevisionExtension := "B",
            RevisionNote := "Original release to library",
            Vendor := "AOICreationsUnlimited", Class := Safety,
            ExecutePrescan := Yes,
            ExecutePostscan := No, ExecuteEnableInFalse := No,
            CreatedDate := "2009-01-05T15:24:59.188Z", CreatedBy
            := "apollo\drjones",
            EditedDate := "2009-02-25T15:05:52.042Z", EditedBy :=
            "apollo\drjones",
            AdditionalHelpText := "My first HI Safety Add-On
            Instruction")
            HISTORY_ENTRY (User := "apollo\drjones",
            Timestamp := "2009-01-05T15:24:59.188Z", SignatureID
            := 68F42D31,
            Description := "My First History Entry!")
            END_HISTORY_ENTRY
            HISTORY_ENTRY (User := "apollo\drjones",
            Timestamp := "2009-02-03T10:24:19.760Z", SignatureID
            := C7013D42,
            Description := "My Second History Entry!")
            END_HISTORY_ENTRY
            HISTORY_ENTRY (User := "apollo\drjones",
            Timestamp := "2009-02-25T15:05:52.042Z", SignatureID
            := F4E691A2,
            Description := "My Last History Entry!")
            END_HISTORY_ENTRY
            END_ADD_ON_INSTRUCTION_DEFINITION
            """
        )


class Tag(unittest.TestCase):
    """Chapter 6."""

    def test_tag(self):
        """Ref p164."""
        l5k.grammar.TAG.parse_string(
            r"""
            TAG
            bits : MySint := [0];
            dest : INT (RADIX := Decimal) := 0;
            overflow OF bits.MyBit0 (RADIX := Binary);
            source : REAL (RADIX := Exponential) := 0.0;
            timer : TIMER[3] := [[0,0,100],[0,10,100],[0,0,50]];
            END_TAG
            """
        )

    def test_forced_tag_data(self):
        """Ref p165."""
        l5k.grammar.TAG.parse_string(
            r"""
            TAG
            dint_a : DINT (RADIX := Decimal) := 0;
            int_a : INT (RADIX := Decimal) := 0;
            tag_a : UDT_A (ProduceCount := 2) := [0,0],
            TagForceData := [0,0,0,0,1,0,-1,-1,1,0,-72,34];
            END_TAG
            """
        )

    def test_consumed_safety(self):
        """Ref p166."""
        l5k.grammar.tag_definition.parse_string(
            r"""
            safetyConsumed : mypcType (Class := Safety,
            Producer := PeerSafetyController,
            RemoteTag := productCount,
            RemoteFile := 0,
            RPI := 10,
            IncludeConnectionStatus := Yes,
            TimeoutMultiplier := 2,
            NetworkDelayMultiplier := 100,
            ReactionTimeLimit := 29.952) := [[2],[0,0,0]],
            TagForceData :=
            [0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0];
            """
        )

    def test_produced_safety(self):
        """Ref p166."""
        l5k.grammar.tag_definition.parse_string(
            r"""
            safetyProduced : mypcType (Class := Safety,
            ProduceCount := 3,
            ProgrammaticallySendEventTrigger := Yes,
            IncludeConnectionStatus := Yes) := [[0],[0,0,0]],
            TagForceData :=
            [0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0];
            """
        )

    def test_alarm(self):
        """Ref p168.

        Converted via OCR.
        """
        l5k.grammar.tag_definition[2].parse_string(
            r"""
            my_alarm2 : ALARM_ANALOG (ALMSG.HH:en-us := "High high alarm message",
            ALMMSG.POS:en-us := "pos alarm message", ALMMSG.NEG:en-us := "neg alarm message",
            EnableIn := false, InFault := false, HHEnabled := true, HEnabled := false,
            LEnabled := false, LLEnabled := false, AckRequired := true, ProgAckAll := false,
            OperAckAll := false, HHProgAck := false, HHOperAck := false, HProgAck := false,
            HOperAck := false, LProgAck := false, LOQperAck := false, LLProgAck := false,
            LLOperAck := false, ROCPosProgAck := false, ROCPosOperAck := false,
            ROCNegProgAck := false, ROCNegOperAck := false, ProgSuppress := false,
            OperSuppress := false, ProgUnsuppress := false, OperUnsuppress := false,
            ProgDisable := false, OperDisable := false, ProgEnable := false, OperEnable := false,
            AlarmCountReset := false, In := 0.0, HHLimit := 0.0, HHSeverity := 500,
            HLimit := 0.0, HSeverity := 500, LLimit := 0.0, LSeverity := 500, LLLimit := 0.0,
            LLSeverity := 500, MinDurationPRE := 0, Deadband := 0.0, ROCPosLimit := 0.0,
            ROCPosSeverity := 500, ROCNegLimit := 0.0, ROCNegSeverity := 500, ROCPeriod := 0.0,
            AssocTagl := "PlantNumber", AssocTag2 := "ShiftNumber", AssocTag3 := "BatchNumber",
            AssocTag4 := "LotNumber", AlarmClass := "tank2", HMICmd := "ft command");

            my_alarm : ALARM DIGITAL (ALMMSG.AM:en-us := "my message",
            Severity := 500, MinDurationPRE := 0, ProgTime := DT#1970-01-01-00:00:00.000000Z,
            EnableIn := false, In := false, InFault := false, Condition := true,
            AckRequired := true, Latched := false, ProgAck := false, OperAck := false,
            ProgReset := false, OperReset := false, ProgSuppress := false OperSuppress := false,
            ProgUnsuppress := false, OperUnsuppress := false, ProgDisable := false,
            OperDisable := false, ProgEnable := false, OperEnable := false,
            AlarmCountReset := false, AssocTagl := "BatchNumber", AssocTag2 := "LotNumber",
            AssocTag3 := "PlantNumber", AssocTag4 := "ShiftNumber", AlarmClass := "tank1",
            HMICmd := "ft command");
            """
        )


class Alarm(unittest.TestCase):
    """Chapter 7."""

    def test_alarm_condition(self):
        """Ref p170."""
        l5k.grammar.ALARM_CONDITION.parse_string(
            r"""
            ALARM_CONDITION PVHH (Name := "PVHH",
            AlarmConditionDefinition := "PVHH",
            Input := "test.PVFault",
            ConditionType := "TRIP",
            Limit := 0.0,
            Severity := 500,
            OnDelay := 500,
            OffDelay := 1000,
            DefaultShelveDuration := 0,
            MaxShelveDuration := 0,
            Deadband := 0.0,
            Used := true,
            InFault := false,
            AckRequired := true,
            Latched := false,
            ProgAck := false,
            OperAck := false,
            ProgReset := false,
            OperReset := false,
            ProgSuppress := false,
            OperSuppress := false,
            ProgUnsuppress := false,
            OperUnsuppress := false,
            OperShelve := false,
            ProgUnshelve := false,
            OperUnshelve := false,
            ProgDisable := false,
            OperDisable := false,
            ProgEnable := false,
            OperEnable := false,
            AlarmCountReset := false,
            AlarmSetOperIncluded := false,
            AlarmSetRollupIncluded := false,
            EvaluationPeriod := 2,
            Expression := 19,
            AssocTag1 := "test.EnableIn",
            AssocTag2 := "test.SPHLimit",
            AssocTag3 := "test.SPLLimit")
            END_ALARM_CONDITION
            """
        )

    def test_alarm_condition_with_message(self):
        """Ref p172."""
        l5k.grammar.ALARM_CONDITION.parse_string(
            r"""
            ALARM_CONDITION HH (ALMMSG.CAM:zh-TW := "mmm",
            Name := "HH",
            Input := "\MainProgram.bool",
            ConditionType := "TRIP",
            Limit := 0.0,
            Severity := 500,
            OnDelay := 0,
            OffDelay := 0,
            DefaultShelveDuration := 0,
            MaxShelveDuration := 0,
            Deadband := 0.0,
            Used := true,
            InFault := false,
            AckRequired := true,
            Latched := false,
            ProgAck := false,
            OperAck := false,
            ProgReset := false,
            OperReset := false,
            ProgSuppress := false,
            OperSuppress := false,
            ProgUnsuppress := false,
            OperUnsuppress := false,
            OperShelve := false,
            ProgUnshelve := false,
            OperUnshelve := false,
            ProgDisable := false,
            OperDisable := false,
            ProgEnable := false,
            OperEnable := false,
            AlarmCountReset := false,
            AlarmSetOperIncluded := true,
            AlarmSetRollupIncluded := true,
            EvaluationPeriod := 2,
            Expression := 128,
            AlarmClass := "aaa",
            HMICmd := "ccc")
            END_ALARM_CONDITION
            """
        )

    def test_alarm_definition(self):
        """Ref p179."""
        l5k.grammar.ALARM_DEFINITION.parse_string(
            r"""
            ALARM_DEFINITION PVHH (ALMMSG.ADM:en-US := "PIDE Message 3",
            ALMMSG.ADM:zh-TW := "This is my message",
            Name := "PVHH",
            Input := "PID_ENHANCED.PVFault",
            ConditionType := "TRIP",
            Limit := 0.0,
            Severity := 500,
            OnDelay := 500,
            OffDelay := 1000,
            DefaultShelveDuration := 0,
            MaxShelveDuration := 0,
            Deadband := 0.0,
            Required := true,
            InFault := false,
            AckRequired := true,
            Latched := false,
            AlarmSetOperIncluded := false,
            AlarmSetRollupIncluded := false,
            EvaluationPeriod := 2,
            Expression := 19,
            AssocTag1 := "PID_ENHANCED.EnableIn",
            AssocTag2 := "PID_ENHANCED.SPHLimit",
            AssocTag3 := "PID_ENHANCED.SPLLimit",
            AlarmClass := "My Class",
            HMICmd := "My FT View Command")
            END_ALARM_DEFINITION
            """
        )


class Program(unittest.TestCase):
    """Chapter 8."""

    def test_source_protected(self):
        """Ref p192.

        Coverted via OCR.
        """
        l5k.grammar.ROUTINE.parse_string(
            r"""
            ENCODED_DATA (EncodedType := ROUTINE,
            Name := "Processcontro1",
            Description := "description on routine",
            Type := SFC,
            EncryptionConfig := 2)

17r8GxtsZCMLfk3JHFYmU7emZMNhRh90EUUPQb5IKS676d/XRznQ+56vf8IVQNNEIDODL1U+UEC301MDetvnJAX2CdwNPRNC1N3CjPApchCL95hdF1y2x3/T47RDSI1299b1XN5v5XUQTGlevktB6dspatujrGLLTf4mOEdFVHMD9qQTNep+e/M9V9Cx51z2s4xc3R1130F9KKobr7j1RdDmAuyRRZLYKTE01ZDpZAS9A1cebPoYuhM1gCF1AUK9eYBkzm/VI5gpH400Vuci/xdt0/9/xPPXKizjoDI2ZOPFdkz74VoGrL43WKONOX2WPC/u4RCCDehNMXBdsYffba1uIvy9FDrJwxod/K8wrIn6BWOkLeBy1VGXCUCxa8oyersEhBLZ6nTYd/wybHvNmpOTLgpI1bhzwyTvttwf4Zw8qBN6Yu762cuwba/btkCQ40uic6Mit6vMt/TFUR4503Hw/dwGPKUaXDBNBbbBVDB11FnCORX/vtt6LwKwozaEVI76sojhC8mNJOLUBdPtZoLafqSF20Mbwedr9Cw6w
            END_ENCODED_DATA
            """
        )

    def test_program(self):
        """Ref p193.

        Converted via OCR.
        """
        l5k.grammar.PROGRAM.parse_string(
            r"""
            PROGRAM MainProgram (MAIN := "MainRoutine",
            MODE := 0,
            DisableFlag := 0,
            UseAsFolder := 0)
            TAG
            Test_CurrentDate : BOOL (RADIX := Decimal) := 0;
            END_TAG

            ROUTINE MainRoutine
            RC: "Get the Controllers real time clock broken down
            by Year, month, day...microseconds and store in a tag so that the values can be used.";
            N: XIC(Test_CurrentDate)GSV
            (WALLCLOCKTIME,,DateTime,TestDateTime.Year);
            END_ROUTINE
            CHILD_PROGRAMS
            Program010010
            END_CHILD_PROGRAMS
            END_PROGRAM
            """
        )

    def test_equipment_phase(self):
        """Ref p194.

        Converted via OCR.
        """
        l5k.grammar.PROGRAM.parse_string(
            r"""
            PROGRAM Add_Cream_M2 (Type := EquipmentPhase,
            MODE := 0,
            DisableFlag := 0,
            InitialstepIndex := 0,
            Initialstate := Idle,
            CompletestateIfNotImpl := statecomplete,
            Lossofcommcmd := None,
            ExternalRequestaction := None
            UseAsFolder := 0)
            TAG
            MyCounter : DINT (RADIX := Decimal) := 0;
            END_TAG

            ST-ROUTINE Running
            '//
            '// All information provided "as Is" -- No warranty or implied merchantability.
            '// Refer to the RSLogix 5000 End User License Agreement CEULA) in the Release Notes.
            '//
            '
            'Mycounter := MyCounter + 1;
            'if (Mycounter > MAX_COUNT) then
            ' PSC();
            ' MyCounter := 0;
            'endif;
            '
            END_ST_ROUTINE
            CHILD_PROGRAMS
            Program010010
            END_CHILD_PROGRAMS
            END_PROGRAM
            """
        )


class LadderLogicRoutine(unittest.TestCase):
    """Chapter 9."""

    def test_routine(self):
        """Ref p199."""
        l5k.grammar.ROUTINE.parse_string(
            r"""
            ROUTINE Ladder_example
            RC: "This is a rung comment for the first rung.";
            N: XIC(input1)XIC(input2)OTE(output1)OTE(output2);
            RC: "This is a rung comment for the second rung.";
            N: XIC(input3)OTE(output3);
            END_ROUTINE
            """
        )

    def test_single_branch(self):
        """Ref p200."""
        l5k.grammar.rung_logic.parse_string(
            r"""
            N: XIC(conveyor_a)[,XIC(input_1) XIO(input_2) ]OTE(light_1);
            """
        )

    def test_two_branches(self):
        """Ref p200."""
        l5k.grammar.rung_logic.parse_string(
            r"""
            N: XIC(conveyor_b)[,XIC(input_1) XIO(input_2) ,XIC(input_a) XIO(input_b) ]OTE(light_2);
            """
        )


class FunctionBlockDiagram(unittest.TestCase):
    """Chapter 10."""

    def test_test_and_pending_edits(self):
        """Ref p216.

        Sheet insertion comments removed.
        """
        l5k.grammar.FBD_ROUTINE.parse_string(
            r"""
            FBD_ROUTINE MyFbdRoutine (SheetSize := "Letter (8.5x11in)", SheetOrientation := Landscape)
            LOGIC (Online_Edit_Type := Orig)

            END_LOGIC
            LOGIC (Online_Edit_Type := Test)

            END_LOGIC
            LOGIC (Online_Edit_Type := Pend)

            END_LOGIC
            END_FBD_ROUTINE
            """
        )

    def test_only_pending_edits(self):
        """Ref p217.

        Sheet insertion comments removed.
        """
        l5k.grammar.FBD_ROUTINE.parse_string(
            r"""
            FBD_ROUTINE MyFbdRoutine (SheetSize := "Letter (8.5x11in)", SheetOrientation := Landscape)
            LOGIC (Online_Edit_Type := Orig)

            END_LOGIC
            LOGIC (Online_Edit_Type := Pend)

            END_LOGIC
            END_FBD_ROUTINE
            """
        )

    def test_routine(self):
        """Ref p232."""
        l5k.grammar.FBD_ROUTINE.parse_string(
            r"""
            FBD_ROUTINE My_FBD_Routine (SheetSize := "Tabloid (11x17in)", SheetOrientation := Landscape)
            SHEET (Name := Input_Scaling)
            IREF (ID := 3,
            X := 120,
            Y := 120,
            Operand := Input_Tag)
            END_IREF
            OREF (ID := 5,
            X := 520,
            Y := 320,
            Operand := Output_Tag)
            END_OREF
            ICON (ID := 4,
            X := 160,
            Y := 320,
            Name := ConnectorName)
            END_ICON
            OCON (ID := 6,
            X := 680,
            Y := 100,
            Name := ConnectorName)
            END_OCON
            MUL_BLOCK (ID := 0,
            X := 440,
            Y := 60,
            Operand := MUL_01,
            VisiblePins := "SourceA, SourceB, Dest")
            END_MUL_BLOCK
            SCL_BLOCK (ID := 1
            X := 240,
            Y := 60,
            Operand := SCL_01,
            VisiblePins := "In, InEUMax, Out, MaxAlarm")
            END_SCL_BLOCK
            PI_BLOCK (ID := 2,
            X := 260,
            Y := 260,
            Operand := PI_01,
            VisiblePins := "In, Initialize, InitialValue, Out, HighAlarm, LowAlarm")
            END_PI_BLOCK
            WIRE (FromElementID := 3,
            FromParameter := "",
            ToElementID := 1,
            ToParameter := In)
            END_WIRE
            WIRE (FromElementID := 4,
            FromParameter := "",
            ToElementID := 2,
            ToParameter := In)
            END_WIRE
            WIRE (FromElementID := 0,
            FromParameter := Dest,
            ToElementID := 6,
            ToParameter := "")
            END_WIRE
            WIRE (FromElementID := 1,
            FromParameter := Out,
            ToElementID := 0,
            ToParameter := SourceA)
            END_WIRE
            WIRE (FromElementID := 2,
            FromParameter := Out,
            ToElementID := 5,
            ToParameter := "")
            END_WIRE
            FEEDBACK_WIRE (FromElementID := 0,
            FromParameter := Dest,
            ToElementID := 0,
            ToParameter := SourceB)
            END_FEEDBACK_WIRE
            ADD_FUNCTION (ID := 13,
            X := 340,
            Y := 120)
            END_ADD_FUNCTION
            END_SHEET
            END_FBD_ROUTINE
            """
        )


class SequentialFunctionChart(unittest.TestCase):
    """Chapter 11."""

    def test_test_and_pending_edits(self):
        """Ref p244.

        SFC logic insertion comments removed.
        """
        l5k.grammar.SFC_ROUTINE.parse_string(
            r"""
            SFC_ROUTINE MySFCRoutine (SheetSize := "Letter (8.5x11in)",
            SheetOrientation := Landscape, StepName := "Step",
            TransitionName := "Tran", ActionName := "Action",
            StopName := "Stop")
            LOGIC (Online_Edit_Type := Orig)

            END_LOGIC
            LOGIC (Online_Edit_Type := Test)

            END_LOGIC
            LOGIC (Online_Edit_Type := Pend)

            END_LOGIC
            END_SFC_ROUTINE
            """
        )

    def test_pending_edits(self):
        """Ref p245.

        SFC logic insertion comments removed.
        """
        l5k.grammar.SFC_ROUTINE.parse_string(
            r"""
            SFC_ROUTINE MySFCRoutine (SheetSize := "Letter (8.5x11in)",
            SheetOrientation := Landscape, StepName := "Step",
            TransitionName := "Tran", ActionName := "Action",
            StopName := "Stop")
            LOGIC (Online_Edit_Type := Orig)

            END_LOGIC
            LOGIC (Online_Edit_Type := Pend)

            END_LOGIC
            END_SFC_ROUTINE
            """
        )

    def test_routine(self):
        """Ref p261."""
        l5k.grammar.SFC_ROUTINE.parse_string(
            r"""
            SFC_ROUTINE Sample_SFC_Routine1 (SheetSize := "Letter (8.5x11in)",
            SheetOrientation := Landscape, StepName := "Step",
            TransitionName := "Tran", ActionName := "Action",
            StopName := "Stop")
            TRANSITION (ID := 0, X := 120, Y := 1000, Operand := C_Array_Tran[31],
            HideDescription := Yes, DescriptionX := 155, DescriptionY := 985,
            DescriptionWidth := 0)
            CONDITION (LanguageType := ST)
            'TempTag > 0
            END_CONDITION
            END_TRANSITION
            BRANCH (ID := 2, Y := 820, BranchType := Simultaneous, BranchFlow := Diverge)
            LEG (ID := 3)
            END_LEG
            LEG (ID := 4)
            END_LEG
            LEG (ID := 5)
            END_LEG
            END_BRANCH
            TRANSITION (ID := 6, X := 420, Y := 760, Operand := Aliased_Tran,
            HideDescription := No, DescriptionX := 520, DescriptionY := 740,
            DescriptionWidth := 0)
            CONDITION (LanguageType := ST)
            'TempTag > 0
            END_CONDITION
            END_TRANSITION
            STOP (ID := 8, X := 460, Y := 880, Operand := ConsumedTag_Stop,
            HideDescription := Yes, DescriptionX := 565, DescriptionY := 865,
            DescriptionWidth := 0)
            END_STOP
            TRANSITION (ID := 10, X := 520, Y := 1360, Operand := Tran_UsedTwice,
            HideDescription := Yes, DescriptionX := 555, DescriptionY := 1345,
            DescriptionWidth := 0)
            CONDITION (LanguageType := ST)
            'TempTag > 0
            END_CONDITION
            END_TRANSITION
            TRANSITION (ID := 12, X := 460, Y := 1160, Operand := Tran_UsedTwice,
            HideDescription := Yes, DescriptionX := 495, DescriptionY := 1145,
            DescriptionWidth := 0)
            CONDITION (LanguageType := ST)
            'TempTag > 0
            END_CONDITION
            END_TRANSITION
            BRANCH (ID := 14, Y := 940, BranchType := Selection, BranchFlow := Diverge,
            Priority := UserDefined)
            LEG (ID := 15)
            END_LEG
            LEG (ID := 16)
            END_LEG
            END_BRANCH
            BRANCH (ID := 17, Y := 1320, BranchType := Simultaneous, BranchFlow := Converge)
            LEG (ID := 18)
            END_LEG
            LEG (ID := 19)
            END_LEG
            END_BRANCH
            STOP (ID := 20, X := 520, Y := 1440, Operand := Aliased_Stop, HideDescription := No,
            DescriptionX := 400, DescriptionY := 1480, DescriptionWidth := 0)
            END_STOP
            STEP (ID := 22, X := 420, Y := 360, Operand := First_Step, HideDescription := Yes,
            DescriptionX := 478, DescriptionY := 345, DescriptionWidth := 0,
            InitialStep := Yes, PresetUsesExpression := No, LimitHighUsesExpression := No,
            LimitLowUsesExpression := No, ShowActions := Yes)
            ACTION (ID := 24, Operand := First_Action, Qualifier := L, IsBoolean := No,
            PresetUsesExpression := No, IndicatorTag := Watch_Tag[3].PRE)
            BODY (LanguageType := ST)
            '
            END_BODY
            END_ACTION
            ACTION (ID := 25, Operand := C_Array_Action[3], Qualifier := SL,
            IsBoolean := No, PresetUsesExpression := No,
            IndicatorTag := C_Produced_IndicatorArray[1])
            BODY (LanguageType := ST)
            '
            END_BODY
            END_ACTION
            ACTION (ID := 26, Operand := UDT_Elem.Action_Member, Qualifier := D,
            IsBoolean := No, PresetUsesExpression := No, IndicatorTag := "")
            BODY (LanguageType := ST)
            '
            END_BODY
            END_ACTION
            ACTION (ID := 27, Operand := Action_000, Qualifier := R, IsBoolean := No,
            PresetUsesExpression := No, IndicatorTag := "")
            BODY (LanguageType := ST)
            '
            END_BODY
            END_ACTION
            ACTION (ID := 28, Operand := Action_001, Qualifier := N, IsBoolean := No,
            PresetUsesExpression := No, IndicatorTag := Aliased_Indicator)
            BODY (LanguageType := ST)
            '
            END_BODY
            END_ACTION
            ACTION (ID := 29, Operand := Action_002, Qualifier := DS, IsBoolean := Yes,
            PresetUsesExpression := No, IndicatorTag := "")
            END_ACTION
            ACTION (ID := 30, Operand := ConsumedTag_Action, Qualifier := P0,
            IsBoolean := No, PresetUsesExpression := No,
            IndicatorTag := ConsumedTag_Indicator)
            BODY (LanguageType := ST)
            '
            END_BODY
            END_ACTION
            END_STEP
            STEP (ID := 31, X := 120, Y := 880, Operand := "C_Array_Step[0,1,2]",
            HideDescription := Yes, DescriptionX := 179, DescriptionY := 865,
            DescriptionWidth := 0, InitialStep := No, PresetUsesExpression := No,
            LimitHighUsesExpression := No, LimitLowUsesExpression := No, ShowActions := Yes)
            END_STEP
            TRANSITION (ID := 33, X := 460, Y := 1000, Operand := NoTag_Tran,
            HideDescription := Yes, DescriptionX := 495, DescriptionY := 985,
            DescriptionWidth := 0)
            CONDITION (LanguageType := ST)
            'TempTag > 0
            END_CONDITION
            END_TRANSITION
            STEP (ID := 35, X := 120, Y := 1080, Operand := UDT_Elem.Step_Member,
            HideDescription := Yes, DescriptionX := 199, DescriptionY := 1065,
            DescriptionWidth := 0, InitialStep := No, PresetUsesExpression := No,
            LimitHighUsesExpression := No, LimitLowUsesExpression := No, ShowActions := Yes)
            END_STEP
            STEP (ID := 37, X := 720, Y := 880, Operand := Step_001, HideDescription := No,
            DescriptionX := 760, DescriptionY := 940, DescriptionWidth := 0,
            InitialStep := No, PresetUsesExpression := No, LimitHighUsesExpression := No,
            LimitLowUsesExpression := No, ShowActions := Yes)
            END_STEP
            BRANCH (ID := 39, Y := 1220, BranchType := Selection, BranchFlow := Converge)
            LEG (ID := 40)
            END_LEG
            LEG (ID := 41)
            END_LEG
            END_BRANCH
            STEP (ID := 42, X := 280, Y := 1260, Operand := Step_000, HideDescription := No,
            DescriptionX := 360, DescriptionY := 1240, DescriptionWidth := 0,
            InitialStep := No, PresetUsesExpression := No, LimitHighUsesExpression := No,
            LimitLowUsesExpression := No, ShowActions := Yes)
            END_STEP
            STEP (ID := 44, X := 460, Y := 1080, Operand := ConsumedTag_Step,
            HideDescription := Yes, DescriptionX := 514, DescriptionY := 1065,
            DescriptionWidth := 0, InitialStep := No, PresetUsesExpression := No,
            LimitHighUsesExpression := No, LimitLowUsesExpression := No, ShowActions := Yes)
            END_STEP
            TRANSITION (ID := 46, X := 120, Y := 1160, Operand := UDT_Elem.Tran_Member,
            HideDescription := Yes, DescriptionX := 155, DescriptionY := 1145,
            DescriptionWidth := 0)
            CONDITION (LanguageType := ST)
            'TempTag > 0
            END_CONDITION
            END_TRANSITION
            DIRECTED_LINK (FromElementID := 46, ToElementID := 41, ShowLink := True)
            END_DIRECTED_LINK
            DIRECTED_LINK (FromElementID := 15, ToElementID := 33, ShowLink := True)
            END_DIRECTED_LINK
            DIRECTED_LINK (FromElementID := 35, TToElementID := 46, ShowLink := True)
            END_DIRECTED_LINK
            DIRECTED_LINK (FromElementID := 3, ToElementID := 37, ShowLink := True)
            END_DIRECTED_LINK
            DIRECTED_LINK (FromElementID := 5, ToElementID := 31, ShowLink := True)
            END_DIRECTED_LINK
            DIRECTED_LINK (FromElementID := 6, ToElementID := 2, ShowLink := True)
            END_DIRECTED_LINK
            DIRECTED_LINK (FromElementID := 22, ToElementID := 6, ShowLink := True)
            END_DIRECTED_LINK
            DIRECTED_LINK (FromElementID := 16, ToElementID := 0, ShowLink := True)
            END_DIRECTED_LINK
            DIRECTED_LINK (FromElementID := 44, ToElementID := 12, ShowLink := True)
            END_DIRECTED_LINK
            DIRECTED_LINK (FromElementID := 33, ToElementID := 44, ShowLink := True)
            END_DIRECTED_LINK
            DIRECTED_LINK (FromElementID := 17, ToElementID := 10, ShowLink := True)
            END_DIRECTED_LINK
            DIRECTED_LINK (FromElementID := 42, ToElementID := 19, ShowLink := True)
            END_DIRECTED_LINK
            DIRECTED_LINK (FromElementID := 37, ToElementID := 18, ShowLink := True)
            END_DIRECTED_LINK
            DIRECTED_LINK (FromElementID := 4, ToElementID := 8, ShowLink := True)
            END_DIRECTED_LINK
            DIRECTED_LINK (FromElementID := 39, ToElementID := 42, ShowLink := True)
            END_DIRECTED_LINK
            DIRECTED_LINK (FromElementID := 10, ToElementID := 20, ShowLink := True)
            END_DIRECTED_LINK
            DIRECTED_LINK (FromElementID := 0, ToElementID := 35, ShowLink := True)
            END_DIRECTED_LINK
            DIRECTED_LINK (FromElementID := 31, ToElementID := 14, ShowLink := True)
            END_DIRECTED_LINK
            DIRECTED_LINK (FromElementID := 12, ToElementID := 40, ShowLink := True)
            END_DIRECTED_LINK
            TEXT_BOX (ID := 48, X := 260, Y := 1380, Width := 0,
            Text := "Simultaneous Branch Converge Text Box")
            END_TEXT_BOX
            ATTACHMENT (FromElementID := 48, ToElementID := 17)
            END_ATTACHMENT
            END_SFC_ROUTINE
            """
        )


class StructuredTextRoutine(unittest.TestCase):
    """Chapter 12."""

    def test_test_and_pending_edits(self):
        """Ref p273.

        Logic insertion comments removed.
        """
        l5k.grammar.ST_ROUTINE.parse_string(
            r"""
            ST_ROUTINE MySTRoutine
            LOGIC (Online_Edit_Type := Orig)

            END_LOGIC
            LOGIC (Online_Edit_Type := Test)

            END_LOGIC
            LOGIC (Online_Edit_Type := Pend)

            END_LOGIC
            END_ST_ROUTINE
            """
        )

    def test_pending_edits(self):
        """Ref p273.

        Logic insertion comments removed.
        """
        l5k.grammar.ST_ROUTINE.parse_string(
            r"""
            ST_ROUTINE MySTRoutine
            LOGIC (Online_Edit_Type := Orig)

            END_LOGIC
            LOGIC (Online_Edit_Type := Pend)

            END_LOGIC
            END_ST_ROUTINE
            """
        )

    def test_routine(self):
        """Ref p274.

        Routine name replaced, sample comment removed, and END statement
        corrected.
        """
        l5k.grammar.ST_ROUTINE.parse_string(
            r"""
            ST_ROUTINE routine_name

            ‘IF (myInteger = 12) THEN
            ‘ myInteger := ((5 * myInputInteger1) + (7 * myInteger2)) - 71;
            ‘ WHILE (myTmpVar >= 0) DO
            ‘ myInteger := myInteger + 3;
            ‘ myTmpVar := myTmpVar - 1;
            ‘ END_WHILE;
            ‘END_IF;
            END_ST_ROUTINE
            """
        )


class Task(unittest.TestCase):
    """Chapter 14."""

    def test_standard(self):
        """Ref p297."""
        l5k.grammar.TASK.parse_string(
            r"""
            TASK joe (Type := Periodic, Priority := 8, Rate := 10000)
            sue;
            betty;
            END_TASK
            """
        )

    def test_safety(self):
        """Ref p298."""
        l5k.grammar.TASK.parse_string(
            r"""
            TASK SafetyTask (Type := PERIODIC,
            Class := Safety,
            Rate := 10,
            Priority := 10,
            Watchdog := 10,
            DisableUpdateOutputs := No,
            InhibitTask := No)
            SafetyProgram;
            END_TASK
            """
        )


class ParameterConnection(unittest.TestCase):
    """Chapter 15."""

    def test_parameter_connection(self):
        """Ref p300.

        Content other than PARAMETER_CONNECTION blocks excluded.
        """
        l5k.grammar.PARAMETER_CONNECTION[1, ...].parse_string(
            r"""
            PARAMETER_CONNECTION (EndPoint1 :=
            \MainProgram.Output_ParameterMain,
            EndPoint2 :=
            \SecondProgram.Input_ParameterFromSub)
            END_PARAMETER_CONNECTION
            PARAMETER_CONNECTION (EndPoint1 :=
            \SubProgram.Output_ParameterSub,
            EndPoint2 :=
            \MainProgram.Input_ParameterMain)
            END_PARAMETER_CONNECTION
            PARAMETER_CONNECTION (EndPoint1 :=
            \SubProgram.Output_ParameterSub,
            EndPoint2 :=
            \SecondProgram.Input_ParameterFromMain)
            END_PARAMETER_CONNECTION
            """
        )


class Trend(unittest.TestCase):
    """Chapter 16."""

    def test_trend(self):
        """Ref p311.

        Template data terminated correctly with closing bracket.
        """
        l5k.grammar.TREND.parse_string(
            r"""
            TREND trend1 (SamplePeriod := 10,
            NumberOfCaptures := 1,
            CaptureSizeType := Samples,
            CaptureSize := 60000,
            StartTriggerType := No Trigger,
            StopTriggerType := No Trigger,
            TrendxVersion := 5.2)
            Template :=
            [208,207,17,224,161,177,26,225,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,62,0,3,0,254,255,9,0,6,0,0,0,0,0,0,0,
            0,0,0,0,1,0,0,0,1,0,0,0,0,0,0,0,0,16,0,0,2,0,0,0,1,0,0,0,254,255,255,255,0,0,0,0,0,0,0,0,255,255,255,
            255,255,255]
            PEN Local:1:I.CHA_Status (Color := 16#00ff_0000,
            Visible := 1,
            Width := 1,
            Type := Analog,
            Style := 0,
            Marker := 0,
            Min := 0.0,
            Max := 100.0)
            END_PEN
            PEN Local:1:I.CHB_Status (Color := 16#0000_ff00,
            Visible := 1,
            Width := 1,
            Type := Analog,
            Style := 0,
            Marker := 0,
            Min := 0.0,
            Max := 100.0)
            END_PEN
            END_TREND
            """
        )


class WatchList(unittest.TestCase):
    """Chapter 17."""

    def test_quick_watch(self):
        """Ref p315."""
        l5k.grammar.QUICK_WATCH[2].parse_string(
            r"""
            QUICK_WATCH (Name := My_Quick_Watch_2)
            WATCH_TAG (Specifier := MyDint);
            WATCH_TAG (Specifier := MySint, Scope := My_Program);
            WATCH_TAG (Specifier := MyAOI, Scope := My_Program);
            WATCH_TAG (Specifier := MyAOI.MyString, Scope := MyProgram);
            END_QUICK_WATCH
            QUICK_WATCH (Name := My_Quick_Watch_1)
            WATCH_TAG (Specifier := MyDint);
            WATCH_TAG (Specifier := MySint, Scope := My_Program);
            WATCH_TAG (Specifier := MyAOI, Scope := My_Program);
            WATCH_TAG (Specifier := MyAOI.MyString, Scope := MyProgram);
            END_QUICK_WATCH
            """
        )


class ControllerConifiguration(unittest.TestCase):
    """Chapter 18."""

    def test_df1(self):
        """Ref p323."""
        l5k.grammar.CONFIG.parse_string(
            r"""
            CONFIG DF1
            (DuplicateDetection := -1,
            ErrorDetection := BCC Error,
            EmbeddedResponseEnable := -1,
            DF1Mode := Pt to Pt,
            ACKTimeout := 50,
            NAKReceiveValue := 3,
            DF1ENQs := 3,
            DF1Retries := 3,
            StationAddress := 0,
            ReplyMessageWait := 50,
            PollingMode := 0,
            MasterMessageTransmit := 0,
            NormalPollNodeFile := NA,
            NormalPollGroupSize := 0,
            PriorityPollNodeFile := NA,
            ActiveStationFile := NA)
            END_CONFIG
            """
        )

    def test_serial_port(self):
        """Ref p324."""
        l5k.grammar.CONFIG.parse_string(
            r"""
            CONFIG SerialPort
            (BaudRate := 19200,
            Parity := No Parity,
            DataBits := 8 Bits of Data,
            StopBits := 1 Stop Bit,
            ComDriverId := DF1,
            RTSOffDelay := 0,
            RTSSendDelay := 0,
            ControlLine := No Handshake,
            RemoteModeChangeFlag := 0,
            ModeChangeAttentionChar := 27,
            SystemModeCharacter := 83,
            UserModeCharacter := 85)
            END_CONFIG
            """
        )


class SafetySignatures(unittest.TestCase):
    """Chapter 20."""

    def test_overall_root(self):
        """Ref p329."""
        l5k.grammar.CONTROLLER.parse_string(
            r"""
            CONTROLLER safety_v36 (SafetySignature := "B3CC8FA3 - 65D512A2 - 25A1A8A7 - A4B46668 - 6F7F560A -
            721374FD - B2ED3906 - 36CBACCC, 02/23/2023, 02:41:57.402 PM",
            SafetyRootSignature := "B3CC8FA3 - 65D512A2 - 25A1A8A7 - A4B46668 - 6F7F560A -
721374FD - B2ED3906 - 36CBACCC",
            SafetyRootSignatureTimestamp := "02/09/2023, 01:45:38.445 PM")
            END_CONTROLLER
            """
        )

    def test_application_rollup(self):
        """Ref p330."""
        l5k.grammar.CONTROLLER.parse_string(
            r"""
            CONTROLLER safety_v36 (SafetyTagMap := " ctrlTagStandard=ctrlTagSafety,
            ctrlTagStandard2=ctrlTagSafety2",
            SafetyTagMapSignature := "F5AFC204 - 9393CBA7 - 0CC9E546 - 31B67107 - 1EE4D63C
            - 63C58FAA - 6717B619 - 686CC114",
            SafetyTagMapSignatureTimestamp := "02/09/2023, 01:45:38.445 PM",
            ControllerAttributesSignature := "F5AFC204 - 9393CBA7 - 0CC9E546 - 31B67107 -
            1EE4D63C - 63C58FAA - 6717B619 - 686CC114",
            ControllerAttributesSignatureTimestamp := "02/09/2023, 01:45:38.445 PM",
            ApplicationRollupSignature := "F5AFC204 - 9393CBA7 - 0CC9E546 - 31B67107 -
            1EE4D63C - 63C58FAA - 6717B619 - 686CC114",
            ApplicationRollupSignatureTimestamp := "02/09/2023, 01:45:38.445 PM")
            END_CONTROLLER
            """
        )

    def test_controller_aggregated_safety_tags(self):
        """Ref p331."""
        l5k.grammar.CONTROLLER.parse_string(
            r"""
            CONTROLLER safety_v36 (TagsRollupSignature := "F5AFC204 - 9393CBA7 - 0CC9E546 - 31B67107 - 1EE4D63C -
            63C58FAA - 6717B619 - 686CC114",
            TagsRollupSignatureTimestamp := "02/09/2023, 01:45:38.445 PM")
            END_CONTROLLER
            """
        )

    def test_safety_tasks(self):
        """Ref p332."""
        l5k.grammar.CONTROLLER.parse_string(
            r"""
            PROGRAM SafetyProgram (Class := Safety,
            ProgramSignature := "F5AFC204 - 9393CBA7 - 0CC9E546 - 31B67107 - 1EE4D63C
            - 63C58FAA - 6717B619 - 686CC114",
            ProgramSignatureTimestamp := "02/09/2023, 01:45:38.445 PM",
            TagsSignature := "F5AFC204 - 9393CBA7 - 0CC9E546 - 31B67107 - 1EE4D63C -
            63C58FAA - 6717B619 - 686CC114",
            TagsSignatureTimestamp := "02/09/2023, 01:45:38.445 PM")
            TAG
            localTagSafety : DINT (RADIX := Decimal) := 0;
            END_TAG
            ROUTINE MainRoutine (RoutineSignature := "F5AFC204 - 9393CBA7 - 0CC9E546 - 31B67107 -
            1EE4D63C - 63C58FAA - 6717B619 - 686CC114",
            RoutineSignatureTimestamp := "02/09/2023, 01:45:38.445 PM")
            END_ROUTINE
            CHILD_PROGRAMS
            END_CHILD_PROGRAMS
            END_PROGRAM
            TASK SafetyTask (Class := Safety,
            TaskSignature := "F5AFC204 - 9393CBA7 - 0CC9E546 - 31B67107 - 1EE4D63C -
            63C58FAA - 6717B619 - 686CC114",
            TaskSignatureTimestamp := "02/09/2023, 01:45:38.445 PM")
            END_TASK
            """
        )

    def test_safety_aoi(self):
        """Ref p334."""
        l5k.grammar.CONTROLLER.parse_string(
            r"""
            CONTROLLER safety_v36 (AoisRollupSignature := "F5AFC204 - 9393CBA7 - 0CC9E546 - 31B67107 - 1EE4D63C -
            63C58FAA - 6717B619 - 686CC114",
            AoisRollupSignatureTimestamp := "02/09/2023, 01:45:38.445 PM")
            ADD_ON_INSTRUCTION_DEFINITION SafetyAOI (Class := Safety,
            AoiSignature := "F5AFC204 - 9393CBA7 - 0CC9E546 -
            31B67107 - 1EE4D63C - 63C58FAA - 6717B619 - 686CC114",
            AoiSignatureTimestamp := "02/09/2023, 01:45:38.445 PM",
            AoiParametersAndLocalTagsRollupSignature := "F5AFC204 -
            9393CBA7 - 0CC9E546 - 31B67107 - 1EE4D63C - 63C58FAA - 6717B619 - 686CC114",
            AoiParametersAndLocalTagsRollupSignatureTimestamp :=
            "02/09/2023, 01:45:38.445 PM")
            PARAMETERS
            EnableIn : BOOL (Description := "Enable Input - System Defined Parameter",
            Usage := Input,
            RADIX := Decimal,
            Required := No,
            Visible := No,
            ExternalAccess := Read Only);
            END_PARAMETERS
            LOCAL_TAGS
            OloSafety : DINT (RADIX := Decimal,
            ExternalAccess := None,
            DefaultData := 0);
            END_LOCAL_TAGS
            ROUTINE Logic (RoutineSignature := "F5AFC204 - 9393CBA7 - 0CC9E546 - 31B67107 - 1EE4D63C -
            63C58FAA - 6717B619 - 686CC114",
            RoutineSignatureTimestamp := "02/09/2023, 01:45:38.445 PM")
            N: XIC(ParamForAOI)OTL(ParamForAOI);
            N: XIC(LocalTagAOI)OTU(LocalTagAOI);
            END_ROUTINE
            END_ADD_ON_INSTRUCTION_DEFINITION
            ENCODED_DATA (EncodedType := ADD_ON_INSTRUCTION_DEFINITION,
            Name := "EncodedSafetyAOI",
            Class := Safety,
            AoiSignature := "F5AFC204 - 9393CBA7 - 0CC9E546 - 31B67107 - 1EE4D63C - 63C58FAA -
            6717B619 - 686CC114",
            AoiSignatureTimestamp := "02/09/2023, 01:45:38.445 PM")
            PARAMETERS
            EnableIn : BOOL (Description := "Enable Input - System Defined Parameter",
            Usage := Input,
            RADIX := Decimal,
            Required := No,
            Visible := No,
            ExternalAccess := Read Only);
            END_PARAMETERS
            ENCODED_DATA_HERE
            END_ENCODED_DATA
            END_CONTROLLER
            """
        )

    def test_safety_modules(self):
        """Ref p336."""
        l5k.grammar.CONTROLLER.parse_string(
            r"""
            CONTROLLER safety_v36 (ModulesRollupSignature := "F5AFC204 - 9393CBA7 - 0CC9E546 - 31B67107 -
            1EE4D63C - 63C58FAA - 6717B619 - 686CC114",
            ModulesRollupSignatureTimestamp := "02/09/2023, 01:45:38.445 PM")
            MODULE safetyIO (ModuleSignature := "F5AFC204 - 9393CBA7 - 0CC9E546 - 31B67107 - 1EE4D63C -
            63C58FAA - 6717B619 - 686CC114",
            ModuleSignatureTimestamp := "02/09/2023, 01:45:38.445 PM"
            ConnectionsRollupSignature := "F5AFC204 - 9393CBA7 - 0CC9E546 - 31B67107 -
            1EE4D63C - 63C58FAA - 6717B619 - 686CC114",
            ConnectionsRollupSignatureTimestamp := "02/09/2023, 01:45:38.445 PM")
            CONNECTION SafetyInput (ConnectionSignature := "F5AFC204 - 9393CBA7 - 0CC9E546 - 31B67107
            - 1EE4D63C - 63C58FAA - 6717B619 - 686CC114",
            ConnectionSignatureTimestamp := "02/09/2023, 01:45:38.445 PM")
            END_CONNECTION
            END_MODULE
            END_CONTROLLER
            """
        )

    def test_authentication_code(self):
        """Ref p337.


        Placeholder (...) removed.
        """
        l5k.grammar.CONTROLLER.parse_string(
            r"""
            CONTROLLER XmlTest
            PROGRAM SafetyProgram END_PROGRAM
            TASK SafetyTask END_TASK
            AUTHENTICATION_CODE SafetySignaturesHmac(Value :=
            "040123456789ABCDEF0123456789ABCDEF0123456789ABCDEF0123456789ABCDEF") END_AUTHENTICATION_CODE
            CONFIG CST END_CONFIG
            CONFIG WallClockTime END_CONFIG
            END_CONTROLLER
            """
        )

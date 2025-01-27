import ResetSymbolsIcon from "clock-common/lib/Components/ResetSymbolsIcon";
import ControlInterface from "clock-common/lib/Tools/ControlInterface";
import SettingsDialog from "clock-common/lib/Components/SettingsDialog";
import { useContext, useState } from "react";
import {
  ComboBox,
  KeyValueSetCheckBox,
  KeyValueSetRadio,
  KeyValueSetSymbol,
  InputNumber,
  CheckBox,
  DropDown,
  PluginConfigContext,
  useKeyValueSetSymbol,
  useBooleanSymbol,
  useIntegerSymbol,
} from "@mplab_harmony/harmony-plugin-client-lib";
import { getDynamicSymbolsFromJSON } from "clock-common/lib/Tools/ClockJSONTools";
import FrequencyLabelComponent from "clock-common/lib/Components/LabelComponent/FrequencyLabelComponent";
import LoadDynamicComponents from "clock-common/lib/Components/Dynamic/LoadDynamicComponents";
import PlainLabel from "clock-common/lib/Components/LabelComponent/PlainLabel";

const settingsArray = [
  "CONF_CLOCK_XOSC32K_ENABLE",
  "XOSC32K_OSCILLATOR_MODE",
  "XOSC32K_FREQ_IN",
  "XOSC32K_ONDEMAND",
  "XOSC32K_CGM",
  "XOSC32K_ENSL",
  "XOSC32K_BOOST",
  "XOSC32K_STARTUP",
  "CONFIG_CLOCK_RTC_SRC",
  "XOSC32K_CFDEN",
  "XOSC32K_CFDPRESC",
  "XOSC32K_SWBACK",
];
const internalOscSettingsArray = [
  "CONFIG_CLOCK_OSC16M_ENABLE",
  "CONFIG_CLOCK_OSC16M_ONDEMAND",
  "CONFIG_CLOCK_OSC16M_RUNSTDBY",
];
const crystalOscSettingsArray = [
  "CONFIG_CLOCK_XOSC_ENABLE",
  "XOSC_AMPGC",
  "CONFIG_CLOCK_XOSC_GAIN",
  "XOSC_OSCILLATOR_MODE",
  "CONFIG_CLOCK_XOSC_FREQUENCY",
  "CONFIG_CLOCK_XOSC_ONDEMAND",
  "CONFIG_CLOCK_XOSC_STARTUP",
  "CONFIG_CLOCK_XOSC_RUNSTDBY",
];

const InternalOscillatorConfig = (props: {
  clockController: ControlInterface[];
  cx: (...classNames: string[]) => string;
}) => {
  const { componentId = "core" } = useContext(PluginConfigContext);

  const internalOSC48Div = useKeyValueSetSymbol({
    componentId,
    symbolId: "CONFIG_CLOCK_OSC16M_FREQSEL",
  });
  const internalOSC48 = useBooleanSymbol({
    componentId,
    symbolId: "CONFIG_CLOCK_OSC16M_ENABLE",
  });
  const crystalOSC = useBooleanSymbol({
    componentId,
    symbolId: "CONFIG_CLOCK_XOSC_ENABLE",
  });
  const xoscFrequency = useIntegerSymbol({
    componentId,
    symbolId: "CONFIG_CLOCK_XOSC_FREQUENCY",
  });
  const externalOSCMode = useKeyValueSetSymbol({
    componentId,
    symbolId: "XOSC_OSCILLATOR_MODE",
  });

  return (
    <div>
      <FrequencyLabelComponent
        componentId={componentId}
        redColorForZeroFrequency={true}
        symbolId={"OSC16M_FREQ"}
        className={props.cx("xosc48MFreq")}
      />
      <FrequencyLabelComponent
        componentId={componentId}
        redColorForZeroFrequency={true}
        symbolId={"XOSC_FREQ"}
        className={props.cx("xoscFreq")}
      />
      <DropDown
        keyValueSetSymbolHook={internalOSC48Div}
        className={props.cx("internalOSC48Div")}
      />
      <CheckBox
        booleanSymbolHook={internalOSC48}
        className={props.cx("internalOSC48")}
      />
      <CheckBox
        booleanSymbolHook={crystalOSC}
        className={props.cx("crystalOSC")}
      />
      <DropDown
        keyValueSetSymbolHook={externalOSCMode}
        className={props.cx("externalOSCMode")}
      />
      <InputNumber
        integerSymbolHook={xoscFrequency}
        className={props.cx("xoscFrequency")}
      />
      <SettingsDialog
        tooltip="Advanced Settings"
        componentId={componentId}
        className={props.cx("internalOscSetting")}
        symbolArray={internalOscSettingsArray}
        dialogWidth="50rem"
        dialogHeight="47rem"
      />
      <SettingsDialog
        tooltip="Advanced Settings"
        componentId={componentId}
        className={props.cx("crystalOscSetting")}
        symbolArray={crystalOscSettingsArray}
        dialogWidth="50rem"
        dialogHeight="47rem"
      />
      <PlainLabel
        disPlayText={internalOSC48Div.selectedOptionPair?.key + ""}
        className={props.cx("internalOSC16DivLabel")}
        booldStatus
      />
      <ResetSymbolsIcon
        tooltip="Reset Clock symbols to default value"
        className={props.cx("internalOscReset")}
        componentId={componentId}
        resetSymbolsArray={internalOscSettingsArray}
      />
      <ResetSymbolsIcon
        tooltip="Reset Clock symbols to default value"
        className={props.cx("crystalOscReset")}
        componentId={componentId}
        resetSymbolsArray={crystalOscSettingsArray}
      />
    </div>
  );
};

export default InternalOscillatorConfig;

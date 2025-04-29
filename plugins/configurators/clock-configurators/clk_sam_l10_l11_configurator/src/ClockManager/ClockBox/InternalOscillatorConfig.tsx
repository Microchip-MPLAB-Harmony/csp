import ResetSymbolsIcon from "clock-common/lib/Components/ResetSymbolsIcon";
import ControlInterface from "clock-common/lib/Tools/ControlInterface";
import SettingsDialog from "clock-common/lib/Components/SettingsDialog";
import { useContext } from "react";
import {
  InputNumber,
  CheckBox,
  DropDown,
  PluginConfigContext,
  useKeyValueSetSymbol,
  useBooleanSymbol,
  useIntegerSymbol,
  KeyValueSetRadio,
} from "@mplab_harmony/harmony-plugin-client-lib";
import FrequencyLabelComponent from "clock-common/lib/Components/LabelComponent/FrequencyLabelComponent";


const internalOscSettingsArray = [
  "CONFIG_CLOCK_OSC16M_ENABLE",
  "CONFIG_CLOCK_OSC16M_ONDEMAND",
  "CONFIG_CLOCK_OSC16M_RUNSTDBY",
  "CONFIG_CLOCK_OSC16M_FREQSEL"
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
  "CONFIG_CLOCK_XOSC_CFDEN"
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
      
      <KeyValueSetRadio
        keyValueSetSymbolHook={externalOSCMode}
        classPrefix="externalOSCMode"
        classResolver={props.cx}
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
      
      <ResetSymbolsIcon
        tooltip="Reset Clock symbols to default value"
        className={props.cx("crystalOscReset")}
        componentId={componentId}
        resetSymbolsArray={[...crystalOscSettingsArray,...internalOscSettingsArray]}
      />
    </div>
  );
};

export default InternalOscillatorConfig;

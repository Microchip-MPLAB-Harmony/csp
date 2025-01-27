import ResetSymbolsIcon from "clock-common/lib/Components/ResetSymbolsIcon";
import ControlInterface from "clock-common/lib/Tools/ControlInterface";
import SettingsDialog from "clock-common/lib/Components/SettingsDialog";
import { useContext, useState } from "react";
import {
  KeyValueSetRadio,
  PluginConfigContext,
  useKeyValueSetSymbol,
} from "@mplab_harmony/harmony-plugin-client-lib";
import { getDynamicSymbolsFromJSON } from "clock-common/lib/Tools/ClockJSONTools";
import FrequencyLabelComponent from "clock-common/lib/Components/LabelComponent/FrequencyLabelComponent";
import LoadDynamicComponents from "clock-common/lib/Components/Dynamic/LoadDynamicComponents";

const osc32K_settings = [
  "CONF_CLOCK_OSC32K_ENABLE",
  "OSC32K_RUNSTDBY",
  "OSC32K_ONDEMAND",
  "OSC32K_EN1K",
  "OSC32K_EN32K",
  "OSC32K_STARTUP",
];

const xosc32K_settings = [
  "CONF_CLOCK_XOSC32K_ENABLE",
  "XOSC32K_OSCILLATOR_MODE",
  "XOSC32K_RUNSTDBY",
  "XOSC32K_ONDEMAND",
  "XOSC32K_EN1K",
  "XOSC32K_EN32K",
  "XOSC32K_STARTUP",
  "CONFIG_CLOCK_RTC_SRC",
];

const Crstal32KhzOscialltorControllerBox = (props: {
  clockController: ControlInterface[];
  cx: (...classNames: string[]) => string;
}) => {
  const { componentId = "core" } = useContext(PluginConfigContext);

  const external32KHzOSCMode = useKeyValueSetSymbol({
    componentId,
    symbolId: "XOSC32K_OSCILLATOR_MODE",
  });

  const [dynamicSymbolInfo] = useState(() =>
    getDynamicSymbolsFromJSON(props.clockController)
  );

  return (
    <div>
      <LoadDynamicComponents
        componentId={componentId}
        dynamicSymbolsInfo={dynamicSymbolInfo}
        cx={props.cx}
      />
      <FrequencyLabelComponent
        componentId={componentId}
        redColorForZeroFrequency={true}
        symbolId={"OSC32K_FREQ"}
        className={props.cx("osc32KFreq")}
      />
      <FrequencyLabelComponent
        componentId={componentId}
        redColorForZeroFrequency={true}
        symbolId={"OSC1K_FREQ"}
        className={props.cx("osc1KFreq")}
      />
      <FrequencyLabelComponent
        componentId={componentId}
        symbolId={"OSCULP1K_FREQ"}
        className={props.cx("osculp1KFreq")}
      />

      <FrequencyLabelComponent
        componentId={componentId}
        symbolId={"OSCULP32K_FREQ"}
        className={props.cx("osculp32KFreq")}
      />
      <FrequencyLabelComponent
        componentId={componentId}
        redColorForZeroFrequency={true}
        symbolId={"XOSC32K_FREQ"}
        className={props.cx("xosc32KFreq")}
      />
      <FrequencyLabelComponent
        componentId={componentId}
        redColorForZeroFrequency={true}
        symbolId={"XOSC1K_FREQ"}
        className={props.cx("xosc1KFreq")}
      />
      <KeyValueSetRadio
        keyValueSetSymbolHook={external32KHzOSCMode}
        classPrefix="external32KHzOSCMode"
        classResolver={props.cx}
      />
      <SettingsDialog
        tooltip="Advanced Settings "
        componentId={componentId}
        className={props.cx("osc32KSettings")}
        symbolArray={osc32K_settings}
        dialogWidth="50rem"
        dialogHeight="47rem"
      />
      <ResetSymbolsIcon
        tooltip="Reset Clock symbols to default value"
        className={props.cx("osc32KReset")}
        componentId={componentId}
        resetSymbolsArray={osc32K_settings}
      />
      <SettingsDialog
        tooltip="Advanced Settings "
        componentId={componentId}
        className={props.cx("xosc32KSettings")}
        symbolArray={xosc32K_settings}
        dialogWidth="50rem"
        dialogHeight="47rem"
      />
      <ResetSymbolsIcon
        tooltip="Reset Clock symbols to default value"
        className={props.cx("xosc32KReset")}
        componentId={componentId}
        resetSymbolsArray={xosc32K_settings}
      />
    </div>
  );
};

export default Crstal32KhzOscialltorControllerBox;

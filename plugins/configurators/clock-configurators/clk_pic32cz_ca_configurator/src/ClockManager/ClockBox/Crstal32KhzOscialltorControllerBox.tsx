import ResetSymbolsIcon from "clock-common/lib/Components/ResetSymbolsIcon";
import ControlInterface from "clock-common/lib/Tools/ControlInterface";
import SettingsDialog from "clock-common/lib/Components/SettingsDialog";
import { useContext } from "react";
import {
  CheckBox,
  KeyValueSetRadio,
  PluginConfigContext,
  useBooleanSymbol,
  useKeyValueSetSymbol,
} from "@mplab_harmony/harmony-plugin-client-lib";
import FrequencyLabelComponent from "clock-common/lib/Components/LabelComponent/FrequencyLabelComponent";


const xosc32K_settings = [
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
            "XOSC32K_SWBACK"
];

const Crstal32KhzOscialltorControllerBox = (props: {
  clockController: ControlInterface[];
  cx: (...classNames: string[]) => string;
}) => {
  const { componentId = "core" } = useContext(PluginConfigContext);

  const oscexternal32KHzOSCMode = useKeyValueSetSymbol({
    componentId,
    symbolId: "XOSC32K_OSCILLATOR_MODE",
  });
  const osc32Crystal32KHzEnable = useBooleanSymbol({
    componentId,
    symbolId: "CONF_CLOCK_XOSC32K_ENABLE",
  });
  const osc32CFDEnable = useBooleanSymbol({
    componentId,
    symbolId: "XOSC32K_CFDEN",
  });

  return (
    <div>
      <CheckBox
        booleanSymbolHook={osc32Crystal32KHzEnable}
        className={props.cx("osc32Crystal32KHzEnable")}
      />
      <CheckBox
        booleanSymbolHook={osc32CFDEnable}
        className={props.cx("osc32CFDEnable")}
      />
      <FrequencyLabelComponent
        componentId={componentId}
        symbolId={"OSCULP1K_FREQ"}
        className={props.cx("osculp1k_freq")}
      />

      <FrequencyLabelComponent
        componentId={componentId}
        symbolId={"OSCULP32K_FREQ"}
        className={props.cx("osculp32k_freq")}
      />
      {((!osc32Crystal32KHzEnable.value &&
        oscexternal32KHzOSCMode.value === 0) ||
        (osc32Crystal32KHzEnable.value &&
          (oscexternal32KHzOSCMode.value === 1 ||
            oscexternal32KHzOSCMode.value === 0))) && (
        <FrequencyLabelComponent
          componentId={componentId}
          redColorForZeroFrequency={true}
          symbolId={"XOSC32K_FREQ"}
          className={props.cx("osc32k_freq")}
        />
      )}
      {osc32Crystal32KHzEnable.value && oscexternal32KHzOSCMode.value === 1 && (
        <FrequencyLabelComponent
          componentId={componentId}
          redColorForZeroFrequency={true}
          symbolId={"XOSC1K_FREQ"}
          className={props.cx("osc1k_freq")}
        />
      )}
      <KeyValueSetRadio
        keyValueSetSymbolHook={oscexternal32KHzOSCMode}
        classPrefix="oscexternal32KHzOSCMode"
        classResolver={props.cx}
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

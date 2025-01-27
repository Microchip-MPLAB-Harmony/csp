import ResetSymbolsIcon from "clock-common/lib/Components/ResetSymbolsIcon";
import ControlInterface from "clock-common/lib/Tools/ControlInterface";
import SettingsDialog from "clock-common/lib/Components/SettingsDialog";
import LoadDynamicComponents from "clock-common/lib/Components/Dynamic/LoadDynamicComponents";
import { useContext, useState } from "react";
import {
  CheckBox,
  DropDown,
  InputNumber,
  KeyValueSetRadio,
  PluginConfigContext,
  useBooleanSymbol,
  useIntegerSymbol,
  useKeyValueSetSymbol,
} from "@mplab_harmony/harmony-plugin-client-lib";
import {
    getAllSymbolsFromJSON,
    getDynamicLabelsFromJSON,
    getDynamicSymbolsFromJSON
  } from 'clock-common/lib/Tools/ClockJSONTools';
import LoadDynamicFreqencyLabels from 'clock-common/lib/Components/Dynamic/LoadDynamicFreqencyLabels';

const settingsArray = [
  "CONFIG_CLOCK_DFLL_ENABLE",
  "CONFIG_CLOCK_DFLL_OPMODE",
  "CONFIG_CLOCK_DFLL_ONDEMAND",
  "CONFIG_CLOCK_DFLL_RUNSTDY",
  "CONFIG_CLOCK_DFLL_USB",
  "CONFIG_CLOCK_DFLL_WAIT_LOCK",
  "CONFIG_CLOCK_DFLL_BYPASS_COARSE",
  "CONFIG_CLOCK_DFLL_QUICK_LOCK",
  "CONFIG_CLOCK_DFLL_CHILL_CYCLE",
  "CONFIG_CLOCK_DFLL_LLAW",
  "CONFIG_CLOCK_DFLL_STABLE",
  "CONFIG_CLOCK_DFLL_COARSE",
  "CONFIG_CLOCK_DFLL_FINE",
  "CONFIG_CLOCK_DFLL_MUL",
];

const MDSLClockBox = (props: {
  clockController: ControlInterface[];
  cx: (...classNames: string[]) => string;
}) => {
  const { componentId = "core" } = useContext(PluginConfigContext);
  const [allJsonSymbols] = useState<string[]>(getAllSymbolsFromJSON(props.clockController));

  const [dynamicSymbolInfo] = useState(() => getDynamicSymbolsFromJSON(props.clockController));
  const [dynamicSymbolLabelInfo] = useState(() => getDynamicLabelsFromJSON(props.clockController));
  
  const slck_xtralsel_en = useKeyValueSetSymbol({
    componentId,
    symbolId: "CLK_SLCK_TDXTALSEL",
  });
  const slck_ext_frq = useIntegerSymbol({
    componentId,
    symbolId: "CLK_SLCK_EXT_FREQ",
  });

  return (
    <div>
      <LoadDynamicComponents
        componentId={componentId}
        dynamicSymbolsInfo={dynamicSymbolInfo}
        cx={props.cx}
      />
      <LoadDynamicFreqencyLabels
        componentId={componentId}
        dynamicLabelSymbolsInfo={dynamicSymbolLabelInfo}
        redColorForZeroFrequency={true}
        cx={props.cx}
      />
      <KeyValueSetRadio
        keyValueSetSymbolHook={slck_xtralsel_en}
        classPrefix="slck_xtralsel_en"
        classResolver={props.cx}
      />
      <InputNumber
        integerSymbolHook={slck_ext_frq}
        className={props.cx("slck_ext_frq")}
      />
      {/* <SettingsDialog
        tooltip="Advanced Settings"
        componentId={componentId}
        className={props.cx("dfllSetting")}
        symbolArray={settingsArray}
        dialogWidth="50rem"
        dialogHeight="47rem"
      />
      <ResetSymbolsIcon
        tooltip="Reset Clock symbols to default value"
        className={props.cx("dfllreset")}
        componentId={componentId}
        resetSymbolsArray={settingsArray}
      /> */}
    </div>
  );
};

export default MDSLClockBox;

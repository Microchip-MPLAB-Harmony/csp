import ResetSymbolsIcon from "clock-common/lib/Components/ResetSymbolsIcon";
import ControlInterface from "clock-common/lib/Tools/ControlInterface";
import SettingsDialog from "clock-common/lib/Components/SettingsDialog";
import { useContext } from "react";
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
import PlainLabel from "clock-common/lib/Components/LabelComponent/PlainLabel";
import FrequencyLabelComponent from "clock-common/lib/Components/LabelComponent/FrequencyLabelComponent";

const settingsArray = [
  "CONFIG_CLOCK_DFLL_ENABLE",
  "CONFIG_CLOCK_DFLL_OPMODE",
  "CONFIG_CLOCK_DFLL_ONDEMAND",
  "CONFIG_CLOCK_DFLL_USB",
  "CONFIG_CLOCK_DFLL_WAIT_LOCK",
  "CONFIG_CLOCK_DFLL_QUICK_LOCK",
  "CONFIG_CLOCK_DFLL_CHILL_CYCLE",
  "CONFIG_CLOCK_DFLL_LLAW",
  "CONFIG_CLOCK_DFLL_STABLE",
  "CONFIG_CLOCK_DFLL_STEP",
  "CONFIG_CLOCK_DFLL_MUL",
];

const DFLLControllerBox = (props: {
  clockController: ControlInterface[];
  cx: (...classNames: string[]) => string;
}) => {
  const { componentId = "core" } = useContext(PluginConfigContext);

  const dfllRefClock = useKeyValueSetSymbol({
    componentId,
    symbolId: "CONFIG_CLOCK_DFLL_OPMODE",
  });
  const dflllChannelSource = useKeyValueSetSymbol({
    componentId,
    symbolId: "GCLK_ID_0_GENSEL",
  });
  const dfllEnable = useBooleanSymbol({
    componentId,
    symbolId: "CONFIG_CLOCK_DFLL_ENABLE",
  });

  const dfllChannelEnable = useBooleanSymbol({
    componentId,
    symbolId: "GCLK_ID_0_CHEN",
  });

  const dfllMultiplier = useIntegerSymbol({
    componentId,
    symbolId: "CONFIG_CLOCK_DFLL_MUL",
  });

  return (
    <div>
      <CheckBox
        booleanSymbolHook={dfllEnable}
        className={props.cx("dfllEnable")}
      />
      <CheckBox
        booleanSymbolHook={dfllChannelEnable}
        className={props.cx("dfllChannelEnable")}
      />
      {dfllEnable.value === true && (
        <FrequencyLabelComponent
          componentId={componentId}
          redColorForZeroFrequency={true}
          symbolId={"DFLL_CLOCK_FREQ"}
          className={props.cx("dfllFreq")}
        />
      )}
      <PlainLabel
        disPlayText={dfllMultiplier.value + ""}
        className={props.cx("dfllMulLabel")}
        booldStatus
      />
      <KeyValueSetRadio
        keyValueSetSymbolHook={dfllRefClock}
        classPrefix="dfllRefClock"
        classResolver={props.cx}
      />
      <DropDown
        keyValueSetSymbolHook={dflllChannelSource}
        className={props.cx("dflllChannelSource")}
      />
      <InputNumber
        integerSymbolHook={dfllMultiplier}
        className={props.cx("dfllMultiplier")}
      />
      <SettingsDialog
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
      />
    </div>
  );
};

export default DFLLControllerBox;

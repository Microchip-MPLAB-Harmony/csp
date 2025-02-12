import ResetSymbolsIcon from "clock-common/lib/Components/ResetSymbolsIcon";
import ControlInterface from "clock-common/lib/Tools/ControlInterface";
import SettingsDialog from "clock-common/lib/Components/SettingsDialog";
import { useContext } from "react";
import {
  CheckBox,
  DropDown,
  InputNumber,
  PluginConfigContext,
  useBooleanSymbol,
  useIntegerSymbol,
  useKeyValueSetSymbol,
} from "@mplab_harmony/harmony-plugin-client-lib";
import FrequencyLabelComponent from "clock-common/lib/Components/LabelComponent/FrequencyLabelComponent";

const settingsArray = ["CLK_MOSCSEL","CLK_MOSCRCEN","CLK_MOSCXTEN","CLK_MOSCXTST", "CLK_MOSCXT_FREQ",];

const MainClockController = (props: {
  clockController: ControlInterface[];
  cx: (...classNames: string[]) => string;
}) => {
  const { componentId = "core" } = useContext(PluginConfigContext);
  const clk_moscsel = useKeyValueSetSymbol({
    componentId,
    symbolId: "CLK_MOSCSEL",
  });

  const clk_moscrcen = useBooleanSymbol({
    componentId,
    symbolId: "CLK_MOSCRCEN",
  });

  const clk_moscxten = useBooleanSymbol({
    componentId,
    symbolId: "CLK_MOSCXTEN",
  });

  const clk_moscxtst = useIntegerSymbol({
    componentId,
    symbolId: "CLK_MOSCXTST",
  });
  const clk_moscxt_freq = useIntegerSymbol({
    componentId,
    symbolId: "CLK_MOSCXT_FREQ",
  });
  return (
    <div>
      <CheckBox
        booleanSymbolHook={clk_moscrcen}
        className={props.cx("clk_moscrcen")}
      />
      <CheckBox
        booleanSymbolHook={clk_moscxten}
        className={props.cx("clk_moscxten")}
      />
      <FrequencyLabelComponent
        className={props.cx("mainClkFrq")}
        componentId={componentId}
        symbolId="MAINCK_FREQUENCY"
        redColorForZeroFrequency
      />
      <DropDown
        keyValueSetSymbolHook={clk_moscsel}
        className={props.cx("clk_moscsel")}
      />
      <InputNumber
        integerSymbolHook={clk_moscxtst}
        className={props.cx("clk_moscxtst")}
      />
      <InputNumber
        integerSymbolHook={clk_moscxt_freq}
        className={props.cx("clk_moscxt_freq")}
      />
      <SettingsDialog
        tooltip="Advanced Settings"
        componentId={componentId}
        className={props.cx("MainClkSetting")}
        symbolArray={settingsArray}
        dialogWidth="50rem"
        dialogHeight="47rem"
      />
      <ResetSymbolsIcon
        tooltip="Reset Clock symbols to default value"
        className={props.cx("MainClkReSetting")}
        componentId={componentId}
        resetSymbolsArray={settingsArray}
      />
    </div>
  );
};

export default MainClockController;

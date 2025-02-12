import ResetSymbolsIcon from "clock-common/lib/Components/ResetSymbolsIcon";
import ControlInterface from "clock-common/lib/Tools/ControlInterface";
import SettingsDialog from "clock-common/lib/Components/SettingsDialog";
import { useContext } from "react";
import {
  CheckBox,
  InputNumber,
  PluginConfigContext,
  useBooleanSymbol,
  useIntegerSymbol,
} from "@mplab_harmony/harmony-plugin-client-lib";
import FrequencyLabelComponent from "clock-common/lib/Components/LabelComponent/FrequencyLabelComponent";
import PlainLabel from "clock-common/lib/Components/LabelComponent/PlainLabel";

const settingsArray = ["CLK_UPLL_EN","CLK_UPLL_MUL","CLK_UPLL_FRACR",];

const UPLLClockController = (props: {
  clockController: ControlInterface[];
  cx: (...classNames: string[]) => string;
}) => {
  const { componentId = "core" } = useContext(PluginConfigContext);
  
  const clk_upll_en = useBooleanSymbol({
    componentId,
    symbolId: "CLK_UPLL_EN",
  });
  const clk_upll_mul = useIntegerSymbol({
    componentId,
    symbolId: "CLK_UPLL_MUL",
  });
  const clk_upll_fracr = useIntegerSymbol({
    componentId,
    symbolId: "CLK_UPLL_FRACR",
  });
  return (
    <div>
      <CheckBox
        booleanSymbolHook={clk_upll_en}
        className={props.cx("clk_upll_en")}
      />
      <PlainLabel disPlayText="" className={props.cx("upllFrefVal")} />
      <label style={{fontSize:'16px'}} className={props.cx("upllMulLabel")}>{clk_upll_mul.value}</label>
      <label style={{fontSize:'16px'}} className={props.cx("upllFracVal")}>{clk_upll_fracr.value}</label>
      <FrequencyLabelComponent
        className={props.cx("upllClkFrq")}
        componentId={componentId}
        symbolId="UPLL_FREQUENCY"
        redColorForZeroFrequency
      />
      <InputNumber
        integerSymbolHook={clk_upll_mul}
        className={props.cx("clk_upll_mul")}
      />
      <InputNumber
        integerSymbolHook={clk_upll_fracr}
        className={props.cx("clk_upll_fracr")}
      />
      <SettingsDialog
        tooltip="Advanced Settings"
        componentId={componentId}
        className={props.cx("upllSetting")}
        symbolArray={settingsArray}
        dialogWidth="50rem"
        dialogHeight="47rem"
      />
      <ResetSymbolsIcon
        tooltip="Reset Clock symbols to default value"
        className={props.cx("upllReSetting")}
        componentId={componentId}
        resetSymbolsArray={settingsArray}
      />
    </div>
  );
};

export default UPLLClockController;

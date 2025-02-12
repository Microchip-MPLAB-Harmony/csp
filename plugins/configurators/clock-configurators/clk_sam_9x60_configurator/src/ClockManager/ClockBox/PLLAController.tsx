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

const settingsArray = ["CLK_PLL_EN","CLK_PLL_DIVPMC","CLK_PLL_MUL","CLK_PLL_FRACR",];

const PLLAClockController = (props: {
  clockController: ControlInterface[];
  cx: (...classNames: string[]) => string;
}) => {
  const { componentId = "core" } = useContext(PluginConfigContext);
  
  const clk_pll_en = useBooleanSymbol({
    componentId,
    symbolId: "CLK_PLL_EN",
  });

  const clk_pll_divpmc = useIntegerSymbol({
    componentId,
    symbolId: "CLK_PLL_DIVPMC",
  });
  const clk_pll_mul = useIntegerSymbol({
    componentId,
    symbolId: "CLK_PLL_MUL",
  });
  const clk_pll_fracr = useIntegerSymbol({
    componentId,
    symbolId: "CLK_PLL_FRACR",
  });
  return (
    <div>
      <CheckBox
        booleanSymbolHook={clk_pll_en}
        className={props.cx("clk_pll_en")}
      />
      
      <FrequencyLabelComponent
        className={props.cx("pllaClkFrq")}
        componentId={componentId}
        symbolId="PLLA_FREQUENCY"
        redColorForZeroFrequency
      />
      <label className={props.cx("pllaDivPmcLabel")}>/ {`(${clk_pll_divpmc.value} + 1)`}</label>
      <PlainLabel disPlayText="" className={props.cx("pllaFrefVal")}/>
      <label style={{fontSize:'16px'}} className={props.cx("pllaMulVal")}>{clk_pll_mul.value}</label>
      <label style={{fontSize:'16px'}} className={props.cx("pllafracVal")}>{clk_pll_fracr.value}</label>
      <InputNumber
        integerSymbolHook={clk_pll_divpmc}
        className={props.cx("clk_pll_divpmc")}
      />
      <InputNumber
        integerSymbolHook={clk_pll_mul}
        className={props.cx("clk_pll_mul")}
      />
      <InputNumber
        integerSymbolHook={clk_pll_fracr}
        className={props.cx("clk_pll_fracr")}
      />
      <SettingsDialog
        tooltip="Advanced Settings"
        componentId={componentId}
        className={props.cx("pllSetting")}
        symbolArray={settingsArray}
        dialogWidth="50rem"
        dialogHeight="47rem"
      />
      <ResetSymbolsIcon
        tooltip="Reset Clock symbols to default value"
        className={props.cx("pllReSetting")}
        componentId={componentId}
        resetSymbolsArray={settingsArray}
      />
    </div>
  );
};

export default PLLAClockController;

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
import FrequencyLabelComponent from "clock-common/lib/Components/LabelComponent/FrequencyLabelComponent";

const settingsArray = ["CLK_TD_OSCSEL","CLK_OSC32BYP","CLK_OSC32EN","CLK_OSC32BYP_FREQ",];

const SlowClockController = (props: {
  clockController: ControlInterface[];
  cx: (...classNames: string[]) => string;
}) => {
  const { componentId = "core" } = useContext(PluginConfigContext);
  const clk_td_oscsel = useKeyValueSetSymbol({
    componentId,
    symbolId: "CLK_TD_OSCSEL",
  });

  const clk_osc32byp = useBooleanSymbol({
    componentId,
    symbolId: "CLK_OSC32BYP",
  });

  const clk_osc32en = useBooleanSymbol({
    componentId,
    symbolId: "CLK_OSC32EN",
  });

  const clk_osc32byp_freq = useIntegerSymbol({
    componentId,
    symbolId: "CLK_OSC32BYP_FREQ",
  });
  
  return (
    <div>
      <CheckBox
        booleanSymbolHook={clk_osc32byp}
        className={props.cx("clk_osc32byp")}
      />
      <CheckBox
        booleanSymbolHook={clk_osc32en}
        className={props.cx("clk_osc32en")}
      />
      <FrequencyLabelComponent
        className={props.cx("monitoringClkFrq")}
        componentId={componentId}
        symbolId="MD_SLOW_CLK_FREQUENCY"
        redColorForZeroFrequency
      />
      <FrequencyLabelComponent
        className={props.cx("slowClkFrq")}
        componentId={componentId}
        symbolId="TD_SLOW_CLOCK_FREQUENCY"
        redColorForZeroFrequency
      />
      <KeyValueSetRadio
        keyValueSetSymbolHook={clk_td_oscsel}
        classPrefix="clk_td_oscsel"
        classResolver={props.cx}
      />
      <InputNumber
        integerSymbolHook={clk_osc32byp_freq}
        className={props.cx("clk_osc32byp_freq")}
        disabled={(clk_td_oscsel.selectedOptionPair?.key!=='XTAL' || clk_osc32byp.value===false)}
      />
      <SettingsDialog
        tooltip="Advanced Settings"
        componentId={componentId}
        className={props.cx("slowClockSetting")}
        symbolArray={settingsArray}
        dialogWidth="50rem"
        dialogHeight="47rem"
      />
      <ResetSymbolsIcon
        tooltip="Reset Clock symbols to default value"
        className={props.cx("slowClockReSetting")}
        componentId={componentId}
        resetSymbolsArray={settingsArray}
      />
    </div>
  );
};

export default SlowClockController;

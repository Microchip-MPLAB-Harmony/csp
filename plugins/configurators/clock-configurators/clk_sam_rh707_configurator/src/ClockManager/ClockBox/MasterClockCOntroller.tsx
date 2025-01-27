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
  getDynamicSymbolsFromJSON,
} from "clock-common/lib/Tools/ClockJSONTools";
import LoadDynamicFreqencyLabels from "clock-common/lib/Components/Dynamic/LoadDynamicFreqencyLabels";
import PlainLabel from "clock-common/lib/Components/LabelComponent/PlainLabel";
import FrequencyLabelComponent from "clock-common/lib/Components/LabelComponent/FrequencyLabelComponent";

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

const MasterClockBox = (props: {
  clockController: ControlInterface[];
  cx: (...classNames: string[]) => string;
}) => {
  const { componentId = "core" } = useContext(PluginConfigContext);
  const [allJsonSymbols] = useState<string[]>(
    getAllSymbolsFromJSON(props.clockController)
  );

  const [dynamicSymbolInfo] = useState(() =>
    getDynamicSymbolsFromJSON(props.clockController)
  );
  const [dynamicSymbolLabelInfo] = useState(() =>
    getDynamicLabelsFromJSON(props.clockController)
  );

  const clk_mck_css = useKeyValueSetSymbol({
    componentId,
    symbolId: "CLK_MCK_CSS",
  });
  const clk_mck_pres = useKeyValueSetSymbol({
    componentId,
    symbolId: "CLK_MCK_PRES",
  });
  const clk_mck_mdiv = useKeyValueSetSymbol({
    componentId,
    symbolId: "CLK_MCK_MDIV",
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
        keyValueSetSymbolHook={clk_mck_css}
        classPrefix="clk_mck_css"
        classResolver={props.cx}
      />
      <PlainLabel
        disPlayText={((clk_mck_pres.selectedOptionPair?.key)?.replace(/^\D+/g, ''))+''}
        className={props.cx("processorPresLabel")}
      />

      <PlainLabel
        disPlayText={clk_mck_mdiv.value +1 +""}
        className={props.cx("clk_mck_mdiv_lbl")}
      />
      <FrequencyLabelComponent
        className={props.cx("masterClkSlowLabeL")}
        componentId={componentId}
        symbolId="CLK_MD_SLCK_FREQ"
        boldLabelStatus={clk_mck_css.value===0}
      />
      <FrequencyLabelComponent
        className={props.cx("masterClkMainLabel")}
        componentId={componentId}
        symbolId="CLK_MAINCK_FREQ"
        boldLabelStatus={clk_mck_css?.value===1}
      />
      
      <FrequencyLabelComponent
        className={props.cx("masterClkPllaLabel")}
        componentId={componentId}
        symbolId="CLK_PLLACK_FREQ"
        boldLabelStatus={clk_mck_css?.value===2}
      />
      {/* <PlainLabel
        disPlayText={masterClkPllaLabel.value + ""}
        className={props.cx("masterClkPllaLabel")}
        booldStatus
      /> */}
      {/* <InputNumber
        integerSymbolHook={slck_ext_frq}
        className={props.cx("slck_ext_frq")}
      /> */}
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

export default MasterClockBox;

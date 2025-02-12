import ResetSymbolsIcon from "clock-common/lib/Components/ResetSymbolsIcon";
import ControlInterface from "clock-common/lib/Tools/ControlInterface";
import SettingsDialog from "clock-common/lib/Components/SettingsDialog";
import { useContext } from "react";
import {
  CheckBox,
  DropDown,
  KeyValueSetRadio,
  PluginConfigContext,
  useBooleanSymbol,
  useKeyValueSetSymbol,
} from "@mplab_harmony/harmony-plugin-client-lib";
import FrequencyLabelComponent from "clock-common/lib/Components/LabelComponent/FrequencyLabelComponent";

const settingsArray = ["CLK_CPU_CKR_CSS","CLK_CPU_CKR_PRES", "CLK_CPU_CKR_MDIV","CLK_DDR_ENABLE","CLK_DDR_ENABLE",];

const PClockController = (props: {
  clockController: ControlInterface[];
  cx: (...classNames: string[]) => string;
}) => {
  const { componentId = "core" } = useContext(PluginConfigContext);
  const clk_cpu_ckr_css = useKeyValueSetSymbol({
    componentId,
    symbolId: "CLK_CPU_CKR_CSS",
  });
  const clk_cpu_ckr_pres = useKeyValueSetSymbol({
    componentId,
    symbolId: "CLK_CPU_CKR_PRES",
  });
  const clk_cpu_ckr_mdiv = useKeyValueSetSymbol({
    componentId,
    symbolId: "CLK_CPU_CKR_MDIV",
  });
  const clk_ddr_enable = useBooleanSymbol({
    componentId,
    symbolId: "CLK_DDR_ENABLE",
  });

  const clk_qspiclk_enable = useBooleanSymbol({
    componentId,
    symbolId: "CLK_QSPICLK_ENABLE",
  });

  const mkdiv_val=clk_cpu_ckr_mdiv.selectedOptionPair?.key.split(/(\d+)/)[1] || '1'
  return (
    <div>
      <KeyValueSetRadio
        keyValueSetSymbolHook={clk_cpu_ckr_css}
        classPrefix="clk_cpu_ckr_css"
        labelClassPrefix="clk_cpu_ckr_cs_l"
        classResolver={props.cx}
      />
      <CheckBox
        booleanSymbolHook={clk_ddr_enable}
        className={props.cx("clk_ddr_enable")}
      />
      <CheckBox
        booleanSymbolHook={clk_qspiclk_enable}
        className={props.cx("clk_qspiclk_enable")}
      />
      <FrequencyLabelComponent
        className={props.cx("processClkFrq")}
        componentId={componentId}
        symbolId="CPU_CLOCK_FREQUENCY"
        redColorForZeroFrequency
      />
      <FrequencyLabelComponent
        className={props.cx("ddfClkFrq")}
        componentId={componentId}
        symbolId="DDRCLK_FREQUENCY"
        redColorForZeroFrequency
      />
      <FrequencyLabelComponent
        className={props.cx("qspiclkFrq")}
        componentId={componentId}
        symbolId="QSPICLK_FREQUENCY"
        redColorForZeroFrequency
      />
      <FrequencyLabelComponent
        className={props.cx("masterClkFrq")}
        componentId={componentId}
        symbolId="MCK_FREQUENCY"
        redColorForZeroFrequency
      />
      <DropDown
        keyValueSetSymbolHook={clk_cpu_ckr_pres}
        className={props.cx("clk_cpu_ckr_pres")}
      />
      <DropDown
        keyValueSetSymbolHook={clk_cpu_ckr_mdiv}
        className={props.cx("clk_cpu_ckr_mdiv")}
      />
      <label className={props.cx("processorPresLabel")}>/ {clk_cpu_ckr_pres.selectedOptionPair?.key.split('_')[1]}</label>
      <label className={props.cx("processorClkDiv")}>/ {mkdiv_val==='1'?'1':parseInt(mkdiv_val)/2}</label>
      <label className={props.cx("processorMdivLabel")}>/ {mkdiv_val}</label>

      <SettingsDialog
        tooltip="Advanced Settings"
        componentId={componentId}
        className={props.cx("pClkSetting")}
        symbolArray={settingsArray}
        dialogWidth="50rem"
        dialogHeight="47rem"
      />
      <ResetSymbolsIcon
        tooltip="Reset Clock symbols to default value"
        className={props.cx("pClkReSetting")}
        componentId={componentId}
        resetSymbolsArray={settingsArray}
      />
    </div>
  );
};

export default PClockController;

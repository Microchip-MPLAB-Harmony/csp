import ResetSymbolsIcon from "clock-common/lib/Components/ResetSymbolsIcon";
import ControlInterface from "clock-common/lib/Tools/ControlInterface";
import SettingsDialog from "clock-common/lib/Components/SettingsDialog";
import LoadDynamicComponents from "clock-common/lib/Components/Dynamic/LoadDynamicComponents";
import { useContext, useEffect, useState } from "react";
import {
  CheckBox,
  DropDown,
  InputNumber,
  KeyValueSetRadio,
  PluginConfigContext,
  symbolApi,
  useBooleanSymbol,
  useIntegerSymbol,
  useKeyValueSetSymbol,
} from "@mplab_harmony/harmony-plugin-client-lib";
import { getDynamicLabelsFromJSON } from "clock-common/lib/Tools/ClockJSONTools";
import LoadDynamicFreqencyLabels from "clock-common/lib/Components/Dynamic/LoadDynamicFreqencyLabels";
import PeripheralClockControllerBox from "./PopUp/PeripheralClockControllerBox";
import PlainLabel from "clock-common/lib/Components/LabelComponent/PlainLabel";

const settingsArray = [];

const MainClockController = (props: {
  clockController: ControlInterface[];
  cx: (...classNames: string[]) => string;
}) => {
  const { componentId = "core" } = useContext(PluginConfigContext);
  const [dynamicSymbolLabelInfo] = useState(() =>
    getDynamicLabelsFromJSON(props.clockController)
  );
  const clk_main_moscsel = useKeyValueSetSymbol({
    componentId,
    symbolId: "CLK_MAINCK_MOSCSEL",
  });
  const clk_main_moscrcf = useKeyValueSetSymbol({
    componentId,
    symbolId: "CLK_MAINCK_MOSCRCF",
  });
  const clk_moscrcen = useBooleanSymbol({
    componentId,
    symbolId: "CLK_MAINCK_MOSCRCEN",
  });
  const clk_moscxten = useBooleanSymbol({
    componentId,
    symbolId: "CLK_MAINCK_MOSCXTEN",
  });
  const clk_moscxtby = useBooleanSymbol({
    componentId,
    symbolId: "CLK_MAINCK_MOSCXTBY",
  });

  const clk_moscxt_freq = useIntegerSymbol({
    componentId,
    symbolId: "CLK_MAINCK_FREQ",
  });

  const clk_moscxtst = useIntegerSymbol({
    componentId,
    symbolId: "CLK_MAINCK_MOSCXTST",
  });
  const slowFrqValue = useIntegerSymbol({
    componentId,
    symbolId: "CLK_TD_SLCK_FREQ",
  });

  const startupCalculation = () => {
    let slowFrq = slowFrqValue.value;
    let clkValue = clk_moscxtst.value;
    let slowFrqValues = slowFrq;
    let value = ((clkValue * 8) / slowFrqValues) * 1000;

    let formatter = new Intl.NumberFormat("en-US", {
      minimumFractionDigits: 2,
      maximumFractionDigits: 2,
    });
    return formatter.format(value) + " ms";
  };

  const autoCal = startupCalculation();

  return (
    <div>
      <LoadDynamicFreqencyLabels
        componentId={componentId}
        dynamicLabelSymbolsInfo={dynamicSymbolLabelInfo}
        redColorForZeroFrequency={true}
        cx={props.cx}
      />
      <KeyValueSetRadio
        keyValueSetSymbolHook={clk_main_moscsel}
        classPrefix="clk_main_moscsel"
        classResolver={props.cx}
      />
      <DropDown
        keyValueSetSymbolHook={clk_main_moscrcf}
        className={props.cx("clk_main_moscrcf")}
        disabled={clk_main_moscsel.selectedOptionPair?.value === "1"}
      />
      <InputNumber
        integerSymbolHook={clk_moscxt_freq}
        className={props.cx("clk_moscxt_freq")}
        disabled={clk_main_moscsel.selectedOptionPair?.value === "0"}
      />

      <CheckBox
        booleanSymbolHook={clk_moscrcen}
        className={props.cx("clk_moscrcen")}
        disabled={clk_main_moscsel.selectedOptionPair?.value === "1"}
      />
      <CheckBox
        booleanSymbolHook={clk_moscxten}
        className={props.cx("clk_moscxten")}
        disabled={clk_main_moscsel.selectedOptionPair?.value === "0"}
      />
      <CheckBox
        booleanSymbolHook={clk_moscxtby}
        className={props.cx("clk_moscxtby")}
        disabled={clk_main_moscsel.selectedOptionPair?.value === "0"}
      />

      <PlainLabel
        className={props.cx("clk_moscxtst")}
        disPlayText="Start-Up Time:"
      ></PlainLabel>
      <InputNumber
        integerSymbolHook={clk_moscxtst}
        className={props.cx("inputNumberClass")}
      />
      <PlainLabel
        disPlayText={"* 8 SCLK cycles = " + autoCal}
        className={props.cx("outputClass")}
      ></PlainLabel>

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

export default MainClockController;

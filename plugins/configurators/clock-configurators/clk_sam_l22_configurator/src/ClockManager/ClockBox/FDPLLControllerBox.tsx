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
  useFloatSymbol,
  useIntegerSymbol,
  useKeyValueSetSymbol,
} from "@mplab_harmony/harmony-plugin-client-lib";
import { getDynamicSymbolsFromJSON } from "clock-common/lib/Tools/ClockJSONTools";
import { GetClockDisplayFreqValue } from "clock-common/lib/Tools/Tools";
import PlainLabel from "clock-common/lib/Components/LabelComponent/PlainLabel";
import FrequencyLabelComponent from "clock-common/lib/Components/LabelComponent/FrequencyLabelComponent";
import { Button } from "primereact/button";
// import FDPLLAutoCalculation from "./PopUp/FDPLLAutoCalculation";
import { Dialog } from "primereact/dialog";
import FDPLLAutoCalculate from "./PopUp/FDPLLAutoCalculate";

const settingsArray = [
  "CONFIG_CLOCK_DPLL_ENABLE",
  "CONFIG_CLOCK_DPLL_ONDEMAND",
  "CONFIG_CLOCK_DPLL_RUNSTDY",
  "CONFIG_CLOCK_DPLL_LDR_INTEGER",
  "CONFIG_CLOCK_DPLL_LDRFRAC_FRACTION",
  "CONFIG_CLOCK_DPLL_PRESCALAR",
  "CONFIG_CLOCK_DPLL_LOCK_BYPASS",
  "CONFIG_CLOCK_DPLL_LOWPOWER_ENABLE",
  "CONFIG_CLOCK_DPLL_WAKEUP_FAST",
  "CONFIG_CLOCK_DPLL_FILTER",
  "CONFIG_CLOCK_DPLL_REF_CLOCK",
  "CONFIG_CLOCK_DPLL_DIVIDER",
];
const getPrescalarLabel = (value: string) => {
  return value.replace(/[^0-9]/g, "");
};
const FDPLLControllerBox = (props: {
  clockController: ControlInterface[];
  cx: (...classNames: string[]) => string;
}) => {
  const { componentId = "core" } = useContext(PluginConfigContext);
  const [dialogStatus, setDialogStatus] = useState(false);
  const dpllRefClock = useKeyValueSetSymbol({
    componentId,
    symbolId: "CONFIG_CLOCK_DPLL_REF_CLOCK",
  });
  const oscFdpllChannelSource = useKeyValueSetSymbol({
    componentId,
    symbolId: "GCLK_ID_1_GENSEL",
  });
  const fdpllEnable = useBooleanSymbol({
    componentId,
    symbolId: "CONFIG_CLOCK_DPLL_ENABLE",
  });

  const oscFdpllChannelEnable = useBooleanSymbol({
    componentId,
    symbolId: "GCLK_ID_1_CHEN",
  });

  const dpllDiv = useIntegerSymbol({
    componentId,
    symbolId: "CONFIG_CLOCK_DPLL_DIVIDER",
  });
  const dpllLdrInt = useIntegerSymbol({
    componentId,
    symbolId: "CONFIG_CLOCK_DPLL_LDR_INTEGER",
  });
  const dpllLdrFrac = useIntegerSymbol({
    componentId,
    symbolId: "CONFIG_CLOCK_DPLL_LDRFRAC_FRACTION",
  });

  const dpllPrescalar = useKeyValueSetSymbol({
    componentId,
    symbolId: "CONFIG_CLOCK_DPLL_PRESCALAR",
  });
  const dpllPrescLabel = getPrescalarLabel(
    dpllPrescalar.selectedOptionPair?.key + ""
  );
  const dpllDivLabel = useIntegerSymbol({
    componentId,
    symbolId: "CONFIG_CLOCK_DPLL_DIVIDER_VALUE",
  });
  const dpllLdrLabel = useFloatSymbol({
    componentId,
    symbolId: "CONFIG_CLOCK_DPLL_MULTIPLIER_VALUE",
  });
  const [dynamicSymbolInfo] = useState(() =>
    getDynamicSymbolsFromJSON(props.clockController)
  );
  const XOSC32K_FREQ = useIntegerSymbol({
    componentId,
    symbolId: "XOSC32K_FREQ",
  });
  const XOSC_FREQ = useIntegerSymbol({ componentId, symbolId: "XOSC_FREQ" });
  const GCLK_ID_1_FREQ = useIntegerSymbol({
    componentId,
    symbolId: "GCLK_ID_1_FREQ",
  });
  const DPLL96M_CLOCK_FREQ = useIntegerSymbol({
    componentId,
    symbolId: "DPLL96M_CLOCK_FREQ",
  });
  const INPUT_MIN_FREQUENCY = 32768;
  const INPUT_MAX_FREQUENCY = 2000000;
  const OUTPUT_MIN_FREQUENCY = 48000000;
  const OUTPUT_MAX_FREQUENCY = 96000000;

  const isInputFrequencyValid = (frequency: any) => {
    return INPUT_MIN_FREQUENCY <= frequency && frequency <= INPUT_MAX_FREQUENCY;
  };

  const isOutputFrequencyValid = (frequency: any) => {
    return (
      OUTPUT_MIN_FREQUENCY <= frequency && frequency <= OUTPUT_MAX_FREQUENCY
    );
  };
  let freq: any = 0;
  switch (dpllRefClock.value) {
    case 0:
      freq = XOSC32K_FREQ.value;
      break;
    case 1:
      freq = XOSC_FREQ.value;
      freq = freq / (2 * (dpllDiv.value + 1));
      break;
    case 2:
      freq = GCLK_ID_1_FREQ.value;
      break;
    default:
      break;
  }

  const getClockSourceItemsAutoCalculate = () => {
    let clockSourceItems: string[] = [];
    for (let x = 0; x < dpllRefClock.optionPairs.length; x++) {
      let ref = dpllRefClock.optionPairs[x].key;
      switch (dpllRefClock.optionPairs[x].key) {
        case 'XOSC32K':
          clockSourceItems[x] = ref + ' (' + GetClockDisplayFreqValue(XOSC32K_FREQ.value) + ')';
          break;
        case 'XOSC':
          clockSourceItems[x] = ref + ' (' + GetClockDisplayFreqValue(XOSC_FREQ.value) + ')';
          break;
        case 'GCLK_DPLL':
          clockSourceItems[x] = ref + ' (' + GetClockDisplayFreqValue(GCLK_ID_1_FREQ.value) + ')';
          break;
      }
    }
    return clockSourceItems;
  };
  let freqVal = GetClockDisplayFreqValue(freq);
  let DPLL96M_CLOCK_FREQ_VAL = GetClockDisplayFreqValue(
    DPLL96M_CLOCK_FREQ.value
  );
  return (
    <div>
      <LoadDynamicComponents
        componentId={componentId}
        dynamicSymbolsInfo={dynamicSymbolInfo}
        cx={props.cx}
      />
      <CheckBox
        booleanSymbolHook={fdpllEnable}
        className={props.cx("fdpllEnable")}
      />
      <CheckBox
        booleanSymbolHook={oscFdpllChannelEnable}
        className={props.cx("oscFdpllChannelEnable")}
      />
      {fdpllEnable.value === true && (
        <>
          <PlainLabel
            disPlayText={freqVal}
            className={props.cx("dpll96MInputFreq")}
            redColorStatus={isInputFrequencyValid(freq) ? false : true}
          />
          <PlainLabel
            disPlayText={DPLL96M_CLOCK_FREQ_VAL}
            className={props.cx("dpll96MFreq")}
            redColorStatus={
              isOutputFrequencyValid(DPLL96M_CLOCK_FREQ.value) ? false : true
            }
          />
        </>
      )}

      <KeyValueSetRadio
        keyValueSetSymbolHook={dpllRefClock}
        classPrefix="dpllRefClock"
        classResolver={props.cx}
        labelClassPrefix="dpllRefClockLabel"
      />
      <DropDown
        keyValueSetSymbolHook={oscFdpllChannelSource}
        className={props.cx("oscFdpllChannelSource")}
      />
      <InputNumber
        integerSymbolHook={dpllDiv}
        className={props.cx("dpllDiv")}
      />
      <InputNumber
        integerSymbolHook={dpllLdrInt}
        className={props.cx("dpllLdrInt")}
      />
      <InputNumber
        integerSymbolHook={dpllLdrFrac}
        className={props.cx("dpllLdrFrac")}
      />
      <DropDown
        keyValueSetSymbolHook={dpllPrescalar}
        className={props.cx("dpllPrescalar")}
      />
      <PlainLabel
        disPlayText={dpllDivLabel.value + ""}
        className={props.cx("dpllDivLabel")}
        booldStatus
      />
      <PlainLabel
        disPlayText={dpllLdrLabel.value + ""}
        className={props.cx("dpllLdrLabel")}
        booldStatus
      />
      <PlainLabel
        disPlayText={dpllPrescLabel}
        className={props.cx("dpllPrescLabel")}
        booldStatus
      />
      {/* <Button className={props.cx("autoCalculate")} label="Auto Calculate" onClick={()=>setDialogStatus(true)} /> */}

      <SettingsDialog
        tooltip="Advanced Settings"
        componentId={componentId}
        className={props.cx("fdpllSetting")}
        symbolArray={settingsArray}
        dialogWidth="50rem"
        dialogHeight="47rem"
      />
      <ResetSymbolsIcon
        tooltip="Reset Clock symbols to default value"
        className={props.cx("fdpllReset")}
        componentId={componentId}
        resetSymbolsArray={settingsArray}
      />
      <Dialog
        header={'FDPLL Auto Settings Calculation'}
        visible={dialogStatus}
        style={{ width: '42rem', height: '32rem' }}
        maximizable={true}
        onHide={() => {
          setDialogStatus(false);
        }}>
        {/* <FDPLLAutoCalculation
          componentId={componentId}
          expectedOutputFreq={DPLL96M_CLOCK_FREQ.value}
          close={() => {
            setDialogStatus(false);
          }}
          clockSourceItems={getClockSourceItemsAutoCalculate()}
          selectedClockIndex={dpllRefClock.value}
          ldrInt={dpllLdrInt.value}
          ldrFrac={dpllLdrFrac.value}
          dpllDiv={dpllDiv.value}
        /> */}
        <FDPLLAutoCalculate/>
      </Dialog>
    </div>
  );
};

export default FDPLLControllerBox;

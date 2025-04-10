import {
  CheckBoxDefault,
  DropDownDefault,
  error,
  InputNumberDefault,
  KeyValueSetRadio,
  useBooleanSymbol,
  useFloatSymbol,
  useIntegerSymbol,
  useKeyValueSetSymbol,
} from "@mplab_harmony/harmony-plugin-client-lib";
import FrequencyLabelComponent from "clock-common/lib/Components/LabelComponent/FrequencyLabelComponent";
import PlainLabel from "clock-common/lib/Components/LabelComponent/PlainLabel";
import ResetSymbolsIcon from "clock-common/lib/Components/ResetSymbolsIcon";
import SettingsDialog from "clock-common/lib/Components/SettingsDialog";
import ControlInterface from "clock-common/lib/Tools/ControlInterface";
import {
  GetClockDisplayFreqValue,
  removeDuplicates,
} from "clock-common/lib/Tools/Tools";

const FDPLLControllerBoxTemplate = (props: {
  index: string;
  fdpllsettingsClassName: string;
  fdpllresetClassName: string;
  fdpllClockSourceClassName: string;
  fdpllEnableClassName: string;
  fdplloscFdpllChannelEnableClassName: string;
  fdpllFrequencyClassName: string;
  fdpllDivLabelClassName: string;
  fdpllDivClassName: string;
  fdplldpllRefClockClassName: string;
  fdpll96MInputFreqClassName: string;
  fdpllLdrIntClassName: string;
  fdpllLdrFracClassName: string;
  fdpllLdrLabelClassName: string;
  fdpllAutoCalculateClassName: string;
  fdpllSettingsSymbolArray: string[];
  fdpllController: ControlInterface[];
  cx: (...classNames: string[]) => string;
  componentId: string;
}) => {
  const nID = parseInt(props.index) + 1;

  const dpllRefClock = useKeyValueSetSymbol({
    componentId: props.componentId,
    symbolId: "CONFIG_CLOCK_DPLL" + props.index + "_REF_CLOCK",
  });

  const CONFIG_CLOCK_DPLL_ENABLE = useBooleanSymbol({
    componentId: props.componentId,
    symbolId: "CONFIG_CLOCK_DPLL" + props.index + "_ENABLE",
  });

  const fdpllMul = useIntegerSymbol({
    componentId: props.componentId,
    symbolId: "CONFIG_CLOCK_DPLL" + props.index + "_DIVIDER_VALUE",
  });

  const fdpllLDr = useFloatSymbol({
    componentId: props.componentId,
    symbolId: "CONFIG_CLOCK_DPLL" + props.index + "_MULTIPLIER_VALUE",
  });

  const XOSC32K_FREQ = useIntegerSymbol({
    componentId: props.componentId,
    symbolId: "XOSC32K_FREQ",
  });
  const XOSC0_FREQ = useIntegerSymbol({
    componentId: props.componentId,
    symbolId: "XOSC0_FREQ",
  });
  const XOSC1_FREQ = useIntegerSymbol({
    componentId: props.componentId,
    symbolId: "XOSC1_FREQ",
  });
  const CONFIG_CLOCK_DPLL_DIVIDER = useIntegerSymbol({
    componentId: props.componentId,
    symbolId: "CONFIG_CLOCK_DPLL" + props.index + "_DIVIDER",
  });
  const GCLK_ID_FREQ = useIntegerSymbol({
    componentId: props.componentId,
    symbolId: "GCLK_ID_" + nID + "_FREQ",
  });

  let symbols: any = props.fdpllController
    .map((e) => e.symbol_id)
    .filter((e) => e !== undefined);
  symbols = symbols.concat(props.fdpllSettingsSymbolArray);
  symbols = removeDuplicates(symbols);

  const FDPLLCustomFrequency = () => {
    let fdpllCustomFreq;
    updateCustomDPLLFreq();

    function updateCustomDPLLFreq() {
      if (CONFIG_CLOCK_DPLL_ENABLE.value === true) {
        fdpllCustomFreq = getFDPLLSourceFrequency();
      } else {
        fdpllCustomFreq = "";
      }
    }

    function getFDPLLSourceFrequency() {
      let freq = 0;

      switch (dpllRefClock.value) {
        case 0:
          freq = XOSC32K_FREQ.value;
          break;
        case 1:
          freq = XOSC0_FREQ.value;
          freq = freq / (2 * (CONFIG_CLOCK_DPLL_DIVIDER.value + 1));
          break;
        case 2:
          freq = XOSC1_FREQ.value;
          freq = freq / (2 * (CONFIG_CLOCK_DPLL_DIVIDER.value + 1));
          break;
        case 3:
          freq = GCLK_ID_FREQ.value;
          break;

        default:
          error(
            "Clock Configurator",
            "FDPLL source selection is more than range"
          );
      }

      freq = Math.floor(freq);
      return freq + "";
    }

    return (
      <div>
        <PlainLabel
          disPlayText={
            fdpllCustomFreq === ""
              ? fdpllCustomFreq
              : GetClockDisplayFreqValue(Number(fdpllCustomFreq))
          }
          className={props.cx(props.fdpll96MInputFreqClassName)}
          redColorStatus={Number(fdpllCustomFreq) === 0}
        />
      </div>
    );
  };

  return (
    <div>
      <InputNumberDefault
        componentId={props.componentId}
        symbolId={"CONFIG_CLOCK_DPLL" + props.index + "_DIVIDER"}
        className={props.cx(props.fdpllDivClassName)}
      />
      <InputNumberDefault
        componentId={props.componentId}
        symbolId={"CONFIG_CLOCK_DPLL" + props.index + "_LDR_INTEGER"}
        className={props.cx(props.fdpllLdrIntClassName)}
      />
      <InputNumberDefault
        componentId={props.componentId}
        symbolId={"CONFIG_CLOCK_DPLL" + props.index + "_LDRFRAC_FRACTION"}
        className={props.cx(props.fdpllLdrFracClassName)}
      />
      {/* <DropDownDefault
        componentId={props.componentId}
        symbolId={'CONFIG_CLOCK_DPLL' + props.index + '_REF_CLOCK'}
        className={props.cx(props.fdplldpllRefClockClassName)}
      /> */}
      <DropDownDefault
        componentId={props.componentId}
        symbolId={"GCLK_ID_" + nID + "_GENSEL"}
        className={props.cx(props.fdpllClockSourceClassName)}
      />
      <CheckBoxDefault
        componentId={props.componentId}
        symbolId={"GCLK_ID_" + nID + "_CHEN"}
        className={props.cx(props.fdplloscFdpllChannelEnableClassName)}
      />
      <CheckBoxDefault
        componentId={props.componentId}
        symbolId={"CONFIG_CLOCK_DPLL" + props.index + "_ENABLE"}
        className={props.cx(props.fdpllEnableClassName)}
      />
      <PlainLabel
        disPlayText={fdpllMul.value + ""}
        className={props.cx(props.fdpllDivLabelClassName)}
      />

      <PlainLabel
        disPlayText={fdpllLDr.value + ""}
        className={props.cx(props.fdpllLdrLabelClassName)}
      />
      <KeyValueSetRadio
        keyValueSetSymbolHook={dpllRefClock}
        classResolver={props.cx}
        classPrefix={"fdpllRadio"}
        labelClassPrefix={"fdpllRadioName"}
      />

      {/* <FrequencyLabelComponent
        componentId={props.componentId}
        symbolId={'DPLL' + props.index + '_CLOCK_FREQ'}
        className={props.cx(props.fdpll96MInputFreqClassName)}
        redColorForZeroFrequency={true}
      /> */}
      <FDPLLCustomFrequency />
      <FrequencyLabelComponent
        componentId={props.componentId}
        symbolId={"DPLL" + props.index + "_CLOCK_FREQ"}
        className={props.cx(props.fdpllFrequencyClassName)}
        redColorForZeroFrequency={true}
      />
      <SettingsDialog
        tooltip={"Fdpll " + props.index + " Configuration"}
        componentId={props.componentId}
        className={props.cx(props.fdpllsettingsClassName)}
        symbolArray={props.fdpllSettingsSymbolArray}
        dialogWidth="50rem"
        dialogHeight="53rem"
      />
      <ResetSymbolsIcon
        tooltip={"Fdpll " + props.index + " symbols to default value"}
        className={props.cx(props.fdpllresetClassName)}
        componentId={props.componentId}
        resetSymbolsArray={symbols}
      />
      {/* <GetButton
        buttonDisplayText={'Auto Calculate'}
        className={'e5x_fdpllAutoCalculate'}
        toolTip={'FDPLL Auto Settings Calculation'}
        buttonClick={FDPLLAutoCalculationButtonClicked}
      /> */}
    </div>
  );
};
export default FDPLLControllerBoxTemplate;

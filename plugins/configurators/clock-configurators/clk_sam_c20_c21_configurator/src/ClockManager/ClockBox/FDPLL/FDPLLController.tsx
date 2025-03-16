import {
  error,
  KeyValueSetRadio,
  PluginConfigContext,
  useBooleanSymbol,
  useFloatSymbol,
  useIntegerSymbol,
  useKeyValueSetSymbol
} from '@mplab_harmony/harmony-plugin-client-lib';
import LoadDynamicComponents from 'clock-common/lib/Components/Dynamic/LoadDynamicComponents';
import LoadDynamicFreqencyLabels from 'clock-common/lib/Components/Dynamic/LoadDynamicFreqencyLabels';
import PlainLabel from 'clock-common/lib/Components/LabelComponent/PlainLabel';
import ResetSymbolsIcon from 'clock-common/lib/Components/ResetSymbolsIcon';
import SettingsDialog from 'clock-common/lib/Components/SettingsDialog';
import {
  getDynamicLabelsFromJSON,
  getDynamicSymbolsFromJSON
} from 'clock-common/lib/Tools/ClockJSONTools';
import ControlInterface from 'clock-common/lib/Tools/ControlInterface';
import { removeDuplicates, GetClockDisplayFreqValue } from 'clock-common/lib/Tools/Tools';
import { useContext, useState } from 'react';
import { GetButton } from 'clock-common/lib/Components/NodeType';
import { Dialog } from 'primereact/dialog';
import FDPLLAutoCalculation from './FDPLLAutoCalculation';

let fdPllRadioSymbolId = 'CONFIG_CLOCK_DPLL_REF_CLOCK';

export const INPUT_MIN_FREQUENCY = 32768;
export const INPUT_MAX_FREQUENCY = 2000000;
export const OUTPUT_MIN_FREQUENCY = 48000000;
export const OUTPUT_MAX_FREQUENCY = 96000000;
export let fdpllcustomFrequencyMap = new Map();

let fdpllSettingsSymbolArray = [
  'CONFIG_CLOCK_DPLL_ENABLE',
  'CONFIG_CLOCK_DPLL_ONDEMAND',
  'CONFIG_CLOCK_DPLL_RUNSTDY',
  'CONFIG_CLOCK_DPLL_LDR_INTEGER',
  'CONFIG_CLOCK_DPLL_LDRFRAC_FRACTION',
  'CONFIG_CLOCK_DPLL_PRESCALAR',
  'CONFIG_CLOCK_DPLL_LOCK_BYPASS',
  'CONFIG_CLOCK_DPLL_LOWPOWER_ENABLE',
  'CONFIG_CLOCK_DPLL_WAKEUP_FAST',
  'CONFIG_CLOCK_DPLL_FILTER',
  'CONFIG_CLOCK_DPLL_REF_CLOCK',
  'CONFIG_CLOCK_DPLL_DIVIDER'
];
let fdPllCustomFrequencyListeners = [
  'XOSC32K_FREQ',
  'XOSC_FREQ',
  'GCLK_ID_0_FREQ',
  'CONFIG_CLOCK_DPLL_DIVIDER_VALUE',
  'CONFIG_CLOCK_DPLL_REF_CLOCK',
  'CONFIG_CLOCK_DPLL_ENABLE',
  'DPLL96M_CLOCK_FREQ'
];

const FDPLLController = (props: {
  fdpllControllerData: ControlInterface[];
  cx: (...classNames: string[]) => string;
}) => {
  const { componentId = 'core' } = useContext(PluginConfigContext);
  const [dialogStatus, setDialogStatus] = useState(false);

  const CONFIG_CLOCK_DPLL_ENABLE = useBooleanSymbol({
    componentId,
    symbolId: 'CONFIG_CLOCK_DPLL_ENABLE'
  });
  const fdpllSymbol = useKeyValueSetSymbol({ componentId, symbolId: fdPllRadioSymbolId });
  const CONFIG_CLOCK_DPLL_PRESCALAR = useKeyValueSetSymbol({
    componentId,
    symbolId: 'CONFIG_CLOCK_DPLL_PRESCALAR'
  });
  const XOSC32K_FREQ = useIntegerSymbol({ componentId, symbolId: 'XOSC32K_FREQ' });
  const XOSC_FREQ = useIntegerSymbol({ componentId, symbolId: 'XOSC_FREQ' });
  const GCLK_ID_0_FREQ = useIntegerSymbol({ componentId, symbolId: 'GCLK_ID_0_FREQ' });
  const CONFIG_CLOCK_DPLL_DIVIDER = useIntegerSymbol({
    componentId,
    symbolId: 'CONFIG_CLOCK_DPLL_DIVIDER'
  });
  const dpllDivLabelValue = useIntegerSymbol({
    componentId,
    symbolId: 'CONFIG_CLOCK_DPLL_DIVIDER_VALUE'
  });
  const CONFIG_CLOCK_DPLL_LDR_INTEGER = useIntegerSymbol({
    componentId: componentId,
    symbolId: 'CONFIG_CLOCK_DPLL_LDR_INTEGER'
  });
  const CONFIG_CLOCK_DPLL_LDRFRAC_FRACTION = useIntegerSymbol({
    componentId: componentId,
    symbolId: 'CONFIG_CLOCK_DPLL_LDRFRAC_FRACTION'
  });
  const CONFIG_CLOCK_DPLL_MULTIPLIER_VALUE = useFloatSymbol({
    componentId,
    symbolId: 'CONFIG_CLOCK_DPLL_MULTIPLIER_VALUE'
  });
  const DPLL96M_CLOCK_FREQ = useIntegerSymbol({ componentId, symbolId: 'DPLL96M_CLOCK_FREQ' });

  function isInputFrequencyValid(frequency: any) {
    return INPUT_MIN_FREQUENCY <= frequency && frequency <= INPUT_MAX_FREQUENCY;
  }

  function isOutputFrequencyValid(frequency: any) {
    return OUTPUT_MIN_FREQUENCY <= frequency && frequency <= OUTPUT_MAX_FREQUENCY;
  }

  const getClockSourceItemsAutoCalculate = () => {
    let clockSourceItems: string[] = [];
    for (let x = 0; x < fdpllSymbol.optionPairs.length; x++) {
      let ref = fdpllSymbol.optionPairs[x].key;
      switch (fdpllSymbol.optionPairs[x].key) {
        case 'XOSC32K':
          clockSourceItems[x] = ref + ' (' + GetClockDisplayFreqValue(XOSC32K_FREQ.value) + ')';
          break;
        case 'XOSC':
          clockSourceItems[x] = ref + ' (' + GetClockDisplayFreqValue(XOSC_FREQ.value) + ')';
          break;
        case 'GCLK_DPLL':
          clockSourceItems[x] = ref + ' (' + GetClockDisplayFreqValue(GCLK_ID_0_FREQ.value) + ')';
          break;
      }
    }
    return clockSourceItems;
  };

  const FDPLLCustomFrequency = () => {
    let fdpllCustomFreq;
    let dpllCalculatedFreq;
    updateCustomDPLLFreq();
    // const symbolChanged = (symbol: ConfigSymbolEvent) => {
    //   updateCustomDPLLFreq();
    //   setCount(count + 1);
    // };
    // fdPllCustomFrequencyListeners.map((e) => addListener(e));
    // function addListener(symbolId: string) {
    //   AddSymbolListener(symbolId);
    //   fdpllcustomFrequencyMap.set(symbolId, {
    //     symbolChanged: symbolChanged
    //   });
    // }

    function updateCustomDPLLFreq() {
      if (CONFIG_CLOCK_DPLL_ENABLE.value === true) {
        fdpllCustomFreq = getFDPLLSourceFrequency();
        dpllCalculatedFreq = getDpllCalculatedFreq();
      } else {
        fdpllCustomFreq = '';
        dpllCalculatedFreq = '';
      }
    }

    function getFDPLLSourceFrequency() {
      let freq = 0;

      switch (fdpllSymbol.value) {
        case 0:
          freq = XOSC32K_FREQ.value;
          break;
        case 1:
          freq = XOSC_FREQ.value;
          freq = freq / (2 * (CONFIG_CLOCK_DPLL_DIVIDER.value + 1));
          break;
        case 2:
          freq = GCLK_ID_0_FREQ.value;
          break;
        default:
          error('Clock Configurator', 'DPLL source selection is more than range');
      }

      freq = Math.round(freq);
      return freq + '';
    }

    function getDpllCalculatedFreq() {
      let dpllPreScalarValue = CONFIG_CLOCK_DPLL_PRESCALAR.selectedOption;

      dpllPreScalarValue = dpllPreScalarValue.replace('DIV', '');
      let inputFreq = DPLL96M_CLOCK_FREQ.value;
      let outputFreq = inputFreq * parseInt(dpllPreScalarValue);
      outputFreq = Math.round(outputFreq);
      return outputFreq + '';
    }

    return (
      <div>
        <PlainLabel
          disPlayText={
            fdpllCustomFreq === ''
              ? fdpllCustomFreq
              : GetClockDisplayFreqValue(Number(fdpllCustomFreq))
          }
          className={props.cx('dpll96MInputFreq')}
          toolTip={
            'Frequency Range : ' +
            GetClockDisplayFreqValue(INPUT_MIN_FREQUENCY) +
            ' to ' +
            GetClockDisplayFreqValue(INPUT_MAX_FREQUENCY)
          }
          redColorStatus={!isInputFrequencyValid(fdpllCustomFreq)}
        />
        <PlainLabel
          disPlayText={
            dpllCalculatedFreq === ''
              ? dpllCalculatedFreq
              : GetClockDisplayFreqValue(Number(dpllCalculatedFreq))
          }
          className={props.cx('dpllCalculatedFreq')}
          toolTip={
            'Frequency Range : ' +
            GetClockDisplayFreqValue(OUTPUT_MIN_FREQUENCY) +
            ' to ' +
            GetClockDisplayFreqValue(OUTPUT_MAX_FREQUENCY)
          }
          redColorStatus={!isOutputFrequencyValid(dpllCalculatedFreq)}
        />
        <PlainLabel
          disPlayText={GetClockDisplayFreqValue(Number(DPLL96M_CLOCK_FREQ.value))}
          className={props.cx('dpll96MFreq')}
          toolTip={
            'Frequency Range : ' +
            GetClockDisplayFreqValue(OUTPUT_MIN_FREQUENCY) +
            ' to ' +
            GetClockDisplayFreqValue(OUTPUT_MAX_FREQUENCY)
          }
          redColorStatus={!isOutputFrequencyValid(DPLL96M_CLOCK_FREQ.value)}
        />
      </div>
    );
  };

  let symbols: any = props.fdpllControllerData
    .map((e) => e.symbol_id)
    .filter((e) => e !== undefined);
  symbols = symbols.concat(fdpllSettingsSymbolArray);
  symbols = removeDuplicates(symbols);

  const [dynamicSymbolsInfo] = useState(() => getDynamicSymbolsFromJSON(props.fdpllControllerData));
  const [dynamicLabelSymbolInfo] = useState(() =>
    getDynamicLabelsFromJSON(props.fdpllControllerData)
  );
  return (
    <div>
      <LoadDynamicComponents
        componentId={componentId}
        dynamicSymbolsInfo={dynamicSymbolsInfo}
        cx={props.cx}
      />
      <LoadDynamicFreqencyLabels
        componentId={componentId}
        dynamicLabelSymbolsInfo={dynamicLabelSymbolInfo}
        cx={props.cx}
      />

      <PlainLabel
        disPlayText={dpllDivLabelValue.value + ''}
        className={props.cx('dpllDivLabel')}
      />

      <PlainLabel
        disPlayText={CONFIG_CLOCK_DPLL_MULTIPLIER_VALUE.value + ''}
        className={props.cx('dpllLdrLabel')}
      />

      <PlainLabel
        disPlayText={CONFIG_CLOCK_DPLL_PRESCALAR.selectedOption.replaceAll('DIV', '')}
        className={props.cx('dpllPrescLabel')}
      />
      <KeyValueSetRadio
        keyValueSetSymbolHook={fdpllSymbol}
        classPrefix={'fdpllRadio'}
        classResolver={props.cx}
        labelClassPrefix={'fdpllRadioName'}
      />
      <FDPLLCustomFrequency />

      <SettingsDialog
        tooltip='FDPLL Configuration'
        componentId={componentId}
        className={props.cx('dpll_settings')}
        symbolArray={fdpllSettingsSymbolArray}
        dialogWidth='55rem'
        dialogHeight='50rem'
      />

      <ResetSymbolsIcon
        tooltip='Reset FDPLL symbols to default value'
        className={props.cx('fdpllReset')}
        componentId={componentId}
        resetSymbolsArray={symbols}
      />
      <GetButton
        label={'Auto Calculate'}
        className={props.cx('fdpllAutoCalculate')}
        tooltip={'Press this to Auto-Calculate FDPLL Frequency'}
        onClick={() => {
          setDialogStatus(true);
        }}
      />

      <Dialog
        header={'FDPLL Auto Settings Calculation'}
        visible={dialogStatus}
        style={{ width: '42rem', height: '32rem' }}
        maximizable={true}
        onHide={() => {
          setDialogStatus(false);
        }}>
        <FDPLLAutoCalculation
          componentId={componentId}
          expectedOutputFreq={DPLL96M_CLOCK_FREQ.value}
          close={() => {
            setDialogStatus(false);
          }}
          clockSourceItems={getClockSourceItemsAutoCalculate()}
          selectedClockIndex={fdpllSymbol.value}
          ldrInt={CONFIG_CLOCK_DPLL_LDR_INTEGER.value}
          ldrFrac={CONFIG_CLOCK_DPLL_LDRFRAC_FRACTION.value}
          dpllDiv={CONFIG_CLOCK_DPLL_DIVIDER.value}
        />
      </Dialog>
    </div>
  );
};
export default FDPLLController;

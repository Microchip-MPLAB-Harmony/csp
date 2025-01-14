import { KeyValueSetRadio, useKeyValueSetSymbol } from '@mplab_harmony/harmony-plugin-client-lib';
import LoadDynamicComponents from 'clock-common/lib/Components/Dynamic/LoadDynamicComponents';
import LoadDynamicFreqencyLabels from 'clock-common/lib/Components/Dynamic/LoadDynamicFreqencyLabels';
import ResetSymbolsIcon from 'clock-common/lib/Components/ResetSymbolsIcon';
import SettingsDialog from 'clock-common/lib/Components/SettingsDialog';
import {
  getDynamicLabelsFromJSON,
  getDynamicSymbolsFromJSON
} from 'clock-common/lib/Tools/ClockJSONTools';
import ControlInterface from 'clock-common/lib/Tools/ControlInterface';
import { removeDuplicates } from 'clock-common/lib/Tools/Tools';
import { useState } from 'react';

let oscillator32KhzRadioSymbolId = 'XOSC32K_OSCILLATOR_MODE';
let internal32KhzOscillatorSettingsSymbolArray = [
  'CONF_CLOCK_OSC32K_ENABLE',
  'OSC32K_RUNSTDBY',
  'OSC32K_ONDEMAND',
  'OSC32K_EN32K',
  'OSC32K_STARTUP'
];
let crsytal32KhzOscillatorSymbolArray = [
  'CONF_CLOCK_XOSC32K_ENABLE',
  'XOSC32K_OSCILLATOR_MODE',
  'XOSC32K_RUNSTDBY',
  'XOSC32K_ONDEMAND',
  'XOSC32K_EN32K',
  'XOSC32K_STARTUP'
];
const ClkD20Oscillators32KHzControllerBox = (props: {
  componentId: string;
  oscillatorData: ControlInterface[];
  cx: (...classNames: string[]) => string;
}) => {
  const oscillator32Khz = useKeyValueSetSymbol({
    componentId: props.componentId,
    symbolId: oscillator32KhzRadioSymbolId
  });

  let symbols: any = props.oscillatorData.map((e) => e.symbol_id).filter((e) => e !== undefined);
  symbols = symbols.concat(internal32KhzOscillatorSettingsSymbolArray);

  symbols = symbols.concat(crsytal32KhzOscillatorSymbolArray);
  symbols = removeDuplicates(symbols);

  const [dynamicSymbolsInfo] = useState(() => getDynamicSymbolsFromJSON(props.oscillatorData));
  const [dynamicLabelSymbolInfo] = useState(() => getDynamicLabelsFromJSON(props.oscillatorData));

  return (
    <div>
      <LoadDynamicComponents
        componentId={props.componentId}
        dynamicSymbolsInfo={dynamicSymbolsInfo}
        cx={props.cx}
      />
      <LoadDynamicFreqencyLabels
        componentId={props.componentId}
        dynamicLabelSymbolsInfo={dynamicLabelSymbolInfo}
        cx={props.cx}
      />
      <KeyValueSetRadio
        keyValueSetSymbolHook={oscillator32Khz}
        classResolver={props.cx}
        classPrefix={'oscillators32KhzContrlRadio'}
      />

      <SettingsDialog
        tooltip='32 KHz High Accuracy Internal Oscillator Configuration'
        componentId={props.componentId}
        className={props.cx('highAccuracyInternalOscillatorSettings')}
        symbolArray={internal32KhzOscillatorSettingsSymbolArray}
        dialogWidth='50rem'
        dialogHeight='30rem'
      />
      <SettingsDialog
        tooltip='32 Khz Crystal Oscillator Configuration'
        componentId={props.componentId}
        className={props.cx('xosc32K_settings')}
        symbolArray={crsytal32KhzOscillatorSymbolArray}
        dialogWidth='50rem'
        dialogHeight='30rem'
      />
      <ResetSymbolsIcon
        tooltip='Reset 32 Khz Oscillator symbols to default value'
        className={props.cx('oscillatorsController32KhzReset')}
        componentId={props.componentId}
        resetSymbolsArray={symbols}
      />
    </div>
  );
};
export default ClkD20Oscillators32KHzControllerBox;

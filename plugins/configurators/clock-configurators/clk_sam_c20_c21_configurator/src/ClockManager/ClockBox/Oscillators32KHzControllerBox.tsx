import {
  KeyValueSetRadio,
  PluginConfigContext,
  useKeyValueSetSymbol
} from '@mplab_harmony/harmony-plugin-client-lib';
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
import { useContext, useState } from 'react';

let oscillator32KhzRadioSymbolId = 'XOSC32K_OSCILLATOR_MODE';
let internal32KhzOscillatorSettingsSymbolArray = [
  'CONF_CLOCK_OSC32K_ENABLE',
  'OSC32K_RUNSTDBY',
  'OSC32K_ONDEMAND',
  'OSC32K_EN1K',
  'OSC32K_EN32K',
  'OSC32K_STARTUP'
];
let crsytal32KhzOscillatorSymbolArray = [
  'CONF_CLOCK_XOSC32K_ENABLE',
  'XOSC32K_OSCILLATOR_MODE',
  'XOSC32K_RUNSTDBY',
  'XOSC32K_ONDEMAND',
  'XOSC32K_EN1K',
  'XOSC32K_EN32K',
  'XOSC32K_STARTUP',
  'CONFIG_CLOCK_RTC_SRC',
  'XOSC32K_CFDEN'
];
const Oscillators32KHzControllerBox = (props: {
  oscillatorData: ControlInterface[];
  cx: (...classNames: string[]) => string;
}) => {
  const { componentId = 'core' } = useContext(PluginConfigContext);
  const oscillatorMode = useKeyValueSetSymbol({
    componentId,
    symbolId: oscillator32KhzRadioSymbolId
  });
  let symbols: any = props.oscillatorData.map((e) => e.symbol_id).filter((e) => e !== undefined);
  symbols = symbols.concat(
    internal32KhzOscillatorSettingsSymbolArray,
    crsytal32KhzOscillatorSymbolArray
  );
  symbols = removeDuplicates(symbols);

  const [dynamicSymbolsInfo] = useState(() => getDynamicSymbolsFromJSON(props.oscillatorData));
  const [dynamicLabelSymbolInfo] = useState(() => getDynamicLabelsFromJSON(props.oscillatorData));

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
      <KeyValueSetRadio
        keyValueSetSymbolHook={oscillatorMode}
        classResolver={props.cx}
        classPrefix={'oscillators32KhzContrlRadio'}
      />

      <SettingsDialog
        tooltip='32 KHz High Accuracy Internal Oscillator Configuration'
        componentId={componentId}
        className={props.cx('osc32K_settings')}
        symbolArray={internal32KhzOscillatorSettingsSymbolArray}
        dialogWidth='50rem'
        dialogHeight='30rem'
      />
      <SettingsDialog
        tooltip='32 Khz Crystal Oscillator Configuration'
        componentId={componentId}
        className={props.cx('xosc32K_settings')}
        symbolArray={crsytal32KhzOscillatorSymbolArray}
        dialogWidth='50rem'
        dialogHeight='40rem'
      />
      <ResetSymbolsIcon
        tooltip='Reset 32 Khz Oscillator symbols to default value'
        className={props.cx('oscillatorsController32KhzReset')}
        componentId={componentId}
        resetSymbolsArray={symbols}
      />
    </div>
  );
};
export default Oscillators32KHzControllerBox;

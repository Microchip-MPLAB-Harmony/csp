import ResetSymbolsIcon from 'clock-common/lib/Components/ResetSymbolsIcon';
import ControlInterface from 'clock-common/lib/Tools/ControlInterface';
import SettingsDialog from 'clock-common/lib/Components/SettingsDialog';
import { useContext, useState } from 'react';
import {
  KeyValueSetRadio,
  PluginConfigContext,
  useKeyValueSetSymbol
} from '@mplab_harmony/harmony-plugin-client-lib';
import { getDynamicSymbolsFromJSON } from 'clock-common/lib/Tools/ClockJSONTools';
import FrequencyLabelComponent from 'clock-common/lib/Components/LabelComponent/FrequencyLabelComponent';
import LoadDynamicComponents from 'clock-common/lib/Components/Dynamic/LoadDynamicComponents';

const settingsArray = [
  'CONF_CLOCK_XOSC32K_ENABLE',
  'XOSC32K_OSCILLATOR_MODE',
  'XOSC32K_FREQ_IN',
  'XOSC32K_ONDEMAND',
  'XOSC32K_CGM',
  'XOSC32K_ENSL',
  'XOSC32K_BOOST',
  'XOSC32K_STARTUP',
  'CONFIG_CLOCK_RTC_SRC',
  'XOSC32K_CFDEN',
  'XOSC32K_CFDPRESC',
  'XOSC32K_SWBACK'
];

const Crstal32MhzOscialltorControllerBox = (props: {
  clockController: ControlInterface[];
  cx: (...classNames: string[]) => string;
}) => {
  const { componentId = 'core' } = useContext(PluginConfigContext);

  const cmb_32Khz_Mode = useKeyValueSetSymbol({
    componentId,
    symbolId: 'XOSC32K_OSCILLATOR_MODE'
  });

  const [dynamicSymbolInfo] = useState(() => getDynamicSymbolsFromJSON(props.clockController));

  return (
    <div>
      <LoadDynamicComponents
        componentId={componentId}
        dynamicSymbolsInfo={dynamicSymbolInfo}
        cx={props.cx}
      />
      <FrequencyLabelComponent
        componentId={componentId}
        redColorForZeroFrequency={true}
        symbolId={'OSCULP1K_FREQ'}
        class={props.cx('osculp1k_freq')}
      />
      <FrequencyLabelComponent
        componentId={componentId}
        redColorForZeroFrequency={true}
        symbolId={'OSCULP32K_FREQ'}
        class={props.cx('osculp32k_freq')}
      />
      <FrequencyLabelComponent
        componentId={componentId}
        symbolId={'XOSC32K_FREQ'}
        class={props.cx('osc32k_freq')}
      />

      <FrequencyLabelComponent
        componentId={componentId}
        symbolId={'XOSC1K_FREQ'}
        class={props.cx('osc1k_freq')}
      />

      <KeyValueSetRadio
        keyValueSetSymbolHook={cmb_32Khz_Mode}
        classPrefix='oscexternal32KHzOSCModeRadio'
        classResolver={props.cx}
      />
      <SettingsDialog
        tooltip='Clock Settings Configuration'
        componentId={componentId}
        className={props.cx('Oscillator32KhzSettings')}
        symbolArray={settingsArray}
        dialogWidth='50rem'
        dialogHeight='47rem'
      />
      <ResetSymbolsIcon
        tooltip='Reset Clock symbols to default value'
        className={props.cx('Oscillator32KhzReset')}
        componentId={componentId}
        resetSymbolsArray={settingsArray}
      />
    </div>
  );
};

export default Crstal32MhzOscialltorControllerBox;

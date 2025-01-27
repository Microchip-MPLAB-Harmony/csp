import ResetSymbolsIcon from 'clock-common/lib/Components/ResetSymbolsIcon';
import ControlInterface from 'clock-common/lib/Tools/ControlInterface';
import SettingsDialog from 'clock-common/lib/Components/SettingsDialog';
import LoadDynamicComponents from 'clock-common/lib/Components/Dynamic/LoadDynamicComponents';
import { useContext, useState } from 'react';
import {
  KeyValueSetRadio,
  PluginConfigContext,
  useBooleanSymbol,
  useKeyValueSetSymbol
} from '@mplab_harmony/harmony-plugin-client-lib';
import { getDynamicSymbolsFromJSON } from 'clock-common/lib/Tools/ClockJSONTools';
import FrequencyLabelComponent from 'clock-common/lib/Components/LabelComponent/FrequencyLabelComponent';

const settingsArray = [
  'CONFIG_CLOCK_XOSC_ENABLE',
  'CONFIG_CLOCK_XOSC_AGC_ENABLE',
  'CONFIG_CLOCK_XOSC_SWBEN',
  'XOSC_OSCILLATOR_MODE',
  'CONFIG_CLOCK_XOSC_FREQUENCY',
  'CONFIG_CLOCK_XOSC_ONDEMAND',
  'CONFIG_CLOCK_XOSC_STARTUP',
  'CONFIG_CLOCK_XOSC_CFDEN',
  'CONFIG_CLOCK_XOSC_CFDPRESC',
  'CONFIG_CLOCK_XOSC_USBHSDIV'
];

const Crystal8MhzControllerBox = (props: {
  clockController: ControlInterface[];
  cx: (...classNames: string[]) => string;
}) => {
  const { componentId = 'core' } = useContext(PluginConfigContext);

  const cmb_oscillator_Mode = useKeyValueSetSymbol({
    componentId,
    symbolId: 'XOSC_OSCILLATOR_MODE'
  });
  const checkCrystalEnable = useBooleanSymbol({
    componentId,
    symbolId: 'CONFIG_CLOCK_XOSC_ENABLE'
  });

  const [dynamicSymbolInfo] = useState(() => getDynamicSymbolsFromJSON(props.clockController));

  return (
    <div>
      <LoadDynamicComponents
        componentId={componentId}
        dynamicSymbolsInfo={dynamicSymbolInfo}
        cx={props.cx}
      />
      {checkCrystalEnable.value === true && (
        <FrequencyLabelComponent
          componentId={componentId}
          redColorForZeroFrequency={true}
          symbolId={'XOSC_FREQ'}
          className={props.cx('xoscFreq')}
        />
      )}
      <KeyValueSetRadio
        keyValueSetSymbolHook={cmb_oscillator_Mode}
        classPrefix='crystal848OscillatorR'
        classResolver={props.cx}
      />
      <SettingsDialog
        tooltip='Settings Configuration'
        componentId={componentId}
        className={props.cx('crystal848_settings')}
        symbolArray={settingsArray}
        dialogWidth='50rem'
        dialogHeight='47rem'
      />
      <ResetSymbolsIcon
        tooltip='Reset clock symbols to default value'
        className={props.cx('crystal848_reset')}
        componentId={componentId}
        resetSymbolsArray={settingsArray}
      />
    </div>
  );
};

export default Crystal8MhzControllerBox;

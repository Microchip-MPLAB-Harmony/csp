import { useContext, useState } from 'react';
import { getCrstalSettingsSymbol } from './CrstalSettingsSymbol';
import CrytalOscillators48MHzControllerBoxTemplate from './CrytalOscillators48MHzControllerBoxTemplate';
import ControlInterface from 'clock-common/lib/Tools/ControlInterface';
import { PluginConfigContext, useBooleanSymbol } from '@mplab_harmony/harmony-plugin-client-lib';
import { ListBox } from 'primereact/listbox';

interface Tab {
  name: string;
  id: string;
  status: string;
}
const newTabs: Tab[] = [
  { name: 'XOSC CTRL 0', id: '0', status: 'CONFIG_CLOCK_XOSC0_ENABLE' },
  { name: 'XOSC CTRL 1', id: '1', status: 'CONFIG_CLOCK_XOSC1_ENABLE' }
];
const CrytalOscillators48MHzControllerXBox = (props: {
  oscillatorData: ControlInterface[];
  cx: (...classNames: string[]) => string;
}) => {
  const { componentId = 'core' } = useContext(PluginConfigContext);
  const [value, setValue] = useState<Tab | null>(newTabs[0]);

  const tabTemplate = (option: any) => {
    // eslint-disable-next-line react-hooks/rules-of-hooks
    const crystalEnable = useBooleanSymbol({
      componentId,
      symbolId: option.status
    });
    return (
      <div
        style={{ fontSize: '11px' }}
        className={crystalEnable.value ? props.cx('enable') : props.cx('disable')}>
        {option.name}
      </div>
    );
  };

  return (
    <div>
      <div>
        <ListBox
          className={props.cx('crystalTab')}
          value={value}
          options={newTabs}
          optionLabel='name'
          itemTemplate={tabTemplate}
          onChange={(e) => setValue(e.value)}
        />
      </div>
      <CrytalOscillators48MHzControllerBoxTemplate
        index={value?.name ? value.id : '0'}
        crystalsettingsClassName={'crystal8_48_oscillators_settings'}
        crystalresetClassName={'crystal8_48_oscillators_reset'}
        crystalXoscFreqInputClassName={'xoscFrequency'}
        crystalEnableClassName={'crystalOSC'}
        crystalFrequencyClassName={'xosc48MFreq'}
        crystalSettingsSymbolArray={getCrstalSettingsSymbol(value?.name ? value.id : '0')}
        crystalController={props.oscillatorData}
        crystalCFDEnableClassName={'xoscxCFDEnable'}
        originalRadioButtonIdentificationId={'XOSC0_OSCILLATOR_MODE'}
        cx={props.cx}
        componentId={componentId}
      />
    </div>
  );
};
export default CrytalOscillators48MHzControllerXBox;

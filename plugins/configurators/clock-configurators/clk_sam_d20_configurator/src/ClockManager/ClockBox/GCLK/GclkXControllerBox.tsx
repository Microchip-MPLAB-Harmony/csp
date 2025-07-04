import { useContext, useState } from 'react';
import ControlInterface from 'clock-common/lib/Tools/ControlInterface';

import { ListBox } from 'primereact/listbox';
import { PluginConfigContext, useBooleanSymbol } from '@mplab_harmony/harmony-plugin-client-lib';
import { getGclockSymbols } from './GclkSymbols';
import GCKLClockControllerBoxTemplate from './GCKLClockControllerBoxTemplate';

interface Tab {
  name: string;
  id: string;
  status: string;
}

export const GCLKTabs: Tab[] = [
  { name: 'GCLK 2', id: '2', status: 'GCLK_INST_NUM2' },
  { name: 'GCLK 3', id: '3', status: 'GCLK_INST_NUM3' },
  { name: 'GCLK 4', id: '4', status: 'GCLK_INST_NUM4' },
  { name: 'GCLK 5', id: '5', status: 'GCLK_INST_NUM5' },
  { name: 'GCLK 6', id: '6', status: 'GCLK_INST_NUM6' },
  { name: 'GCLK 7', id: '7', status: 'GCLK_INST_NUM7' }
];

const GclkXControllerBox = (props: {
  controller: ControlInterface[];
  cx: (...classNames: string[]) => string;
}) => {
  const { componentId = 'core' } = useContext(PluginConfigContext);

  const [value, setValue] = useState<Tab | null>(GCLKTabs[0]);

  const tabTemplate = (option: any) => {
    // eslint-disable-next-line react-hooks/rules-of-hooks
    const GCLKClocKEnable = useBooleanSymbol({
      componentId,
      symbolId: option.status
    });
    return (
      <div
        style={{ fontSize: '11px' }}
        className={GCLKClocKEnable.value ? props.cx('enable') : props.cx('disable')}>
        {option.name}
      </div>
    );
  };
  return (
    <div>
      <div>
        <ListBox
          className={props.cx('gclkXgenTab')}
          value={value}
          options={GCLKTabs}
          optionLabel='name'
          itemTemplate={tabTemplate}
          onChange={(e) => setValue(e.value)}
        />
      </div>
      <GCKLClockControllerBoxTemplate
        tabTitle={value?.name ? value.id : '2'}
        gclkSettingsSymbolArray={getGclockSymbols(value?.name ? value.id : '2')}
        gclkController={props.controller}
        componentId={componentId}
        cx={props.cx}
        gclKsettingsClassName={'gclkGenX_settings'}
        gclkresetClassName={'gclkGenXReset'}
        gclKinputNumberClassName={'gclkGenXDiv'}
        gclkEnableClassName={'gclkGenXEnable'}
        gclkFrequencyClassName={'gclkGenXFreq'}
        gclkDivLabelClassName={'gclkGenXDivLabel'}
        gclkRadioName='gclkGenXRadio'
        gclkRadioLabelName='gclkGenXRadioName'
      />
    </div>
  );
};
export default GclkXControllerBox;

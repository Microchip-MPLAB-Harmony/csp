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
        style={{ fontSize: '10px' }}
        className={GCLKClocKEnable.value ? props.cx('enable') : props.cx('disable')}>
        {option.name}
      </div>
    );
  };
  return (
    <div>
      <div>
        <ListBox
          className={props.cx('gclkTabbedPane')}
          value={value}
          options={GCLKTabs}
          optionLabel='name'
          itemTemplate={tabTemplate}
          onChange={(e) => {
            if (e.value === null) return;
            setValue(e.value);
          }}
        />
      </div>
      <GCKLClockControllerBoxTemplate
        tabTitle={value?.name ? value.id : '2'}
        gclkSettingsSymbolArray={getGclockSymbols(value?.name ? value.id : '2')}
        gclkController={props.controller}
        componentId={componentId}
        cx={props.cx}
        gclKsettingsClassName={'gclkGenX_settings'}
        gclkresetClassName={'gclkGenX_reset'}
        gclKinputNumberClassName={'gclkGenXDiv'}
        gclkEnableClassName={'gclkGenXEnable'}
        gclkFrequencyClassName={'gclkGenxFreq'}
        gclkDivLabelClassName={'gclkGenXDivLabel'}
        gclkRadioName='gclkGenXSourceRadio'
        gclkRadioLabelName='gclkGenXSourceRadioName'
      />
    </div>
  );
};
export default GclkXControllerBox;
